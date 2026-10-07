---
package_version: "4.0.1"
language: "KPS 9.x"
reviewed: "2026-10-07"
---

# Publication checks

## Key takeaway
This report distinguishes verified file structure from evidence quality, reader usability and domain effectiveness. None of the latter follows from a passing checker.

## Summary
The current publication passes its standalone profile checker and 30 regression scenarios. Headings were rendered locally with pandoc 3.1.11.1 using its GFM reader and independently parsed with markdown-it-py. The final archive is extracted and checked again before delivery. These are local checks, not tests inside GitHub, MkDocs, a mobile reader or a swimming/engineering workflow.

## Final structural inventory
| Measure | Result |
|---|---:|
| Markdown documents | 95 |
| Core knowledge objects | 55 |
| Supporting Reference records | 24 |
| Resolved local links and fragments | 917 |
| Resolved typed relationships | 277 |
| Numbered Practice stages | 18 |
| Heading identifiers | 1042 |
| Canonical knowledge and Reference summary recipients | 50 |
| Direct or declared summary dependencies | 278 |
| Payload-file checksums in the final manifest | 100 |

## What the publication checker covers
Files have one meaningful title, Key takeaway and Summary; knowledge types match their folders. JSON-compatible one-line YAML carries stable IDs and the KPS 9.x declaration. Inline links target real local files or actual whole-heading slugs. StageN numbers are consecutive, stage maps exist, and cards have local goal, why, action, observation, success and next fields plus procedures. Methods have rationale and evaluation/limit sections. References have external publication links and an explicit inspection extent.

Principle-imperative and short/link-only-stage checks are heuristics. They flag likely authoring failures; they do not prove semantic quality, correct classification or comprehension. The five roles are KPS authoring conventions, not a universal ontology.

## Regression tests actually run
All 30 scenarios pass. They include a clean baseline; missing/empty summaries; an imperative Principle; missing Method rationale; a link-only stage action; stage-number gaps; invented TI fragments; duplicate headings or IDs; missing/outside targets; wrong/unresolved relationship roles; composition cycles; metadata mistaken for an anchor; stale summary dependencies; an exact-version declaration used where a major line is required; old language metadata; HTML anchors; wikilinks; missing reference access detail; manifest tampering/unlisted payload; ignored fenced examples; valid frozen hashes; duplicate YAML keys; missing stage maps; and preventing a snapshot refresh from hiding broken links.

Run `python test_validate.py` to repeat these tests. Each mutation occurs in a temporary copy and does not modify published knowledge.

## Independent rendering and parsing
Every published Markdown body was rendered through Pandoc GFM to HTML5; generated heading IDs were compared with the profile's expected IDs. MarkdownIt independently extracted ordinary link destinations and agreed with the checker. Whitespace introduced by HTML pretty-printing was normalized for title comparison, not for identifiers. No deployment to an actual GitHub or MkDocs site was performed. Use the [Navigation click test](NAVIGATION.md#a-small-click-test) in the viewer actually selected.

## Summary maintenance
`summary-dependencies.json` records hashes of canonical knowledge/Reference files directly linked or declared by a recipient. Changed dependencies flag a review; they do not automatically rewrite the recipient or prove a new source conclusion. Refresh with `python validate.py . --accept-reviewed-summaries` only after deliberately reviewing affected summaries. Documentation/root release notes are not mistaken for core knowledge identities.

## Evidence review and limitations
[Source review](SOURCE-REVIEW.md) lists each current inspection extent and access gap. [Content review](REVIEW.md) describes the authoring questions and integration focus. No exhaustive systematic review, independent professional audit, raw-data reanalysis, learner trial, real project execution or reader usability test was performed. No personal outcome or organizational acceptance is inferred.

## Archive and compatibility checks
The archive contains only this domain root and is checked after independent extraction. `MANIFEST.sha256` covers every payload file except the manifest itself; the separately supplied archive hash covers the ZIP. Run `python validate.py . --manifest` after extraction. KPS 9.x is the compatibility line; 9.0.0 is the exact inspected authoring contract for this release. Future minor versions have not already been tested. REM checking concerns publication only and never project metamodel conformance.

## Public repository draft verification
The publication draft contains 55 knowledge objects, 24 publication Reference records, three Practices and 18 numbered stages. The local publication validator checks 102 authored Markdown documents and 953 local links. The source-review information is inherited from Swim 4.0.0; there was no additional primary-source inspection or individual swimming user study.
