# Academy of Mercenary Arts — Recruitment Site

Public recruitment and general-information website for the Academy of Mercenary Arts.

> Developing Fighters. Building Warlords.

## Project status

**Public v1 forged — ready for GitHub Pages publication**

The full four-page recruitment site is built:

1. **Home** — public explanation, Academy identity, Fighter Track overview, training method, values, and primary recruitment calls to action.
2. **About** — purpose, Academy Standard, Cadets and Preceptors, Preceptor's Creed, and authority boundaries.
3. **Training** — F100–F500 Fighter Track, representative courses, lesson method, Dragonspine Civic Arms, and Graduate Trial gates.
4. **Start Here** — newcomer fit, first-visit flow, what to bring, safety, local Obsidian Gate connection, and FAQ.

## Design

The site is intentionally:

- mobile-first,
- dependency-light,
- accessible,
- static and fast,
- usable without JavaScript except for enhanced mobile navigation,
- medieval in identity without becoming a game HUD,
- and clear about the Academy's relationship to Amtgard and proper field authority.

The current CSS-built shield/book/sword treatment and favicon are development identity marks. Replace them with final approved Academy heraldry when the production crest asset is ready.

## Local development

Run the structural check:

```bash
python scripts/check_site.py
```

Preview locally:

```bash
python -m http.server 8080
```

Then visit:

```
http://localhost:8080/
```

## GitHub Pages publication

This is a plain static site and can publish directly from the repository root.

In GitHub:

1. Open **Settings → Pages**.
2. Under **Build and deployment**, choose **Deploy from a branch**.
3. Select **main** and **/(root)**.
4. Save.

Expected public URL:

```
https://blimblam666.github.io/AMARecruitmentSite/
```

## Project documents

- [Site Blueprint](docs/SITE_BLUEPRINT.md)
- [Build-Ready Foundation](docs/BUILD_READY_FOUNDATION.md)

## Pre-launch media upgrades

The site can publish now, but the strongest later visual upgrade will be replacing the CSS hero emblem with the final Academy crest and adding approved real Academy/Amtgard training photographs.

Do not use unverified social/contact links or stale weekly schedules merely to fill space.

## Authority standard

The Academy teaches skill, safety, discipline, and learning habits. It does **not** replace Amtgard's current Rules of Play, Dragonspine Corpora, local reeves, weapon checkers, champions, officers, event staff, or other proper authorities.
