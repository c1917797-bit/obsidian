{"timestamp": "2026-05-28T10:06:19.176057", "level": "INFO", "name": "IntelligenceOS", "message": "IntelligenceOS initialized"}
{"timestamp": "2026-05-28T10:29:48.505543", "level": "INFO", "name": "IntelligenceOS", "message": "IntelligenceOS initialized"}
{"timestamp": "2026-05-28T10:29:48.505543", "level": "INFO", "name": "IntelligenceOS", "message": "============================================================"}
{"timestamp": "2026-05-28T10:29:48.505543", "level": "INFO", "name": "IntelligenceOS", "message": "AI Intelligence OS - 每日流水线"}
{"timestamp": "2026-05-28T10:29:48.505543", "level": "INFO", "name": "IntelligenceOS", "message": "开始时间: 2026-05-28 10:29:48"}
{"timestamp": "2026-05-28T10:29:48.530325", "level": "INFO", "name": "IntelligenceOS", "message": "============================================================"}
{"timestamp": "2026-05-28T10:29:48.530325", "level": "INFO", "name": "IntelligenceOS", "message": "STEP: CRAWL [STARTED]", "step": "CRAWL", "status": "STARTED"}
{"timestamp": "2026-05-28T10:29:48.530325", "level": "INFO", "name": "IntelligenceOS", "message": "开始采集 25 个信源..."}
{"timestamp": "2026-05-28T10:29:48.530325", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: HuggingFace Daily Papers"}
{"timestamp": "2026-05-28T10:29:49.979892", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 20 条 (新增 20)"}
{"timestamp": "2026-05-28T10:29:49.979892", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: arXiv cs.LG"}
{"timestamp": "2026-05-28T10:30:06.838619", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 20 条 (新增 20)"}
{"timestamp": "2026-05-28T10:30:06.838619", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: arXiv cs.CL"}
{"timestamp": "2026-05-28T10:30:07.172836", "level": "WARNING", "name": "IntelligenceOS", "message": "Request failed (1/3): http://export.arxiv.org/api/query?search_query=cat:cs.CL&max_results=20&sortBy=submittedDate&sortOrder=descending - 429 Client Error: Unknown Error for url: https://export.arxiv.org/api/query?search_query=cat:cs.CL&max_results=20&sortBy=submittedDate&sortOrder=descending"}
{"timestamp": "2026-05-28T10:30:24.888521", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 20 条 (新增 20)"}
{"timestamp": "2026-05-28T10:30:24.888521", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: arXiv cs.AI"}
{"timestamp": "2026-05-28T10:30:55.005211", "level": "WARNING", "name": "IntelligenceOS", "message": "Request failed (1/3): http://export.arxiv.org/api/query?search_query=cat:cs.AI&max_results=20&sortBy=submittedDate&sortOrder=descending - HTTPSConnectionPool(host='export.arxiv.org', port=443): Read timed out. (read timeout=30)"}
{"timestamp": "2026-05-28T10:30:57.438182", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 20 条 (新增 20)"}
{"timestamp": "2026-05-28T10:30:57.438182", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: arXiv cs.DC"}
{"timestamp": "2026-05-28T10:31:12.848865", "level": "WARNING", "name": "IntelligenceOS", "message": "Request failed (1/3): http://export.arxiv.org/api/query?search_query=cat:cs.DC&max_results=20&sortBy=submittedDate&sortOrder=descending - 429 Client Error: Too Many Requests for url: https://export.arxiv.org/api/query?search_query=cat:cs.DC&max_results=20&sortBy=submittedDate&sortOrder=descending"}
{"timestamp": "2026-05-28T10:31:43.953636", "level": "WARNING", "name": "IntelligenceOS", "message": "Request failed (2/3): http://export.arxiv.org/api/query?search_query=cat:cs.DC&max_results=20&sortBy=submittedDate&sortOrder=descending - HTTPSConnectionPool(host='export.arxiv.org', port=443): Read timed out. (read timeout=30)"}
{"timestamp": "2026-05-28T10:32:16.171428", "level": "WARNING", "name": "IntelligenceOS", "message": "Request failed (3/3): http://export.arxiv.org/api/query?search_query=cat:cs.DC&max_results=20&sortBy=submittedDate&sortOrder=descending - HTTPSConnectionPool(host='export.arxiv.org', port=443): Read timed out. (read timeout=30)"}
{"timestamp": "2026-05-28T10:32:16.171428", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 0 条 (新增 0)"}
{"timestamp": "2026-05-28T10:32:16.171428", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: arXiv cs.MA"}
{"timestamp": "2026-05-28T10:32:31.903906", "level": "WARNING", "name": "IntelligenceOS", "message": "Request failed (1/3): http://export.arxiv.org/api/query?search_query=cat:cs.MA&max_results=20&sortBy=submittedDate&sortOrder=descending - 429 Client Error: Too Many Requests for url: https://export.arxiv.org/api/query?search_query=cat:cs.MA&max_results=20&sortBy=submittedDate&sortOrder=descending"}
{"timestamp": "2026-05-28T10:32:33.203803", "level": "WARNING", "name": "IntelligenceOS", "message": "Request failed (2/3): http://export.arxiv.org/api/query?search_query=cat:cs.MA&max_results=20&sortBy=submittedDate&sortOrder=descending - 429 Client Error: Unknown Error for url: https://export.arxiv.org/api/query?search_query=cat:cs.MA&max_results=20&sortBy=submittedDate&sortOrder=descending"}
{"timestamp": "2026-05-28T10:32:50.950520", "level": "WARNING", "name": "IntelligenceOS", "message": "Request failed (3/3): http://export.arxiv.org/api/query?search_query=cat:cs.MA&max_results=20&sortBy=submittedDate&sortOrder=descending - 429 Client Error: Too Many Requests for url: https://export.arxiv.org/api/query?search_query=cat:cs.MA&max_results=20&sortBy=submittedDate&sortOrder=descending"}
{"timestamp": "2026-05-28T10:32:50.950520", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 0 条 (新增 0)"}
{"timestamp": "2026-05-28T10:32:50.950520", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: vLLM Releases"}
{"timestamp": "2026-05-28T10:32:53.118420", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 10 条 (新增 10)"}
{"timestamp": "2026-05-28T10:32:53.119016", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: SGLang Releases"}
{"timestamp": "2026-05-28T10:32:58.166968", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 10 条 (新增 10)"}
{"timestamp": "2026-05-28T10:32:58.166968", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: DeepSeek Releases"}
{"timestamp": "2026-05-28T10:32:59.493317", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 1 条 (新增 1)"}
{"timestamp": "2026-05-28T10:32:59.493317", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: Qwen Releases"}
{"timestamp": "2026-05-28T10:33:01.070232", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 0 条 (新增 0)"}
{"timestamp": "2026-05-28T10:33:01.070232", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: PyTorch Blog"}
{"timestamp": "2026-05-28T10:33:20.352120", "level": "WARNING", "name": "IntelligenceOS", "message": "Request failed (1/3): https://pytorch.org/blog/feed.xml - ('Connection aborted.', ConnectionResetError(10054, 'An existing connection was forcibly closed by the remote host', None, 10054, None))"}
{"timestamp": "2026-05-28T10:33:40.735539", "level": "WARNING", "name": "IntelligenceOS", "message": "Request failed (2/3): https://pytorch.org/blog/feed.xml - ('Connection aborted.', ConnectionResetError(10054, 'An existing connection was forcibly closed by the remote host', None, 10054, None))"}
{"timestamp": "2026-05-28T10:34:02.002094", "level": "WARNING", "name": "IntelligenceOS", "message": "Request failed (3/3): https://pytorch.org/blog/feed.xml - ('Connection aborted.', ConnectionResetError(10054, 'An existing connection was forcibly closed by the remote host', None, 10054, None))"}
{"timestamp": "2026-05-28T10:34:02.003095", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 0 条 (新增 0)"}
{"timestamp": "2026-05-28T10:34:02.003095", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: Google DeepMind Blog"}
{"timestamp": "2026-05-28T10:34:03.438044", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 30 条 (新增 30)"}
{"timestamp": "2026-05-28T10:34:03.438044", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: OpenAI Blog"}
{"timestamp": "2026-05-28T10:34:06.160101", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 30 条 (新增 30)"}
{"timestamp": "2026-05-28T10:34:06.160101", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: LMSYS Releases"}
{"timestamp": "2026-05-28T10:34:08.352535", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 10 条 (新增 10)"}
{"timestamp": "2026-05-28T10:34:08.352535", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: SWE-Bench Releases"}
{"timestamp": "2026-05-28T10:34:10.002514", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 10 条 (新增 10)"}
{"timestamp": "2026-05-28T10:34:10.002514", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: AutoGen Releases"}
{"timestamp": "2026-05-28T10:34:16.610969", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 10 条 (新增 10)"}
{"timestamp": "2026-05-28T10:34:16.610969", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: DSPy Releases"}
{"timestamp": "2026-05-28T10:34:33.302788", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 10 条 (新增 10)"}
{"timestamp": "2026-05-28T10:34:33.302788", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: LangChain Releases"}
{"timestamp": "2026-05-28T10:34:35.278320", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 10 条 (新增 10)"}
{"timestamp": "2026-05-28T10:34:35.278320", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: LlamaIndex Releases"}
{"timestamp": "2026-05-28T10:34:38.043595", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 10 条 (新增 10)"}
{"timestamp": "2026-05-28T10:34:38.043595", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: DeepSpeed Releases"}
{"timestamp": "2026-05-28T10:34:40.635333", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 10 条 (新增 10)"}
{"timestamp": "2026-05-28T10:34:40.635333", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: FlashAttention Releases"}
{"timestamp": "2026-05-28T10:34:41.902598", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 0 条 (新增 0)"}
{"timestamp": "2026-05-28T10:34:41.902598", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: TensorRT-LLM Releases"}
{"timestamp": "2026-05-28T10:34:45.852201", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 10 条 (新增 10)"}
{"timestamp": "2026-05-28T10:34:45.852201", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: llama.cpp Releases"}
{"timestamp": "2026-05-28T10:34:47.943728", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 10 条 (新增 10)"}
{"timestamp": "2026-05-28T10:34:47.943728", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: 量子位"}
{"timestamp": "2026-05-28T10:34:51.741511", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 10 条 (新增 10)"}
{"timestamp": "2026-05-28T10:34:51.741511", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: TechCrunch AI"}
{"timestamp": "2026-05-28T10:34:53.052100", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 20 条 (新增 20)"}
{"timestamp": "2026-05-28T10:34:53.052100", "level": "INFO", "name": "IntelligenceOS", "message": "METRIC: crawled=281", "metric": true}
{"timestamp": "2026-05-28T10:34:53.052100", "level": "INFO", "name": "IntelligenceOS", "message": "METRIC: new_signals=281", "metric": true}
{"timestamp": "2026-05-28T10:34:53.052100", "level": "INFO", "name": "IntelligenceOS", "message": "采集完成: 281 条信号"}
{"timestamp": "2026-05-28T10:34:53.052100", "level": "INFO", "name": "IntelligenceOS", "message": "STEP: CRAWL [COMPLETED]", "step": "CRAWL", "status": "COMPLETED", "count": 281}
{"timestamp": "2026-05-28T10:34:53.052100", "level": "INFO", "name": "IntelligenceOS", "message": "STEP: CLASSIFY [STARTED]", "step": "CLASSIFY", "status": "STARTED"}
{"timestamp": "2026-05-28T10:35:06.769155", "level": "ERROR", "name": "IntelligenceOS", "message": "LLM classification error: Unterminated string starting at: line 1 column 1 (char 0)"}
{"timestamp": "2026-05-28T10:35:12.579396", "level": "ERROR", "name": "IntelligenceOS", "message": "LLM classification error: Unterminated string starting at: line 1 column 1 (char 0)"}
{"timestamp": "2026-05-28T10:35:22.001975", "level": "ERROR", "name": "IntelligenceOS", "message": "LLM classification error: Unterminated string starting at: line 1 column 1 (char 0)"}
{"timestamp": "2026-05-28T10:35:33.902063", "level": "ERROR", "name": "IntelligenceOS", "message": "LLM classification error: Unterminated string starting at: line 1 column 1 (char 0)"}
{"timestamp": "2026-05-28T10:37:38.732897", "level": "ERROR", "name": "IntelligenceOS", "message": "LLM classification error: HTTPSConnectionPool(host='api.minimax.chat', port=443): Read timed out. (read timeout=120)"}
{"timestamp": "2026-05-28T10:37:43.290592", "level": "ERROR", "name": "IntelligenceOS", "message": "LLM classification error: Unterminated string starting at: line 1 column 1 (char 0)"}
{"timestamp": "2026-05-28T10:37:57.135888", "level": "ERROR", "name": "IntelligenceOS", "message": "LLM classification error: Unterminated string starting at: line 1 column 1 (char 0)"}
{"timestamp": "2026-05-28T10:38:06.100308", "level": "ERROR", "name": "IntelligenceOS", "message": "LLM classification error: Unterminated string starting at: line 1 column 1 (char 0)"}
{"timestamp": "2026-05-28T10:38:32.316712", "level": "ERROR", "name": "IntelligenceOS", "message": "LLM classification error: Unterminated string starting at: line 1 column 1 (char 0)"}
{"timestamp": "2026-05-28T10:38:56.913223", "level": "ERROR", "name": "IntelligenceOS", "message": "LLM classification error: Unterminated string starting at: line 1 column 1 (char 0)"}
{"timestamp": "2026-05-28T10:39:05.207564", "level": "ERROR", "name": "IntelligenceOS", "message": "LLM classification error: Unterminated string starting at: line 1 column 1 (char 0)"}
{"timestamp": "2026-05-28T10:39:19.816401", "level": "ERROR", "name": "IntelligenceOS", "message": "LLM classification error: Unterminated string starting at: line 1 column 1 (char 0)"}
{"timestamp": "2026-05-28T10:39:24.149685", "level": "ERROR", "name": "IntelligenceOS", "message": "LLM classification error: Unterminated string starting at: line 1 column 1 (char 0)"}
{"timestamp": "2026-05-28T10:39:28.366136", "level": "ERROR", "name": "IntelligenceOS", "message": "LLM classification error: Unterminated string starting at: line 1 column 1 (char 0)"}
{"timestamp": "2026-05-28T10:39:38.932269", "level": "ERROR", "name": "IntelligenceOS", "message": "LLM classification error: Unterminated string starting at: line 1 column 1 (char 0)"}
{"timestamp": "2026-05-28T10:39:42.465563", "level": "ERROR", "name": "IntelligenceOS", "message": "LLM classification error: Unterminated string starting at: line 1 column 1 (char 0)"}
{"timestamp": "2026-05-28T10:41:48.914062", "level": "INFO", "name": "IntelligenceOS", "message": "IntelligenceOS initialized"}
{"timestamp": "2026-05-28T10:41:49.463903", "level": "INFO", "name": "IntelligenceOS", "message": "已保存 50 条事件 (进度 50/100)"}
{"timestamp": "2026-05-28T10:41:49.997428", "level": "INFO", "name": "IntelligenceOS", "message": "已保存 50 条事件 (进度 100/100)"}
{"timestamp": "2026-05-28T10:41:49.997428", "level": "INFO", "name": "IntelligenceOS", "message": "METRIC: classified=100", "metric": true}
{"timestamp": "2026-05-28T10:41:49.997428", "level": "INFO", "name": "IntelligenceOS", "message": "分类完成: 100 条事件, 错误 0 条"}
{"timestamp": "2026-05-28T10:42:05.397286", "level": "INFO", "name": "IntelligenceOS", "message": "IntelligenceOS initialized"}
{"timestamp": "2026-05-28T10:42:16.713867", "level": "INFO", "name": "IntelligenceOS", "message": "METRIC: reports_generated=1", "metric": true}
{"timestamp": "2026-05-28T10:42:16.713867", "level": "INFO", "name": "IntelligenceOS", "message": "Saved daily report: C:\\Users\\Huawei\\Documents\\code\\Obsidian\\2_工作流层\\Daily\\2026-05-28.md"}
{"timestamp": "2026-05-28T10:43:03.663228", "level": "INFO", "name": "IntelligenceOS", "message": "IntelligenceOS initialized"}
{"timestamp": "2026-05-28T10:45:04.410965", "level": "ERROR", "name": "IntelligenceOS", "message": "Failed to generate weekly report: HTTPSConnectionPool(host='api.minimax.chat', port=443): Read timed out. (read timeout=120)"}
{"timestamp": "2026-05-28T10:45:04.428687", "level": "INFO", "name": "IntelligenceOS", "message": "METRIC: reports_generated=1", "metric": true}
{"timestamp": "2026-05-28T10:45:04.428687", "level": "INFO", "name": "IntelligenceOS", "message": "Saved weekly report: C:\\Users\\Huawei\\Documents\\code\\Obsidian\\2_工作流层\\Weekly\\Weekly_2026-W22.md"}
{"timestamp": "2026-05-28T10:45:24.695268", "level": "INFO", "name": "IntelligenceOS", "message": "METRIC: reports_generated=1", "metric": true}
{"timestamp": "2026-05-28T10:45:24.695268", "level": "INFO", "name": "IntelligenceOS", "message": "Saved technical report: C:\\Users\\Huawei\\Documents\\code\\Obsidian\\2_工作流层\\Weekly\\技术收敛_2026-05-28_821e617f.md"}
{"timestamp": "2026-05-28T10:48:44.993078", "level": "INFO", "name": "IntelligenceOS", "message": "IntelligenceOS initialized"}
{"timestamp": "2026-05-28T10:50:45.714103", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1 failed: HTTPSConnectionPool(host='api.minimax.chat', port=443): Read timed out. (read timeout=120)"}
{"timestamp": "2026-05-28T10:52:48.363100", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 2 failed: HTTPSConnectionPool(host='api.minimax.chat', port=443): Read timed out. (read timeout=120)"}
{"timestamp": "2026-05-28T10:54:24.937739", "level": "INFO", "name": "IntelligenceOS", "message": "IntelligenceOS initialized"}
{"timestamp": "2026-05-28T10:54:46.271993", "level": "INFO", "name": "IntelligenceOS", "message": "METRIC: reports_generated=1", "metric": true}
{"timestamp": "2026-05-28T10:54:46.273686", "level": "INFO", "name": "IntelligenceOS", "message": "Saved daily report: C:\\Users\\Huawei\\Documents\\code\\Obsidian\\2_工作流层\\Daily\\2026-05-28.md"}
{"timestamp": "2026-05-28T10:55:49.337902", "level": "INFO", "name": "IntelligenceOS", "message": "Saved weekly report: C:\\Users\\Huawei\\Documents\\code\\Obsidian\\2_工作流层\\Weekly\\Weekly_2026-W22.md"}
{"timestamp": "2026-05-28T11:14:15.190300", "level": "INFO", "name": "IntelligenceOS", "message": "IntelligenceOS initialized"}
{"timestamp": "2026-05-28T11:14:15.190300", "level": "INFO", "name": "IntelligenceOS", "message": "============================================================"}
{"timestamp": "2026-05-28T11:14:15.190300", "level": "INFO", "name": "IntelligenceOS", "message": "AI Intelligence OS - 每日流水线"}
{"timestamp": "2026-05-28T11:14:15.190300", "level": "INFO", "name": "IntelligenceOS", "message": "开始时间: 2026-05-28 11:14:15"}
{"timestamp": "2026-05-28T11:14:15.190300", "level": "INFO", "name": "IntelligenceOS", "message": "============================================================"}
{"timestamp": "2026-05-28T11:14:15.190300", "level": "INFO", "name": "IntelligenceOS", "message": "STEP: CRAWL [STARTED]", "step": "CRAWL", "status": "STARTED"}
{"timestamp": "2026-05-28T11:14:15.190300", "level": "INFO", "name": "IntelligenceOS", "message": "开始采集 25 个信源..."}
{"timestamp": "2026-05-28T11:14:15.190300", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: HuggingFace Daily Papers"}
{"timestamp": "2026-05-28T11:14:16.577903", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 20 条 (新增 20)"}
{"timestamp": "2026-05-28T11:14:16.577903", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: arXiv cs.LG"}
{"timestamp": "2026-05-28T11:14:18.023085", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 20 条 (新增 20)"}
{"timestamp": "2026-05-28T11:14:18.023085", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: arXiv cs.CL"}
{"timestamp": "2026-05-28T11:14:19.309731", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 20 条 (新增 20)"}
{"timestamp": "2026-05-28T11:14:19.309731", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: arXiv cs.AI"}
{"timestamp": "2026-05-28T11:14:20.602432", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 20 条 (新增 20)"}
{"timestamp": "2026-05-28T11:14:20.603085", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: arXiv cs.DC"}
{"timestamp": "2026-05-28T11:14:35.291739", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 20 条 (新增 20)"}
{"timestamp": "2026-05-28T11:14:35.291739", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: arXiv cs.MA"}
{"timestamp": "2026-05-28T11:15:05.609089", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 20 条 (新增 20)"}
{"timestamp": "2026-05-28T11:15:05.609089", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: vLLM Releases"}
{"timestamp": "2026-05-28T11:15:07.911699", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 10 条 (新增 10)"}
{"timestamp": "2026-05-28T11:15:07.911699", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: SGLang Releases"}
{"timestamp": "2026-05-28T11:15:15.605018", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 10 条 (新增 10)"}
{"timestamp": "2026-05-28T11:15:15.605018", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: DeepSeek Releases"}
{"timestamp": "2026-05-28T11:15:16.948302", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 1 条 (新增 1)"}
{"timestamp": "2026-05-28T11:15:16.948302", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: Qwen Releases"}
{"timestamp": "2026-05-28T11:15:18.443757", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 0 条 (新增 0)"}
{"timestamp": "2026-05-28T11:15:18.443757", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: PyTorch Blog"}
{"timestamp": "2026-05-28T11:15:37.708232", "level": "WARNING", "name": "IntelligenceOS", "message": "Request failed (1/3): https://pytorch.org/blog/feed.xml - ('Connection aborted.', ConnectionResetError(10054, 'An existing connection was forcibly closed by the remote host', None, 10054, None))"}
{"timestamp": "2026-05-28T11:15:58.032599", "level": "WARNING", "name": "IntelligenceOS", "message": "Request failed (2/3): https://pytorch.org/blog/feed.xml - ('Connection aborted.', ConnectionResetError(10054, 'An existing connection was forcibly closed by the remote host', None, 10054, None))"}
{"timestamp": "2026-05-28T11:16:19.300205", "level": "WARNING", "name": "IntelligenceOS", "message": "Request failed (3/3): https://pytorch.org/blog/feed.xml - ('Connection aborted.', ConnectionResetError(10054, 'An existing connection was forcibly closed by the remote host', None, 10054, None))"}
{"timestamp": "2026-05-28T11:16:19.300205", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 0 条 (新增 0)"}
{"timestamp": "2026-05-28T11:16:19.300205", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: Google DeepMind Blog"}
{"timestamp": "2026-05-28T11:16:20.708605", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 30 条 (新增 30)"}
{"timestamp": "2026-05-28T11:16:20.708605", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: OpenAI Blog"}
{"timestamp": "2026-05-28T11:16:23.159451", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 30 条 (新增 30)"}
{"timestamp": "2026-05-28T11:16:23.159451", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: LMSYS Releases"}
{"timestamp": "2026-05-28T11:16:25.442333", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 10 条 (新增 10)"}
{"timestamp": "2026-05-28T11:16:25.442333", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: SWE-Bench Releases"}
{"timestamp": "2026-05-28T11:16:27.070207", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 10 条 (新增 10)"}
{"timestamp": "2026-05-28T11:16:27.070207", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: AutoGen Releases"}
{"timestamp": "2026-05-28T11:16:29.020035", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 10 条 (新增 10)"}
{"timestamp": "2026-05-28T11:16:29.020035", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: DSPy Releases"}
{"timestamp": "2026-05-28T11:16:31.828736", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 10 条 (新增 10)"}
{"timestamp": "2026-05-28T11:16:31.828736", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: LangChain Releases"}
{"timestamp": "2026-05-28T11:16:34.477386", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 10 条 (新增 10)"}
{"timestamp": "2026-05-28T11:16:34.477386", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: LlamaIndex Releases"}
{"timestamp": "2026-05-28T11:16:37.526601", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 10 条 (新增 10)"}
{"timestamp": "2026-05-28T11:16:37.526601", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: DeepSpeed Releases"}
{"timestamp": "2026-05-28T11:16:40.195926", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 10 条 (新增 10)"}
{"timestamp": "2026-05-28T11:16:40.195926", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: FlashAttention Releases"}
{"timestamp": "2026-05-28T11:16:41.383995", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 0 条 (新增 0)"}
{"timestamp": "2026-05-28T11:16:41.383995", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: TensorRT-LLM Releases"}
{"timestamp": "2026-05-28T11:16:47.419792", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 10 条 (新增 10)"}
{"timestamp": "2026-05-28T11:16:47.419792", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: llama.cpp Releases"}
{"timestamp": "2026-05-28T11:16:49.810041", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 10 条 (新增 10)"}
{"timestamp": "2026-05-28T11:16:49.810041", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: 量子位"}
{"timestamp": "2026-05-28T11:17:01.644660", "level": "WARNING", "name": "IntelligenceOS", "message": "Request failed (1/3): https://www.qbitai.com/rss - ('Connection aborted.', ConnectionResetError(10054, 'An existing connection was forcibly closed by the remote host', None, 10054, None))"}
{"timestamp": "2026-05-28T11:17:05.973869", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 10 条 (新增 10)"}
{"timestamp": "2026-05-28T11:17:05.975621", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: TechCrunch AI"}
{"timestamp": "2026-05-28T11:17:07.284566", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 20 条 (新增 20)"}
{"timestamp": "2026-05-28T11:17:07.284566", "level": "INFO", "name": "IntelligenceOS", "message": "METRIC: crawled=321", "metric": true}
{"timestamp": "2026-05-28T11:17:07.284566", "level": "INFO", "name": "IntelligenceOS", "message": "METRIC: new_signals=321", "metric": true}
{"timestamp": "2026-05-28T11:17:07.284566", "level": "INFO", "name": "IntelligenceOS", "message": "采集完成: 321 条信号"}
{"timestamp": "2026-05-28T11:17:07.284566", "level": "INFO", "name": "IntelligenceOS", "message": "STEP: CRAWL [COMPLETED]", "step": "CRAWL", "status": "COMPLETED", "count": 321}
{"timestamp": "2026-05-28T11:17:07.284566", "level": "INFO", "name": "IntelligenceOS", "message": "STEP: CLASSIFY [STARTED]", "step": "CLASSIFY", "status": "STARTED"}
{"timestamp": "2026-05-28T11:17:07.858416", "level": "INFO", "name": "IntelligenceOS", "message": "已保存 50 条事件 (进度 50/321)"}
{"timestamp": "2026-05-28T11:17:08.444958", "level": "INFO", "name": "IntelligenceOS", "message": "已保存 50 条事件 (进度 100/321)"}
{"timestamp": "2026-05-28T11:17:09.049725", "level": "INFO", "name": "IntelligenceOS", "message": "已保存 50 条事件 (进度 150/321)"}
{"timestamp": "2026-05-28T11:17:09.638393", "level": "INFO", "name": "IntelligenceOS", "message": "已保存 50 条事件 (进度 200/321)"}
{"timestamp": "2026-05-28T11:17:10.157537", "level": "INFO", "name": "IntelligenceOS", "message": "已保存 50 条事件 (进度 250/321)"}
{"timestamp": "2026-05-28T11:17:10.673322", "level": "INFO", "name": "IntelligenceOS", "message": "已保存 50 条事件 (进度 300/321)"}
{"timestamp": "2026-05-28T11:17:10.895522", "level": "INFO", "name": "IntelligenceOS", "message": "已保存最后 21 条事件"}
{"timestamp": "2026-05-28T11:17:10.895522", "level": "INFO", "name": "IntelligenceOS", "message": "METRIC: classified=321", "metric": true}
{"timestamp": "2026-05-28T11:17:10.895522", "level": "INFO", "name": "IntelligenceOS", "message": "分类完成: 321 条事件, 错误 0 条"}
{"timestamp": "2026-05-28T11:17:11.024247", "level": "INFO", "name": "IntelligenceOS", "message": "分类完成: 21 条事件, 保存 21 条"}
{"timestamp": "2026-05-28T11:17:11.024247", "level": "INFO", "name": "IntelligenceOS", "message": "STEP: CLASSIFY [COMPLETED]", "step": "CLASSIFY", "status": "COMPLETED", "count": 21, "saved": 21}
{"timestamp": "2026-05-28T11:17:11.024247", "level": "INFO", "name": "IntelligenceOS", "message": "STEP: TREND [STARTED]", "step": "TREND", "status": "STARTED"}
{"timestamp": "2026-05-28T11:17:11.092976", "level": "INFO", "name": "IntelligenceOS", "message": "趋势分析: 5 热门技术"}
{"timestamp": "2026-05-28T11:17:11.092976", "level": "INFO", "name": "IntelligenceOS", "message": "STEP: TREND [COMPLETED]", "step": "TREND", "status": "COMPLETED", "trending": 5}
{"timestamp": "2026-05-28T11:17:11.092976", "level": "INFO", "name": "IntelligenceOS", "message": "STEP: QUALITY [STARTED]", "step": "QUALITY", "status": "STARTED"}
{"timestamp": "2026-05-28T11:17:11.092976", "level": "INFO", "name": "IntelligenceOS", "message": "Quality check: PASSED", "issues": 0}
{"timestamp": "2026-05-28T11:17:11.092976", "level": "WARNING", "name": "IntelligenceOS", "message": "质量门禁未通过: ['信源健康度不佳，优先处理失败信源']"}
{"timestamp": "2026-05-28T11:17:11.092976", "level": "INFO", "name": "IntelligenceOS", "message": "STEP: QUALITY [FAILED]", "step": "QUALITY", "status": "FAILED", "issues": []}
{"timestamp": "2026-05-28T11:17:11.092976", "level": "INFO", "name": "IntelligenceOS", "message": "STEP: QUALITY [PROCEEDING]", "step": "QUALITY", "status": "PROCEEDING", "reason": "force_or_partial"}
{"timestamp": "2026-05-28T11:17:11.092976", "level": "INFO", "name": "IntelligenceOS", "message": "STEP: REPORT [STARTED]", "step": "REPORT", "status": "STARTED"}
{"timestamp": "2026-05-28T11:17:43.970380", "level": "INFO", "name": "IntelligenceOS", "message": "METRIC: reports_generated=1", "metric": true}
{"timestamp": "2026-05-28T11:17:54.883361", "level": "INFO", "name": "IntelligenceOS", "message": "METRIC: reports_generated=1", "metric": true}
{"timestamp": "2026-05-28T11:17:54.883361", "level": "INFO", "name": "IntelligenceOS", "message": "报告生成: Daily + Weekly"}
{"timestamp": "2026-05-28T11:17:54.883361", "level": "INFO", "name": "IntelligenceOS", "message": "STEP: REPORT [COMPLETED]", "step": "REPORT", "status": "COMPLETED", "daily": "fb598af9e7acb627", "weekly": "46e96e49c51b1715"}
{"timestamp": "2026-05-28T11:17:54.883361", "level": "INFO", "name": "IntelligenceOS", "message": "STEP: OUTPUT [STARTED]", "step": "OUTPUT", "status": "STARTED"}
{"timestamp": "2026-05-28T11:17:54.883361", "level": "INFO", "name": "IntelligenceOS", "message": "Saved daily report: C:\\Users\\Huawei\\Documents\\code\\Obsidian\\2_工作流层\\Daily\\2026-05-28.md"}
{"timestamp": "2026-05-28T11:17:54.883361", "level": "INFO", "name": "IntelligenceOS", "message": "Saved weekly report: C:\\Users\\Huawei\\Documents\\code\\Obsidian\\2_工作流层\\Weekly\\Weekly_2026-W22.md"}
{"timestamp": "2026-05-28T11:17:54.883361", "level": "INFO", "name": "IntelligenceOS", "message": "报告已输出到Obsidian"}
{"timestamp": "2026-05-28T11:17:54.883361", "level": "INFO", "name": "IntelligenceOS", "message": "STEP: OUTPUT [COMPLETED]", "step": "OUTPUT", "status": "COMPLETED"}
{"timestamp": "2026-05-28T11:17:54.883361", "level": "INFO", "name": "IntelligenceOS", "message": "============================================================"}
{"timestamp": "2026-05-28T11:17:54.883361", "level": "INFO", "name": "IntelligenceOS", "message": "每日流水线完成"}
{"timestamp": "2026-05-28T11:17:54.883361", "level": "INFO", "name": "IntelligenceOS", "message": "  采集: 321 条信号"}
{"timestamp": "2026-05-28T11:17:54.883361", "level": "INFO", "name": "IntelligenceOS", "message": "  分类: 21 条事件"}
{"timestamp": "2026-05-28T11:17:54.883361", "level": "INFO", "name": "IntelligenceOS", "message": "  质量门禁: 未通过"}
{"timestamp": "2026-05-28T11:17:54.883361", "level": "INFO", "name": "IntelligenceOS", "message": "  报告: 2 份"}
{"timestamp": "2026-05-28T11:17:54.883361", "level": "INFO", "name": "IntelligenceOS", "message": "  错误: 0 个"}
{"timestamp": "2026-05-28T11:17:54.883361", "level": "INFO", "name": "IntelligenceOS", "message": "  耗时: 219.7 秒"}
{"timestamp": "2026-05-28T11:17:54.883361", "level": "INFO", "name": "IntelligenceOS", "message": "============================================================"}
{"timestamp": "2026-05-28T11:17:54.883361", "level": "INFO", "name": "IntelligenceOS", "message": "METRIC: daily_pipeline_completed=1", "metric": true}
{"timestamp": "2026-05-28T11:22:31.424041", "level": "INFO", "name": "IntelligenceOS", "message": "IntelligenceOS initialized"}
{"timestamp": "2026-05-28T11:22:31.424041", "level": "INFO", "name": "IntelligenceOS", "message": "============================================================"}
{"timestamp": "2026-05-28T11:22:31.424041", "level": "INFO", "name": "IntelligenceOS", "message": "AI Intelligence OS - 每日流水线"}
{"timestamp": "2026-05-28T11:22:31.424041", "level": "INFO", "name": "IntelligenceOS", "message": "开始时间: 2026-05-28 11:22:31"}
{"timestamp": "2026-05-28T11:22:31.424041", "level": "INFO", "name": "IntelligenceOS", "message": "============================================================"}
{"timestamp": "2026-05-28T11:22:31.424041", "level": "INFO", "name": "IntelligenceOS", "message": "STEP: CRAWL [STARTED]", "step": "CRAWL", "status": "STARTED"}
{"timestamp": "2026-05-28T11:22:31.424041", "level": "INFO", "name": "IntelligenceOS", "message": "开始采集 25 个信源..."}
{"timestamp": "2026-05-28T11:22:31.424041", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: HuggingFace Daily Papers"}
{"timestamp": "2026-05-28T11:22:32.843267", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 20 条 (新增 20)"}
{"timestamp": "2026-05-28T11:22:32.843267", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: arXiv cs.LG"}
{"timestamp": "2026-05-28T11:22:34.352993", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 20 条 (新增 20)"}
{"timestamp": "2026-05-28T11:22:34.352993", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: arXiv cs.CL"}
{"timestamp": "2026-05-28T11:22:35.656096", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 20 条 (新增 20)"}
{"timestamp": "2026-05-28T11:22:35.656096", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: arXiv cs.AI"}
{"timestamp": "2026-05-28T11:22:37.005863", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 20 条 (新增 20)"}
{"timestamp": "2026-05-28T11:22:37.005863", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: arXiv cs.DC"}
{"timestamp": "2026-05-28T11:22:38.302952", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 20 条 (新增 20)"}
{"timestamp": "2026-05-28T11:22:38.302952", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: arXiv cs.MA"}
{"timestamp": "2026-05-28T11:22:39.636241", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 20 条 (新增 20)"}
{"timestamp": "2026-05-28T11:22:39.636241", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: vLLM Releases"}
{"timestamp": "2026-05-28T11:22:42.018379", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 10 条 (新增 10)"}
{"timestamp": "2026-05-28T11:22:42.018379", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: SGLang Releases"}
{"timestamp": "2026-05-28T11:22:47.608687", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 10 条 (新增 10)"}
{"timestamp": "2026-05-28T11:22:47.608687", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: DeepSeek Releases"}
{"timestamp": "2026-05-28T11:22:48.930860", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 1 条 (新增 1)"}
{"timestamp": "2026-05-28T11:22:48.930860", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: Qwen Releases"}
{"timestamp": "2026-05-28T11:22:50.354919", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 0 条 (新增 0)"}
{"timestamp": "2026-05-28T11:22:50.354919", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: PyTorch Blog"}
{"timestamp": "2026-05-28T11:23:00.036089", "level": "WARNING", "name": "IntelligenceOS", "message": "Request failed (1/3): https://pytorch.org/blog/feed.xml - ('Connection aborted.', ConnectionResetError(10054, 'An existing connection was forcibly closed by the remote host', None, 10054, None))"}
{"timestamp": "2026-05-28T11:23:20.285949", "level": "WARNING", "name": "IntelligenceOS", "message": "Request failed (2/3): https://pytorch.org/blog/feed.xml - ('Connection aborted.', ConnectionResetError(10054, 'An existing connection was forcibly closed by the remote host', None, 10054, None))"}
{"timestamp": "2026-05-28T11:23:41.568913", "level": "WARNING", "name": "IntelligenceOS", "message": "Request failed (3/3): https://pytorch.org/blog/feed.xml - ('Connection aborted.', ConnectionResetError(10054, 'An existing connection was forcibly closed by the remote host', None, 10054, None))"}
{"timestamp": "2026-05-28T11:23:41.568913", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 0 条 (新增 0)"}
{"timestamp": "2026-05-28T11:23:41.568913", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: Google DeepMind Blog"}
{"timestamp": "2026-05-28T11:23:43.006140", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 30 条 (新增 30)"}
{"timestamp": "2026-05-28T11:23:43.008147", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: OpenAI Blog"}
{"timestamp": "2026-05-28T11:23:45.459783", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 30 条 (新增 30)"}
{"timestamp": "2026-05-28T11:23:45.459783", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: LMSYS Releases"}
{"timestamp": "2026-05-28T11:23:47.828434", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 10 条 (新增 10)"}
{"timestamp": "2026-05-28T11:23:47.828434", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: SWE-Bench Releases"}
{"timestamp": "2026-05-28T11:23:50.196456", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 10 条 (新增 10)"}
{"timestamp": "2026-05-28T11:23:50.196456", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: AutoGen Releases"}
{"timestamp": "2026-05-28T11:23:52.185340", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 10 条 (新增 10)"}
{"timestamp": "2026-05-28T11:23:52.185340", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: DSPy Releases"}
{"timestamp": "2026-05-28T11:23:54.552041", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 10 条 (新增 10)"}
{"timestamp": "2026-05-28T11:23:54.552041", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: LangChain Releases"}
{"timestamp": "2026-05-28T11:23:56.646241", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 10 条 (新增 10)"}
{"timestamp": "2026-05-28T11:23:56.646241", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: LlamaIndex Releases"}
{"timestamp": "2026-05-28T11:23:59.551996", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 10 条 (新增 10)"}
{"timestamp": "2026-05-28T11:23:59.551996", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: DeepSpeed Releases"}
{"timestamp": "2026-05-28T11:24:02.094285", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 10 条 (新增 10)"}
{"timestamp": "2026-05-28T11:24:02.094285", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: FlashAttention Releases"}
{"timestamp": "2026-05-28T11:24:03.318654", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 0 条 (新增 0)"}
{"timestamp": "2026-05-28T11:24:03.320661", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: TensorRT-LLM Releases"}
{"timestamp": "2026-05-28T11:24:07.487352", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 10 条 (新增 10)"}
{"timestamp": "2026-05-28T11:24:07.487352", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: llama.cpp Releases"}
{"timestamp": "2026-05-28T11:24:09.742082", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 10 条 (新增 10)"}
{"timestamp": "2026-05-28T11:24:09.742082", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: 量子位"}
{"timestamp": "2026-05-28T11:24:12.768655", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 10 条 (新增 10)"}
{"timestamp": "2026-05-28T11:24:12.768655", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: TechCrunch AI"}
{"timestamp": "2026-05-28T11:24:14.085232", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 20 条 (新增 20)"}
{"timestamp": "2026-05-28T11:24:14.085232", "level": "INFO", "name": "IntelligenceOS", "message": "METRIC: crawled=321", "metric": true}
{"timestamp": "2026-05-28T11:24:14.085232", "level": "INFO", "name": "IntelligenceOS", "message": "METRIC: new_signals=321", "metric": true}
{"timestamp": "2026-05-28T11:24:14.085232", "level": "INFO", "name": "IntelligenceOS", "message": "采集完成: 321 条信号"}
{"timestamp": "2026-05-28T11:24:14.085232", "level": "INFO", "name": "IntelligenceOS", "message": "STEP: CRAWL [COMPLETED]", "step": "CRAWL", "status": "COMPLETED", "count": 321}
{"timestamp": "2026-05-28T11:24:14.085232", "level": "INFO", "name": "IntelligenceOS", "message": "STEP: CLASSIFY [STARTED]", "step": "CLASSIFY", "status": "STARTED"}
{"timestamp": "2026-05-28T11:24:14.685102", "level": "INFO", "name": "IntelligenceOS", "message": "已保存 50 条事件 (进度 50/321)"}
{"timestamp": "2026-05-28T11:24:15.335210", "level": "INFO", "name": "IntelligenceOS", "message": "已保存 50 条事件 (进度 100/321)"}
{"timestamp": "2026-05-28T11:24:15.909206", "level": "INFO", "name": "IntelligenceOS", "message": "已保存 50 条事件 (进度 150/321)"}
{"timestamp": "2026-05-28T11:24:16.457763", "level": "INFO", "name": "IntelligenceOS", "message": "已保存 50 条事件 (进度 200/321)"}
{"timestamp": "2026-05-28T11:24:17.002142", "level": "INFO", "name": "IntelligenceOS", "message": "已保存 50 条事件 (进度 250/321)"}
{"timestamp": "2026-05-28T11:24:17.558414", "level": "INFO", "name": "IntelligenceOS", "message": "已保存 50 条事件 (进度 300/321)"}
{"timestamp": "2026-05-28T11:24:17.789083", "level": "INFO", "name": "IntelligenceOS", "message": "已保存最后 21 条事件"}
{"timestamp": "2026-05-28T11:24:17.789083", "level": "INFO", "name": "IntelligenceOS", "message": "METRIC: classified=321", "metric": true}
{"timestamp": "2026-05-28T11:24:17.789083", "level": "INFO", "name": "IntelligenceOS", "message": "分类完成: 321 条事件, 错误 0 条"}
{"timestamp": "2026-05-28T11:24:18.485155", "level": "INFO", "name": "IntelligenceOS", "message": "分类完成: 21 条事件, 保存 21 条"}
{"timestamp": "2026-05-28T11:24:18.485155", "level": "INFO", "name": "IntelligenceOS", "message": "STEP: CLASSIFY [COMPLETED]", "step": "CLASSIFY", "status": "COMPLETED", "count": 21, "saved": 21}
{"timestamp": "2026-05-28T11:24:18.485155", "level": "INFO", "name": "IntelligenceOS", "message": "STEP: TREND [STARTED]", "step": "TREND", "status": "STARTED"}
{"timestamp": "2026-05-28T11:24:18.551613", "level": "INFO", "name": "IntelligenceOS", "message": "趋势分析: 5 热门技术"}
{"timestamp": "2026-05-28T11:24:18.551613", "level": "INFO", "name": "IntelligenceOS", "message": "STEP: TREND [COMPLETED]", "step": "TREND", "status": "COMPLETED", "trending": 5}
{"timestamp": "2026-05-28T11:24:18.551613", "level": "INFO", "name": "IntelligenceOS", "message": "STEP: QUALITY [STARTED]", "step": "QUALITY", "status": "STARTED"}
{"timestamp": "2026-05-28T11:24:18.551613", "level": "INFO", "name": "IntelligenceOS", "message": "Quality check: PASSED", "issues": 0}
{"timestamp": "2026-05-28T11:24:18.551613", "level": "WARNING", "name": "IntelligenceOS", "message": "质量门禁未通过: ['信源健康度不佳，优先处理失败信源']"}
{"timestamp": "2026-05-28T11:24:18.551613", "level": "INFO", "name": "IntelligenceOS", "message": "STEP: QUALITY [FAILED]", "step": "QUALITY", "status": "FAILED", "issues": []}
{"timestamp": "2026-05-28T11:24:18.551613", "level": "INFO", "name": "IntelligenceOS", "message": "STEP: QUALITY [PROCEEDING]", "step": "QUALITY", "status": "PROCEEDING", "reason": "force_or_partial"}
{"timestamp": "2026-05-28T11:24:18.551613", "level": "INFO", "name": "IntelligenceOS", "message": "STEP: REPORT [STARTED]", "step": "REPORT", "status": "STARTED"}
{"timestamp": "2026-05-28T11:24:18.567455", "level": "INFO", "name": "IntelligenceOS", "message": "METRIC: reports_generated=1", "metric": true}
{"timestamp": "2026-05-28T11:24:18.568469", "level": "ERROR", "name": "IntelligenceOS", "message": "Report阶段失败: '<' not supported between instances of 'TechEvent' and 'TechEvent'"}
{"timestamp": "2026-05-28T11:24:18.568469", "level": "INFO", "name": "IntelligenceOS", "message": "STEP: OUTPUT [STARTED]", "step": "OUTPUT", "status": "STARTED"}
{"timestamp": "2026-05-28T11:24:18.568469", "level": "INFO", "name": "IntelligenceOS", "message": "Saved daily report: C:\\Users\\Huawei\\Documents\\code\\Obsidian\\2_工作流层\\Daily\\2026-05-28.md"}
{"timestamp": "2026-05-28T11:24:18.568469", "level": "ERROR", "name": "IntelligenceOS", "message": "Output阶段失败: local variable 'weekly_report' referenced before assignment"}
{"timestamp": "2026-05-28T11:24:18.568469", "level": "INFO", "name": "IntelligenceOS", "message": "============================================================"}
{"timestamp": "2026-05-28T11:24:18.568469", "level": "INFO", "name": "IntelligenceOS", "message": "每日流水线完成"}
{"timestamp": "2026-05-28T11:24:18.568469", "level": "INFO", "name": "IntelligenceOS", "message": "  采集: 321 条信号"}
{"timestamp": "2026-05-28T11:24:18.568469", "level": "INFO", "name": "IntelligenceOS", "message": "  分类: 21 条事件"}
{"timestamp": "2026-05-28T11:24:18.568469", "level": "INFO", "name": "IntelligenceOS", "message": "  质量门禁: 未通过"}
{"timestamp": "2026-05-28T11:24:18.568469", "level": "INFO", "name": "IntelligenceOS", "message": "  报告: 0 份"}
{"timestamp": "2026-05-28T11:24:18.568469", "level": "INFO", "name": "IntelligenceOS", "message": "  错误: 2 个"}
{"timestamp": "2026-05-28T11:24:18.568469", "level": "INFO", "name": "IntelligenceOS", "message": "  耗时: 107.1 秒"}
{"timestamp": "2026-05-28T11:24:18.568469", "level": "INFO", "name": "IntelligenceOS", "message": "============================================================"}
{"timestamp": "2026-05-28T11:24:18.568469", "level": "INFO", "name": "IntelligenceOS", "message": "METRIC: daily_pipeline_completed=1", "metric": true}
{"timestamp": "2026-05-28T11:25:18.476800", "level": "INFO", "name": "IntelligenceOS", "message": "IntelligenceOS initialized"}
{"timestamp": "2026-05-28T11:25:18.476800", "level": "INFO", "name": "IntelligenceOS", "message": "============================================================"}
{"timestamp": "2026-05-28T11:25:18.476800", "level": "INFO", "name": "IntelligenceOS", "message": "AI Intelligence OS - 每日流水线"}
{"timestamp": "2026-05-28T11:25:18.476800", "level": "INFO", "name": "IntelligenceOS", "message": "开始时间: 2026-05-28 11:25:18"}
{"timestamp": "2026-05-28T11:25:18.476800", "level": "INFO", "name": "IntelligenceOS", "message": "============================================================"}
{"timestamp": "2026-05-28T11:25:18.476800", "level": "INFO", "name": "IntelligenceOS", "message": "STEP: CRAWL [STARTED]", "step": "CRAWL", "status": "STARTED"}
{"timestamp": "2026-05-28T11:25:18.476800", "level": "INFO", "name": "IntelligenceOS", "message": "开始采集 25 个信源..."}
{"timestamp": "2026-05-28T11:25:18.476800", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: HuggingFace Daily Papers"}
{"timestamp": "2026-05-28T11:25:19.894079", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 20 条 (新增 20)"}
{"timestamp": "2026-05-28T11:25:19.894079", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: arXiv cs.LG"}
{"timestamp": "2026-05-28T11:25:21.359041", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 20 条 (新增 20)"}
{"timestamp": "2026-05-28T11:25:21.359041", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: arXiv cs.CL"}
{"timestamp": "2026-05-28T11:25:22.676438", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 20 条 (新增 20)"}
{"timestamp": "2026-05-28T11:25:22.676438", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: arXiv cs.AI"}
{"timestamp": "2026-05-28T11:25:23.974802", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 20 条 (新增 20)"}
{"timestamp": "2026-05-28T11:25:23.974802", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: arXiv cs.DC"}
{"timestamp": "2026-05-28T11:25:25.286453", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 20 条 (新增 20)"}
{"timestamp": "2026-05-28T11:25:25.286453", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: arXiv cs.MA"}
{"timestamp": "2026-05-28T11:25:26.590621", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 20 条 (新增 20)"}
{"timestamp": "2026-05-28T11:25:26.592627", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: vLLM Releases"}
{"timestamp": "2026-05-28T11:25:28.953711", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 10 条 (新增 10)"}
{"timestamp": "2026-05-28T11:25:28.953711", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: SGLang Releases"}
{"timestamp": "2026-05-28T11:25:33.834308", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 10 条 (新增 10)"}
{"timestamp": "2026-05-28T11:25:33.834308", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: DeepSeek Releases"}
{"timestamp": "2026-05-28T11:25:35.146274", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 1 条 (新增 1)"}
{"timestamp": "2026-05-28T11:25:35.146274", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: Qwen Releases"}
{"timestamp": "2026-05-28T11:25:36.601365", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 0 条 (新增 0)"}
{"timestamp": "2026-05-28T11:25:36.601365", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: PyTorch Blog"}
{"timestamp": "2026-05-28T11:25:38.140274", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 10 条 (新增 10)"}
{"timestamp": "2026-05-28T11:25:38.140274", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: Google DeepMind Blog"}
{"timestamp": "2026-05-28T11:25:39.531517", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 30 条 (新增 30)"}
{"timestamp": "2026-05-28T11:25:39.531517", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: OpenAI Blog"}
{"timestamp": "2026-05-28T11:25:42.162466", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 30 条 (新增 30)"}
{"timestamp": "2026-05-28T11:25:42.162466", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: LMSYS Releases"}
{"timestamp": "2026-05-28T11:25:44.249599", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 10 条 (新增 10)"}
{"timestamp": "2026-05-28T11:25:44.249599", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: SWE-Bench Releases"}
{"timestamp": "2026-05-28T11:25:45.871383", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 10 条 (新增 10)"}
{"timestamp": "2026-05-28T11:25:45.871383", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: AutoGen Releases"}
{"timestamp": "2026-05-28T11:25:47.817354", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 10 条 (新增 10)"}
{"timestamp": "2026-05-28T11:25:47.817354", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: DSPy Releases"}
{"timestamp": "2026-05-28T11:25:50.534166", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 10 条 (新增 10)"}
{"timestamp": "2026-05-28T11:25:50.534166", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: LangChain Releases"}
{"timestamp": "2026-05-28T11:25:52.577216", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 10 条 (新增 10)"}
{"timestamp": "2026-05-28T11:25:52.577216", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: LlamaIndex Releases"}
{"timestamp": "2026-05-28T11:25:55.217574", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 10 条 (新增 10)"}
{"timestamp": "2026-05-28T11:25:55.217574", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: DeepSpeed Releases"}
{"timestamp": "2026-05-28T11:25:57.494423", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 10 条 (新增 10)"}
{"timestamp": "2026-05-28T11:25:57.494423", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: FlashAttention Releases"}
{"timestamp": "2026-05-28T11:25:58.784400", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 0 条 (新增 0)"}
{"timestamp": "2026-05-28T11:25:58.784400", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: TensorRT-LLM Releases"}
{"timestamp": "2026-05-28T11:26:02.592484", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 10 条 (新增 10)"}
{"timestamp": "2026-05-28T11:26:02.592484", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: llama.cpp Releases"}
{"timestamp": "2026-05-28T11:26:05.143462", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 10 条 (新增 10)"}
{"timestamp": "2026-05-28T11:26:05.143462", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: 量子位"}
{"timestamp": "2026-05-28T11:26:08.382919", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 10 条 (新增 10)"}
{"timestamp": "2026-05-28T11:26:08.383885", "level": "INFO", "name": "IntelligenceOS", "message": "Crawling: TechCrunch AI"}
{"timestamp": "2026-05-28T11:26:09.670321", "level": "INFO", "name": "IntelligenceOS", "message": "  -> 获取 20 条 (新增 20)"}
{"timestamp": "2026-05-28T11:26:09.670321", "level": "INFO", "name": "IntelligenceOS", "message": "METRIC: crawled=331", "metric": true}
{"timestamp": "2026-05-28T11:26:09.670321", "level": "INFO", "name": "IntelligenceOS", "message": "METRIC: new_signals=331", "metric": true}
{"timestamp": "2026-05-28T11:26:09.670321", "level": "INFO", "name": "IntelligenceOS", "message": "采集完成: 331 条信号"}
{"timestamp": "2026-05-28T11:26:09.670321", "level": "INFO", "name": "IntelligenceOS", "message": "STEP: CRAWL [COMPLETED]", "step": "CRAWL", "status": "COMPLETED", "count": 331}
{"timestamp": "2026-05-28T11:26:09.670321", "level": "INFO", "name": "IntelligenceOS", "message": "STEP: CLASSIFY [STARTED]", "step": "CLASSIFY", "status": "STARTED"}
{"timestamp": "2026-05-28T11:26:10.234424", "level": "INFO", "name": "IntelligenceOS", "message": "已保存 50 条事件 (进度 50/331)"}
{"timestamp": "2026-05-28T11:26:10.782852", "level": "INFO", "name": "IntelligenceOS", "message": "已保存 50 条事件 (进度 100/331)"}
{"timestamp": "2026-05-28T11:26:11.317250", "level": "INFO", "name": "IntelligenceOS", "message": "已保存 50 条事件 (进度 150/331)"}
{"timestamp": "2026-05-28T11:26:11.838074", "level": "INFO", "name": "IntelligenceOS", "message": "已保存 50 条事件 (进度 200/331)"}
{"timestamp": "2026-05-28T11:26:12.383760", "level": "INFO", "name": "IntelligenceOS", "message": "已保存 50 条事件 (进度 250/331)"}
{"timestamp": "2026-05-28T11:26:12.917189", "level": "INFO", "name": "IntelligenceOS", "message": "已保存 50 条事件 (进度 300/331)"}
{"timestamp": "2026-05-28T11:26:14.013892", "level": "INFO", "name": "IntelligenceOS", "message": "已保存最后 31 条事件"}
{"timestamp": "2026-05-28T11:26:14.014895", "level": "INFO", "name": "IntelligenceOS", "message": "METRIC: classified=331", "metric": true}
{"timestamp": "2026-05-28T11:26:14.014895", "level": "INFO", "name": "IntelligenceOS", "message": "分类完成: 331 条事件, 错误 0 条"}
{"timestamp": "2026-05-28T11:26:14.247061", "level": "INFO", "name": "IntelligenceOS", "message": "分类完成: 31 条事件, 保存 31 条"}
{"timestamp": "2026-05-28T11:26:14.247061", "level": "INFO", "name": "IntelligenceOS", "message": "STEP: CLASSIFY [COMPLETED]", "step": "CLASSIFY", "status": "COMPLETED", "count": 31, "saved": 31}
{"timestamp": "2026-05-28T11:26:14.247061", "level": "INFO", "name": "IntelligenceOS", "message": "STEP: TREND [STARTED]", "step": "TREND", "status": "STARTED"}
{"timestamp": "2026-05-28T11:26:14.382860", "level": "INFO", "name": "IntelligenceOS", "message": "趋势分析: 5 热门技术"}
{"timestamp": "2026-05-28T11:26:14.382860", "level": "INFO", "name": "IntelligenceOS", "message": "STEP: TREND [COMPLETED]", "step": "TREND", "status": "COMPLETED", "trending": 5}
{"timestamp": "2026-05-28T11:26:14.383863", "level": "INFO", "name": "IntelligenceOS", "message": "STEP: QUALITY [STARTED]", "step": "QUALITY", "status": "STARTED"}
{"timestamp": "2026-05-28T11:26:14.384326", "level": "INFO", "name": "IntelligenceOS", "message": "Quality check: PASSED", "issues": 0}
{"timestamp": "2026-05-28T11:26:14.386334", "level": "WARNING", "name": "IntelligenceOS", "message": "质量门禁未通过: ['信源健康度不佳，优先处理失败信源']"}
{"timestamp": "2026-05-28T11:26:14.386334", "level": "INFO", "name": "IntelligenceOS", "message": "STEP: QUALITY [FAILED]", "step": "QUALITY", "status": "FAILED", "issues": []}
{"timestamp": "2026-05-28T11:26:14.386334", "level": "INFO", "name": "IntelligenceOS", "message": "STEP: QUALITY [PROCEEDING]", "step": "QUALITY", "status": "PROCEEDING", "reason": "force_or_partial"}
{"timestamp": "2026-05-28T11:26:14.386334", "level": "INFO", "name": "IntelligenceOS", "message": "STEP: REPORT [STARTED]", "step": "REPORT", "status": "STARTED"}
{"timestamp": "2026-05-28T11:26:14.388367", "level": "INFO", "name": "IntelligenceOS", "message": "METRIC: reports_generated=1", "metric": true}
{"timestamp": "2026-05-28T11:26:14.388367", "level": "ERROR", "name": "IntelligenceOS", "message": "Report阶段失败: '<' not supported between instances of 'TechEvent' and 'TechEvent'"}
{"timestamp": "2026-05-28T11:26:14.388367", "level": "INFO", "name": "IntelligenceOS", "message": "STEP: OUTPUT [STARTED]", "step": "OUTPUT", "status": "STARTED"}
{"timestamp": "2026-05-28T11:26:14.388367", "level": "INFO", "name": "IntelligenceOS", "message": "Saved daily report: C:\\Users\\Huawei\\Documents\\code\\Obsidian\\2_工作流层\\Daily\\2026-05-28.md"}
{"timestamp": "2026-05-28T11:26:14.388367", "level": "ERROR", "name": "IntelligenceOS", "message": "Output阶段失败: local variable 'weekly_report' referenced before assignment"}
{"timestamp": "2026-05-28T11:26:14.388367", "level": "INFO", "name": "IntelligenceOS", "message": "============================================================"}
{"timestamp": "2026-05-28T11:26:14.388367", "level": "INFO", "name": "IntelligenceOS", "message": "每日流水线完成"}
{"timestamp": "2026-05-28T11:26:14.388367", "level": "INFO", "name": "IntelligenceOS", "message": "  采集: 331 条信号"}
{"timestamp": "2026-05-28T11:26:14.388367", "level": "INFO", "name": "IntelligenceOS", "message": "  分类: 31 条事件"}
{"timestamp": "2026-05-28T11:26:14.388367", "level": "INFO", "name": "IntelligenceOS", "message": "  质量门禁: 未通过"}
{"timestamp": "2026-05-28T11:26:14.388367", "level": "INFO", "name": "IntelligenceOS", "message": "  报告: 0 份"}
{"timestamp": "2026-05-28T11:26:14.388367", "level": "INFO", "name": "IntelligenceOS", "message": "  错误: 2 个"}
{"timestamp": "2026-05-28T11:26:14.399010", "level": "INFO", "name": "IntelligenceOS", "message": "  耗时: 55.9 秒"}
{"timestamp": "2026-05-28T11:26:14.399010", "level": "INFO", "name": "IntelligenceOS", "message": "============================================================"}
{"timestamp": "2026-05-28T11:26:14.399010", "level": "INFO", "name": "IntelligenceOS", "message": "METRIC: daily_pipeline_completed=1", "metric": true}
{"timestamp": "2026-05-28T13:36:01.745517", "level": "INFO", "name": "IntelligenceOS", "message": "Fetching iclr2025 papers from https://raw.githubusercontent.com/Papercopilot/paperlists/main/iclr/iclr2025.json"}
{"timestamp": "2026-05-28T13:36:10.528584", "level": "INFO", "name": "IntelligenceOS", "message": "Loaded 11677 papers for iclr2025"}
{"timestamp": "2026-05-28T13:36:10.678586", "level": "INFO", "name": "IntelligenceOS", "message": "Fetching neurips2024 papers from https://raw.githubusercontent.com/Papercopilot/paperlists/main/neurips/neurips2024.json"}
{"timestamp": "2026-05-28T13:36:10.978678", "level": "ERROR", "name": "IntelligenceOS", "message": "Failed to load papers for neurips2024: 404 Client Error: Not Found for url: https://raw.githubusercontent.com/Papercopilot/paperlists/main/neurips/neurips2024.json"}
{"timestamp": "2026-05-28T13:36:10.978678", "level": "INFO", "name": "IntelligenceOS", "message": "Fetching neurips2024 papers from https://raw.githubusercontent.com/Papercopilot/paperlists/main/neurips/neurips2024.json"}
{"timestamp": "2026-05-28T13:36:11.128842", "level": "ERROR", "name": "IntelligenceOS", "message": "Failed to load papers for neurips2024: 404 Client Error: Not Found for url: https://raw.githubusercontent.com/Papercopilot/paperlists/main/neurips/neurips2024.json"}
{"timestamp": "2026-05-28T13:36:11.128842", "level": "INFO", "name": "IntelligenceOS", "message": "Fetching neurips2024 papers from https://raw.githubusercontent.com/Papercopilot/paperlists/main/neurips/neurips2024.json"}
{"timestamp": "2026-05-28T13:36:11.263818", "level": "ERROR", "name": "IntelligenceOS", "message": "Failed to load papers for neurips2024: 404 Client Error: Not Found for url: https://raw.githubusercontent.com/Papercopilot/paperlists/main/neurips/neurips2024.json"}
{"timestamp": "2026-05-28T13:36:11.263818", "level": "INFO", "name": "IntelligenceOS", "message": "Fetching neurips2024 papers from https://raw.githubusercontent.com/Papercopilot/paperlists/main/neurips/neurips2024.json"}
{"timestamp": "2026-05-28T13:36:11.412506", "level": "ERROR", "name": "IntelligenceOS", "message": "Failed to load papers for neurips2024: 404 Client Error: Not Found for url: https://raw.githubusercontent.com/Papercopilot/paperlists/main/neurips/neurips2024.json"}
{"timestamp": "2026-05-28T13:36:11.412506", "level": "INFO", "name": "IntelligenceOS", "message": "Fetching neurips2024 papers from https://raw.githubusercontent.com/Papercopilot/paperlists/main/neurips/neurips2024.json"}
{"timestamp": "2026-05-28T13:36:11.590529", "level": "ERROR", "name": "IntelligenceOS", "message": "Failed to load papers for neurips2024: 404 Client Error: Not Found for url: https://raw.githubusercontent.com/Papercopilot/paperlists/main/neurips/neurips2024.json"}
{"timestamp": "2026-05-28T13:36:11.590529", "level": "INFO", "name": "IntelligenceOS", "message": "Fetching icml2024 papers from https://raw.githubusercontent.com/Papercopilot/paperlists/main/icml/icml2024.json"}
{"timestamp": "2026-05-28T13:36:13.701789", "level": "INFO", "name": "IntelligenceOS", "message": "Loaded 2610 papers for icml2024"}
{"timestamp": "2026-05-28T13:36:13.712030", "level": "INFO", "name": "IntelligenceOS", "message": "Starting deep research on: Agent Architecture and Frameworks 2025"}
{"timestamp": "2026-05-28T13:36:13.712030", "level": "INFO", "name": "IntelligenceOS", "message": "Search phase: Agent Architecture and Frameworks 2025"}
{"timestamp": "2026-05-28T13:36:13.712030", "level": "INFO", "name": "IntelligenceOS", "message": "Web search fallback for: Agent Architecture and Frameworks 2025"}
{"timestamp": "2026-05-28T13:36:13.712030", "level": "INFO", "name": "IntelligenceOS", "message": "Analyze phase: 1 results"}
{"timestamp": "2026-05-28T13:36:13.712030", "level": "INFO", "name": "IntelligenceOS", "message": "Synthesize phase"}
{"timestamp": "2026-05-28T13:36:13.712030", "level": "INFO", "name": "IntelligenceOS", "message": "Deep research complete for: Agent Architecture and Frameworks 2025"}
{"timestamp": "2026-05-28T13:36:13.712030", "level": "INFO", "name": "IntelligenceOS", "message": "Starting deep research on: Multi-Agent Collaboration and Communication Protocols"}
{"timestamp": "2026-05-28T13:36:13.712030", "level": "INFO", "name": "IntelligenceOS", "message": "Search phase: Multi-Agent Collaboration and Communication Protocols"}
{"timestamp": "2026-05-28T13:36:13.712030", "level": "INFO", "name": "IntelligenceOS", "message": "Web search fallback for: Multi-Agent Collaboration and Communication Protocols"}
{"timestamp": "2026-05-28T13:36:13.712030", "level": "INFO", "name": "IntelligenceOS", "message": "Analyze phase: 1 results"}
{"timestamp": "2026-05-28T13:36:13.712030", "level": "INFO", "name": "IntelligenceOS", "message": "Synthesize phase"}
{"timestamp": "2026-05-28T13:36:13.712030", "level": "INFO", "name": "IntelligenceOS", "message": "Deep research complete for: Multi-Agent Collaboration and Communication Protocols"}
{"timestamp": "2026-05-28T13:36:13.712030", "level": "INFO", "name": "IntelligenceOS", "message": "Starting deep research on: Agent Memory and State Management"}
{"timestamp": "2026-05-28T13:36:13.712030", "level": "INFO", "name": "IntelligenceOS", "message": "Search phase: Agent Memory and State Management"}
{"timestamp": "2026-05-28T13:36:13.712030", "level": "INFO", "name": "IntelligenceOS", "message": "Web search fallback for: Agent Memory and State Management"}
{"timestamp": "2026-05-28T13:36:13.712030", "level": "INFO", "name": "IntelligenceOS", "message": "Analyze phase: 1 results"}
{"timestamp": "2026-05-28T13:36:13.712030", "level": "INFO", "name": "IntelligenceOS", "message": "Synthesize phase"}
{"timestamp": "2026-05-28T13:36:13.712030", "level": "INFO", "name": "IntelligenceOS", "message": "Deep research complete for: Agent Memory and State Management"}
{"timestamp": "2026-05-28T13:36:13.727655", "level": "INFO", "name": "IntelligenceOS", "message": "Notebook saved: C:\\Users\\Huawei\\Documents\\code\\Obsidian\\3_工具资源层\\ai-intelligence-os\\layers\\data\\reports\\litprog_report_20260528_133613.ipynb"}
{"timestamp": "2026-05-28T14:43:57.231893", "level": "INFO", "name": "IntelligenceOS", "message": "Loaded output format config with 9 categories"}
{"timestamp": "2026-05-28T14:51:45.131383", "level": "INFO", "name": "IntelligenceOS", "message": "Loaded output format config with 9 categories"}
{"timestamp": "2026-05-28T14:52:41.914758", "level": "INFO", "name": "IntelligenceOS", "message": "Loaded output format config with 9 categories"}
{"timestamp": "2026-05-28T14:54:58.925113", "level": "INFO", "name": "IntelligenceOS", "message": "Loaded output format config with 9 categories"}
{"timestamp": "2026-05-28T14:56:54.877889", "level": "INFO", "name": "IntelligenceOS", "message": "Loaded output format config with 9 categories"}
{"timestamp": "2026-05-28T14:58:06.675461", "level": "INFO", "name": "IntelligenceOS", "message": "Loaded output format config with 9 categories"}
{"timestamp": "2026-05-28T14:58:57.021672", "level": "INFO", "name": "IntelligenceOS", "message": "Loaded output format config with 9 categories"}
{"timestamp": "2026-05-28T15:02:16.223853", "level": "INFO", "name": "IntelligenceOS", "message": "Loaded output format config with 9 categories"}
{"timestamp": "2026-05-28T15:04:49.072441", "level": "INFO", "name": "IntelligenceOS", "message": "Loaded output format config with 9 categories"}
{"timestamp": "2026-05-28T15:05:31.534933", "level": "INFO", "name": "IntelligenceOS", "message": "Loaded output format config with 9 categories"}
{"timestamp": "2026-05-28T15:47:13.012622", "level": "WARNING", "name": "IntelligenceOS", "message": "Failed to load output format config: Expecting ',' delimiter: line 60 column 324 (char 2001)"}
{"timestamp": "2026-05-28T15:47:28.142748", "level": "WARNING", "name": "IntelligenceOS", "message": "Failed to generate event insight: name 're' is not defined"}
{"timestamp": "2026-05-28T15:47:41.115119", "level": "WARNING", "name": "IntelligenceOS", "message": "Failed to generate event insight: name 're' is not defined"}
{"timestamp": "2026-05-28T15:47:48.649258", "level": "WARNING", "name": "IntelligenceOS", "message": "Failed to generate event insight: name 're' is not defined"}
{"timestamp": "2026-05-28T15:47:55.992520", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T15:48:02.226030", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 2: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T15:48:11.930722", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 3: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T15:48:18.607150", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T15:48:25.893075", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 2: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T15:48:32.665730", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 3: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T15:48:47.897843", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T15:49:00.097941", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 2: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T15:49:20.246705", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 3: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T15:49:29.312595", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T15:49:37.546815", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 2: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T15:49:52.926938", "level": "WARNING", "name": "IntelligenceOS", "message": "Failed to generate tech insight: name 're' is not defined"}
{"timestamp": "2026-05-28T15:50:06.841986", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T15:50:12.938700", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 2: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T15:56:30.915560", "level": "INFO", "name": "IntelligenceOS", "message": "Loaded output format config with 9 categories"}
{"timestamp": "2026-05-28T15:56:40.916482", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T15:57:13.183145", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T15:57:22.332798", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 2: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T15:57:44.432789", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T15:57:59.274656", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 2: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T15:58:07.083113", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 3: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T15:58:24.797690", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T15:58:47.598825", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 2: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T15:59:03.173320", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 3: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T15:59:11.556490", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T15:59:18.307077", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 2: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T15:59:24.520273", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 3: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T15:59:31.200611", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:00:14.814016", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:07:37.665373", "level": "INFO", "name": "IntelligenceOS", "message": "Loaded output format config with 9 categories"}
{"timestamp": "2026-05-28T16:07:47.362384", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:07:54.187381", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 2: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:08:04.913800", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 3: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:08:15.374698", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:08:23.918939", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 2: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:08:40.949711", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:08:53.627833", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:09:01.053797", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 2: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:09:20.580831", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:10:04.982614", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:10:18.503703", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:10:26.394043", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 2: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:10:32.093165", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 3: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:10:55.760347", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:13:08.921852", "level": "INFO", "name": "IntelligenceOS", "message": "Loaded output format config with 9 categories"}
{"timestamp": "2026-05-28T16:13:27.105355", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:13:48.880019", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:14:05.487937", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 2: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:14:24.150440", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:14:38.373740", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 2: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:14:46.477462", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 3: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:14:55.660066", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:15:03.426227", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 2: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:15:15.830286", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 3: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:15:43.269171", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:15:56.459379", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 2: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:16:14.649430", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 3: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:16:22.377417", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:16:33.345720", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 2: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:16:43.734402", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 3: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:17:16.228477", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:17:32.431240", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 2: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:17:57.801564", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 3: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:18:25.035033", "level": "INFO", "name": "IntelligenceOS", "message": "Loaded output format config with 9 categories"}
{"timestamp": "2026-05-28T16:18:30.800661", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:18:43.894055", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:18:49.685371", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 2: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:18:58.118487", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 3: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:19:05.432730", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:19:22.567010", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:19:31.707299", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 2: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:19:40.461935", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 3: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:19:46.153435", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:19:57.915985", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 2: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:20:32.958383", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:20:53.075644", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 2: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:21:16.908169", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:21:28.465514", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 2: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:21:35.279332", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 3: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:21:42.778535", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:21:59.763850", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 2: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:22:15.909634", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 3: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:22:23.450602", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:22:49.905789", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:27:37.947512", "level": "INFO", "name": "IntelligenceOS", "message": "Loaded output format config with 9 categories"}
{"timestamp": "2026-05-28T16:27:49.677434", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:27:55.109323", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 2: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:28:08.977754", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 3: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:28:15.589822", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:28:20.789789", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 2: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:28:27.692328", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 3: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:28:33.798244", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:28:39.424455", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 2: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:29:01.660903", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:29:34.634149", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:29:55.497830", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 2: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:30:19.666012", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 3: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:31:03.205639", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:31:19.087872", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 2: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:31:45.526624", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 3: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:34:50.857497", "level": "INFO", "name": "IntelligenceOS", "message": "Loaded output format config with 9 categories"}
{"timestamp": "2026-05-28T16:34:57.574080", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:35:08.193403", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 2: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:35:16.940541", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 3: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:35:25.240154", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:35:31.708325", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 2: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:35:39.512066", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 3: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:35:48.144656", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:35:55.809379", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 2: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:36:03.942010", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 3: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:36:15.844999", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:36:38.289271", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:36:45.572276", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 2: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:36:52.674982", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 3: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:37:10.528762", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:37:22.408280", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 2: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:37:30.322476", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 3: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:37:56.065149", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:38:10.503995", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 2: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:38:43.558383", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:38:59.020798", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 2: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:39:07.967774", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 3: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:39:25.024638", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:39:42.481486", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 2: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:39:59.253801", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 3: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:40:08.983468", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:40:19.196262", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 2: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:40:32.042907", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 3: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:40:38.343728", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:40:51.885651", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:40:58.289189", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 2: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:41:05.972613", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 3: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:41:30.606598", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:42:00.513701", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 2: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:42:11.165170", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 3: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:59:06.812253", "level": "INFO", "name": "IntelligenceOS", "message": "Loaded output format config with 9 categories"}
{"timestamp": "2026-05-28T16:59:19.678615", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:59:25.178082", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 2: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T16:59:43.468432", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T17:00:16.452859", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T17:00:32.218261", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T17:00:45.126164", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 2: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T17:01:21.950981", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T17:01:41.493452", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 2: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T17:01:54.968735", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 3: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T17:02:28.200924", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T17:03:14.948202", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T17:04:02.951594", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T17:04:24.316157", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 2: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T17:04:43.230205", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 3: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T17:05:16.104473", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T17:05:36.413690", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 2: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T17:05:54.666555", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 3: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T17:06:35.892064", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T17:07:23.080251", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T17:08:02.601474", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 2: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T17:08:19.193071", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T17:08:28.832235", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 2: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T17:08:36.443809", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 3: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T17:08:48.635639", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T17:08:55.461854", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 2: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T17:09:18.612185", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T17:09:34.123931", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 2: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T17:09:58.176488", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 3: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T17:10:19.997334", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T17:10:43.447604", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 2: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T17:11:06.841875", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 3: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T17:11:24.745055", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 1: Empty or short response, retrying..."}
{"timestamp": "2026-05-28T17:11:51.108955", "level": "WARNING", "name": "IntelligenceOS", "message": "Attempt 2: Empty or short response, retrying..."}
