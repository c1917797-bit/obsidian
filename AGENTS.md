# Codex instructions for this Obsidian vault

This vault is a long-lived knowledge base. Accuracy, traceability, and reviewability are more important than producing many notes.

## Default behavior

- Keep `.obsidian/`, `.trash/`, attachments, and existing notes read-only unless the user explicitly requests an edit.
- Search for duplicates and related notes before creating anything.
- Put unclassified generated notes in `0_Codex工作台/Inbox/`.
- Preserve UTF-8, YAML frontmatter, Markdown, embeds, tags, and `[[wikilinks]]`.
- Follow the five-layer routing in `📋_目录导航.md`.
- Never bulk move, rename, delete, or rewrite without a preview and explicit approval.
- Never store credentials, tokens, passwords, private keys, or environment secrets in this vault.
- Separate sourced facts, Codex analysis, and open questions. Do not present inference as fact.

## Repeatable workflow

1. Run `powershell -File "0_Codex工作台/tools/obsidian-codex.ps1" status`.
2. Search before writing with `... obsidian-codex.ps1 search -Query "<topic>"`.
3. Read only the most relevant source notes.
4. Create with `... obsidian-codex.ps1 new -Title "<title>" -Source "<url-or-path>"`.
5. Fill 来源事实, Codex 分析, 关联笔记, and 待验证问题.
6. Run `... obsidian-codex.ps1 validate -Path "<note-path>"`.
7. Recommend a destination and wikilinks. Move or merge only after confirmation.

## User-intent shortcuts

- “搜索我的 Obsidian”：search only; return note paths and concise evidence.
- “整理到 Obsidian”：create one Inbox note unless a final destination is explicit.
- “更新这篇笔记”：edit only the named note and preserve metadata and links.
- “整理 Inbox”：report duplicate/merge/archive recommendations first; do not move files.
- “生成周报”：use dated notes, cite wikilinks, and create a reviewable Inbox draft.

Research downloads, parser output, logs, images, and presentation assets belong in the active Codex workspace `.tmp/`, not in the vault.

Primary guide: [[0_Codex工作台/Codex-Obsidian对接指南]]

## Inference radar workflow

For AI inference requests, read [[1_AI情报溯源/信源/AI推理一手信源清单]] and [[1_AI情报溯源/规则/AI推理情报评分与核验规则]]. Prefer primary sources. Create candidates with inference-radar.ps1. Never promote without source, experimental conditions, evidence score and value score. Never create a full report from zero evidence. Exclude general Agent news unless it changes inference latency, throughput, memory or cost.
