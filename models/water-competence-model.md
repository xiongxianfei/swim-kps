---
id: "swim:mo:water-competence-model"
type: "model"
version: "1.0.0"
language: "KPS 9.x"
status: "draft"
reviewed: null
basis_kind: "authored task readiness model with attributed safety inputs"
confidence: "bounded explanation; not a competence assessment"
references: ["swim:r:redcross"]
uses_models: ["swim:mo:breathing-and-air-access-model", "swim:mo:body-support-and-balance-model"]
---

# Water competence and task readiness model

## Key takeaway

Readiness depends on the swimmer, the specific task, its setting and available assistance together.

## Summary

Water competence includes skills, judgement and appropriate responses to conditions. This Model represents the narrower question of readiness for a supervised surface-swimming task. A recognised movement or a flotation aid does not establish reliable air access, stopping or recovery. Changing support or environment changes the question even if the intended movement stays the same.

## Purpose and boundary

Explain why a task can be manageable with a secure handhold yet unsuitable without it. This is a qualitative readiness system, not a complete water-competence curriculum, a scoring test or an emergency rescue procedure. Its intended use is understanding entry conditions, not granting permission to attempt an unfamiliar skill.

## Essential terms and components

| Component | Meaning and role |
|---|---|
| Capability | What the person can already do dependably in the relevant conditions |
| Task demand | Required movement, attention, breathing and duration |
| Environment | Depth, permitted area, footing and available support |
| Assistance | Suitable supervision and the close help the person needs |
| Recovery | An already learned way to stop and regain air and stable support |

Confidence is a feeling; capability requires appropriate evidence. Recovery means ending the activity under control, not merely finishing its intended distance.

## Representation and mechanism

```text
person + task + environment + assistance
                 ↓
dependable breathing, control and known recovery?
                 ↓
task-specific readiness remains conditional on these conditions
```

This is a conjunction of necessary conditions, not a numerical sum: confidence cannot compensate for missing air access. Support also changes the physical task. A wall supplies an external force and a stable reference, while a free swimmer must manage movement and recovery without that contact. Removing the wall therefore changes both mechanics and the capabilities required.

## Interfaces

| Connected Model | What crosses the boundary |
|---|---|
| [Breathing and air access](breathing-and-air-access-model.md) | Actual mouth clearance and ventilation are requirements for readiness, not consequences of having read a breathing cue |
| [Body support and balance](body-support-and-balance-model.md) | The availability and location of support change forces, orientation and recovery conditions |
| [Self coaching](self-coaching-model.md) | Readiness limits which questions can be explored in water; an uncertain entry condition routes to instruction or land study |

## Worked example

**Constructed case:** A learner can describe a kick and perform its sequence while holding the wall, but has not learned to regain standing after releasing support. The sequence supplies information about leg action. It supplies no evidence of unsupported recovery. The missing condition is not resolved by doing the same action farther from the wall; appropriate in-person instruction is needed first.

## Assumptions and limits

The setting is a suitable lifeguarded pool with a companion; weak or inexperienced swimmers need appropriate close assistance. Dependable air access, stopping and recovery must already exist for the selected task. A kickboard is not drowning protection. Stop for pain, dizziness, distress, repeated water inhalation or unreliable support and obtain help. No breath restriction, hyperventilation, forced submersion or painful movement belongs in the task. These conditions restate the package's [Safety boundary](../SAFETY.md); they do not certify individual readiness or teach rescue.

## Evidence and evaluation

[Red Cross Swimming Safety](../references/american-red-cross-undated-swimming-safety.md) supports supervised areas, a buddy and close help for inexperienced swimmers. Its safety tips were rechecked in official HTML on 2026-10-14. The conditional representation and example are authored applications of that guidance and the existing package boundary, not an externally validated assessment instrument. No swimmer was assessed.
