# Changelog

Notable changes to the bionic-coding.com site.

## [Unreleased]

### Added

- A five-page CRUX section (`/crux/`, `/crux/installation/`, `/crux/setup/`,
  `/crux/reference/`, `/crux/in-practice/`) with a `crux` layout that renders a series
  nav and a prev/next pager from `_data/crux.yml`. CRUX takes the manifesto's
  top-nav slot; the manifesto stays at `/manifesto/`.
- Homepage: a "Bionic Tools" block introducing Crux (`crux_blurb` in `index.md`) at
  the bottom of the page, below the manifesto callout, and an "Explore crux →" hero link.

### Fixed

- Mobile nav (≤46rem): the menu card renders as an out-of-flow overlay, so the page no
  longer reflows when it opens or closes. Outside-press and Escape close it, and the
  About link is verified present in the top nav.

### Changed

- README.md, USER_GUIDE.md, and CLAUDE.md are excluded from the published site; they
  previously leaked into `_site`.

Both changes are recorded in `bionic/journal/2026-08.md` and ADR-0005
(`bionic/adrs/ADR-0005-serve-a-landing-homepage-and-a-five-item-top-nav.md`).
