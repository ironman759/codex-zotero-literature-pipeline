#!/usr/bin/env python3
"""Minimal evidence gate for a candidate PDF.

Checks bytes, PDF magic, and (when available) pdftotext readability. It does
not decide bibliographic identity; the caller must compare title/author/DOI.
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
from pathlib import Path


def verify(path: Path) -> dict:
    result = {
        "path": str(path),
        "exists": path.is_file(),
        "size": path.stat().st_size if path.is_file() else 0,
        "pdf_header": False,
        "readable": False,
        "ok": False,
    }
    if not result["exists"]:
        result["reason"] = "file-not-found"
        return result
    with path.open("rb") as fh:
        result["pdf_header"] = fh.read(5) == b"%PDF-"
    if not result["pdf_header"]:
        result["reason"] = "missing-pdf-header"
        return result
    pdftotext = shutil.which("pdftotext")
    if pdftotext:
        proc = subprocess.run(
            [pdftotext, "-f", "1", "-l", "1", str(path), "-"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=30,
        )
        result["readable"] = proc.returncode == 0 and bool(proc.stdout.strip())
    else:
        # Header and nonzero size are still useful, but do not claim parsing.
        result["readable"] = None
    result["ok"] = bool(result["pdf_header"] and result["size"] > 0 and result["readable"] is not False)
    if not result["ok"]:
        result["reason"] = "unreadable-pdf"
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path)
    args = parser.parse_args()
    result = verify(args.path)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
