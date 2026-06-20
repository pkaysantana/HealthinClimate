---
name: dataset-triage
description: >-
  Rapidly assess a candidate dataset for a Health in Climate project — coverage,
  granularity, freshness, licensing, and fitness for the question at hand. Use
  when deciding whether a dataset is worth ingesting before committing build time.
---

# Dataset Triage

Score a candidate dataset fast, before you sink time into ingesting it.

## When to use

- You found a dataset (London Datastore, Met Office, DEFRA, NHS, Copernicus, etc.)
  and need to decide *go / no-go* in minutes.
- You have several overlapping sources and must pick one.

## Triage checklist

1. **Question fit** — does it actually answer the project question, or just look
   relevant? Name the column(s)/feature(s) you'd use.
2. **Geography & granularity** — does it resolve to the unit you need (borough,
   LSOA, sub-local-authority, postcode)? London-specific or national?
3. **Time coverage & freshness** — date range, update cadence, last refresh.
4. **Access** — open download vs. signed/expiring URL vs. API key vs. login.
   Flag short-lived signed (SAS) links — see [[data-provenance]].
5. **Format & size** — GeoJSON / CSV / API; rough row/feature count; will it fit
   in `data/raw/` and process locally?
6. **Licensing** — open (OGL), attribution required, or restricted? Demo-safe?

## Output

A short verdict block:

```
VERDICT: go | maybe | no-go
Fit:        <one line>
Granularity:<unit>
Freshness:  <range / cadence>
Access:     <open | key | signed-url | login>  [⚠ if expiring]
License:    <OGL / other>  [demo-safe? yes/no]
Blockers:   <anything that kills it>
```

Record provenance for anything you keep with [[data-provenance]]; if it informs a
build choice, hand off to [[health-climate-idea-selector]].
