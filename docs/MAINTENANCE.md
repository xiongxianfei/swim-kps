---
language: "KPS 9.x"
package_version: "4.0.1"
---

# Maintaining Swim KPS

## Key takeaway

Read the Markdown directly and use the pinned validator with focused local checks when maintaining it.

## Summary

The five knowledge folders and supporting Reference records retain their identities and content. Reader aids live in `guides/`; authoring, library indexes and review guidance live in `docs/`; earlier release records live in `docs/history/`. Safety remains prominently available at the root.

## Commands and purpose

Run from the repository root with Python 3 and its standard library:

```bash
python3 validate.py .
python3 -m unittest discover -s tests -v
```

`validate.py` detects broken links, invalid metadata, incomplete structure and changed dependencies. The local test suite verifies the pinned checker and Swim-specific Git-file and manifest handling. Both commands run in CI. No script is needed for swimming practice, reading, navigation or ordinary Git sync.

The local checker keeps standalone validation possible without a sibling checkout. `upstream-lock.json` records its digest and adaptations. Core owns the common regression coverage at the pinned source revision; focused local tests cover the adaptations. Replacing this copy requires a compatibility review. This cleanup does not upgrade the inspected KPS contract.

## Dependency and archive checks

Inspect changed source meanings and the summaries that depend on them. Only after that review may `python3 validate.py . --accept-reviewed-summaries` record new fingerprints. Ordinary checks never accept them automatically.

For a packaged snapshot, update the checksum inventory and run `python3 validate.py . --manifest`. The inventory uses the validator's `manifest_payload_files` exclusions so Git metadata and caches are excluded while unexpected content remains detectable. A manifest is an archive check, not evidence review.

Text uses LF line endings under `.gitattributes`, keeping exact-byte fingerprints consistent across checkouts. Restore intended line endings before treating a checksum difference as a knowledge revision.

## Layout migration

Update bookmarks to the paths below. Old root document URLs do not automatically redirect. Internal links have been rebased; knowledge paths and Practice stage anchors remain stable.

| Former root path | Current path |
|---|---|
| `START-HERE.md` | [guides/START-HERE.md](../guides/START-HERE.md) |
| `POOL-CARD.md` | [guides/POOL-CARD.md](../guides/POOL-CARD.md) |
| `SESSION-TEMPLATE.md` | [guides/SESSION-TEMPLATE.md](../guides/SESSION-TEMPLATE.md) |
| `PRIVATE-RECORDS.md` | [guides/PRIVATE-RECORDS.md](../guides/PRIVATE-RECORDS.md) |
| `WHY-MAP.md` | [guides/WHY-MAP.md](../guides/WHY-MAP.md) |
| `AUTHORING.md` | [docs/AUTHORING.md](../docs/AUTHORING.md) |
| `COMPATIBILITY.md` | [docs/COMPATIBILITY.md](../docs/COMPATIBILITY.md) |
| `INDEX.md` | [docs/INDEX.md](../docs/INDEX.md) |
| `NAVIGATION.md` | [docs/NAVIGATION.md](../docs/NAVIGATION.md) |
| `REVIEW.md` | [docs/REVIEW.md](../docs/REVIEW.md) |
| `SOURCE-REVIEW.md` | [docs/SOURCE-REVIEW.md](../docs/SOURCE-REVIEW.md) |
| `SOURCE-SYNTHESIS.md` | [docs/SOURCE-SYNTHESIS.md](../docs/SOURCE-SYNTHESIS.md) |
| `GOVERNANCE.md` | [docs/GOVERNANCE.md](../docs/GOVERNANCE.md) |
| `PUBLISHING.md` | [docs/PUBLISHING.md](../docs/PUBLISHING.md) |
| `CONTRIBUTING.md` | [.github/CONTRIBUTING.md](../.github/CONTRIBUTING.md) |
| `CODE_OF_CONDUCT.md` | [.github/CODE_OF_CONDUCT.md](../.github/CODE_OF_CONDUCT.md) |
| `SECURITY.md` | [.github/SECURITY.md](../.github/SECURITY.md) |
| `CHECKS.md` | [docs/history/4.0.1-checks.md](../docs/history/4.0.1-checks.md) |
| `RELEASE.md` | [docs/history/4.0.1-release.md](../docs/history/4.0.1-release.md) |

## Review boundaries

The historical [4.0.1 check report](history/4.0.1-checks.md) records earlier checks. Report current results with each change. These checks do not establish safety, competence, scientific truth or independent expert review. Actual personal session records remain outside this public library.

## Layout dependency review

The 2026-10-13 cleanup preserved the explanatory and safety text, metadata, knowledge identities and stage headings of all 55 knowledge objects and 24 Reference records. Nine of those files changed only existing document paths; the source-register links were also rebased. Receiving summaries retain the same claims and conditions. Dependency fingerprints were refreshed for these path-only changes after comparison with the committed baseline. This is an editorial and mechanical review, not independent swimming-safety or scientific review.

## Test allowlist

Retain validation of the actual package, pinned-checker integrity, Git-metadata exclusion and manifest behavior that detects altered or unexpected payloads while excluding tool state. Common validator regressions remain with Core's source versions; the local tests cover Swim's recorded adaptations. The copied general suite is removed. Content, safety and source review remain human responsibilities under the existing contribution guidance.
