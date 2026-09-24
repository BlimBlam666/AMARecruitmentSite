# Academy of Mercenary Arts — Recruitment Site

Public recruitment and general-information website for the Academy of Mercenary Arts.

> Developing Fighters. Building Warlords.

## Project status

**Foundation complete — ready for public page build**

The blueprint is approved and the shared technical foundation is in place. The repository now has four page shells, a mobile-first Academy design system, accessible responsive navigation, shared header/footer, a development favicon placeholder, a custom 404 page, and automated structural validation.

The real public-facing homepage content is the next implementation phase.

## Purpose

This site is the Academy's public front gate. It should help a newcomer quickly understand:

- what the Academy of Mercenary Arts is,
- what people learn here,
- what the culture values,
- what a first experience looks like,
- how the Academy relates to Amtgard and local field authority,
- and how to take the next step.

The site is **not** intended to replace the Academy Command Hall, the full course library, Amtgard's Rules of Play, Dragonspine governance, local reeves, park officers, or other official authorities.

## Site map

1. **Home** — recruitment story and primary first impression
2. **About** — mission, values, Cadets, Preceptors, and authority boundaries
3. **Training** — the Academy training path and representative courses
4. **Start Here** — first-day expectations and verified next steps

Supporting links and social channels belong in the footer or contextual calls to action rather than becoming additional top-level pages.

## Development

Run the structural check:

```bash
python scripts/check_site.py
```

Preview locally:

```bash
python -m http.server 8080
```

Then visit `http://localhost:8080/`.

## Project documents

- [Site Blueprint](docs/SITE_BLUEPRINT.md)
- [Build-Ready Foundation](docs/BUILD_READY_FOUNDATION.md)

## Media status

The current favicon and `AMA` shield mark are development placeholders only. Final Academy heraldry and approved training photography must replace them before public launch.

## Authority standard

The Academy teaches skill, safety, discipline, and learning habits. It does **not** replace Amtgard's current Rules of Play, Dragonspine Corpora, local reeves, weapon checkers, champions, officers, event staff, or other proper authorities.
