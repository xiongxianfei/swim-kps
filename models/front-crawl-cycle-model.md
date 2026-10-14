---
id: "swim:mo:front-crawl-cycle-model"
type: "model"
version: "4.0.2"
language: "KPS 9.x"
status: "draft"
reviewed: null
basis_kind: "authored model with attributed inputs"
confidence: "scope-dependent; see evaluation"
references: ["swim:r:se-crawl", "swim:r:usms-crawl-pull", "swim:r:usms-crawl-kick", "swim:r:usms-crawl-breath"]
uses_principles: ["swim:p:limb-configuration-changes-the-effect-of-effort", "swim:p:air-access-and-stroking-share-timing", "swim:p:relative-timing-changes-the-whole-stroke"]
uses_concepts: ["swim:c:stroke-cycle", "swim:c:breathing-cycle", "swim:c:coordination"]
uses_models: ["swim:mo:breathing-and-air-access-model", "swim:mo:flutter-kick-model", "swim:mo:front-crawl-arm-action-model", "swim:mo:front-crawl-body-rotation-model"]
perspectives: ["respiratory-physiology"]
---

# Front crawl cycle model

## Key takeaway

Relate alternating arm action, body rotation, kick and side breathing.

## Summary

Use one arm’s entry as a repeatable marker and locate preparation, underwater action, exit, recovery and the breathing turn. The opposite arm continues its own cycle; a fixed catch-up pause is not assumed.

## Local explanatory basis

Changing limb orientation and motion can change the direction and useful contribution of the interaction with water. A sustainable breathing pattern depends on coordinating ventilation, a clear route to air and the ongoing stroke task. The effects of component movements depend partly on their timing relative to other movements and the breathing opportunity.

## Purpose
Relate alternating arm action, body rotation, kick and side breathing.

## Representation
`Entry/reach → hand–forearm preparation → underwater action → recovery → next entry`, with the other arm alternating and body roll, kick and ventilation occurring throughout.

| Event relationship | Starting checkpoint | Qualification |
|---|---|---|
| Entry and catch | Comfortable same-side track followed by preparation | Not a fixed angle, S curve or mandated thumb-first entry |
| Underwater action and recovery | Usable backward-directed interaction followed by an unforced return | Not a rigid elbow angle or maximum finish behind the body |
| Breath and recovery-side arm | Turn with the body as that arm moves back/into recovery; return the face before entry as a useful reference | Not an exact phase clock; air access overrides the cue |
| Opposite arm and breath | The arm continues its coordinated role rather than becoming a fixed support pole | No compulsory catch-up pause |
| Kick and whole task | Manageable alternating action coexists with breathing | No universal kick count or amplitude |

Source disagreement about entry and path is documented in the synthesis. The chosen fairly neutral, same-side entry is a starting reference rather than comparative proof of superior efficiency.

## Boundary and essential terms

This is the integration system for both arms, flutter kick, torso rotation and breathing. One **two-arm cycle** can be marked from a right-hand entry to the next right-hand entry. **Relative timing** locates a left-arm, leg or breathing event within that interval. A **phase relationship** describes this timing, not a mandated pause or an ideal count.

The relationships are useful because motion in one component changes the context of another. A head turn occurs while an arm recovers and the torso rotates; the mouth's resulting position depends on their combination. Leg events also occur within this changing configuration. Describing each component separately is therefore necessary but insufficient to describe the full cycle.

## Interfaces

| Connected Model | Relationship |
|---|---|
| [Arm action](front-crawl-arm-action-model.md) | Supplies each arm's local events; this Model describes their relationship to one another |
| [Flutter kick](flutter-kick-model.md) | Supplies alternating leg events without requiring a fixed number per arm cycle |
| [Body rotation](front-crawl-body-rotation-model.md) | Supplies shoulder, pelvis and head orientations relative to the arm events |
| [Breathing and air access](breathing-and-air-access-model.md) | Separates the presence of a turn from actual clearance and ventilation |

## Worked example

**Constructed case:** Two cycles have the same arm-entry count and leg-beat count. In the second, the breathing turn begins later relative to the recovering arm, and mouth clearance is absent. The counts did not reveal the coordination change. Event order and clearance are needed to describe it. The observation supports a timing question, not a universal instruction to hold the opposite arm still or breathe less often.

## Assumptions
Freestyle means front crawl here. No race-rule analysis, compulsory breathing side/count, locked shoulder or rigid S-shaped path.

## Implications
If breathing disrupts the stroke, inspect the arm event and rotation as well as the head. If entry crosses the midline, check from a suitable viewpoint rather than diagnosing it from a side-only recording.

## Evidence and evaluation
[Improving your front crawl technique](../references/swim-england-2018-improving-front-crawl-technique.md#technique-guidance-in-this-source), [Freestyle Pull: The Complete Guide](../references/us-masters-swimming-undated-freestyle-pull.md#entry-and-underwater-preparation), [Freestyle Kick: The Complete Guide](../references/us-masters-swimming-undated-freestyle-kick.md#flutter-kick-roles-and-alternating-action) and [Freestyle Breathing: The Complete Guide](../references/us-masters-swimming-undated-freestyle-breathing.md#air-access-with-rotation-and-recovery) inform the map. They disagree on some entry/path cues; [Swimming source synthesis — evidence, inference and disagreement](../docs/SOURCE-SYNTHESIS.md) records that disagreement and the provisional reference selected here.

## Limits
This phase map does not specify unique joint trajectories. A flatter entry is a chosen starting reference, not proven superiority over every other safe variant.

## Local evidence summary


[Improving your front crawl technique](../references/swim-england-2018-improving-front-crawl-technique.md#technique-guidance-in-this-source) contributes: The guide describes alternating arm action with kick and rotation; it also recommends thumb-first entry and an hourglass-like hand path.

[Freestyle Pull: The Complete Guide](../references/us-masters-swimming-undated-freestyle-pull.md#entry-and-underwater-preparation) contributes: The guide presents a relatively flat, shoulder-region hand entry and explains hand/forearm repositioning before the propulsive action.

[Freestyle Kick: The Complete Guide](../references/us-masters-swimming-undated-freestyle-kick.md#flutter-kick-roles-and-alternating-action) contributes: The guide assigns the flutter kick propulsive, balance and coordination roles and describes alternating leg action.

Citation identifies support for the stated claim and scope. Any further causal or practical inference remains separately reviewable.

## Deeper knowledge

Canonical dependencies and Reference records provide additional derivation, source inspection and alternatives. They are not required to carry out the local explanation or procedure.

- **Concepts:** [Stroke cycle](../concepts/stroke-cycle.md)
- **Concepts:** [Breathing cycle](../concepts/breathing-cycle.md)
- **Concepts:** [Coordination](../concepts/coordination.md)
- **Principles:** [Limb configuration changes the effect of effort](../principles/limb-configuration-changes-the-effect-of-effort.md)
- **Principles:** [Air access and stroking share timing](../principles/air-access-and-stroking-share-timing.md)
- **Principles:** [Relative timing changes the whole stroke](../principles/relative-timing-changes-the-whole-stroke.md)
- **References:** [Improving your front crawl technique](../references/swim-england-2018-improving-front-crawl-technique.md)
- **References:** [Freestyle Pull: The Complete Guide](../references/us-masters-swimming-undated-freestyle-pull.md)
- **References:** [Freestyle Kick: The Complete Guide](../references/us-masters-swimming-undated-freestyle-kick.md)
- **References:** [Freestyle Breathing: The Complete Guide](../references/us-masters-swimming-undated-freestyle-breathing.md)
