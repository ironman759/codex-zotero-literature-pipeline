# Codex Zotero Literature Pipeline

An Agent Skill for building or repairing Zotero project collections. It covers search logs, identifier-based deduplication, metadata checks, PDF archiving, and verification of managed attachments.

## Get started

Place this repository, named `codex-zotero-literature-pipeline`, in a skill directory recognized by your agent. Invoke `$codex-zotero-literature-pipeline` in Codex or point your agent at [SKILL.md](SKILL.md).

> Use $codex-zotero-literature-pipeline to repair missing PDFs in my Zotero project collection. Start with a dry run and use public full text first.

Use your existing search tools and a Zotero integration with read/write access to the intended library. Managed attachment import and readback depend on the active integration. Institutional access uses your own library's sign-in flow.

The optional PDF checker runs with Python 3.8+ and uses Poppler's `pdftotext` when available.

```sh
python3 scripts/verify_pdf.py /path/to/article.pdf
```

Check the JSON `readable` field. If it is `null`, the result covers basic file checks only. If text extraction fails, inspect a rendered page or use OCR. Verify article identity separately.
