---
id: "swim:mo:effort-and-pacing-model"
type: "model"
version: "1.0.0"
language: "KPS 9.x"
status: "draft"
reviewed: null
basis_kind: "authored qualitative regulation model"
confidence: "bounded interpretation; no physiological prescription"
references: ["swim:r:physiology", "swim:r:load-consensus"]
uses_models: ["swim:mo:breathing-and-air-access-model", "swim:mo:stroke-measurement-model", "swim:mo:training-and-adaptation-model"]
uses_concepts: ["swim:c:perceived-effort"]
---

# Effort and pacing model

## Key takeaway

Pace describes motion over time; effort describes the swimmer's experience of demand. They are related but not interchangeable.

## Summary

Pacing distributes speed and effort across a task. Current capacity, recent activity, movement execution and breathing opportunities influence how that task feels and whether control continues. The Model separates a measured outcome, a subjective response and a decision about continued demand.

## Purpose and boundary

Explain why the same pace may feel different on different occasions, and why a faster result need not meet a comfortable self-coaching goal. Represent the current task, not long-term adaptation, race optimisation or clinical exercise tolerance.

## Essential terms and components

| Variable | Meaning |
|---|---|
| Speed | Distance divided by time |
| Pace | Time per specified distance, or the distribution of speed through a task |
| Perceived effort | The person's reported sense of how demanding the task is |
| External demand | What is being done: duration, distance, movement and rest conditions |
| Internal response | Physiological and psychological response to that demand |
| Current control | Ability to maintain dependable breathing, stopping and the selected movement |

## Representation and mechanism

```text
chosen task + current capacity + recent activity + conditions
                              ↓
                 effort, movement and breathing response
                              ↓
            interpretation → retain / reduce / stop / seek help
```

This is a qualitative decision representation, not a formula for estimating capacity. Muscles require energy; ventilation and circulation support oxygen supply and carbon-dioxide removal. Clearance of the mouth supplies an opportunity to breathe, but does not measure gas exchange or establish adequate ventilation. A timing cue therefore cannot replace attention to the actual response.

Changing speed can also change arm/leg timing and water resistance. A controlled pace comparison needs both the external conditions and the response; otherwise an effort difference might be assigned to technique despite different rest, duration or prior activity. Feedback informs a provisional choice, not a diagnosis of the hidden limiting system.

## Interfaces

| Connected Model | Relationship |
|---|---|
| [Breathing and air access](breathing-and-air-access-model.md) | Demand and the available air window must coexist; a prescribed stroke count cannot guarantee this |
| [Measurement](stroke-measurement-model.md) | Time, distance, effort convention and context make comparisons interpretable |
| [Training and adaptation](training-and-adaptation-model.md) | Recent load and recovery affect current response; one response does not establish a lasting capacity change |

## Worked example

**Constructed arithmetic:** Two familiar surface segments are each 20 m in 30 s, giving the same mean speed, about 0.67 m/s. The second is reported as harder and follows less rest. Equal speed establishes equal average motion under the distance/time convention. It does not establish equal internal demand or prove that a stroke change failed. Rest and execution remain alternative explanations. If air access or control is unreliable, the comparison ends regardless of the time.

## Assumptions and limits

Ordinary supervised surface swimming within already dependable capabilities. No heart-rate zone, lactate threshold, fixed breathing count, maximal test or restricted-breath task is inferred. Stop for pain, dizziness, unusual breathlessness or distress; obtain appropriate help rather than repeatedly testing symptoms. This Model is not an exercise prescription.

## Evidence and evaluation

[NHLBI](../references/nhlbi-2025-what-breathing-does-for-the-body.md) explains oxygen/carbon-dioxide exchange; selected HTML was rechecked on 2026-10-14. The [IOC load consensus](../references/soligard-2016-load-in-sport.md) distinguishes external work from individual response, with the access limits stated in its record. The feedback representation and arithmetic example are authored, not a validated pacing algorithm.
