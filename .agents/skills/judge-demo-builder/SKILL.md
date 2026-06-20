# Judge Demo Builder Skill

## Purpose

Use this skill when the team needs to turn a climate-health idea into a judge-facing demo, pitch, submission, video, or final presentation.

The goal is not to build the biggest product. The goal is to create the clearest possible judged experience:

```text
A specific user faces a specific climate-health problem.
The product uses credible data and AI to support a specific decision.
The demo shows that decision being made earlier, more safely, or more effectively than before.
```

This skill should help the team avoid vague dashboards, overbuilt prototypes, unclear AI claims, weak evidence, and demos that fail live.

## When to Use

Use this skill when asked to:

* define the first judged milestone
* design the judge-facing dashboard
* build the demo flow
* write the 3-minute pitch
* prepare Devpost text
* prepare a short video script
* prepare a social media post
* map the product to judging criteria
* decide what to show live versus cached
* simplify a product idea before final submission
* create fallback plans for demo reliability

## Core Principle

The demo should not show every feature.

The demo should show the core decision.

A strong hackathon demo answers:

```text
Who is the user?
What climate-health risk are they facing?
What decision do they need to make?
What data does the product use?
What does AI add?
What action becomes possible?
Why does this matter for health outcomes or resilience?
Why is the approach feasible and scalable?
What are the ethical and data limitations?
```

If the product cannot answer those questions, do not build more features. Clarify the product first.

## Judging Criteria Lens

Always map the project against these criteria:

```text
Impact:
Does the solution plausibly improve health outcomes or climate resilience?

Team:
Does the project reflect interdisciplinary collaboration and user awareness?

AI + Data:
Does the solution use relevant datasets, AI tools, or analytical methods in a meaningful way?

Innovation:
Is the approach novel, creative, or distinct from a generic dashboard or chatbot?

Feasibility:
Can the intended user realistically use this under existing constraints?

Scalability:
Could this expand beyond the pilot case?

Sustainability and resource use:
Does the team avoid wasteful AI use, unnecessary infrastructure, or unrealistic deployment assumptions?

Evidence and measurement:
How would success be measured?

Ethics and governance:
Are privacy, safety, bias, uncertainty, and data limitations acknowledged?
```

When reviewing a demo, score each area from 1 to 5 and explain the gap.

## Demo Surface Rules

A good demo surface should be:

* visible within 10 seconds
* understandable within 30 seconds
* actionable within 60 seconds
* connected to the pitch narrative
* supported by clear evidence and caveats
* reliable on cached or local data
* not dependent on fragile live APIs

Avoid demo surfaces that are:

* just a landing page
* just a chatbot
* just a static map
* just a model output
* mostly settings/account pages
* dependent on patient-identifiable data
* dependent on live geospatial/API processing
* impossible to explain in the final pitch

## Required Demo Flow

For every candidate product, produce a judge demo flow in this format:

```markdown
# Judge Demo Flow

## Demo Sentence

In one sentence, what will the judge see?

## User

Who is using the product?

## Problem

What climate-health problem are they facing?

## Decision

What decision must the user make?

## Before Product

What would the user do today without this tool?

## With Product

What does the product let them do earlier, faster, or better?

## Demo Steps

1.
2.
3.
4.
5.

## Final Output

What is the concrete output the product generates?

## Why It Matters

How does the output improve health outcomes, resilience, or preparedness?

## Evidence Used

Which datasets, assumptions, or models support the result?

## AI Role

What does AI do that is genuinely useful?

## Caveats

What should not be overclaimed?

## Fallback

What happens if the live demo fails?
```

## First Milestone Rule

The first judged milestone should be the smallest complete loop from evidence to action.

It should include:

```text
input/scenario
→ data/evidence
→ analysis/risk/readiness result
→ explanation
→ recommended action
→ output/export/shareable brief
```

Do not make authentication, account settings, database polish, onboarding, or advanced integrations the first milestone unless they are essential to the judged decision.

## Demo Reliability Rules

The final demo must not depend on fragile live processes.

Prefer:

* cached data
* small sample datasets
* precomputed model outputs
* precomputed maps
* local JSON/CSV files
* deterministic demo scenarios
* clear fallbacks

Avoid running these live during the pitch unless already proven reliable:

* large geospatial joins
* remote satellite queries
* PDF extraction
* long LLM processing chains
* external API calls
* database migrations
* package installs
* anything requiring secrets to work on stage

If a live model/API feature is included, provide a cached fallback that looks the same in the UI.

## Evidence-to-Action Pattern

Every demo should follow this pattern:

```text
Evidence:
What data or observation triggered the risk?

Interpretation:
What does the system infer from the evidence?

Decision:
What should the user do?

Action:
What does the product generate or prioritise?

Measurement:
How would we know whether the action worked?
```

Example:

```text
Evidence:
Rainfall anomaly rises and published disease reports show early cholera signal.

Interpretation:
Flood-linked cholera risk is high in specific LGAs.

Decision:
Which facilities should receive supplies or access planning first?

Action:
Ranked list of facilities and SMS advisory.

Measurement:
Fewer stockouts, faster pre-positioning, fewer service interruptions.
```

## AI Claim Discipline

Do not claim “AI predicts everything.”

Be specific.

Acceptable AI roles include:

```text
- extracting structured data from messy reports
- summarising evidence into a decision brief
- identifying missing or inconsistent fields
- ranking risk using defined features
- generating low-bandwidth advisory messages
- helping users interpret uncertainty
```

Risky or weak AI claims include:

```text
- “AI will solve climate-health”
- “AI predicts outbreaks accurately” without validation
- “AI replaces public health decision-makers”
- “AI knows which patients are at risk” without data and governance
```

Always distinguish between:

```text
rule-based logic
statistical model
machine learning model
LLM extraction
LLM advisory generation
synthetic demo output
validated real-world prediction
```

## Health and Safety Claim Discipline

For health-related projects, always state whether the product is:

```text
educational prototype
operational dashboard
research tool
public health decision-support prototype
clinical decision-support tool
regulated medical device
```

For a hackathon, default to:

```text
public health / operational decision-support prototype
```

Do not present the product as clinically validated.

Do not imply that the tool diagnoses, treats, or replaces clinicians or public health authorities.

## Data Boundary Rules

Prefer public, aggregate, synthetic, or clearly authorised data.

If using synthetic data, label it.

If using personal, patient-level, facility-level, or partner-provided data, document:

```text
source
permission basis
privacy risk
access controls
why it is necessary
how it is protected
what is shown publicly
```

For demos, avoid identifiable data entirely unless explicitly authorised and necessary.

## Pitch Structure

Use this 3-minute pitch structure:

```text
0:00–0:20 — Problem
What is the climate-health failure mode?

0:20–0:40 — User
Who experiences the problem and what decision do they need to make?

0:40–1:20 — Product
Show the workflow: input → evidence → risk/readiness result.

1:20–2:00 — Action
Show the ranked action, brief, advisory, export, or intervention plan.

2:00–2:25 — AI + Data
Explain what data and AI do, without overclaiming.

2:25–2:45 — Feasibility + Ethics
Explain public/synthetic data boundary, caveats, and why this can work.

2:45–3:00 — Scale
Show how the same pattern expands to more places, hazards, diseases, or facilities.
```

## Slide Structure

If making slides, use 5 slides maximum:

```text
Slide 1 — Problem and user
Slide 2 — Product workflow
Slide 3 — Demo output / action list
Slide 4 — AI, data, evidence, caveats
Slide 5 — Impact, feasibility, scale
```

Do not overload slides with technical architecture unless the judges ask.

The technical architecture should support the story, not replace it.

## Devpost Structure

When preparing a Devpost submission, use:

```markdown
# Project Name

## One-line Summary

## Problem

## User

## What It Does

## How It Uses AI and Data

## How We Built It

## Data Sources and Provenance

## Impact

## Feasibility

## Ethics, Privacy, and Safety

## What We Would Build Next

## Team
```

## Video Script Structure

The short video should be simple:

```text
1. State the problem.
2. Show the product in one screen.
3. Click through the core workflow.
4. Show the final output.
5. Explain why this matters.
6. End with scale and next step.
```

Do not record a long technical walkthrough.

Do not spend the first half of the video on team introductions.

## Social Post Structure

Use this structure:

```text
We built [project name] at Health in Climate AI.

Problem:
[One clear climate-health failure mode]

Solution:
[One sentence on what the product does]

Why it matters:
[Health/resilience impact]

How it works:
[Data + AI in simple terms]

What’s next:
[Scale or implementation pathway]
```

Keep it specific.

Avoid phrases like “revolutionary,” “game-changing,” or “AI-powered solution” unless backed by a concrete claim.

## Demo Freeze Checklist

Before final demo, check:

```text
App opens from the final URL.
Core demo path works without login issues.
All data needed for demo is cached or local.
No API key is exposed in frontend code.
Synthetic data is labelled.
Charts/maps load quickly.
The final output is visible.
The pitch matches the UI.
Fallback screenshots/video exist.
Team has rehearsed at least twice.
One person knows what to say if the app breaks.
```

## Fallback Plan

Every demo must have:

```text
Primary demo:
Live app with cached data.

Fallback 1:
Local app or local screenshots.

Fallback 2:
Short screen recording.

Fallback 3:
Static slide showing the final output.
```

If the live demo fails, do not apologise for long. Say:

```text
The live app is having a loading issue, so I’ll use the cached walkthrough. The core workflow is the same: evidence enters here, the model produces this risk/readiness output, and the user receives this action brief.
```

## Review Output Format

When reviewing a product idea or demo, output:

```markdown
# Judge Demo Review

## Current Demo Sentence

## What the Judge Will Understand

## What the Judge May Not Understand

## Strongest Judging Criteria

## Weakest Judging Criteria

## Demo Risk

## Evidence Risk

## Ethics/Governance Risk

## Minimum Viable Judge Flow

## What to Build Next

## What to Cut

## Final Pitch Line

## Rehearsal Questions Judges May Ask
```

## Cut Rules

Cut anything that does not strengthen the judged decision.

Usually cut:

* extra pages
* account/profile flows
* multiple unrelated hazards
* multiple unrelated countries
* weak visualisations
* vague AI chat features
* unverified datasets
* claims that cannot be defended
* stretch features that endanger the core demo

Keep:

* one strong user
* one strong climate-health problem
* one strong evidence pipeline
* one visible decision output
* one clear AI contribution
* one honest caveat
* one scale story

## Core Reminder

A judge does not reward the largest repo.

A judge rewards the clearest credible solution.

Build the smallest product that proves:

```text
This climate-health risk can be seen earlier.
This user can act sooner.
This data/AI workflow makes the action more targeted.
This could scale responsibly beyond the demo.
```
