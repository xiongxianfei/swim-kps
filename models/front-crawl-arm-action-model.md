---
id: "swim:mo:front-crawl-arm-action-model"
type: "model"
version: "1.0.0"
language: "KPS 9.x"
status: "draft"
reviewed: null
basis_kind: "authored model with attributed inputs"
confidence: "qualitative account retaining coaching alternatives"
references: ["swim:r:se-crawl", "swim:r:usms-crawl-pull"]
uses_models: ["swim:mo:force-and-resistance-model", "swim:mo:front-crawl-body-rotation-model", "swim:mo:front-crawl-cycle-model"]
---

# Front crawl arm action model

## Key takeaway

Each arm repeats a connected cycle; entry, preparation, underwater action and recovery influence one another.

## Summary

An arm enters, changes its hand and forearm orientation, acts through the water, exits and returns. The other arm has a concurrent cycle. This Model explains one arm's recurring function; the whole-stroke Model explains their relative timing alongside breathing, rotation and kicking.

## Purpose and boundary

Explain why recognising an entry or hand path is insufficient to explain the whole arm cycle. Include the hand, forearm, upper arm, torso reference and surrounding water. Treat the opposite arm, body rotation and breathing as connected systems rather than assuming a fixed catch-up pause.

## Essential terms and components

| Term | Meaning |
|---|---|
| Entry | Hand crosses the water surface to begin the underwater portion |
| Catch or preparation | Hand and forearm reposition for the ensuing water interaction |
| Underwater action | Continued arm movement interacting with water after preparation |
| Exit and recovery | Transition out of the water and return toward the next entry |
| Cycle | One named arm's entry to its next entry; two individual entries occur in a complete two-arm cycle |

## Representation and mechanism

```text
entry → preparation → underwater action → exit → recovery → entry
             configuration + water-relative movement
                              ↓
                 fluid force on the arm
```

Entry establishes conditions for preparation. Preparation changes the surface orientation presented by the hand and forearm; it is not literally gripping stationary water. Subsequent movement contributes to forces on the swimmer. Recovery establishes the next entry, so an entry difference can originate before the hand touches the water.

Net forward acceleration depends on the sum of external forces on the whole swimmer. A path described relative to the torso differs from a path relative to the pool because the swimmer translates and rotates. Neither tracing establishes force magnitude. Phase names organise observations; they do not imply that water interaction starts or stops instantaneously at each label.

## Interfaces

| Connected Model | Relationship |
|---|---|
| [Body rotation](front-crawl-body-rotation-model.md) | Torso orientation changes the reference for the arm path and the recovery configuration |
| [Front crawl cycle](front-crawl-cycle-model.md) | The opposite arm and breathing events determine the context of each local phase |
| [Force and resistance](force-and-resistance-model.md) | Arm-water interaction is one contribution to whole-body motion, not an isolated speed reading |

## Worked example

**Constructed case:** A side recording shows a hand moving backward relative to the torso. A reader labels the movement an effective catch. The recording establishes a relative path, but not necessarily the hand/forearm orientation, water-relative velocity or force. A view that reveals preparation can answer the configuration question; measured motion still cannot isolate that arm's contribution. The Model identifies which information is missing without prescribing a harder pull.

## Assumptions and limits

Surface front crawl with unforced movement. Swim England specifies a thumb-first entry and an hourglass-like path; USMS describes a relatively flat entry with individual variation. The package retains a comfortable same-side entry as a starting reference, not a proven universal optimum. No locked reach, rigid S path, maximal finish or prescribed elbow angle follows. Pain ends the aggravating task. Activities remain in the [arm Method](../methods/explore-front-crawl-arms.md).

## Evidence and evaluation

The official [Swim England](../references/swim-england-2018-improving-front-crawl-technique.md) arm section and [USMS](../references/us-masters-swimming-undated-freestyle-pull.md) introductory, entry and preparation text were rechecked on 2026-10-14. Linked videos, sets and exercises were not evaluated. Their movement descriptions inform the phase account; reference-frame reasoning and the example are authored applications of mechanics. Their disagreement is retained rather than counted as independent confirmation of one technique.
