# Testing checklist

## Automated execution

Run `npm test` (Node 18+ and Python 3). No npm install is required.

- core.test.cjs checks schema/link integrity, review date arithmetic, due selection, state persistence, invalid import rejection, search, escaping, sharing URL cleaning, activity interpretation and exact scientific values.
- app-smoke.test.cjs executes app.js in a simulated DOM and checks routes, all lessons/figures/tables, landing controls, lesson top reset, term/diagram return, saved answers through End review, topic-filter question advancement, review scheduling and note escaping.
- verify_project.py checks all source assets, provenance presence, local dependencies, absence of runtime network clients, three-theme contrast pairs, breakpoint/reduced-motion rules and handover files.

See tests/verification-report.json and tests/TEST_RESULTS.md for actual results. Simulated DOM does not prove browser rendering or native API behavior.

## Real-browser checks still required

- [ ] Open local file and recommended localhost address in Chrome/Edge/Firefox/Safari.
- [ ] At 360/390px, tablet width and desktop: check overflow, readable figures, drawer, dropdowns and focus visibility in all three themes.
- [ ] Keyboard-only: skip link, navigation, details, concept nodes, dialog focus trap, Escape and exact return focus.
- [ ] At a long lesson’s middle, open a term, a related term and Previous term; Return restores position.
- [ ] On a zoomed figure with nested scroll, open a glossary explanation and return without changing image/scroll.
- [ ] Choose a topic directly; Next/Previous start at the top.
- [ ] In Practice, answer, End review, reopen; saved response remains. Test topic/type/difficulty/missed filters.
- [ ] Reveal/rate cards; reload; due schedule persists. Change due filter and review all cards.
- [ ] Enter a note/bookmark/checklist item; reload; export; change browser/origin; import.
- [ ] Import invalid JSON and wrong-version JSON; current state remains intact.
- [ ] Restrict storage, deny clipboard/fullscreen and test fallback messages.
- [ ] View all original figures and every oral slide; poster zoom and fit; download original files.
- [ ] Test native Share and explicit Copy link on the actual protected production URL; verify notes are not exported.
- [ ] Verify social previews on intended services rather than guaranteeing icon display.

## Scientific review

- [ ] Confirm six runs/four BioSamples and shared ALL source remain clear.
- [ ] Keep reference features distinct from altered genes.
- [ ] Keep identity separate from extent/depth of coverage.
- [ ] Keep filter P-values separate from group tests.
- [ ] Do not call pooled coding labels hotspots or annotations validated biomarkers.
- [ ] Check heat-map source processing before adding numeric interpretation.
- [ ] Review any newly added external background against authoritative primary sources.

## Version 1.1 manual checks

- [ ] Confirm the darker Light, true-black Dark and deep-plum Colour palettes on the actual display.
- [ ] Choose each objective in Overview and inside a lesson; confirm direct entry and the current objective/lesson indicator.
- [ ] Click underlined terms inside explanations, original manuscript prose, tables and glossary definitions; verify accurate definitions and precise return.
- [ ] Confirm image glossary keys and unchanged figure pixels.
- [ ] Confirm uppercase ALL links correctly and ordinary “all” remains ordinary text.

## Version 1.2 sharing update

Added a 1200 × 630 PNG sharing card with the existing app icon/title; PNG favicon, apple-touch and home-screen icons; static Open Graph/Twitter Card metadata; and a deployment-time real-production-URL configuration script. The Vercel build command now runs content generation and metadata configuration. Existing learning features and storage ids are unchanged. Verify the actual deployed URL and platform previews after deployment; cached or protected pages may not display a card.
