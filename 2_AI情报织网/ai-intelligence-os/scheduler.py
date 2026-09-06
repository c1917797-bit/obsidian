"""
Pipeline Scheduler - 自动化调度器
支持：
- Windows Task Scheduler 集成
- 定时任务（每日多次采集）
- 并行处理多个任务
"""
import os
import sys
import json
import time
import subprocess
from datetime import datetime, timedelta
from typing import List, Dict, Optional

from core.logger import get_logger

logger = get_logger("PipelineScheduler")


class PipelineScheduler:
    """
    流水线调度器
    管理每日流水线的自动化执行
    """

    def __init__(self, pipeline_path: str = None):
        self.pipeline_path = pipeline_path or os.path.join(
            os.path.dirname(__file__), 'main.py'
        )
        self.config = self._load_config()

    def _load_config(self) -> Dict:
        """加载调度配置"""
        config_path = os.path.join(
            os.path.dirname(__file__), '..', '..', 'config', 'scheduler_config.json'
        )

        default_config = {
            "schedules": [
                {
                    "name": "daily_morning",
                    "time": "08:00",
                    "mode": "daily",
                    "enabled": True
                },
                {
                    "name": "daily_evening",
                    "time": "20:00",
                    "mode": "daily",
                    "enabled": True
                },
                {
                    "name": "weekly_report",
                    "day": "monday",
                    "time": "09:00",
                    "mode": "weekly",
                    "enabled": True
                }
            ],
            "api_key_env": "MINIMAX_API_KEY",
            "max_concurrent": 1,
            "retry_on_failure": True,
            "max_retries": 3
        }

        if os.path.exists(config_path):
            try:
                with open(config_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                logger.warning(f"Failed to load scheduler config: {e}")

        return default_config

    def run_baseline_scan(self) -> bool:
        """Run daily incremental baseline scan using local conference data"""
        try:
            sys.path.insert(0, os.path.dirname(__file__))
            from layers.paper_analysis.baseline_scanner import scan_baseline
            result = scan_baseline(
                venues=['iclr', 'nips'],
                years=[2025],
                min_score=20.0,
                full=False,
                dry_run=False
            )
            logger.info(f"Baseline scan completed: {result}")
            return True
        except Exception as e:
            logger.error(f"Baseline scan failed: {e}")
            return False
    def _save_config(self):
        """保存调度配置"""
        config_path = os.path.join(
            os.path.dirname(__file__), '..', '..', 'config', 'scheduler_config.json'
        )
        os.makedirs(os.path.dirname(config_path), exist_ok=True)

        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, indent=2, ensure_ascii=False)

    def run_pipeline(self, mode: str = 'daily', force: bool = False) -> bool:
        """
        执行流水线
        mode: daily, weekly, baseline_scan, query
        """
        api_key = os.environ.get(self.config.get('api_key_env', 'MINIMAX_API_KEY'))
        if not api_key:
            logger.error("MINIMAX_API_KEY not set")
            return False

        if mode in ('baseline', 'baseline_scan'):
            return self.run_baseline_scan()

        cmd = [
            sys.executable,
            self.pipeline_path,
            '--mode', mode
        ]

        if force:
            cmd.append('--force')

        try:
            logger.info(f"Starting pipeline: {mode}")
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=600
            )

            if result.returncode == 0:
                logger.info(f"Pipeline completed successfully: {mode}")
                return True
            else:
                logger.error(f"Pipeline failed: {result.stderr[:500]}")
                return False

        except subprocess.TimeoutExpired:
            logger.error(f"Pipeline timeout: {mode}")
            return False
        except Exception as e:
            logger.error(f"Pipeline exception: {e}")
            return False

    def run_scheduled_tasks(self):
        """运行所有启用的定时任务"""
        now = datetime.now()
        current_time = now.strftime('%H:%M')
        current_day = now.strftime('%A').lower()

        logger.info(f"Checking schedules at {current_time} on {current_day}")

        for schedule in self.config.get('schedules', []):
            if not schedule.get('enabled', True):
                continue

            schedule_time = schedule.get('time', '')
            schedule_day = schedule.get('day', '').lower()

            if schedule_time != current_time:
                continue

            if schedule.get('mode') == 'weekly' and schedule_day != current_day:
                continue

            mode = schedule.get('mode', 'daily')
            logger.info(f"Running scheduled task: {schedule['name']}")

            success = self.run_pipeline(mode=mode)

            if not success and self.config.get('retry_on_failure', True):
                max_retries = self.config.get('max_retries', 3)
                for attempt in range(max_retries):
                    logger.info(f"Retry {attempt+1}/{max_retries}...")
                    time.sleep(60)
                    if self.run_pipeline(mode=mode):
                        break

    def setup_windows_task(self, task_name: str = "IntelligenceOS_Daily"):
        """
        设置Windows计划任务
        每天自动运行
        """
        try:
            schedule = self.config['schedules'][0]
            time_str = schedule.get('time', '08:00')

            cmd = f'''
            $action = New-ScheduledTaskAction -Execute "python" -Argument "{self.pipeline_path} --mode daily"
            $trigger = New-ScheduledTaskTrigger -Daily -At {time_str}
            $settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries
            Register-ScheduledTask -TaskName "{task_name}" -Action $action -Trigger $trigger -Settings $settings -Force
            '''

            result = subprocess.run(
                ['powershell', '-Command', cmd],
                capture_output=True,
                text=True
            )

            if result.returncode == 0:
                logger.info(f"Windows task created: {task_name}")
                return True
            else:
                logger.error(f"Failed to create Windows task: {result.stderr}")
                return False

        except Exception as e:
            logger.error(f"Setup Windows task error: {e}")
            return False

    def add_schedule(self, name: str, time: str, mode: str = 'daily', day: str = None):
        """添加新的调度任务"""
        schedule = {
            "name": name,
            "time": time,
            "mode": mode,
            "enabled": True
        }

        if day:
            schedule["day"] = day

        self.config.setdefault('schedules', []).append(schedule)
        self._save_config()

        logger.info(f"Added schedule: {name} at {time} (mode: {mode})")

    def remove_schedule(self, name: str):
        """移除调度任务"""
        schedules = self.config.get('schedules', [])
        self.config['schedules'] = [s for s in schedules if s.get('name') != name]
        self._save_config()

        logger.info(f"Removed schedule: {name}")

    def list_schedules(self) -> List[Dict]:
        """列出所有调度任务"""
        return self.config.get('schedules', [])

    def enable_schedule(self, name: str):
        """启用调度任务"""
        for schedule in self.config.get('schedules', []):
            if schedule.get('name') == name:
                schedule['enabled'] = True
        self._save_config()

    def disable_schedule(self, name: str):
        """禁用调度任务"""
        for schedule in self.config.get('schedules', []):
            if schedule.get('name') == name:
                schedule['enabled'] = False
        self._save_config()


def create_scheduler() -> PipelineScheduler:
    """创建调度器"""
    return PipelineScheduler()


def run_as_daemon(check_interval: int = 60):
    """
    作为守护进程运行
    持续检查并执行调度任务
    """
    scheduler = create_scheduler()

    logger.info("Starting scheduler daemon...")
    logger.info(f"Check interval: {check_interval}s")

    while True:
        try:
            scheduler.run_scheduled_tasks()
        except Exception as e:
            logger.error(f"Daemon error: {e}")

        time.sleep(check_interval)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Intelligence OS Scheduler')
    parser.add_argument('--setup-task', action='store_true', help='Setup Windows task')
    parser.add_argument('--list', action='store_true', help='List schedules')
    parser.add_argument('--add', nargs=3, metavar=('NAME', 'TIME', 'MODE'), help='Add schedule')
    parser.add_argument('--run-now', choices=['daily', 'weekly', 'baseline'], help='Run pipeline now')
    parser.add_argument('--daemon', action='store_true', help='Run as daemon')

    args = parser.parse_args()

    scheduler = create_scheduler()

    if args.setup_task:
        scheduler.setup_windows_task()

    elif args.list:
        for s in scheduler.list_schedules():
            status = "ENABLED" if s.get('enabled') else "DISABLED"
            print(f"  [{status}] {s['name']} at {s['time']} ({s['mode']})")

    elif args.add:
        scheduler.add_schedule(args.add[0], args.add[1], args.add[2])

    elif args.run_now:
        scheduler.run_pipeline(mode=args.run_now, force=True)

    elif args.daemon:
        run_as_daemon()

    else:
        print("Intelligence OS Scheduler")
        print("  --setup-task    Setup Windows scheduled task")
        print("  --list          List all schedules")
        print("  --add NAME TIME MODE   Add a new schedule")
        print("  --run-now daily|weekly    Run pipeline now")
        print("  --daemon        Run as daemon (continuous)")