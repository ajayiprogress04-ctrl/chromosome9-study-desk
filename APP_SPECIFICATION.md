# Application specification

## User and purpose

Progress Ajayi’s personal workspace for learning, revising and defending the supplied chromosome 9 analysis. Architecture is static, browser-local and expandable through structured content. The initial scope is the supplied study, not a general biomedical encyclopedia.

## Source authority and identity

1. Manuscript: scientific claims, study units, exact observations and limits.
2. Oral presentation: presentation sequence and rehearsal emphasis.
3. Poster: concise communication priorities.
4. App_Preferences.md: interface and interaction requirements.

No experimental mechanisms, allele coordinates, effect sizes or clinical performance are invented. An original-data analysis is not reclassified as a review. Sections, table/figure numbers and slide numbers are used because stable manuscript page numbers were not established.

## Implemented modules and acceptance criteria

| Module | Working behavior | Acceptance |
|---|---|---|
| Dashboard | Grouped objective dropdown; guide/share/copy; activity behind disclosure | No compulsory progress bar or cluttered KPI grid |
| Navigator/detail mode | One lesson; summary/WHY; expandable science/evidence | Objective selection opens its first lesson directly; Previous/Next start at top |
| Concept explorer | Linked hierarchy and labelled schematic | All relations have support descriptions; no causal implication |
| Guided path | Six inferred objectives, 15 lessons | Sources and prerequisites follow actual study logic |
| Glossary | 105 searchable names, focused dialog | Previous term and precise return preserve context |
| Recall | 56 cards; reveal; four ratings; due filter | Ratings create real due timestamps and persist |
| Questions | 15 MCQ + 15 short answer; type/topic/difficulty/missed filters | Answers saved; rationale available; short answers explicitly self-assessed |
| Comparisons | Five focused source-linked tables | Distinctions preserve measurement units |
| Visuals | Seven figures/eight panels, two tables | Original images intact; cautions next to evidence |
| Oral preparation | Ten slide previews, explanations, questions, checklist/timer | No fabricated claims; End review preserves answers |
| Critical appraisal | Strengths, limitations, discrepancies and matrix | No unsupported numerical quality score |
| Notes/search | Global search, bookmarks, notes, backup/import | Escaped user content; no network transfer |
| Original sources | Text manuscript view, slide/poster viewer, downloads | DOCX text transcription is not misrepresented as layout rendering |

## Journeys

- Overview → topic dropdown → concise lesson → optional detail → term dialog → Return to lesson at same position.
- Figure library → original image → explanation term → Return to diagram with the image/zoom/scroll intact.
- Flashcards → recall aloud → reveal → grade → saved next due date → End review → overview.
- Questions → answer/compare → saved response → End review → overview, with work retained.
- Source viewer → select slide/section → zoom/fit/download; return through explicit navigation.
- Notes → export backup → same app on another origin → validate/import backup.

## Non-functional requirements

Vanilla HTML/CSS/JS; minimal dependencies (none at runtime); local fonts/assets; no credentials; static hash routing; readable responsive CSS; keyboard controls and visible focus; reduced-motion support; no analytics. State version 1 is validated before import, and unreadable stored state is preserved for recovery. Native sharing/fullscreen/clipboard have fallbacks. The developer profile is copied from the inspected reference; appendicitis-specific dedication and clinical workflows are excluded.

## Deliberate adaptations

The master request’s dashboard-progress requirement is implemented in an optional activity disclosure to respect the newer preference against a landing progress bar. Main lessons show source details on demand. No right-side progress/bookmark panel or six-button toolbar is added. Scientific diagrams describe the analysis process, not a newly invented biological pathway. There is no hosted AI explanation service; explanations are authored source-linked content.

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
