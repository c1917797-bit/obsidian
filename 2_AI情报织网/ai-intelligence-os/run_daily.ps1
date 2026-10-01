if (-not $env:MINIMAX_API_KEY) {
    throw "MINIMAX_API_KEY is not set. Configure it in your environment (e.g. `$env:MINIMAX_API_KEY` or a secrets manager)."
}
Set-Location "C:/Users/Huawei/Documents/code/Obsidian/2_AI情报织网/ai-intelligence-os"
python main.py --mode daily --force 2>&1