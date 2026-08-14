# Changelog

Notable changes to the bionic-coding.com site.

## [Unreleased]

### Fixed

- Mobile nav (≤46rem): the menu card renders as an out-of-flow overlay, so the page no
  longer reflows when it opens or closes. Outside-press and Escape close it, and the
  About link is verified present in the top nav.

### Changed

- README.md, USER_GUIDE.md, and CLAUDE.md are excluded from the published site; they
  previously leaked into `_site`.

Both changes are recorded in `bionic/journal/2026-08.md` and ADR-0005
(`bionic/adrs/ADR-0005-serve-a-landing-homepage-and-a-five-item-top-nav.md`).
