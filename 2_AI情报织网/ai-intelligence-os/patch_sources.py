"""Patch script to add openreview and hf_api_filtered support to crawler_agent.py"""
import re

path = 'C:/Users/Huawei/Documents/code/Obsidian/2_AI情报织网/ai-intelligence-os/layers/agents/crawler_agent.py'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Patch collect_source dispatch
old_dispatch = """        if feed_type == 'hf_api':
            return self.collect_huggingface(source)
        elif feed_type == 'paperlists_json':
            return self.collect_paperlists(source)
        elif feed_type == 'web':
            return self.collect_web(source)
        elif feed_type == 'twitter_rss':
            return self.collect_twitter_rss(source)
        elif 'arxiv.org' in source.get('url', ''):
            return self.collect_rss(source)
        else:
            return self.collect_rss(source)"""

new_dispatch = """        if feed_type == 'hf_api' or feed_type == 'hf_api_filtered':
            signals = self.collect_huggingface(source)
            if feed_type == 'hf_api_filtered' and source.get('keywords'):
                kw_list = [k.lower() for k in source['keywords']]
                filtered = []
                for sig in signals:
                    text = (sig.title + ' ' + sig.summary).lower()
                    if any(kw in text for kw in kw_list):
                        filtered.append(sig)
                logger.info(f"HF filtered: {len(signals)} -> {len(filtered)}")
                signals = filtered
            return signals
        elif feed_type == 'paperlists_json':
            return self.collect_paperlists(source)
        elif feed_type == 'web':
            return self.collect_web(source)
        elif feed_type == 'twitter_rss':
            return self.collect_twitter_rss(source)
        elif feed_type == 'openreview':
            return self.collect_openreview(source)
        elif 'arxiv.org' in source.get('url', ''):
            return self.collect_rss(source)
        else:
            return self.collect_rss(source)"""

content = content.replace(old_dispatch, new_dispatch)

# 2. Add collect_openreview before collect_github
old_github = "    def collect_github(self, repo: str) -> List[Signal]:"
new_openreview = """    def collect_openreview(self, source: Dict) -> List[Signal]:
        \"\"\"采集 OpenReview 论文（under-review）\"\"\"
        signals = []
        try:
            url = source['url']
            headers = {
                'User-Agent': 'Mozilla/5.0 (compatible; AI-Intelligence-OS/1.0)',
                'Accept': 'application/json'
            }
            resp = self.session.get(url, timeout=30, headers=headers)
            if resp.status_code != 200:
                logger.warning(f"OpenReview API {resp.status_code}: {source.get('id')}")
                return signals

            data = json.loads(resp.text)
            notes = data.get('notes', [])
            logger.info(f"OpenReview: {len(notes)} notes from {source.get('name')}")

            for note in notes[:30]:
                try:
                    note_id = note.get('id', '')
                    title = note.get('title', 'No Title')
                    abstract = note.get('abstract', '')

                    authors = note.get('authors', [])
                    if isinstance(authors, list) and len(authors) > 0:
                        if isinstance(authors[0], dict):
                            authors = [a.get('name', '') for a in authors[:5]]
                        else:
                            authors = authors[:5]
                    else:
                        authors = []

                    # OpenReview 热门信号：metarevision 次数（修改轮次越多越重要）+ 回复数
                    metarev = note.get('metarevision', 0) or 0
                    reply_count = note.get('replyCount', 0) or 0
                    reply_count_str = str(reply_count)

                    tc = note.get('tcconf', {}) or {}
                    venue = tc.get('venue', 'NeurIPS/ICML 2026')
                    cdate = tc.get('cdate', '')

                    signal_id = self._generate_id(note_id or title)
                    signal = Signal(
                        id=signal_id,
                        title=title.strip()[:200] if title else 'No Title',
                        url=f"https://openreview.net/forum?id={note_id}" if note_id else '',
                        source=source.get('name', 'OpenReview'),
                        source_id=source.get('id', 'openreview'),
                        source_type='openreview',
                        category='academic',
                        priority='P1',
                        published=cdate,
                        summary=abstract[:500] if abstract else '',
                        authors=authors,
                        tags=['openreview', 'under-review', f'metarev:{metarev}'],
                        language='en'
                    )
                    signals.append(signal)
                except Exception as e:
                    logger.error(f"Failed to parse OpenReview note: {e}")
                    continue

            logger.info(f"OpenReview: {len(signals)} papers from {source.get('name')}")
        except Exception as e:
            logger.error(f"OpenReview采集失败 {source.get('id')}: {e}")
        return signals

    def collect_github(self, repo: str) -> List[Signal]:"""

content = content.replace(old_github, new_openreview)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch applied successfully")
