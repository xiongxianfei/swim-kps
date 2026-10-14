---
id: "swim:mo:stroke-measurement-model"
type: "model"
version: "4.0.2"
language: "KPS 9.x"
status: "draft"
reviewed: null
basis_kind: "authored model with attributed inputs"
confidence: "scope-dependent; see evaluation"
references: ["swim:r:arm-kinematics"]
uses_principles: ["swim:p:fewer-strokes-do-not-identify-lower-energy-cost", "swim:p:observation-does-not-identify-one-cause"]
uses_concepts: ["swim:c:stroke-metrics", "swim:c:perceived-effort"]
uses_models: ["swim:mo:effort-and-pacing-model", "swim:mo:force-and-resistance-model", "swim:mo:self-coaching-model", "swim:mo:training-and-adaptation-model"]
perspectives: ["fluid-dynamics", "biomechanics"]
---

# Comparable swim measurement model

## Key takeaway

Make ordinary pool observations interpretable without claiming metabolic efficiency.

## Summary

On the same familiar distance, count one breaststroke cycle or define front-crawl counts explicitly. Record start, push-off, time, rest and effort; flag incomparable repeats rather than manufacture a trend.

## Local explanatory basis

Stroke count alone does not determine speed, metabolic cost or whole-stroke effectiveness. A sensation, visible motion or single performance change can be consistent with more than one explanation.

## Purpose
Make ordinary pool observations interpretable without claiming metabolic efficiency.

## Representation
For distance `d` and elapsed time `t`, average speed is `d/t`. A stroke count needs a definition: one complete breaststroke cycle, or one front-crawl arm entry versus a two-arm cycle. Record the convention.

| Record | Why it matters |
|---|---|
| Distance, start, stop and push-off | These can change apparent speed and count |
| Time and count together | Count alone does not identify speed |
| Effort and breathing comfort | These are subjective outcomes, not oxygen-consumption measurements |
| Task, rest, order and assistance | These affect comparisons |
| Whether the intended change occurred | A failed manipulation cannot test its proposed effect |

Do not compute stroke length from a full-length distance while silently including a variable push-off. Comparisons of surface cycles need the relevant surface distance/time.

## Boundary and essential terms

The system transforms a swimming event into a record and a bounded comparison. **Measurement convention** defines what is counted and where timing starts and stops. **Uncertainty** describes limited resolution or confidence in that record. A **confounder** is another differing condition that can offer an alternative explanation for a result. A **proxy** is an indirect indicator, such as a stroke count used to discuss movement organisation rather than to measure energy expenditure.

The components are the task, observer/device, event definitions, recorded values and interpretation. A change in any of them can change the result. Clear definitions prevent a measurement difference from being mistaken for a physical change; multiple complementary observations reduce ambiguity without eliminating it.

## Interfaces

| Connected Model | Relationship |
|---|---|
| [Self coaching](self-coaching-model.md) | Receives observations and their limits, then makes a provisional decision |
| [Effort and pacing](effort-and-pacing-model.md) | Supplies task demand and reported effort alongside time and distance |
| [Force and resistance](force-and-resistance-model.md) | Explains why whole-body motion cannot isolate individual fluid forces |
| [Training and adaptation](training-and-adaptation-model.md) | Requires comparable observations across occasions before a capacity trend can be proposed |

## Worked example

**Constructed arithmetic:** Over an explicitly measured 20 m surface segment, A takes 20 s and 10 two-arm cycles; B takes 22 s and 9. Mean speed is 1.00 versus about 0.91 m/s, while distance per counted cycle is 2.00 versus about 2.22 m. B travels farther per cycle but is slower. Neither result identifies energy cost. If one count instead means individual arm entries, the apparent comparison is invalid until the convention is corrected. The example excludes push-off distance by definition; these are not recorded swims.

## Assumptions
Pool length and counting convention are known; timing has ordinary manual error. No precise speed or energetic threshold is implied.

## Implications
Use a small set of complementary signals. A faster or lower-count attempt that causes breathing distress does not meet a comfortable self-coaching goal.

## Evidence and evaluation
The arithmetic is definitional. [Comparison of the arm-stroke kinematics between maximal and sub-maximal breaststroke swimming using discrete data and time series analysis](../references/gourgoulis-2022-breaststroke-arm-kinematics.md#pace-related-phase-differences) illustrates task-dependent stroke parameters, not validation of a consumer metric. Individual measurement uncertainty should be recorded.

## Limits
Stroking metrics cannot diagnose drag, tissue loading or aerobic capacity. Do not run maximal tests to make a number look better.

## Local evidence summary


[Comparison of the arm-stroke kinematics between maximal and sub-maximal breaststroke swimming using discrete data and time series analysis](../references/gourgoulis-2022-breaststroke-arm-kinematics.md#pace-related-phase-differences) contributes: Glide and recovery timing differed between maximal and submaximal trials in the reported group.

Citation identifies support for the stated claim and scope. Any further causal or practical inference remains separately reviewable.

## Deeper knowledge

Canonical dependencies and Reference records provide additional derivation, source inspection and alternatives. They are not required to carry out the local explanation or procedure.

- **Concepts:** [Stroke metrics](../concepts/stroke-metrics.md)
- **Concepts:** [Perceived effort](../concepts/perceived-effort.md)
- **Principles:** [Fewer strokes do not identify lower energy cost](../principles/fewer-strokes-do-not-identify-lower-energy-cost.md)
- **Principles:** [Observation does not identify one cause](../principles/observation-does-not-identify-one-cause.md)
- **References:** [Comparison of the arm-stroke kinematics between maximal and sub-maximal breaststroke swimming using discrete data and time series analysis](../references/gourgoulis-2022-breaststroke-arm-kinematics.md)
