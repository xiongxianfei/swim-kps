---
id: "swim:mo:body-support-and-balance-model"
type: "model"
version: "4.0.2"
language: "KPS 9.x"
status: "draft"
reviewed: null
basis_kind: "authored model with attributed inputs"
confidence: "scope-dependent; see evaluation"
references: ["swim:r:physics", "swim:r:rnli"]
uses_principles: ["swim:p:buoyancy-and-orientation-are-distinct", "swim:p:observation-does-not-identify-one-cause"]
uses_concepts: ["swim:c:buoyancy", "swim:c:body-alignment"]
uses_models: ["swim:mo:breaststroke-kick-model", "swim:mo:breathing-and-air-access-model", "swim:mo:force-and-resistance-model", "swim:mo:water-competence-model"]
perspectives: ["fluid-dynamics", "biomechanics"]
---

# Body support and balance model

## Key takeaway

Separate floating support, orientation and movement when investigating sinking or rocking sensations.

## Summary

Record whether a pitch change follows the breath, leg recovery or arm entry. A wall adds an external support force, so a supported posture need not predict the same body orientation while swimming.

## Local explanatory basis

A body can have enough buoyant support to float while adopting an orientation that is not horizontal. A sensation, visible motion or single performance change can be consistent with more than one explanation.

## Purpose
Separate floating support, orientation and movement when investigating sinking or rocking sensations.

## Representation
```text
weight + distributed buoyant support + other fluid forces
                  ↓
       translation and rotation of the body
                  ↑
      posture, breathing, movement and water conditions
```

Hydrostatic buoyancy concerns displaced-water weight. The balance of moments also matters to orientation; total upward support alone does not imply horizontal legs.

## Boundary and essential terms

The represented system is the swimmer's whole body, with water, gravity and any wall contact supplying external forces. **Weight** acts downward through the centre of mass, the mass-weighted average body position. **Buoyancy** is the net hydrostatic support associated with displaced water; its resultant acts through the centre of buoyancy, the centre of the displaced volume. **Moment** means the turning effect of a force about a selected point or axis. Its magnitude depends on force and perpendicular distance from that axis to the force's line of action.

In the hydrostatic approximation, buoyancy is `water density × gravitational acceleration × displaced volume`. Equal upward and downward resultant forces can remove vertical acceleration without cancelling their turning effects. Orientation depends on the moment balance as well. In movement, additional fluid forces and changing body configuration enter both balances; the static picture alone is insufficient.

## Interfaces

| Connected Model | Relationship |
|---|---|
| [Force and resistance](force-and-resistance-model.md) | The same external forces contribute to translation; their application points also matter to orientation |
| [Breathing and air access](breathing-and-air-access-model.md) | Body and head orientation affect mouth clearance, while breathing and body movement change the configuration |
| [Breaststroke kick](breaststroke-kick-model.md) | Leg recovery changes body configuration and water interaction within the balance problem |
| [Water competence](water-competence-model.md) | Known support and recovery conditions constrain the task; floating is not a readiness certificate |

## Worked example

**Constructed case:** A swimmer's legs rest lower than the chest while the body remains supported at the surface. That observation is compatible with buoyant support and a nonhorizontal orientation. Adding a wall hold introduces another external force and moment, so a more horizontal supported posture does not establish that the swimmer has changed buoyancy or can maintain that orientation unaided. The Model separates support from orientation without requiring a corrective drill.

## Assumptions
The task has dependable support/footing and an already known way to clear the mouth and recover. A first-time unsupported float or standing recovery needs appropriate in-person instruction. A secure wall changes the forces and support, so it cannot be used to infer the same balance or propulsion as free swimming. Emergency back-floating guidance and a prone technique rehearsal serve different goals.

## Implications
A float with lower legs is not automatically faulty. A breathing-related dip should be checked against actual movement timing, not attributed immediately to the neck, hips or “weak core.”

## Evidence and evaluation
[University Physics Volume 1](../references/moebs-2016-university-physics-volume-1.md#moment-arms-and-hydrostatic-buoyancy) supplies the physical relationship; [Float to Live](../references/rnli-undated-float-to-live.md#floating-and-individual-body-position) supplies practical variability guidance. Video may describe posture but does not independently measure its drag.

## Limits
No ideal pelvis angle, rigid-bracing requirement or health diagnosis follows. Seek support when control or air access is uncertain.

## Local evidence summary


[University Physics Volume 1](../references/moebs-2016-university-physics-volume-1.md#moment-arms-and-hydrostatic-buoyancy) contributes: A force’s rotational effect depends on its direction and moment arm; hydrostatic buoyancy equals the weight of displaced fluid.

[Float to Live](../references/rnli-undated-float-to-live.md#floating-and-individual-body-position) contributes: Floating can involve gentle movement and varies between people; perfectly horizontal legs are not a universal condition.

Citation identifies support for the stated claim and scope. Any further causal or practical inference remains separately reviewable.

## Deeper knowledge

Canonical dependencies and Reference records provide additional derivation, source inspection and alternatives. They are not required to carry out the local explanation or procedure.

- **Concepts:** [Buoyancy](../concepts/buoyancy.md)
- **Concepts:** [Body alignment](../concepts/body-alignment.md)
- **Principles:** [Buoyancy and orientation are distinct](../principles/buoyancy-and-orientation-are-distinct.md)
- **Principles:** [Observation does not identify one cause](../principles/observation-does-not-identify-one-cause.md)
- **References:** [University Physics Volume 1](../references/moebs-2016-university-physics-volume-1.md)
- **References:** [Float to Live](../references/rnli-undated-float-to-live.md)
