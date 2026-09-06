#!/usr/bin/env python3
"""
[DEPRECATED] 此文件已废弃，请使用 ai-intelligence-os/main.py

迁移指南:
    旧: python daily_pipeline.py
    新: python ai-intelligence-os/main.py daily

    旧: python daily_pipeline.py --collect-only
    新: python ai-intelligence-os/main.py daily --collect-only

    旧: python daily_pipeline.py --report-only
    新: python ai-intelligence-os/main.py daily --report-only

自动重定向到新系统:
"""
import os
import sys
import subprocess

def main():
    new_main = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "..", "ai-intelligence-os", "main.py"
    )
    new_main = os.path.normpath(new_main)

    if not os.path.exists(new_main):
        print("[ERROR] ai-intelligence-os/main.py not found at: {}".format(new_main))
        sys.exit(1)

    args = sys.argv[1:]

    if "--collect-only" in args:
        cmd = ["python", new_main, "daily"]
    elif "--report-only" in args:
        cmd = ["python", new_main, "daily", "--report-only"]
    else:
        cmd = ["python", new_main, "daily"]

    print("[DEPRECATED] Redirecting to: {}".format(" ".join(cmd)))
    result = subprocess.run(cmd, cwd=os.path.dirname(new_main))
    sys.exit(result.returncode)

if __name__ == "__main__":
    main()
