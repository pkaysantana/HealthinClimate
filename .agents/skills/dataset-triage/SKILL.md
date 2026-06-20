# `.agents/skills/dataset-triage/SKILL.md`

# Dataset Triage Skill

## Purpose

Use this skill when the team needs to inspect, compare, prioritise, or reject datasets for a climate-health hackathon prototype.

The goal is not to find the most impressive dataset. The goal is to identify which datasets can support a working, judge-facing prototype within the available time.

This skill should help the team decide:

* which datasets are usable immediately
* which datasets require cleaning or transformation
* which datasets should only be used as reference material
* which datasets are too slow, unclear, large, fragile, or legally risky for the hackathon
* which datasets best support impact, AI/data use, feasibility, scalability, evidence, and ethics

Do not lock the repo into one product idea unless a final product brief exists.

## When to Use

Use this skill when asked to:

* inventory datasets
* compare datasets
* choose datasets for an idea
* assess whether a dataset is suitable for a demo
* prepare dataset documentation
* identify public, synthetic, partner-provided, or unclear data
* connect datasets to candidate ideas
* decide whether a dataset should be committed, cached, sampled, or fetched

## Core Behaviour

For each dataset, classify it using this structure:

```text
Dataset name:
Location/path:
Source:
Theme:
Geography:
Time coverage:
Format:
Size:
Access method:
License/usage status:
Public/synthetic/partner-provided/unclear:
Health relevance:
Climate relevance:
Operational relevance:
Ease of use:
Demo usefulness:
Ethics/privacy risk:
Quality caveats:
Recommended use:
Do not use for:
```

## Scoring Matrix

Score each dataset from 1 to 5 on:

```text
1. Relevance to the likely product idea
2. Climate-health relevance
3. Ease of use in 24–48 hours
4. Source trust/provenance clarity
5. Geographic usefulness
6. Health-system/actionability relevance
7. Demo value
8. Ethics/privacy safety
9. Feasibility of cleaning/transformation
10. Scalability story
```

Then produce an overall recommendation:

```text
Use now:
Use if time:
Reference only:
Avoid for this hackathon:
Needs permission/clarification:
```

## Dataset Triage Rules

Prefer datasets that are:

* public or clearly authorised
* small enough to inspect quickly
* easy to transform into CSV/JSON/GeoJSON
* directly connected to a user decision
* useful for a visual or ranked action output
* explainable to judges in one sentence
* compatible with public/synthetic-only data boundaries

Be cautious with datasets that are:

* very large
* poorly documented
* licence-unclear
* patient-level or identifiable
* dependent on fragile APIs
* only usable after heavy geospatial processing
* impressive but not connected to a decision
* hard to explain in a 3-minute pitch

Reject or defer datasets that:

* contain secrets or credentials
* include identifiable personal/health data without a clear governance basis
* cannot be cited or explained
* require long setup steps that block the demo
* are not relevant to any candidate product idea

## Output Format

When triaging datasets, produce:

```markdown
# Dataset Triage Report

## Executive Recommendation

Use these datasets first:
1.
2.
3.

Avoid or defer:
1.
2.
3.

## Dataset Inventory

| Dataset | Theme | Geography | Format | Public/Synthetic/Partner/Unclear | Demo Usefulness | Risk | Recommendation |
|---|---|---|---|---|---|---|---|

## Best Dataset Combinations

### Candidate Idea 1:
Required datasets:
Useful optional datasets:
Missing data:
Synthetic fallback:

### Candidate Idea 2:
Required datasets:
Useful optional datasets:
Missing data:
Synthetic fallback:

## Data Risks

## Next Actions
```

## Important Constraints

Do not overclaim data quality.

Do not treat synthetic data as real.

Do not imply that public aggregate data can prove individual clinical risk.

Do not import large raw datasets into the repo unless explicitly asked.

If a dataset is useful but large, recommend committing a small sample and adding a fetch script or manifest.

If a dataset has unclear licensing or provenance, flag it clearly.
