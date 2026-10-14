---
id: "swim:mo:front-crawl-body-rotation-model"
type: "model"
version: "1.0.0"
language: "KPS 9.x"
status: "draft"
reviewed: null
basis_kind: "authored model with attributed inputs"
confidence: "qualitative orientation and timing account"
references: ["swim:r:se-crawl", "swim:r:physics"]
uses_models: ["swim:mo:front-crawl-arm-action-model", "swim:mo:flutter-kick-model", "swim:mo:breathing-and-air-access-model", "swim:mo:front-crawl-cycle-model"]
---

# Front crawl body rotation model

## Key takeaway

Body roll changes the geometry of arm action and breathing; its amount and timing are different questions.

## Summary

Front crawl includes alternating rotation around the swimmer's lengthwise axis. Shoulder, pelvis and head orientations need not be identical. Rotation interacts with arm recovery, underwater action and the air-access window. A visible roll angle alone does not establish appropriate timing, breathing clearance or force production.

## Purpose and boundary

Explain the orientation relationship between torso, arms and breathing in ordinary surface front crawl. This is a kinematic account, meaning a description of motion and its relationships, with a qualitative mechanical boundary. It does not calculate the muscle activity or torque producing a particular swimmer's roll.

## Essential terms and components

| Variable | Meaning |
|---|---|
| Roll | Rotation around the approximate head-to-foot axis |
| Pitch | Head-up/head-down rotation, distinct from roll |
| Yaw | Turning left/right in the horizontal plane, also distinct from roll |
| Shoulder and pelvis orientation | Separate observations of the upper and lower torso |
| Head orientation | Relation of the face to the torso and water, including a breathing turn |
| Phase | Position of an orientation event within the arm cycle |

## Representation and mechanism

```text
arm events ↔ alternating torso orientation ↔ leg events
                         ↕
              head orientation and air window
```

The arrows describe coupled relationships, not a claim that every event directly causes every other event. Rotating the torso changes the position of the recovering shoulder relative to the surface and the reference frame for the underwater arm. Turning the head during a breathing opportunity changes where the mouth lies relative to the water; torso roll alone does not guarantee clearance.

Angular momentum describes motion about a chosen origin, accounting for the mass, velocity and position of the moving parts. For the whole swimmer, external moments change total angular momentum about an inertial origin or the centre of mass. A moment is the turning effect of a force about a chosen axis. Internal segment motion can redistribute angular momentum and alter segment orientation, so the torso is not a rigid block whose roll is explained by one isolated muscle or kick. This Model does not resolve those dynamics quantitatively.

## Interfaces

| Connected Model | Relationship |
|---|---|
| [Arm action](front-crawl-arm-action-model.md) | Shoulder orientation and arm event timing jointly describe recovery and underwater configuration |
| [Flutter kick](flutter-kick-model.md) | Alternating leg action participates in the force and rotational context |
| [Breathing and air access](breathing-and-air-access-model.md) | Head orientation within the torso/arm sequence determines a candidate clearance window, not adequate ventilation by itself |
| [Front crawl cycle](front-crawl-cycle-model.md) | Places these relationships within a complete repeatable cycle |

## Worked example

**Constructed comparison:** Two cycle descriptions show the same maximum shoulder roll. In A, the mouth clears during recovery; in B, the head turn occurs after that opportunity and clearance is absent. Equal maximum roll does not imply equal air access. The difference is in relative timing and geometry, so simply increasing the angle is not a conclusion supported by this observation.

## Assumptions and limits

No exact angle, rigid shoulder-pelvis coupling or forced neck turn is prescribed. A side-only view may not resolve all three rotations. Pain or unreliable breathing ends a task; increasing roll through discomfort is not a diagnostic experiment. This is an explanation, not a new side-floating drill.

## Evidence and evaluation

[Swim England](../references/swim-england-2018-improving-front-crawl-technique.md) describes shoulder/hip rotation, recovery and the breathing turn; its body-position and breathing text was rechecked on 2026-10-14. Numerical angles and posture cues are not adopted as universal requirements. [University Physics](../references/moebs-2016-university-physics-volume-1.md) supplies moment reasoning; its additional angular-momentum basis is identified in that record. The representation and example are authored synthesis, not a measured optimal-roll study.
