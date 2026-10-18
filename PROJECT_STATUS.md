# Project status

Version 2.1.0 · 18 October 2026

## Complete

- Four source roles confirmed; manuscript and source presentations inspected.
- Reference live HTML/CSS/JS and latest GitHub commit inspected; live/reference biography matched.
- Complete buildless app, source files and local assets included.
- 15 lessons, 105 glossary terms, 56 cards, 30 questions, five comparisons and eight supported concept relationships.
- All original manuscript figure panels and substantive tables; ten oral-slide previews and single-page poster preview.
- Search, three themes, collapsed sidebar, focused lessons, term dialogs, concept map, revision scheduling, question outcomes, private notes/bookmarks, backup import/export, recovery protection, rehearsal checklist/timer, source reconciliation and developer profile.
- Requested Markdown documentation and beginner setup/deployment instructions.

## Verification

Automated results are in tests/TEST_RESULTS.md and tests/verification-report.json. Tests are meaningful logic/static/simulated-DOM checks; actual browser rendering, mobile interaction, native dialogs/fullscreen/share/clipboard and live deployment were not verified. No supported browser-control skill was exposed for managed preview, so no alternate browser path was used.

## Known limits

- No deployment, private hosting access control, Git commit/push or domain setup has been performed.
- File-origin persistence varies by browser; use one stable local-server address and export backups.
- No cross-device sync, AI-generated on-demand answers, clinical decision support or validated readiness score.
- Word reading view is extracted text, not original page layout. PowerPoint previews are images; editable originals are downloadable.
- The developer profile follows the current published reference; recheck it when qualifications change.
- Reference titles on raster figures retain legacy mutation wording; explanations flag the discrepancy.
- The original analysis matrix, exact heat-map conversion/imputation and complete platform-specific pipeline settings are not supplied.
- Literature citations are preserved from the manuscript, not independently audited.
- A new chromosome SVG icon is used because no separate approved logo was supplied. Social preview behavior is platform-dependent.

## Next action

Extract the ZIP and open index.html, preferably through the local-server option in START_HERE.txt. Run the real-browser checklist before deploying. If deploying, use an intended private source repository and appropriate website access protection; repository privacy does not protect a public website.

## Version 1.1 update

Six objective-based sequences, 102 glossary terms, solid inline glossary underlines and substantially deeper Light/Dark/Colour palettes are implemented. Existing 56 flashcards and 30 questions retain ids and saved work. New glossary entries do not silently generate extra flashcards.

## Version 1.2 sharing update

Added a 1200 × 630 PNG sharing card with the existing app icon/title; PNG favicon, apple-touch and home-screen icons; static Open Graph/Twitter Card metadata; and a deployment-time real-production-URL configuration script. The Vercel build command now runs content generation and metadata configuration. Existing learning features and storage ids are unchanged. Verify the actual deployed URL and platform previews after deployment; cached or protected pages may not display a card.

## Version 2.0 learning upgrade

- 145 structured activities cover every glossary entry and all lessons, figures, tables, methodology, comparisons and oral rehearsal.
- Worked scenarios contain information, steps, model answers and principles. Separate practice supports choices, numeric input, optional calculation reasoning and free response.
- In the current guided flow, the current question immediately follows its example. Answers stay hidden before an attempt. Hints, feedback, correction tasks and end-of-objective transfer checks support application.
- Rubrics support transparent accurate, partial or needs-revision self-assessment. No automatic free-text grading is provided.
- New optional learning records preserve attempt counts and latest outcomes through compatible version-1 backups. Existing notes, cards, bank question IDs and visual return behavior remain.
- Preference brief version 14 makes this standard reusable in future educational applications.
- Browser visual/mobile verification and deployment remain unperformed.

## Version 2.1 restructuring

The main objective journey is now a saved step sequence rather than a long lesson with an optional added learning card. Glossary entries are example-first. Full notes, original images/tables, provenance, scientific cautions and downloads remain available as reference. Existing notes, bank/card identifiers, schedules and version-1 backups are preserved.

Dropdown selection now covers workspace sections, grouped objectives, reviewed steps, terms, comparisons, evidence, gallery filters, bank answers, card ratings and self-assessment. Other apps have not been modified; the reusable preference applies when they are available for an upgrade.

## Version 2.2.0 — repeated practical learning

The screenshot-approved example / demonstrated answer / why / remember layout is retained. Every ordinary guided concept and every glossary entry now presents three existing, distinct tasks in sequence: application, correction of a claim, and transfer of reasoning. These follow-ups are part of the normal journey rather than optional buttons. A single answered question cannot enable the main Continue action. Feedback, explicit rubric self-assessment, reviewed-task dropdowns and the selected task are saved locally and included in backups. Previously saved responses remain valid.

All 105 glossary entries have three tasks each (315 existing authored tasks). Objective paths retain their concept steps and two final checks. Task slots by objective are 68, 161, 14, 59, 41 and 17; concepts shared between glossary/objectives reuse the same saved responses, and final checks can revisit transfer prompts. These are practice opportunities, not counts of unique concepts or validated mastery. Return and related-term navigation remain available without forcing completion.

No new scientific findings or external medical advice were added. Written responses remain self-assessed against rubrics. Desktop/mobile visual testing and deployment were not performed.
