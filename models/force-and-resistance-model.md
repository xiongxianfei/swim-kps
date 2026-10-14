---
id: "swim:mo:force-and-resistance-model"
type: "model"
version: "4.0.2"
language: "KPS 9.x"
status: "draft"
reviewed: null
basis_kind: "authored model with attributed inputs"
confidence: "scope-dependent; see evaluation"
references: ["swim:r:physics", "swim:r:drag", "swim:r:head-drag"]
uses_principles: ["swim:p:resistance-varies-with-speed-and-configuration", "swim:p:force-direction-and-application-affect-motion"]
uses_concepts: ["swim:c:drag", "swim:c:propulsion"]
uses_models: ["swim:mo:body-support-and-balance-model", "swim:mo:breaststroke-arm-action-model", "swim:mo:breaststroke-kick-model", "swim:mo:stroke-measurement-model"]
perspectives: ["fluid-dynamics", "biomechanics"]
---

# Force and resistance model

## Key takeaway

Interpret changes in forward motion without claiming that a simple equation determines the best technique.

## Summary

For a constant-mass approximation, net external forward force equals mass times forward acceleration. A speed change reveals the combined effect, not the isolated contribution of one hand movement.

## Local explanatory basis

The resistance encountered by a moving swimmer depends on speed relative to water, body configuration and flow conditions. The direction and point of application of external forces affect both the swimmer’s translation and rotation.

## Purpose
Interpret changes in forward motion without claiming that a simple equation determines the best technique.

## Representation
For the constant-mass whole-body approximation:

```text
sum of external forward forces = mass × forward acceleration
```

A useful rough drag representation is `D = 0.5 × density × Cd × reference area × relative speed²`. Here D is drag force, density is the fluid mass per unit volume, Cd is the dimensionless drag coefficient under the chosen area convention, and relative speed is the body’s speed with respect to the water. Geometry, orientation, flow regime and the chosen reference area affect the coefficient. Separating all fluid forces into “propulsion” and “drag” is itself a modeling choice in an unsteady articulated swimmer.

## Boundary and essential terms

The system is the entire swimmer, not one hand or foot. **External forces** come from water, gravity and any contact with a wall or aid. **Acceleration** is change in velocity over time; it is not the same as speed. **Propulsion** names contributions supporting the chosen direction of travel, while **resistance** names opposing contributions under the chosen decomposition. Pressure and friction distributed over the body contribute to the resultant water force.

Internal muscle forces change limb movement but do not appear as extra external thrust in the whole-body force sum. Geometry and water-relative motion connect that movement to external fluid forces. A force that changes forward motion can also contribute a turning moment depending on where and how it acts.

## Interfaces

| Connected Model | Relationship |
|---|---|
| [Body support and balance](body-support-and-balance-model.md) | Force application points and configuration enter the rotational account |
| [Breaststroke arm action](breaststroke-arm-action-model.md) and [kick](breaststroke-kick-model.md) | Limb movement changes fluid interaction; neither component can be inferred from whole-swimmer speed alone |
| [Stroke measurement](stroke-measurement-model.md) | Time and distance describe motion but do not separate the unseen force contributions |

## Worked example

**Constructed calculation:** A 70 kg whole-body approximation gaining 0.10 m/s of forward velocity in 0.50 s has mean acceleration 0.20 m/s² and mean net forward external force 14 N. That is the combined resultant, not a 14 N hand force: opposing resistance and contributions from other limbs remain unresolved. If a wall is involved, its force belongs in the same sum. The numbers illustrate Newton's relation and are not measurements of a swimmer.

## Assumptions
Classical mechanics; a specified water-relative motion and coordinate direction. No assumption that an actively swimming body has a constant drag coefficient or a rigid shape.

## Implications
An adjustment might change force direction, resistance, balance and breathing at once. A slower repeat can reflect a different effort or push-off, not necessarily increased drag. Use the model to generate alternatives, not to infer unseen forces from appearance.

## Evidence and evaluation
[University Physics Volume 1](../references/moebs-2016-university-physics-volume-1.md#net-force-and-translational-motion) and [Drag Equation](../references/nasa-undated-drag-equation.md#drag-equation-and-flow-dependent-coefficient) support the relationships. [Effect of The Swimmer’s Head Position on Passive Drag](../references/cortesi-2015-head-position-and-passive-drag.md#head-position-under-passive-towing) concerns measured passive drag under towing, not ordinary active technique. Compare observations with explicit predictions.

## Limits
The model does not calculate metabolic cost, prescribe the hand path, prove a cue works or diagnose discomfort.

## Local evidence summary


[University Physics Volume 1](../references/moebs-2016-university-physics-volume-1.md#net-force-and-translational-motion) contributes: In the constant-mass classical approximation, net external force determines centre-of-mass acceleration.

[Drag Equation](../references/nasa-undated-drag-equation.md#drag-equation-and-flow-dependent-coefficient) contributes: The conventional drag equation relates drag to density, speed squared, reference area and a drag coefficient; the coefficient depends on the configuration and reference-area convention.

[Effect of The Swimmer’s Head Position on Passive Drag](../references/cortesi-2015-head-position-and-passive-drag.md#head-position-under-passive-towing) contributes: Head position affected passive underwater drag in experienced male swimmers under the study’s towing conditions.

Citation identifies support for the stated claim and scope. Any further causal or practical inference remains separately reviewable.

## Deeper knowledge

Canonical dependencies and Reference records provide additional derivation, source inspection and alternatives. They are not required to carry out the local explanation or procedure.

- **Concepts:** [Drag](../concepts/drag.md)
- **Concepts:** [Propulsion](../concepts/propulsion.md)
- **Principles:** [Resistance varies with speed and configuration](../principles/resistance-varies-with-speed-and-configuration.md)
- **Principles:** [Force direction and application affect motion](../principles/force-direction-and-application-affect-motion.md)
- **References:** [University Physics Volume 1](../references/moebs-2016-university-physics-volume-1.md)
- **References:** [Drag Equation](../references/nasa-undated-drag-equation.md)
- **References:** [Effect of The Swimmer’s Head Position on Passive Drag](../references/cortesi-2015-head-position-and-passive-drag.md)
