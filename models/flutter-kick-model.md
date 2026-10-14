---
id: "swim:mo:flutter-kick-model"
type: "model"
version: "1.0.0"
language: "KPS 9.x"
status: "draft"
reviewed: null
basis_kind: "authored model with attributed inputs"
confidence: "qualitative account; no force or energy estimate"
references: ["swim:r:usms-crawl-kick", "swim:r:se-crawl"]
uses_models: ["swim:mo:force-and-resistance-model", "swim:mo:body-support-and-balance-model", "swim:mo:front-crawl-cycle-model", "swim:mo:effort-and-pacing-model"]
---

# Flutter kick model

## Key takeaway

Alternating leg action can contribute to movement, balance and coordination; counting beats alone does not explain its effect.

## Summary

Each leg alternates downward and upward movement as hip, knee and ankle configuration change. The two legs interact with water while their timing connects to arms and body rotation. The result depends on configuration, relative motion and the surrounding stroke, not simply kick size or frequency.

## Purpose and boundary

Explain the leg action within surface front crawl. Include the connected leg and foot rather than treating the foot as an independent paddle. Whole-stroke pacing, detailed muscle recruitment and individual energy cost are outside the local mechanism.

## Essential terms and components

| Variable | Meaning |
|---|---|
| Downbeat and upbeat | Alternating downward and upward portions of a leg's action in the swimmer's current orientation |
| Amplitude | Range of leg/foot excursion under an explicitly chosen viewpoint |
| Configuration | Hip, knee, ankle and foot positions through the action |
| Beat count | Number of individual kicks per stated arm-cycle convention |
| Phase relationship | Where each leg event occurs relative to an arm or rotation event |

## Representation and mechanism

```text
left leg:  down → up   → down
right leg: up   → down → up
             ↕ timing with arm cycle and body rotation
```

This schematic shows alternating action, not equal phase lengths or mandatory pauses. Movement and orientation of the legs and feet affect fluid forces. Those forces can have translational and rotational effects; a forward component is only one possible contribution. The return portion also prepares the next action. The whole swimmer's balance and movement reflect combined forces, including those associated with the arms and torso.

A larger or faster kick changes multiple variables. It cannot be assumed to increase useful forward motion in proportion to effort. Splash is neither a force measurement nor a direct measure of wasted energy. A two-, four- or six-beat label states a timing count, not an energy rating or a requirement for this learner.

## Interfaces

| Connected Model | Relationship |
|---|---|
| [Support and balance](body-support-and-balance-model.md) | Leg-water forces and configuration enter the orientation account |
| [Force and resistance](force-and-resistance-model.md) | Kick contribution is combined with all other external forces |
| [Front crawl cycle](front-crawl-cycle-model.md) | Leg events align with arm and rotation events; changing one rhythm changes their relationship |
| [Effort and pacing](effort-and-pacing-model.md) | Leg activity contributes to whole-task demand, which cannot be inferred from beat count alone |

## Worked example

**Constructed comparison:** A and B both show six kicks per two-arm cycle. B has larger leg excursions and a different moment of reversal relative to arm entry. The beat label is unchanged, but configuration and relative timing are different. If B feels harder, that is an effort observation; it does not by itself establish a larger propulsive contribution or lower body position. Those remain separate questions.

## Assumptions and limits

Manageable surface swimming, comfortable joints and available air. No fixed amplitude, kick ratio, locked knees or forced ankle range. No unsupported vertical-kick or reduced-breath exercise is introduced. Pain, distress or unreliable support ends the task. Use the existing [flutter-kick Method](../methods/explore-flutter-kick.md) for bounded activities.

## Evidence and evaluation

The [USMS guide](../references/us-masters-swimming-undated-freestyle-kick.md) describes alternating phases and propulsive, balance and coordination roles. [Swim England](../references/swim-england-2018-improving-front-crawl-technique.md) supplies a small-action coaching reference. Selected written descriptions were rechecked on 2026-10-14; videos and training sets were not evaluated. The phase comparison is constructed, not a measured efficacy finding. Neither source supplies an individual force allocation or metabolic estimate.
