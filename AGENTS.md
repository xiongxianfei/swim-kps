---
package_version: "4.0.1"
language: "KPS 9.x"
status: "draft"
reviewed: null
---

# Agent guidance

## Key takeaway

Apply the shared Core Engineering Principles together with this repository's authoring, evidence and contribution boundaries.

## Summary

These repository-wide instructions apply to knowledge, code, tools and workflows. The nine Core Engineering Principles are maintained verbatim across the six knowledge repositories; propose shared revisions together and keep domain-specific instructions below. Each repository carries its own copy for independent use. These are working agreements, not scientific KPS Principle objects or a replacement for the authoring contract.

## Project purpose

Help readers understand breaststroke and front crawl and use bounded, evidence-aware self-coaching Practices. Use the [subject map](docs/subject-map.md) for connected topics and the [index](docs/INDEX.md) for explanations. Reading this library does not establish competence or replace appropriate in-person supervision.

## Core Engineering Principles

1. **Self-contained knowledge.** Make each substantive document understandable on its own: explain the problem, essential terms, prerequisites, mechanisms, examples, and boundaries. Link to deeper material without requiring readers to follow links to understand the core argument. Keep canonical definitions in one place; avoid needless duplication.

2. **Reader-centered quality.** Evaluate whether a reader can explain *what happens, how, why, and when*; apply the knowledge to a realistic problem; predict likely outcomes and failure modes; and recognize opportunities to improve results. Correctness and clear reasoning matter more than polished prose.

3. **Goal-oriented work.** Identify the intended reader outcome before substantial work. Choose the smallest sufficient change; prioritize important knowledge gaps and useful results. Avoid speculative infrastructure, redundant research, unnecessary documentation, and rituals that do not advance the goal. Do not skip essential verification to save effort.

4. **Reuse before invention.** Look for established theory, standards, sources, methods, libraries, and tools before building alternatives. Prefer suitable, proven approaches; weigh fitness, reliability, cost, maintenance, and lock-in. Create custom solutions only when a material requirement justifies them.

5. **Mechanisms before memorization.** Explain causal relationships, relevant variables, assumptions, boundary conditions, and trade-offs. Show how the mechanism informs decisions and practical action. Surface possible improvements and testable hypotheses, clearly separating proposed innovations from demonstrated results.

6. **Delete obsolete internal compatibility.** When replacing internal code, paths, workflows, or knowledge structures, migrate affected uses and remove superseded implementations. Do not add internal legacy shims, deprecated aliases, dual-write logic, or competing canonical documents. Assess *external* contracts separately and honor actual obligations. Preserve unique evidence, provenance, and historically useful knowledge; remove obsolete representations, not valuable facts.

7. **Fix the problem class.** For defects or inconsistencies, identify the underlying cause and check for related instances. Make the smallest coherent change that addresses the confirmed class; add proportionate checks or regression coverage where useful. Do not turn isolated issues into speculative redesigns.

8. **Think before acting.** Before substantive work, clarify the intended outcome, inspect relevant context, challenge important assumptions, and consider dependencies, risks, and the simplest sound approach. Scale planning to the task: small, reversible changes need no formal plan; consequential or hard-to-reverse changes deserve more analysis. Avoid analysis that does not improve the decision.

9. **Test the core first; validate by risk.** First verify the main outcome: for software, the changed behavior; for knowledge, whether a reader can use it to reason through a representative problem. Expand to affected dependencies, contracts, edge cases, or regressions when the likelihood and impact of failure justify it. Prefer focused checks over redundant tests or unrelated full suites; never omit essential verification merely to save time.

## Project guidance

- Read [Swim authoring](docs/AUTHORING.md) and its [pinned Core contract](https://github.com/xiongxianfei/knowledge-practice-system/blob/8fd410d1a8dec8b3e38352c9166639906049ec55/AUTHORING.md). Preserve this package's declared format instead of silently adopting a newer Core release.
- Keep the five knowledge roles and publication-based Reference records. Preserve self-contained summaries, safe procedures, scoped statements and real heading-derived links. `StageN` numbers express recommended order; prerequisites determine actual dependencies.
- Follow [Safety](SAFETY.md). Do not diagnose pain, prescribe breath restriction, hyperventilation or forced repetitions, or suggest technique through pain. Maintain stop and fallback guidance.
- Separate observations, interpretations, explanations and trial suggestions. Do not invent session results or turn a personal cue into a universal law. Safety-, evidence- and human-experience-related changes require meaningful separate human review.
- Cite actually inspected evidence, preserve access limits and alternatives, and do not copy restricted publications or figures. Keep personal session records private under [Private records](guides/PRIVATE-RECORDS.md); public templates remain blank.
- Maintain subject navigation from established accounts and scope, aligning explanations and gaps beside each topic. Practices own their activity sequences and safety prerequisites.

## Verification

Run from the repository root as described in [Maintenance](docs/MAINTENANCE.md):

```bash
python3 validate.py .
python3 -m unittest discover -s tests -v
```

Inspect changed Practices in rendered Markdown. Review changed source meaning and receiving summaries before accepting dependency fingerprints. Use manifest checks for packaged archives as documented in Maintenance. Report actual results and limits; automated checks do not establish swimming safety, scientific correctness or independent review.

## Contribution workflow

Follow [Contributing](.github/CONTRIBUTING.md). Use a focused branch and PR to `main`; describe affected claims, evidence, safety implications and actual checks. Merge or release only within owner authorization. Preserve unrelated work, the pinned checker and LF text under `.gitattributes`; do not disable checks or treat technical CI as human safety review.
