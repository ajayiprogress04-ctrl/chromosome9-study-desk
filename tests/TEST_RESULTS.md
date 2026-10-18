# Verification results

Executed 18 October 2026 for version 2.0.0.

| Check | Actual result |
|---|---|
| Build and JavaScript syntax | Passed for app.js, learning.js and core.js |
| Existing core logic | 15 test groups passed |
| Simulated DOM workflows | 30 groups passed, including 8 new learning interaction groups |
| New learning content/state logic | 11 groups passed |
| Static/source/asset checks | 332 passed, zero findings |
| Structured coverage | 145 activities, including every one of 105 glossary terms |
| First application task types | 117 multiple-choice, 18 numeric, 10 open response |
| Follow-up work | Each activity has a distinct rubric-based correction task and transfer task |
| Prior preference preservation | All earlier content retained, with three documented superseding edits |
| Original figure assets | Preserved byte-for-byte |
| Deployment | Not performed |
| Real-browser desktop/mobile layout, native sharing/fullscreen/clipboard | Not performed |

The 145 activities intentionally reuse relevant underlying concepts across learning surfaces. They are not a claim of 145 independently researched findings or unique scientific concepts. First application tasks are followed by a different correction and transfer task. The existing 56 flashcards and 30 bank questions retain their identifiers and behavior.

The tests cover full glossary and learning-surface coverage, complete worked reasoning, objective/source links, missing/placeholder content rejection, correct numeric arithmetic and units, choice feedback, hidden initial practice/feedback, hints, submit/reveal, distinct retry/transfer stages, partial rubric self-assessment, learner-text escaping, draft persistence, optional learning records and older version-1 backup compatibility. Existing flexible visual return, source assets, themes, sharing configuration and question/card persistence continue to pass.

Automatic grading checks choices or numeric results. Written reasoning and transfer responses are self-assessed with explicit rubrics. Only attempt counts and the latest response/outcome are stored, not a full answer transcript. Reveals are assisted study. No validated mastery or clinical-readiness score is claimed.

Declarative JSON Schema validation was not run because the optional jsonschema package is unavailable. The required executable structure, reference and coverage validator runs in the build and browser initialization and passes. Browser visual/mobile behavior remains a manual acceptance item in TESTING_CHECKLIST.md; no alternate browser automation was used.

## Retained earlier verification history

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
