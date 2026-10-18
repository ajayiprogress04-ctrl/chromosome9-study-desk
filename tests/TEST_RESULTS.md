# Verification results

Executed 17 October 2026 in the supplied container.

| Check | Actual result |
|---|---|
| JavaScript syntax | app.js and core.js parse successfully |
| Core logic | 15 test groups passed |
| Simulated DOM workflows | 16 test groups passed |
| Static/source/asset checks | 327 passed, zero findings |
| Three-theme computed contrast | Normal text/action pairs ≥ 4.5:1; focus/control boundaries ≥ 3:1 |
| Original scientific images | All eight image files match DOCX package bytes |
| Local font and preview assets | WOFF signatures, portrait and all oral/poster PNGs verified |
| Deployment | Not performed |
| Real-browser layout, mobile, fullscreen, clipboard, native share | Not performed |

Core groups cover schema links, interval arithmetic, due queues, saved-state roundtrip, invalid import rejection, cross-type search, escaping, clean share addresses, transparent activity indicators and exact reported values.

Simulated interface groups cover main routes, every lesson/figure/table, explicit landing controls, Previous/Next top reset, glossary history and precise lesson/diagram return, answers retained after End review, topic-filter question advancement, persisted review ratings, escaped notes, invalid routes and real import handlers for valid/invalid backups. These use an explicitly limited test double rather than a browser DOM.

Source checks confirm original assets and structured-content consistency. They do not prove the biological validity of the original analysis or audit external papers. No original matrix or executable bioinformatics pipeline was supplied.

The managed environment did not expose the supported browser-control capability; no alternate browser automation or preview server was used. Browser checklist items remain in TESTING_CHECKLIST.md.

## Version 1.1 regression coverage

Verified longest-phrase and inflected glossary links, acronym disambiguation (ALL versus ordinary “all”), idempotence/no nested controls, preservation of attributes/form fields, definition self-link exclusion, complete objective lesson assignment, objective-first landing and sidebar navigation, direct objective-to-first-lesson routing and whole-objective practice/card filters. All six objectives cover exactly the existing 15 lessons. State ids and storage key remain unchanged. The new theme contrast results are in verification-report.json. Real-browser visual/native checks remain outstanding.

## Version 1.2 sharing checks

Verified PNG dimensions and signatures, all icon asset sizes, static image/alt metadata, generated absolute image/canonical URLs, clean production config, invalid protocol/credential rejection, repeated-domain updates without duplicate tags and unchanged body content. The sharing card was inspected as a local rendered image. No live social-platform preview or deployment was tested.

Version 1.3.0: all existing automated checks plus sourced-teaching regression checks pass. 41 background entries and links are present; no real browser or deployment verification.

Version 1.3.1: automated suite passes, including exact title-phrase linking and glossary search. Browser visual and deployment checks remain unperformed.

Version 1.4.0: automated suite passes. Simulated DOM confirms all eight figure image files in their corresponding lessons and gallery, both tables visible in lessons/gallery, and methodology schematic in design/processing. No real browser visual inspection or deployment performed.

Version 1.4.1: automated suite passes, including simulated figure/table return restoring the prior gallery scroll offset while lessons still start at the top. Image dimensions reserve preview space. No real browser or deployment verification.

Version 1.5.0: all automated checks pass, including figure-specific teaching in lesson, gallery and enlarged views, glossary links, methodology arrows and both table guides. Previous gallery-position regression remains passing. No real browser or deployment verification.

Version 1.6.0: automated suite passes, including explicit two-way visual/objective links, all lesson evidence sections, gallery objective groups, direct methodology view and Figure 2 in Objective 3. Browser visual and deployment verification not performed.

Version 1.6.1: automated suite passes. Simulated navigation verifies lesson→figure→Back restores lesson and scroll; gallery→figure→table returns through both prior views; methodology return restores expanded sections. Real browser appearance and deployment remain unverified.
