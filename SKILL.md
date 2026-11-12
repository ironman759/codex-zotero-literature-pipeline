---
name: codex-zotero-literature-pipeline
description: Build or repair a project literature collection in Zotero with reproducible searches, identifier deduplication, metadata checks, verified PDF attachments, and an audit trail. Use for project literature imports, user-supplied PDF batches, or missing-full-text repair.
---

# Codex–Zotero Literature Pipeline

Use the search, browser, and Zotero tools available in the current environment. For a temporary literature lookup, return a sourced brief or candidate list. Start the archival and Zotero workflow when the user asks to build or repair a project collection.

## Scope and preflight

- Read the project brief and existing search or import logs. Establish the question, inclusion criteria, sources, destination library and collection, full-text access policy, and any protected collections. Ask only about unresolved choices that affect the result.
- Discover the active Zotero tool schema and check that the intended library and collection are readable. Confirm that the chosen route supports each planned write and readback. Read [Zotero operations](references/zotero-operations.md) when writing or repairing items.
- Before writing, prepare a dry run with item identifiers, verified creators, planned changes, destination, and current access states. An explicit request to import or repair authorizes the stated mutations within that scope. If the destination or write scope is ambiguous, resolve it first.

## Search and match

1. Choose sources suited to the question, such as PubMed, Europe PMC, Crossref, OpenAlex, or a discipline-specific index. Log each query when issued, with source, date, result count if available, and any expansion or stopping decision.
2. Normalize identifiers and deduplicate by DOI, PMID, PMCID, or another verified identifier. Verify cross-source matches against bibliographic metadata. Treat title-only matches as candidates for review. Check the full destination listing across pages and distinguish parent records from notes and attachments.
3. Check title, year, creators, and canonical source URL against the publisher or a trusted bibliographic record. Fill missing creators when the source supports them. Reuse an existing matching parent. If an import or translation returns an unknown result, reread Zotero before retrying.

## Retrieve, verify, and archive

Follow [full-text access](references/full-text.md) for open, institutional, and user-supplied PDFs.

1. Check existing project and Zotero copies before downloading. Verify a candidate's nonzero size, PDF header, readability, and bibliographic identity. Use its title, creators, and DOI or another reliable identifier. The optional `scripts/verify_pdf.py` checks the file and reports first-page text extraction when Poppler is available. If extraction is inconclusive, inspect a rendered page or use OCR before accepting the PDF.
2. Record each original file, its SHA-256 digest, its source and version, and the match. Archive one verified copy under the project's source directory, organized by its primary topic. Record additional topics in the manifest. Reuse identical bytes and preserve the original staging file. If two versions differ, keep the version decision traceable.
3. Attach the verified file to the matched Zotero parent as a managed attachment when supported. Preserve existing memberships, attachments, and unrelated tags. Add only agreed project memberships and serialize writes.

## Read back and report

- Reread changed parents, memberships, creators, and child attachments. Verify the child's parent and the PDF bytes returned by Zotero or found in managed storage. Compare the digest with the archived copy when available. Apply a verified-PDF access tag only after these checks pass.
- Record query history, source-to-archive and parent-to-attachment mappings, item and attachment keys, before/after changes, and unresolved exceptions. Keep these records in the project. For repairs, capture the affected fields and memberships before writing and scope any rollback to changes from the current run.
- Report verified attachments, records awaiting user action, and failures as distinct outcomes. When a tool cannot perform or verify a write, report the remaining action and its evidence.
