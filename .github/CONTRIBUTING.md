---
package_version: "4.0.1"
language: "KPS 9.x"
reviewed: null
---

# Contributing to Swim KPS

## Key takeaway

Make a focused, source-grounded improvement that readers can understand and use within its stated boundaries.

## Summary

Use one branch and PR for a reviewable change. The [pinned KPS authoring contract](https://github.com/xiongxianfei/knowledge-practice-system/blob/8fd410d1a8dec8b3e38352c9166639906049ec55/AUTHORING.md) defines the shared document roles and format; this guide contains Swim-specific authoring, navigation and contribution instructions. [Maintenance](../docs/MAINTENANCE.md) owns the check commands.

## Authoring swimming knowledge

Follow [Safety](../SAFETY.md) and preserve the package's declared KPS format. Keep observations, interpretations, explanations and proposed trials distinguishable. A personal cue or successful attempt does not establish a general mechanism. Keep procedures self-contained, including prerequisites, rationale, observations, counter-signals and fallback; do not move essential instructions behind links.

Changes affecting air access, breath control, water depth, unsupported skills, pain or injury must state the intended population and stop conditions. Do not prescribe breath restriction, hyperventilation, forced repetitions, painful movement or rehabilitation through a stroke cue. A medically concerning symptom requires appropriate qualified help. Keep unverified physical claims qualified or excluded.

Use the [source synthesis](../docs/SOURCE-SYNTHESIS.md) to compare claims and alternatives. [Reference records](../references/README.md) identify publications, actual inspection scope, source families and non-claims. Preserve disagreements and access limits; citation count is not independent evidence count. Sources and figures remain subject to their own rights.

## Body of Knowledge Outline

Maintain [required coverage and introductory depth](../docs/body-of-knowledge-outline.md) from established accounts within the swimming scope. Use direct topic headings with a central question, scope, components, relationships and meaningful interfaces. Align explanations and gaps with each topic; preserve overlap. Each agreed subsystem has one primary, self-contained Model explaining its purpose, boundary, essential terms, components, relationships, representation, meaningful interfaces, worked example and source limits. Keep essential definitions and interface conditions inline; links provide deeper explanation. Retain whole-stroke integration Models. A heading alone is not a reason to invent a new subsystem.

The outline owns coverage, the [index](../docs/INDEX.md) owns file inventory, and Practices own activity order and safety prerequisites. Keep one overview illustration aligned with the text; additional pictures are optional and user-selected. Embed images without redundant full-size links. Maintain the Markdown directly; retain the five knowledge roles and pinned authoring contract.

## Links and stage headings

Use UTF-8 Markdown with LF, ordinary relative file links and the actual destination heading. The package's conservative heading profile uses English letters, digits and single spaces, with lowercase hyphenated fragments. For example, `## Stage1 Breathing and air access` has the fragment `#stage1-breathing-and-air-access`; neither `#stage1` alone nor a YAML identity creates that target.

`StageN` numbers express recommended order, not entry permission or permanent identity. Keep stage labels such as **Goal** and **Next** bold rather than creating repeated ambiguous headings. When renaming a file or reordering a stage, repair its stage map, incoming links and affected dependency records. Personal records should identify the stage name and Practice version, not just its number. Existing links into earlier releases may still need that earlier version.

Use document-relative paths including `.md`, with matching case. Avoid wiki-links, manual HTML anchors and viewer-specific editions. Check relevant file links and heading links in an ordinary Markdown viewer, including its back navigation; parser success does not certify every renderer. The [GitHub](../references/github-undated-markdown-formatting.md), [MkDocs](../references/mkdocs-undated-writing-your-docs.md) and [Python Markdown](../references/python-markdown-undated-toc-extension.md) records describe the inspected support and its limits.

## Privacy and rights

Keep personal session records outside the public repository and the [public session template](../guides/SESSION-TEMPLATE.md) blank. Public examples must distinguish constructed teaching examples, hypotheses and actual observations published with permission. Do not publish identifying health information, another person's footage or restricted source material without authorization. See [Private records](../guides/PRIVATE-RECORDS.md).

Submit only material you have the rights to contribute under the [MIT license](../LICENSE). Preserve attribution and link to external publications rather than copying them; a citation does not grant reuse rights.

## Review

Choose a representative bounded question, hide outgoing links and check whether the document supplies the explanation or permitted action without missing essential conditions. Concepts need clear distinctions; Principles need scoped explanatory relationships; Models need representations and assumptions; Methods and Practices need executable local content and fallback. Restore links and check that receiving summaries preserve their sources' meanings and limits. Record actual findings rather than prefilling a successful result.

Safety-, evidence- and human-experience-related changes require meaningful separate human review. Maintainers assess evidence, counterevidence, scope, privacy, rights, compatibility and usability; they may request narrower claims or decline unsupported ones. Automated checks establish structure, not swimming safety, scientific validity or individual suitability. Inspect changed Practices in rendered Markdown.

## Pull requests and releases

1. Inspect the branch and local work; preserve unrelated changes. Identify the owning file, question and intended improvement.
2. Make the smallest coherent change and update affected links, summaries and metadata. State source access and applicable limits when claims change.
3. Run the [maintenance checks](../docs/MAINTENANCE.md). Report actual local results and remote CI separately; record current review results in the PR.
4. Open one focused PR to `main` when publication is authorized. The repository owner is the initial maintainer and decides acceptance under the existing permissions and branch protections. Acceptance concerns the change, not endorsement of a contributor's abilities.
5. Merge only within owner authorization. Create tags and official releases only when explicitly requested; preserve licensing and attribution.

Swim content versions evolve independently of KPS language versions. Before changing compatibility or the checker pin, compare the required meanings, metadata, stage semantics and navigation contract, then review representative documents and record the tested version. Breaking authoring requirements need a language-major review; optional features requiring a later release need an explicit minimum. The declarations in [publication metadata](../publication.json) are not proof that future releases have been tested.

## Issues

Use the knowledge-correction or safety-concern issue template with the affected claim and proposed correction. GitHub issues are public. Immediate danger requires appropriate local assistance rather than an asynchronous issue. Use a private maintainer contact only after one has been configured.
