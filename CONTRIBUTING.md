---
package_version: "4.0.1"
language: "KPS 9.x"
reviewed: "2026-10-07"
---

# Contributing to Swim KPS

## Key takeaway
Contribute clear, safe, evidence-aware corrections and reusable self-coaching knowledge, not universal instructions inferred from one swimmer.

## Summary
Contribute clear, safe, evidence-aware corrections and reusable self-coaching knowledge, not universal instructions inferred from one swimmer.

## Before contributing
Read [Swim safety](SAFETY.md), [Swim authoring guidance](AUTHORING.md), the [KPS Core authoring contract](https://github.com/xiongxianfei/knowledge-practice-system/blob/8fd410d1a8dec8b3e38352c9166639906049ec55/AUTHORING.md), and the [Source review](SOURCE-REVIEW.md). Keep private or identifying session records outside this public repository. Do not upload another person's video, diagnoses or health history.

## What belongs here
- Corrections to a specific Concept, Principle, Model, Method, Practice or Reference claim, with precise file and section.
- Better distinctions, bounded hypotheses and evidence-checked explanations.
- Safer self-coaching procedures, observable success/counter-signals and stop/fallback routes.
- Improved access to the two substantial self-coaching Practices, without turning them into a rigid instructor curriculum.

A contribution based on personal experience should identify itself as **one observation**, and describe what it does not establish. Generalized instructions require separate direct support and clear limitations.

## Report an issue
Use a knowledge-correction or safety-concern issue template. For possible immediate danger, do not rely on an asynchronous public GitHub issue or swimming advice; stop the activity and use appropriate in-person safety or emergency channels. For private disclosures use a maintainer contact only after it has been configured; GitHub issues are public.

## Prepare a pull request
1. Identify the claim/question, exact affected file(s), population/task scope and intended improvement.
2. Explain the rationale and cite inspected publications, stating abstract-only/full-text access, disagreement and limits.
3. State safe prerequisites, contraindications, observation, success signals and fallback if an actionable Method/Practice changes.
4. Maintain a self-contained local procedure and link targets. Preserve the `Stage1`, `Stage2` recommended-order convention from KPS Core.
5. Review dependent summaries and metadata. Run `python3 validate.py .` and `python3 test_validate.py`.
6. Explain what you did not test. Do not claim scientific validation simply because automated checks pass.

## Rights and license
By submitting content, confirm you have the rights to submit it under this repository's proposed [MIT license](LICENSE). Provide attribution and an external link rather than uploading someone else's article, images or videos. Scientific citations are not copyright permission.

## Review standards
Maintainers assess local completeness, evidence quality, independence, plausible counterevidence, safety, copyright, privacy, compatibility and usability for supervised self-coaching. A reviewer may request additional limits or decline a claim that exceeds the available support.
