---
package_version: "4.0.1"
language: "KPS 9.x"
reviewed: null
---

# Swim authoring and maintenance guidance

## Key takeaway
KPS Core defines valid KPS 9.x documents; Swim adds swimming-specific evidence, safety, privacy and contributor-review expectations without redefining the core authoring contract.

## Summary
Follow the [authoritative KPS 9.x authoring contract](https://github.com/xiongxianfei/knowledge-practice-system/blob/8fd410d1a8dec8b3e38352c9166639906049ec55/AUTHORING.md) for knowledge roles, filenames, YAML metadata, self-contained content, `Stage1` headings, links and structural checks. The guidance below concerns swim-specific decisions and review. This repository is readable and its structural checker runs without another repository checked out.

## Body of Knowledge Outline

The authored [Body of Knowledge Outline](body-of-knowledge-outline.md) defines required coverage and introductory depth from established accounts within the swimming scope. Use direct topic headings with a central question, scope, components and relationships, and meaningful interfaces. Align existing explanations and gaps with the required topics. A Model explains a coherent system; a heading does not require a separate Model, and interfaces do not disqualify it from being a subsystem. Preserve useful overlap and source disagreements.

Practices own activities, order and safety prerequisites. The outline owns coverage; the [index](INDEX.md) owns the file inventory. Retain the five role folders. Keep one overall illustration aligned with the outline; other illustrations are optional and user-selected. Embed it without a redundant full-size link. Maintain the Markdown directly, without a generator, new knowledge type or change to the pinned authoring contract.

## Swimming claims and limits
- Keep observations, interpretations, explanations and actionable trial suggestions distinguishable.
- Include conditions and counter-signals whenever a Method might not transfer to another swimmer.
- Do not represent a personal cue, successful session or unsupervised trial as proof of a general mechanism.
- Never prescribe breath restriction, hyperventilation, forced repetitions or technique through pain. Maintain the [Safety boundary](../SAFETY.md).
- A medically concerning symptom is outside the scope of a swim cue; stop and seek appropriate qualified help rather than diagnosing through Markdown advice.

## Private experience versus public knowledge
Real personal session notes belong outside the public repository unless the author consciously chooses to publish a non-identifying excerpt. Keep [Session template](../guides/SESSION-TEMPLATE.md) blank in the public package. Public examples, if later added, must say whether they are fictional teaching examples, observed case reports with permission, or structured hypotheses. Contributors must not disclose identifiable health details or information about another swimmer without permission.

## Reviewing references
Use [Source synthesis](SOURCE-SYNTHESIS.md) for claim-focused comparison; retain the actual publication, evidence contribution, access extent and non-claims in each [Reference record](../references/README.md). Do not add published full-text PDFs or third-party diagrams without rights. The source review inherited from Swim 4.0.0 is not a fresh inspection for this repository-packaging release.

## Local maintenance and checks
Update a changed document's dependent local summaries after reviewing their meaning. Use `python3 validate.py .` and `python3 -m unittest discover -s tests -v` from the repository root, and inspect changed Practices in ordinary rendered Markdown. Run `python3 validate.py . --accept-reviewed-summaries` only after dependent summaries have actually been reviewed. The checker verifies publication structure, not swimming science, competence or safety for a particular person.

## Deeper knowledge
[Read the KPS Core contract](https://github.com/xiongxianfei/knowledge-practice-system/blob/8fd410d1a8dec8b3e38352c9166639906049ec55/AUTHORING.md) · [Contributing](../.github/CONTRIBUTING.md) · [Compatibility](COMPATIBILITY.md) · [Navigation](NAVIGATION.md).
