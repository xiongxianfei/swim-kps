---
package_version: "4.0.1"
language: "KPS 9.x"
reviewed: "2026-10-07"
---

# Swim KPS

## Key takeaway
Explore evidence-aware, self-contained breaststroke and freestyle self-coaching knowledge, while keeping safety, observation, uncertainty and personal experience distinct.

## Summary
Swim KPS is a public, open-source self-coaching knowledge package for swimmers and contributors—not a swimming-instructor curriculum, individualized assessment, medical recommendation or substitute for in-person supervision. The two stroke Practices include reference movements, the reasons for trying them, executable procedures, troubleshooting and blank current-technique summaries. No ability, distance achievement, pain diagnosis or completed session has been inferred.

## Start safely
Begin with [Start here](START-HERE.md) and the inline safety boundary of the selected Practice: [Self coach breaststroke](practices/self-coach-breaststroke.md) or [Self coach freestyle](practices/self-coach-freestyle.md). Breaststroke has eight stages and freestyle seven; each supplies a summary, understanding, procedure, observations and next/fallback.

Self-coaching means choosing your learning question, not swimming alone. Use a suitable lifeguarded pool with a companion and appropriate close assistance when inexperienced. If you cannot reliably get air, stop and regain support in the chosen task, obtain in-person instruction before unsupported experiments. Stop for pain, distress or repeated water inhalation. No forced breath restriction, hyperventilation, racing pullouts, diving, open-water work or rehabilitation is prescribed. [Red Cross safety](references/american-red-cross-undated-swimming-safety.md) and [Dangerous breath holding](references/boyd-2015-dangerous-underwater-breath-holding.md) support these boundaries, not personal clearance.

## Structure and reading profile
The five core folders are `concepts/`, `principles/`, `models/`, `methods/` and `practices/`. `references/` holds Markdown records identifying external publications and their actual contributions. No original source binaries, platform-specific editions or sibling-package files are required.

Every substantial document begins with a Key takeaway and Summary. Each Practice contains actual staged understanding and actions, not only links. Stage headings use `Stage1`, `Stage2` and so on for recommended order; entry conditions remain the real prerequisites. Meaningful headings generate conventional lowercase hyphenated links. The YAML ID is not an anchor.

## Package and language versions
Package version: **4.0.1**. Language compatibility: **KPS 9.x**. Exact authoring contract checked for this release: **9.0.0**. Compatibility is a promise about unchanged required meanings within that major line, not a claim that future tools or releases have been tested. See [Compatibility](COMPATIBILITY.md).

## Maintenance and validation
Edit one canonical package. After revising a dependency, inspect the local summaries that use it. Run `python validate.py .`, review any stale summaries, then use `--accept-reviewed-summaries` only after the review is actually complete. For frozen-release hashes run `python validate.py . --manifest`. Python's standard library is sufficient for this package checker; no KPS install is needed.

The [authoritative KPS Core contract](https://github.com/xiongxianfei/knowledge-practice-system/blob/8fd410d1a8dec8b3e38352c9166639906049ec55/AUTHORING.md) defines shared authoring requirements, while [Swim authoring](AUTHORING.md) documents domain-specific boundaries. The [Navigation guide](NAVIGATION.md) contains an actual click test. The [Checks report](CHECKS.md) separates automated checks from source inspection and unperformed user testing. [Contributing](CONTRIBUTING.md) describes safe evidence-based improvements and privacy rules.

## Evidence and limits
Read the [Source review](SOURCE-REVIEW.md) and the local evidence summaries before extrapolating a claim. Reference count is not independent evidence count. The package is authored synthesis; working links, metadata and checksums do not establish scientific truth, competence, suitability or effectiveness. Only Markdown reference records are bundled.

## Find knowledge
[Knowledge index](INDEX.md) and [Method to reason map](WHY-MAP.md) connect tasks to their rationale. [Release notes](RELEASE.md) explain the breaking publication changes. Extract to a fresh directory rather than over an older edition.

## Public participation and personal observations
This repository publishes reusable explanations, bounded Methods, self-contained Practices and structured Reference records. It does **not** publish the author's personal swimming journal. Actual session records should be stored separately and privately; the [blank session template](SESSION-TEMPLATE.md) is available for private reuse. Do not upload personal health records, another swimmer's footage or identifying details in Issues or PRs.

Submit a [knowledge correction or proposal](CONTRIBUTING.md) with the specific claim, observed limitation, source access extent and proposed revision. A reported result is an individual observation, not a universal instruction.

## License and publication
Project-authored text and code are offered under the [MIT license](LICENSE), subject to review of publication rights; external Reference records identify third-party publications without re-licensing those publications. [Release notes](RELEASE.md) distinguish packaging from changes to swimming evidence. This release is based on Swim 4.0.0 knowledge, not a new validation of the swimming claims. [Publication instructions](PUBLISHING.md).
