---
id: "swim:mo:breaststroke-arm-action-model"
type: "model"
version: "1.0.0"
language: "KPS 9.x"
status: "draft"
reviewed: null
basis_kind: "authored model with attributed inputs"
confidence: "qualitative surface stroke account"
references: ["swim:r:se-breast", "swim:r:usms-breast-pull"]
uses_models: ["swim:mo:force-and-resistance-model", "swim:mo:breaststroke-cycle-model", "swim:mo:breathing-and-air-access-model"]
---

# Breaststroke arm action model

## Key takeaway

Explain the arm cycle through preparation, interaction with water and return to a position for the next action.

## Summary

The surface breaststroke arms move together through outward preparation, inward action and forward recovery. Hand and forearm orientation affects the interaction with water; recovery changes that interaction while repositioning the arms. These functions connect the local arm cycle to breathing and kick timing without prescribing a unique hand path.

## Purpose and boundary

Explain what the arms contribute and why a larger pull is not automatically a better whole stroke. The system includes both arms and their movement relative to the torso and water. Kick events and mouth clearance are interfaces. Racing pullouts, joint-load calculation and rehabilitation are outside scope.

## Essential terms and components

| Component or event | Meaning |
|---|---|
| Preparation or catch | Reorientation of hand and forearm for the following water interaction; water is not a fixed handle |
| Inward action | Movement bringing the hands and forearms toward the front of the upper body |
| Recovery | Forward repositioning for the next cycle |
| Configuration | Relative positions and orientations of hand, forearm, upper arm and torso |
| Relative motion | Movement with respect to the water, which differs from movement with respect to the swimmer |

## Representation and mechanism

```text
forward extension → outward preparation → inward action
       ↑                                   ↓
       └──────── forward recovery ─────────┘
```

The sequence is a description of connected events, not four fixed holds. Configuration and water-relative motion jointly influence fluid forces. A force component along the swimming direction contributes to forward acceleration; other components and their points of application affect body movement and rotation. Whole-swimmer acceleration depends on all external forces, not the arm action alone.

Recovery has two jobs in this account: it establishes the next starting configuration and changes the swimmer's interaction with water while the arms move forward. An extended backward sweep also changes the return path and timing. Its whole-cycle effect cannot be judged from the pulling phase alone. No constant force percentage is assigned to the arms.

## Interfaces

| Connected Model | Relationship |
|---|---|
| [Force and resistance](force-and-resistance-model.md) | Arm configuration and motion contribute to the combined external-force balance; visible hand travel does not measure force |
| [Breathing and air access](breathing-and-air-access-model.md) | Arm and upper-body events coincide with a candidate mouth-clearance window; clearance still has to occur |
| [Breaststroke cycle](breaststroke-cycle-model.md) | Arm return is located relative to leg preparation and kick completion; event overlap matters |

## Worked example

**Constructed comparison:** Two descriptions have the same arm preparation. In A, the inward action transitions directly into forward recovery. In B, the hands continue farther back before returning, and the arms are still returning when the kick finishes. The observable difference concerns both the arm return path and its relation to the kick. It does not establish that B produces less arm force or that A is universally faster. The useful explanatory question is how a change in one phase altered the following phase and its interface.

## Assumptions and limits

Normal surface breaststroke; comfortable movement; no ideal width, elbow angle or recovery height inferred. Some vertical hand movement is consistent with preparation and does not alone identify excessive pressing. Pain is a stopping signal, not evidence of one technical cause. This explanation introduces no new drill; the [arm Method](../methods/explore-breaststroke-arms.md) retains the activity and its prerequisites.

## Evidence and evaluation

[Swim England](../references/swim-england-2018-improving-breaststroke-technique.md) describes outward preparation, inward action and forward return. [USMS](../references/us-masters-swimming-undated-breaststroke-pull.md) relates orientation to pulling and discusses recovery demands. Selected official HTML arm sections were rechecked on 2026-10-14; videos, sets and exercises were not evaluated. The force interpretation and comparison are authored synthesis using the existing mechanical account. Neither source establishes an individually optimal trajectory.
