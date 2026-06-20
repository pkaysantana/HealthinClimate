---
name: judge-demo-builder
description: >-
  Shape a chosen project into a tight, judge-ready demo — narrative, the one
  killer visual, and a scripted walkthrough mapped to the judging criteria. Use
  when preparing the submission or pitch.
---

# Judge Demo Builder

Package the work so judges grasp the value in the first 30 seconds and can score
it against their rubric.

## When to use

- A project is chosen (via [[health-climate-idea-selector]]) and you're preparing
  the demo, pitch, or written submission.

## Build the demo around

1. **The hook (≤30s)** — the problem and who it hurts, in one sentence.
   "Heat-vulnerable boroughs are X; here's where and why."
2. **The killer visual** — one map/chart that makes the insight obvious. Pick the
   single artifact that earns the reaction; cut the rest.
3. **The evidence** — name the datasets and *why they're trustworthy* (provenance
   from [[data-provenance]]). Judges reward defensible data.
4. **The action** — what someone (council, NHS, resident) could *do* with this.
5. **The scripted walkthrough** — a literal click-by-click run sheet timed to the
   slot. Rehearse it; assume the live data fetch fails and pre-cache results in
   `data/cached/`.

## Map to judging criteria

Keep a checklist in `docs/judging/`:

```
Criterion        | Covered by            | Evidence
Impact           | hook + action         | <slide/visual>
Innovation       | differentiation       | <...>
Technical depth  | data + pipeline       | <scripts/, data/processed/>
Data integrity   | provenance            | docs/datasets/PROVENANCE.md
Presentation     | scripted walkthrough  | run sheet
```

## Failure-proofing

- **Pre-cache everything** for the live demo — never depend on an expiring signed
  URL mid-pitch.
- Have a 60-second fallback if a tool breaks: a recorded clip or static screenshot.
