"""
Pipeline Lock - 防止并发执行
"""
import os
import time
import filelock

LOCK_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'locks')
LOCK_FILE = os.path.join(LOCK_DIR, 'pipeline.lock')


def acquire_lock(timeout: int = 0) -> filelock.FileLock:
    """
    获取流水线锁
    timeout=0 表示无限等待（单实例运行）
    timeout>0 表示最多等N秒（用于定时任务防重复触发）
    """
    os.makedirs(LOCK_DIR, exist_ok=True)
    lock = filelock.FileLock(LOCK_FILE, timeout=timeout)
    try:
        lock.acquire()
        return lock
    except filelock.Timeout:
        return None


def release_lock(lock: filelock.FileLock):
    """释放锁"""
    try:
        lock.release()
    except Exception:
        pass


def is_locked() -> bool:
    """检查是否已有锁存在"""
    return os.path.exists(LOCK_FILE)


class PipelineLock:
    """上下文管理器式的流水线锁"""

    def __init__(self, wait_timeout: int = 0):
        self.wait_timeout = wait_timeout
        self.lock = None

    def __enter__(self):
        self.lock = acquire_lock(timeout=self.wait_timeout)
        if self.lock is None:
            from core.logger import get_logger
            logger = get_logger("PipelineLock")
            logger.warning("Pipeline already running, skipping this execution")
            return None
        return self.lock

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.lock:
            release_lock(self.lock)