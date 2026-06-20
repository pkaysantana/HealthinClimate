---
name: data-provenance
description: >-
  Capture where every dataset came from and how it was obtained so results stay
  reproducible and demo-safe. Use whenever a dataset lands in data/raw/ or a
  download URL needs recording, especially short-lived signed (SAS) links.
---

# Data Provenance

Every file in `data/raw/` should be traceable to its source. Judges and
teammates need to know what the data is, where it came from, and whether it can
be re-fetched.

## When to use

- A new file lands in `data/raw/` (manual download or `make install`).
- A source uses an **expiring signed URL** (e.g. ArcGIS SAS links — the starter's
  Met Office links expire ~1h after minting and 403 afterward).
- Before a demo, to confirm nothing depends on a stale or unlicensed source.

## Record per dataset

Append an entry to `docs/datasets/PROVENANCE.md` (create if missing):

```
## <filename>
- Source:     <publisher + page URL>
- Obtained:   <date> via <make install | manual | API>
- URL type:   <permanent | api-key | signed/SAS (expires!)>
- Refresh:    <how to re-fetch — command or steps>
- License:    <OGL / other>  attribution: <text>
- Notes:      <transformations, known gaps>
```

## Rules

- **Never commit raw data or secrets.** Keep `data/raw/`, `data/cached/` out of
  git (gitignore); commit only provenance + scripts.
- **Signed URLs are not provenance** — they expire. Record the *source page* and
  the *refresh procedure*, not just the throwaway link.
- Pair with [[dataset-triage]] when assessing a new source; the data you keep
  flows into [[health-climate-idea-selector]] and [[judge-demo-builder]].
