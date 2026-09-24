# Build-Ready Foundation

The planning phase is complete and the repository now contains the shared technical foundation for the public Academy website.

## What exists now

- Four real routes:
  - `/`
  - `/about/`
  - `/training/`
  - `/start/`
- Shared responsive header and footer.
- Accessible mobile navigation with Escape-key support and ARIA state.
- Skip links and visible keyboard focus.
- Academy design tokens for obsidian, parchment/bone, brass, thistle, and iron.
- Mobile-first typography and spacing.
- Reduced-motion support.
- Development favicon/brand placeholder clearly marked as non-canonical.
- Custom 404 page.
- GitHub Pages static-serving support through `.nojekyll`.
- Automated structural validation on pushes and pull requests.

## Deliberately not complete yet

The real public site content has **not** been built into the shells. That is the next phase.

The following remain intentionally pending:

1. Final Academy crest / favicon.
2. Approved real training photographs.
3. Verified social links.
4. Verified Amtgard / Rules / Dragonspine / Obsidian Gate links.
5. Verified public contact method.
6. Verified current attendance location/time.
7. Current waiver / age requirement source.
8. Loaner-equipment policy.
9. Final Open Graph/share image.
10. GitHub Pages publication.

## Next implementation target

### Phase 2 — Home Page

Build the approved homepage narrative in this order:

1. Hero
2. Training With Purpose
3. Training Path
4. What Training Feels Like
5. The Fighter We Are Trying to Build
6. Academy / Amtgard Relationship
7. Final recruitment CTA

The homepage should be fully useful with temporary media placeholders before real photographs are substituted.

## Development rule

Do not add a feature merely because it is easy to code.

Every public element must help a newcomer:
- understand the Academy,
- trust the Academy,
- see the training path,
- or take the next step.

## Local check

From the repository root:

```bash
python scripts/check_site.py
python -m http.server 8080
```

Then open:

```
http://localhost:8080/
```

The structural checker should pass before each merge.
