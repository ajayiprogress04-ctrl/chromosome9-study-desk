# Learning-system implementation

## Audit

The existing vanilla JavaScript app has 6 learning objectives, 15 lessons, 105 glossary terms, 7 figures (8 images), 2 source tables, 56 flashcards, 30 bank questions, 5 comparisons and 10 oral-rehearsal slides. Content is local JSON compiled to a browser script. Progress uses version-1 localStorage and JSON backups. Existing examples are mostly short illustrations; practice is largely separate. Free-response language grading is not implemented.

## Implementation plan

1. Preserve the preference brief and add the permanent objective–demonstration–practice–feedback standard.
2. Add a structured, source-linked learning activity for every glossary entry and relevant learning surface.
3. Implement progressive worked demonstrations, gated questions, hints, submission/reveal, explanatory feedback, rubric self-assessment and transfer practice.
4. Add compatible local progress fields, validation, coverage and interaction tests. Preserve existing navigation, themes and saved state.

## Verification boundary

Automated logic and simulated-DOM checks are separate from browser visual/mobile checks. No AI grading, cross-device sync, real clinical assessment or validated mastery claim is provided.

## Implemented

- `content/learning.json`: 145 source-linked activities, covering 105 glossary entries, 15 lessons, 7 figures, 3 other visual activities, 5 comparisons and 10 rehearsal slides. Lesson activities intentionally reuse relevant underlying concepts rather than invent unrelated new facts.
- `learning.js`: reusable progressive worked example, independent choice/number/free response, hint, feedback, rubric, further practice and transfer controls.
- `core.js`: complete coverage/content validation, numeric and choice grading, optional compatible attempt records and separate activity summaries.
- `app.js`: integration across existing views, private draft capture, context-preserving practice refresh and current guide updates.
- Tests cover missing/placeholder content, objective links, answer gating, arithmetic, feedback, partial self-assessment, escaping, old backups, persistence, prior visual navigation and original assets.

## Remaining limits

No glossary entry is missing a worked example or practice opportunity under the structural coverage audit. The app does not provide AI free-text grading, drag ordering, diagram-label scoring or unlimited generated new questions. Each activity supplies a first application, a separate correction task and a transfer task. Original manuscript gaps (raw matrix, complete heat-map preprocessing and allele-level validation) remain unresolved and explicit. No new study result or patient history is invented.

Automatic scoring covers choices and numeric results. Written explanations and transfer checks use a learner-completed rubric; a numeric result alone does not validate reasoning. The interface records counts and latest outcomes, not a full transcript of every previous answer. Real-browser desktop/mobile, native sharing and deployment checks remain pending.

## Version 2.1: restructure rather than add more content

- Six guided paths render one example and immediate question at a time, with response-gated Continue, reviewed-step selection, a saved cursor and two final transfer checks.
- Glossary terms show the scenario before optional definitions. Duplicate visible explanations are reduced; full scientific reference remains accessible.
- Comparisons, revision and rehearsal use focused example-first views. The question bank demonstrates a related scenario, then presents its existing question with dropdown submission.
- Native dropdowns replace remaining unnecessary selection rows and long option lists. Direct actions remain buttons.
- Simulated tests traverse every path, exercise final check/self-assessment handling, test blocked future-step selection, answer-gating, saved return position and actual dropdown handlers.
- Actual browser rendering/mobile behavior and deployment remain unverified. No other app has been changed by this package.

## Version 2.2.0 — repeated practical learning

The screenshot-approved example / demonstrated answer / why / remember layout is retained. Every ordinary guided concept and every glossary entry now presents three existing, distinct tasks in sequence: application, correction of a claim, and transfer of reasoning. These follow-ups are part of the normal journey rather than optional buttons. A single answered question cannot enable the main Continue action. Feedback, explicit rubric self-assessment, reviewed-task dropdowns and the selected task are saved locally and included in backups. Previously saved responses remain valid.

All 105 glossary entries have three tasks each (315 existing authored tasks). Objective paths retain their concept steps and two final checks. Task slots by objective are 68, 161, 14, 59, 41 and 17; concepts shared between glossary/objectives reuse the same saved responses, and final checks can revisit transfer prompts. These are practice opportunities, not counts of unique concepts or validated mastery. Return and related-term navigation remain available without forcing completion.

No new scientific findings or external medical advice were added. Written responses remain self-assessed against rubrics. Desktop/mobile visual testing and deployment were not performed.

## Version 2.3.0 — simpler app built around examples

The start page immediately shows the saved objective concept and its example/practice sequence. Five primary dropdown destinations replace the large main menu: Start, Objectives, Worked Examples, Glossary and Figures/Tables. Supporting tools remain under More practice and reference; documents, long notes and source-gallery previews remain available in collapsed reference sections.

Thirty authored hypothetical worked cases (two per topic) add 90 tasks. There are now 175 worked-example units and 525 authored practice tasks. The Worked Examples library filters by objective, saves its selected example and filter, and requires the three-task sequence before sequential Next. Each glossary entry can switch between its own term example and two clearly labelled related topic cases. All other instructional components use the same three-task sequence. The original question bank remains a separate source-linked practice bank with demonstrated examples.

New cases cover scope, causal overclaims, biological provenance, sequence processing, identity/coverage, calling filters, annotation units, summary statistics, predicted coding consequences, coordinate context, set overlap, clustering, heat-map scaling and conclusions. All new numbers and invented labels are hypothetical, not new study findings. Existing figures, tables, source files, themes, sharing and backups are retained.

Old objective cursors at final checks enter the new cases before the final checks; previous answers, notes and completed-step identifiers are preserved. Returning from the glossary refreshes any shared activity’s phase while restoring the previous view and scroll.

Objective task slots (including repeated final checks) are: {'o1': 86, 'o2': 185, 'o3': 20, 'o4': 71, 'o5': 59, 'o6': 29}. These slots reuse saved concepts across views and are not a count of unique findings or validated mastery. Free responses remain explicitly self-assessed. No deployment or real-browser desktop/mobile visual verification was performed.

## Version 2.4.0 — simple dropdown practice replaces compulsory assessment

This is the current interaction standard and supersedes the earlier three-task gate. The practice component now contains only the worked example, demonstrated answer, why, memory reminder, one dropdown question and brief feedback. Another question offers more practice; one response is enough to continue to the next example. The progress/review panel, worked-reasoning disclosure, written peer-review response, model/rubric comparison, rubric checkboxes, self-assessment controls and confusion/source disclosure within the card are removed.

All 175 worked units have three live dropdown questions (525 question slots). These include application, reasoning and recognising a mistaken claim, built from the existing source-linked teaching content. They are not 525 unique scientific findings, and many concepts are reused across app areas. Hypothetical cases remain labelled. The old rich practice/retry/mastery fields remain only as legacy content and source context; they are not the live interaction. The `simplePractice` array defines current choice questions. Live responses use unit:choice:phase keys and selected phases use choice-phase-unit notes, so old private written responses remain intact and cannot incorrectly count as new choice attempts.

The former question-bank and flashcard routes open the unified example library. Supporting sources, diagrams, glossary definitions and private notes remain available. Five primary destinations and flexible return are retained. Definitions are optional reference, while practical examples carry the learning experience.

Verification includes all 525 dropdown questions, all 105 glossary entries and every guided objective step, short feedback, empty-choice handling, assisted repeats, saved task/selection, glossary return, retained legacy answers and backup import. Old rubric and mandatory-three-stage assertions were replaced because those interactions were explicitly removed. No deployment or real-browser desktop/mobile layout test was performed.
