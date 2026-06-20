# `.agents/skills/health-climate-idea-selector/SKILL.md`

# Health Climate Idea Selector Skill

## Purpose

Use this skill to compare candidate climate-health product ideas and help the team choose the strongest hackathon direction.

The goal is to choose an idea that is:

* impactful
* feasible
* data-supported
* judge-readable
* buildable within the hackathon
* ethically safe
* scalable beyond the first demo
* suitable for the actual team’s skills

This skill should not force a decision too early. It should keep options open until the team has enough information.

## When to Use

Use this skill when:

* the team has not finalised the idea
* multiple candidate ideas are being discussed
* the team needs to compare heat, flood, respiratory, infrastructure, supply chain, or other climate-health directions
* new teammates bring new expertise
* datasets have been inventoried and need to be mapped to ideas
* the team needs to choose a Milestone 1 evidence story

## Candidate Idea Template

For each idea, evaluate:

```markdown
## Candidate: [Name]

One-line pitch:
Primary user:
User pain:
Climate-health link:
Before / During / After phase:
Health outcome or resilience outcome:
Core decision the product supports:
AI role:
Datasets needed:
Available datasets:
Missing datasets:
Synthetic fallback:
Demo surface:
Build difficulty:
Main technical risk:
Main data risk:
Main ethics/governance risk:
Why judges would care:
Why this might fail:
Minimum viable demo:
Scale story:
```

## Judging Criteria Scoring

Score each idea from 1 to 5:

```text
Impact:
Team fit:
AI + Data:
Innovation:
Feasibility:
Scalability:
Sustainability/resource use:
Evidence and measurement:
Ethics and governance:
Demo clarity:
```

Then give:

```text
Total score:
Confidence level:
Recommended rank:
```

## Candidate Ideas to Consider

Always consider at least these options unless the team has explicitly ruled them out:

```text
1. Flood/cholera facility readiness
2. Heat vulnerability and prevention briefing
3. Climate-health infrastructure verification assistant
4. Respiratory/air-quality early warning
5. Health-system supply chain continuity
6. Low-carbon care / sustainable infrastructure decision support
```

## Decision Rules

Prefer ideas that have:

* a clear user
* a clear climate-health event
* a clear decision
* available public or synthetic-safe data
* a visible demo surface
* an explainable AI/data component
* a plausible implementation pathway
* a strong “before the crisis escalates” story
* an ethical data boundary

Be cautious with ideas that:

* require patient-level data
* need live APIs to work during judging
* depend on complex mobile workflows
* require unvalidated clinical claims
* need too many datasets joined before anything works
* sound impressive but do not produce an action
* cannot be explained in under 30 seconds

## Recommended Output

When asked to choose between ideas, produce:

```markdown
# Idea Selection Review

## Current Best Choice

## Ranking

| Rank | Idea | Score | Why |
|---|---|---|---|

## Best Fit for Current Team

## Best Fit for Available Data

## Best Fit for Judging Criteria

## Fastest Demo

## Highest-Risk Idea

## Recommended Milestone 1

## What to Ask Teammates Before Locking
```

## Core Principle

The final idea should not be “a dashboard” or “an AI model.”

The final idea should be:

```text
A specific user uses a specific evidence workflow to make a specific climate-health decision earlier than they otherwise could.
```
