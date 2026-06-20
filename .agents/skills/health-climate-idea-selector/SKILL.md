---
name: health-climate-idea-selector
description: >-
  Turn available datasets into a ranked shortlist of Health in Climate project
  ideas, scored on impact, feasibility, data-readiness, and demo-ability. Use
  when choosing what to build during the hackathon.
---

# Health & Climate Idea Selector

Convert "we have these datasets" into "we should build this," with a defensible
ranking instead of a hunch.

## When to use

- Early in the hackathon, picking the project.
- Mid-event, when a dataset falls through (e.g. an expired source) and you need a
  fast pivot.

## Inputs

- Available, triaged datasets (see [[dataset-triage]]) with known provenance
  (see [[data-provenance]]).
- The challenge framing: London-focused, outcome-driven questions like
  "Find the most heat-vulnerable boroughs and explain why" or
  "Compare summer temperature projections with air quality and NHS pressure."

## Score each idea (1–5)

| Criterion | Question |
| --- | --- |
| **Impact** | Does it address a real health-in-climate need? |
| **Feasibility** | Buildable in the time left with current skills? |
| **Data-readiness** | Is the data in hand, clean enough, demo-safe? |
| **Differentiation** | More than an obvious chart? Insight or action? |
| **Demo-ability** | Can it be shown convincingly in <3 min? |

Weight **data-readiness** and **demo-ability** heavily — a brilliant idea with no
usable data loses to a solid idea you can actually show.

## Output

```
SHORTLIST (ranked)
1. <idea> — total <n>/25 | datasets: <...> | risk: <...>
2. ...
RECOMMENDATION: <idea> because <one line>
```

Hand the winner to [[judge-demo-builder]].
