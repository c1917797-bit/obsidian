"""
日志模块 - 结构化日志+指标
统一日志输出，支持文件和控制台
"""
import os
import sys
import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Optional, Dict, Any
from enum import Enum

class LogLevel(Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"

class StructuredLogger:
    """
    结构化日志记录器
    - 输出到控制台（彩色）
    - 输出到文件（JSON格式）
    - 支持指标收集
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, name: str = "IntelligenceOS", log_dir: str = None):
        if self._initialized:
            return

        self.name = name
        self.log_dir = log_dir or os.path.join(
            os.path.dirname(__file__), '..', 'logs'
        )
        os.makedirs(self.log_dir, exist_ok=True)

        self.log_file = os.path.join(
            self.log_dir,
            f"{name}_{datetime.now().strftime('%Y%m%d')}.log"
        )

        self.metrics_file = os.path.join(
            self.log_dir,
            f"metrics_{datetime.now().strftime('%Y%m%d')}.json"
        )

        self.metrics: Dict[str, Any] = {
            'crawled': 0,
            'classified': 0,
            'saved': 0,
            'reports': 0,
            'errors': 0,
            'start_time': datetime.now().isoformat()
        }

        self._setup_logger()
        self._initialized = True

    def _setup_logger(self):
        """设置logger"""
        self.logger = logging.getLogger(self.name)
        self.logger.setLevel(logging.DEBUG)

        # 清除已有的handlers
        self.logger.handlers = []

        # Console handler with UTF-8 encoding
        console = logging.StreamHandler(sys.stdout)
        console.setLevel(logging.INFO)
        console_formatter = logging.Formatter(
            '%(asctime)s [%(levelname)s] %(message)s',
            datefmt='%H:%M:%S'
        )
        console.setFormatter(console_formatter)
        console.encoding = 'utf-8'
        self.logger.addHandler(console)

        # File handler (JSON)
        file_handler = logging.FileHandler(self.log_file, encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)
        file_formatter = logging.Formatter('%(message)s')
        file_handler.setFormatter(file_formatter)
        self.logger.addHandler(file_handler)

    def _safe_log(self, level: str, message: str, **kwargs):
        """安全记录日志，捕获编码错误"""
        try:
            formatted = self._format_message(level, message, **kwargs)
            self.logger.log(getattr(logging, level), formatted)
        except (UnicodeEncodeError, TypeError):
            # Fallback: ASCII-safe message
            safe_message = message.encode('ascii', 'replace').decode('ascii')
            fallback_entry = {
                'timestamp': datetime.now().isoformat(),
                'level': level,
                'name': self.name,
                'message': safe_message
            }
            fallback_formatted = json.dumps(fallback_entry, ensure_ascii=False)
            try:
                self.logger.log(getattr(logging, level), fallback_formatted)
            except:
                pass

    def _format_message(self, level: str, message: str, **kwargs) -> str:
        """格式化日志消息"""
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'level': level,
            'name': self.name,
            'message': message,
            **kwargs
        }
        return json.dumps(log_entry, ensure_ascii=False)

    def debug(self, message: str, **kwargs):
        self._safe_log('DEBUG', message, **kwargs)

    def info(self, message: str, **kwargs):
        self._safe_log('INFO', message, **kwargs)

    def warning(self, message: str, **kwargs):
        self._safe_log('WARNING', message, **kwargs)

    def error(self, message: str, **kwargs):
        self._safe_log('ERROR', message, **kwargs)
        self.metrics['errors'] += 1

    def critical(self, message: str, **kwargs):
        self._safe_log('CRITICAL', message, **kwargs)
        self.metrics['errors'] += 1

    def log_metric(self, key: str, value: Any):
        """记录指标"""
        self.metrics[key] = value
        self.info(f"METRIC: {key}={value}", metric=True)

    def log_step(self, step: str, status: str, **details):
        """记录步骤状态"""
        self.info(f"STEP: {step} [{status}]", step=step, status=status, **details)

    def log_pipeline(self, pipeline: str, step: int, total: int, message: str):
        """记录流水线进度"""
        self.info(
            f"[{step}/{total}] {message}",
            pipeline=pipeline,
            step=step,
            total=total,
            progress=f"{step/total*100:.0f}%"
        )

    def get_metrics(self) -> Dict[str, Any]:
        """获取当前指标"""
        self.metrics['uptime'] = (
            datetime.now() - datetime.fromisoformat(self.metrics['start_time'])
        ).total_seconds()
        return self.metrics.copy()

    def save_metrics(self):
        """保存指标到文件"""
        metrics = self.get_metrics()
        with open(self.metrics_file, 'w', encoding='utf-8') as f:
            json.dump(metrics, f, ensure_ascii=False, indent=2)

    def close(self):
        """关闭logger"""
        self.save_metrics()
        for handler in self.logger.handlers:
            handler.close()

def get_logger(name: str = "IntelligenceOS") -> StructuredLogger:
    """获取logger实例"""
    return StructuredLogger(name)

# 全局logger实例
logger = get_logger()