# Raw research checkpoints

Bulk search output is intentionally local-only.

On 2026-10-25 the GitHub issue collector observed **537 unique issue records** before GitHub Search API rate limiting caused **3 configured queries** to fail. The durable research corpus cites the issue URLs and curated claims in `../sources.md` and `../problem-evidence.csv`.

The repository does not retain full third-party issue bodies. They can contain arbitrary instructions, configuration snippets, credential-shaped placeholders, personal information, or large copyrighted text that is unnecessary for reproducibility.

Run this from the repository root:

    powershell -ExecutionPolicy Bypass -File .\scripts\collect_github_evidence.ps1

The current collector writes metadata only to `research/raw/github-issues.local.json`, which is ignored by Git. It records repository, issue number/title/URL, dates, state, labels, search tags, and failed queries.
