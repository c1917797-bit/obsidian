@echo off
chcp 65001 >nul
cd /d "C:\Users\Huawei\Documents\code\Obsidian\2_AI情报织网\ai-intelligence-os"
set PYTHONUTF8=1
python main.py --mode daily --force
