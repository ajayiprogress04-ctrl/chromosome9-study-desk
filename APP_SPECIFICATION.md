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
| Guided path | Four inferred modules, 15 lessons | Sources and prerequisites follow actual study logic |
| Glossary | 102 searchable names, focused dialog | Previous term and precise return preserve context |
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
