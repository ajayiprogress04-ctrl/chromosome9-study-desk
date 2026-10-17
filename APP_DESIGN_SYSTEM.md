# Design system

Authority: App_Preferences.md (version 5, 18 October 2026), plus actual inspected reference source. The reference repository’s latest inspected commit was `81ebc624a2ae96248645c6cf7299b6ef90124b63`, “Upgrade 5”, timestamp 2026-10-16T15:07:19Z. The published and repository about.js files matched byte-for-byte during inspection.

## Continuity

- Local Source Sans 3 for interface/body; Cormorant Garamond for restrained headings.
- Ruby/burgundy action colour, navy educational links, bronze module labels, green evidence feedback.
- Three complete token sets: Light, Dark, Colour. All ordinary text/action pairs are computed in verification-report.json; secondary text and control outlines are included.
- Compact flat sections, small rounded controls, subtle linework, expandable long explanations.
- No appendicitis variables, statistics workspaces or report-generation code copied.

## Implemented tokens

| Role | Light | Dark | Colour |
|---|---|---|---|
| Background | #d6c1ad | #000000 | #0c0012 |
| Surface | #efddca | #030207 | #20001c |
| Main text | #100d16 | #fff8f2 | #fff5e8 |
| Secondary text | #352033 | #e0ccd9 | #f2d2e1 |
| Accent text | #590019 | #ffadca | #ffbad3 |
| Action fill | #520018 | #690025 | #650020 |
| Focus | #5a1400 | #ffda85 | #ffe18f |

Source files: styles.css, index.html, app.js. Themes update all app controls through variables. Scientific source images keep their original colours on a neutral viewer background.

## Type, layout and controls

17px base type, responsive 1.9–2.35rem main headings, about 76ch lesson measure. Desktop sidebar 245px, tablet 215px; mobile drawer breakpoint 680px. Main content has no competing right-side panel. Topic selectors are grouped by manuscript-derived module. Main controls target at least 42px height; inline glossary terms use compact underlined text to preserve reading flow.

Previous/Next starts the next lesson at top. Glossary explanation uses a modal over the existing content instead of replacing it, preserving image zoom and nested scroll. Precise return restores focus to the originating term. A mobile shade and Escape close the drawer. Explicit Quick guide/Share app/Copy link sit together on Overview.

## Developer, imagery and branding

Approved published biography and portrait identify Progress Ajayi, physiologist and bioinformatician; first-class Physiology undergraduate qualification; Human Physiology master’s with distinction; PhD Molecular Biology and Genomics in progress. No unrelated identity or qualifications were inferred. The reference-specific dedication is omitted. Local font files and their OFL licence texts are included.

No separate app logo was supplied. A small original chromosome icon was created as a code-native SVG; it is not represented as a supplied logo or institutional mark. Real manuscript images and source previews are preserved without arbitrary numbered hotspots. No anatomy imagery is invented.

## Verification boundary

Computed contrast is a static check, not a complete accessibility certification. Keyboard semantics and responsive breakpoint presence are checked statically/simulated. Actual layout, mobile drawer focus behavior, browser fullscreen/native sharing and cross-platform social preview need real-browser checks. CSS does not guarantee identical rendering across devices.

## Version 1.1 changes

Light now uses deeper warm tan surfaces with dark wine/navy/green text. Dark uses true black and near-black plum surfaces. Colour uses near-black plum and oxblood. Required contrast is checked for each theme. Glossary words use solid underlines throughout rendered prose, definitions, figures, tables and manuscript text. Native controls, headings and answer-choice buttons remain intact; image labels use the linked key below the original figure. Six numbered learning objectives govern the landing dropdown, class navigation and lesson indicators.

## Version 1.2 sharing update

Added a 1200 × 630 PNG sharing card with the existing app icon/title; PNG favicon, apple-touch and home-screen icons; static Open Graph/Twitter Card metadata; and a deployment-time real-production-URL configuration script. The Vercel build command now runs content generation and metadata configuration. Existing learning features and storage ids are unchanged. Verify the actual deployed URL and platform previews after deployment; cached or protected pages may not display a card.
