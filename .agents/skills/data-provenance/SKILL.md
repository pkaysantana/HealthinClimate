# `.agents/skills/data-provenance/SKILL.md`

# Data Provenance Skill

## Purpose

Use this skill to preserve an evidence trail for every dataset, transformation, generated output, chart, model feature, dashboard metric, and claim used in the hackathon project.

The goal is to make the project credible, auditable, and judge-ready.

This skill should ensure that every piece of evidence can answer:

* Where did this data come from?
* Who produced it?
* What geography and time period does it cover?
* What transformations did we apply?
* What assumptions did we make?
* What are its limitations?
* Is it public, synthetic, partner-provided, or unclear?
* Can we safely show it in a public demo?
* What should we say if judges ask about it?

## When to Use

Use this skill when:

* adding a dataset
* creating sample or synthetic data
* cleaning or transforming raw data
* building a model feature
* generating dashboard metrics
* writing a pitch claim
* creating charts or maps
* preparing Devpost/project documentation
* reviewing whether the project is ethically and legally safe to present

## Required Provenance Record

For every dataset, create or update a provenance entry with this structure:

```markdown
## Dataset: [Name]

Source:
URL or access method:
Producer/organisation:
Downloaded/accessed on:
Geography:
Time range:
File format:
Raw file location:
Processed file location:
Public / synthetic / partner-provided / unclear:
Licence / usage terms:
Contains personal data? Yes/No/Unclear:
Contains health-sensitive data? Yes/No/Unclear:
Level of aggregation:
Main variables:
Transformations applied:
Assumptions:
Known limitations:
Quality concerns:
How it is used in the demo:
What it should not be used to claim:
Fallback if unavailable:
```

## Transformation Record

For every script or manual transformation, document:

```markdown
## Transformation: [Name]

Input files:
Output files:
Script/path:
Purpose:
Steps performed:
Columns added:
Columns removed:
Rows filtered:
Geography changed? Yes/No:
Aggregation changed? Yes/No:
Synthetic data introduced? Yes/No:
Assumptions:
Validation checks:
Known risks:
```

## Synthetic Data Rules

Synthetic data is allowed for demos, but it must be labelled clearly.

For synthetic data, document:

```markdown
## Synthetic Data: [Name]

Why synthetic data is needed:
What real-world concept it represents:
How values were generated:
Which fields are synthetic:
Which fields, if any, are based on public data:
What assumptions were used:
What claims this synthetic data can support:
What claims this synthetic data cannot support:
```

Never present synthetic values as observed reality.

Use phrases like:

* “illustrative synthetic facility stock”
* “demo data”
* “simulated record”
* “logic is real; values are illustrative”

Do not use phrases like:

* “verified facility stock”
* “actual patient demand”
* “confirmed facility readiness”
* unless those claims are true and documented.

## Claim Provenance

For every important pitch or dashboard claim, create a claim record:

```markdown
## Claim: [Claim text]

Evidence source:
Dataset(s):
Computation:
Assumption:
Confidence level:
Limitations:
Can be shown to judges? Yes/No/With caveat:
Suggested wording:
```

## Output Format

When asked to review provenance, produce:

```markdown
# Provenance Review

## Safe to Use Publicly

## Needs Caveat

## Do Not Claim Yet

## Missing Evidence

## Synthetic or Illustrative Components

## Recommended Wording for Pitch

## Files to Update
```

## Safety and Governance Rules

Do not commit API keys, secrets, credentials, private data, identifiable health information, or unauthorised partner data.

If a data source is unclear, mark it as unclear.

If a claim is unsupported, say so directly.

If a model output is heuristic, label it as heuristic.

If a dashboard metric is based on synthetic or incomplete data, label it in the UI or documentation.

If the project involves health outcomes, distinguish between:

* educational prototype
* operational dashboard
* research tool
* clinical decision-support tool
* regulated medical device

Do not present the hackathon prototype as clinically validated.
