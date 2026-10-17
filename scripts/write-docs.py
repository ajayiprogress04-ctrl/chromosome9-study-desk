from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1];D=json.loads((R/'content/research.json').read_text())
def write(name,s):(R/name).write_text(s.strip()+'\n')
write('README.md','''# Chromosome 9 Study Desk

A personal learning workspace for **Chromosome 9 Variant Annotation Profiles Across Public Acute Leukemia Sequencing Datasets**. Subtitle: **Understand the evidence. Explain the study.**

The name identifies the chromosome focus and the personal study purpose. It is a descriptive project name; trademark or product-name uniqueness is not claimed. Repository identifier: `chromosome9-study-desk`.

## Start using it

1. Extract the complete ZIP into one folder.
2. Open `index.html` in a modern browser. The pre-generated content script and local assets are included; there are no CDNs or paid services.
3. Choose a topic or open Quick guide. No login or API key is needed.

For a consistent local address, open a terminal in the extracted folder and run `python3 -m http.server 8000` (Windows: `py -m http.server 8000`). Open `http://localhost:8000`. Browser-local storage on file URLs is browser-dependent; the local-server option is recommended for repeat use. The content does not use `fetch`, so local-file loading does not depend on JSON CORS access.

## Included learning tools

- 15 source-linked lessons, grouped into foundations, methods, results, and appraisal/defence.
- Concise WHY explanations, expandable details, misconceptions and evidence.
- 41 glossary entries with related terms and context-preserving return.
- 56 flashcards with transparent, implemented interval scheduling.
- 30 questions: 15 multiple-choice and 15 self-assessed short answers.
- Five comparison tables, an explanatory concept map, all seven manuscript figures (eight image panels), both substantive source tables, all ten oral-slide previews and the poster preview.
- Slide rehearsal guides, inferred audience questions, checklist and session timer.
- Manuscript text reading view, source reconciliation, search, bookmarks and private notes.
- Light, Dark and Colour themes; remembered desktop sidebar; mobile drawer styles.

The manuscript is a secondary descriptive sequencing-data analysis, **not a review article**. Slides and poster are companion summaries. Lessons do not establish leukemia-specific variants or biomarkers.

## What persists

Read markers, notes, bookmarks, flashcard ratings/due dates, question answers, appearance preferences and rehearsal checklist use `localStorage`, under `c9-study-desk-v1`. Refreshing the same origin normally preserves them. A new browser, device, URL or cleared site storage does not. Storage restrictions can leave changes only in memory; the app reports this. Export/import a JSON backup in Bookmarks and private notes. An invalid saved state is preserved for recovery export instead of silently overwritten.

Review position and timer are session-only. Question correctness for short answers is your self-assessment. Activity indicators are not a validated mastery score. Scheduling rules are in `LEARNING_ARCHITECTURE.md`.

## Edit or maintain

No package install is needed. With Node 18+ and Python 3 available:

```sh
npm run build
npm test
```

Edit science in `content/research.json`, then rebuild `content/content.js`. `content/source-extract.json` contains manuscript paragraphs, the two substantive tables and extracted slide/poster text. `scripts/seed-content.py` is the initial authored seed; it overwrites research.json when explicitly run, so do not run it over later editorial updates. The normal build does not run the seed. `core.js` contains reusable validation/storage/review/search logic. `app.js` contains the interface. All scientific images are local.

## GitHub and Vercel

This deliverable has **not** been committed, pushed or deployed. It includes manuscript and presentation source files. Use a **private GitHub repository by default**; do not publish confidential research or personal learning backups.

1. Create your intended private GitHub repository.
2. Upload the **extracted folder contents**, with index.html at the repository root. Do not upload the ZIP as the application.
3. In Vercel, import that repository, choose Other, leave the build command empty, and set the output directory to `.`. The included vercel.json describes static hosting.
4. Configure appropriate access protection before relying on the site as private. A private GitHub repository alone does **not** make its deployed website private. Review hosting access controls and the included research material before deployment.
5. Open the returned real address. Optionally put your actual clean production URL in config.js. No domain is reserved or configured by this project.
6. Export a progress backup before changing origin, then import it on the new address.

There is no backend or authentication in this ZIP. Sharing copies an address, not notes. No analytics or external scientific API is called. Developer contact links open external services only when clicked.

## Verification limits

The handover includes automated core tests, simulated-DOM workflow checks, asset checks and computed contrast checks. It does not claim a real-browser visual, responsive, fullscreen, native-share or clipboard-permission audit. The environment did not expose the supported browser QA capability, so no preview server or alternate browser automation was used. Check those items before relying on a deployed version. Original DOCX layout is not rendered by the app; the reading view is extracted text. Slides and poster use image previews and downloadable editable originals.

See TESTING_CHECKLIST.md and tests/verification-report.json. Font licences are in assets. Biography and portrait follow the published reference Hub, not unrelated account memory.
''')
write('APP_SPECIFICATION.md','''# Application specification

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
| Dashboard | Topic dropdown; guide/share/copy; activity behind disclosure | No compulsory progress bar or cluttered KPI grid |
| Navigator/detail mode | One lesson; summary/WHY; expandable science/evidence | Topic selection opens directly; Previous/Next start at top |
| Concept explorer | Linked hierarchy and labelled schematic | All relations have support descriptions; no causal implication |
| Guided path | Four inferred modules, 15 lessons | Sources and prerequisites follow actual study logic |
| Glossary | 41 searchable names, focused dialog | Previous term and precise return preserve context |
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
''')
write('APP_DESIGN_SYSTEM.md','''# Design system

Authority: App_Preferences.md (version 3, 17 October 2026), plus actual inspected reference source. The reference repository’s latest inspected commit was `81ebc624a2ae96248645c6cf7299b6ef90124b63`, “Upgrade 5”, timestamp 2026-10-16T15:07:19Z. The published and repository about.js files matched byte-for-byte during inspection.

## Continuity

- Local Source Sans 3 for interface/body; Cormorant Garamond for restrained headings.
- Ruby/burgundy action colour, navy educational links, bronze module labels, green evidence feedback.
- Three complete token sets: Light, Dark, Colour. All ordinary text/action pairs are computed in verification-report.json; secondary text and control outlines are included.
- Compact flat sections, small rounded controls, subtle linework, expandable long explanations.
- No appendicitis variables, statistics workspaces or report-generation code copied.

## Implemented tokens

| Role | Light | Dark | Colour |
|---|---|---|---|
| Background | #f6f3ee | #030405 | #200d20 |
| Surface | #fffdf9 | #0c0f13 | #35152d |
| Main text | #172535 | #faf8f5 | #fff7ec |
| Secondary text | #4a5663 | #c2ccd6 | #edcfdc |
| Accent text | #800c31 | #ff9eb8 | #ffc0d3 |
| Action fill | #800c31 | #94113b | #841035 |
| Focus | #8e3c00 | #ffdb7d | #ffe094 |

Source files: styles.css, index.html, app.js. Themes update all app controls through variables. Scientific source images keep their original colours on a neutral viewer background.

## Type, layout and controls

17px base type, responsive 1.9–2.35rem main headings, about 76ch lesson measure. Desktop sidebar 245px, tablet 215px; mobile drawer breakpoint 680px. Main content has no competing right-side panel. Topic selectors are grouped by manuscript-derived module. Main controls target at least 42px height; inline glossary terms use compact underlined text to preserve reading flow.

Previous/Next starts the next lesson at top. Glossary explanation uses a modal over the existing content instead of replacing it, preserving image zoom and nested scroll. Precise return restores focus to the originating term. A mobile shade and Escape close the drawer. Explicit Quick guide/Share app/Copy link sit together on Overview.

## Developer, imagery and branding

Approved published biography and portrait identify Progress Ajayi, physiologist and bioinformatician; first-class Physiology undergraduate qualification; Human Physiology master’s with distinction; PhD Molecular Biology and Genomics in progress. No unrelated identity or qualifications were inferred. The reference-specific dedication is omitted. Local font files and their OFL licence texts are included.

No separate app logo was supplied. A small original chromosome icon was created as a code-native SVG; it is not represented as a supplied logo or institutional mark. Real manuscript images and source previews are preserved without arbitrary numbered hotspots. No anatomy imagery is invented.

## Verification boundary

Computed contrast is a static check, not a complete accessibility certification. Keyboard semantics and responsive breakpoint presence are checked statically/simulated. Actual layout, mobile drawer focus behavior, browser fullscreen/native sharing and cross-platform social preview need real-browser checks. CSS does not guarantee identical rendering across devices.
''')
write('LEARNING_ARCHITECTURE.md','''# Learning architecture

## Pathway

Four modules follow the actual analysis:

1. Foundations: chromosome rationale, study design, biological provenance.
2. Methods: processing, identity/coverage, calling/filter thresholds, annotation units.
3. Results: counts, coding summaries, pooled positions, overlap, clustering, heat map.
4. Appraisal and defence: limitations and a defensible synthesis.

These learning objectives are inferred from manuscript sections, not claimed as original objectives verbatim. Each topic has a short summary, WHY explanation, detail, evidence, misconception, example, terms, related lessons and provenance. More detail is hidden by default. Educational analogies do not add results.

## Concept relationships

The graph connects biological provenance to observation, observation to annotation-set recovery, record definitions to counts, coding context to position interpretation, and limitations to conclusions. Each edge states its meaning and labels explicit manuscript discussion versus educational synthesis. No causal biological network is inferred from these descriptive data.

## Active recall and scheduling

56 cards cover topic synthesis and terminology. Recall before revealing; rate Again, Hard, Good or Easy. The algorithm in core.js stores {grade, level, due, last}:

- Again: 10 minutes, level reset to 0.
- Hard: 1 day, non-Again level increments.
- Good: 3 × 2^(level−1) days after increment.
- Easy: 7 × 2^(level−1) days after increment.
- Levels cap at 10 and every interval caps at 365 days.

No validation or mastery guarantee is claimed. Due timestamps depend on the device clock. New or due only is a filter; all cards remain available. User ratings are self-reported. Activity indicators are descriptive counts of read markers and question outcomes, not a validated score.

## Question bank

30 source-supported questions: 15 MCQs and 15 short answers. Fields include topic, difficulty, type, objective, source, answer, explanation and support classification. MCQ distractors represent real interpretation errors, and rationales distinguish them from the best answer. Short answers are compared to model explanations and explicitly self-assessed; there is no language-model or keyword grading. Missed questions remain available for revision. Reattempt is deliberate, and End review does not clear answers.

## Oral explanation

Each of the ten oral slides has a key message, authored explanation guide and inferred follow-up question/model answer. These are newly authored teaching aids, not recovered speaker notes. A session timer and persisted rehearsal checklist support practice without claiming a validated readiness assessment.

## Boundaries and gaps

No clinical diagnosis, mechanistic leukemia simulation, patient prevalence estimate or independent bibliographic audit is provided. The study’s reference-feature counts, predicted effects and pooled coding labels are distinguished from altered genes, validated consequences and genomic hotspots. Missing processing details and the heat-map transformation remain open questions rather than guessed implementations.
''')
rows=['| Topic / module | Principal learning point | Manuscript | Oral | Poster | Reconciliation |','|---|---|---|---|---|---|']
for t in D['topics']:
 rows.append('| '+' | '.join([t['title']+' / '+t['group'],t['summary'],t['source'],', '.join(map(str,t['slides'])),t['poster'],'Manuscript controls scientific detail; companions are compressed.'])+' |')
write('SOURCE_CONTENT_MAP.md','''# Source reconciliation and content map

## Supplied/available sources

| File in project | Purpose |
|---|---|
| sources/Manuscript.docx | Primary complete scientific manuscript (uploaded Manuscript(2), byte-identical to Manuscript(1)) |
| sources/Oral_Presentation.pptx | Completed ten-slide ORA presentation |
| sources/Poster.pptx | Completed single-page FASCON poster |
| App_Preferences.md | Interface/development authority |

Manuscript paragraphs, both substantive tables and extracted oral/poster text are retained in content/source-extract.json. The third DOCX table is a figure-layout container with A/B labels, not a third scientific data table; its two actual Figure 5 images are preserved. Section/table/figure provenance is used rather than invented page numbers.

## Reconciliation matrix

'''+ '\n'.join(rows)+'''

## Discrepancies requiring attention

- The build request describes a review manuscript. The actual study is a secondary descriptive analysis of public sequencing runs.
- Legacy raster titles use “mutation burden”, “mutations” and “mutation profiles”. The revised manuscript defines the counted material as annotation records, not validated distinct somatic mutations. Original pixels are retained, and explanations flag the terminology.
- The heat-map workflow mentions unit-variance scaling and imputation, while its caption describes a 0–1 colour scale. The exact conversion and imputation rule need the original code/matrix. No values are reconstructed by reading pixels.
- Presentation compression omits settings, many gene/position labels, and references. This is an omission, not permission to change the manuscript results.
- No email or assigned slot was supplied. None is fabricated.

## Figure map

| Figure | Local image | Source |
|---|---|---|
| 1 counts | image1.png | §3.2.2 |
| 2 selected genes | image2.png | §3.2.2 |
| 3 protein effects | image3.png | §3.2.3 |
| 4 amino-acid categories | image4.png | §3.2.4 |
| 5 A/B overlap | image5.png / image6.png | §3.2.5 |
| 6 dendrogram | image7.png | §3.2.6 |
| 7 heat map | image8.png | §3.2.6 |

All figures are unchanged manuscript assets. Explanatory tables and the concept map are newly authored learning tools. Speaker guides/questions are inferred teaching material, not recovered original speaker notes.
''')
write('CONTENT_SCHEMA.md','''# Content schema

Primary content: content/research.json. Browser bundle: content/content.js, generated by scripts/build-content.cjs. Original extraction: content/source-extract.json. No interface logic is embedded in scientific content.

IDs are stable and unique **within their collection**; a glossary term and a lesson may intentionally share an id, and the route/kind scopes it.

| Collection | Required learning fields |
|---|---|
| topics | id, title, group, summary, why, detail, evidence, misconception, example, terms[], related[], source, slides[], poster, steps[], support |
| terms | id, term, full, plain, why, mechanism, remember, origin, source, related[], topic, support |
| flashcards | id, topic, front, back, source |
| questions | id, topic, type, difficulty, objective, prompt, answer, explanation, source, support; MCQ additionally options[], correct index |
| comparisons | id, title, headers[], rows[][], source |
| figures | id, title, files[], meaning, caution, source, topic |
| slides | id, number, title, image, message, guide, topic, source, question, answer, questionKind |
| relationships | [from-topic, to-topic, meaning, support-classification] |
| discrepancies | title, detail, source |

Support classes distinguish faithful paraphrases, explanatory interpretations, inferred questions and unresolved source issues. Neither an analogy nor an unanswered question is a new scientific finding. Glossary definitions are educational explanations in source context, not falsely quoted definitions. Historical naming is left unspecified when not supplied.

## Persistent state version 1

`{version, theme, sidebar, read[], bookmarks[], notes{}, ratings{}, answers{}, recent[], rehearsal{}, lastTopic}`.

- notes maps topic/draft ids to strings.
- ratings maps card ids to {grade, level, due, last}; due/last use epoch milliseconds.
- answers maps question ids to {response, correct, at, selfAssessed?}.
- read/recent/bookmarks contain topic ids; rehearsal maps checklist indices to booleans.
- theme is light/dark/colour; sidebar is a desktop-collapse boolean.

core.js validates imported state and scientific links. Maximum backup upload size is 3 MB. Notes and responses are length-limited by import validation and escaped on output. No submitted text is evaluated as HTML or code. Unknown state versions are rejected. Unreadable on-device state is preserved for raw recovery export; an intentional valid import replaces it.

Schema checks validate structure/references, not scientific truth. Scientific content still requires comparison against supplied documents. A draft JSON Schema is also supplied in content/schema.json for tooling; the executable checks are in core.js and scripts/verify_project.py.
''')
write('BUILD_PLAN.md','''# Build plan and maintenance milestones

| Stage | Result | State |
|---|---|---|
| Intake | All four source roles confirmed | Complete |
| Inspection | Manuscript, oral/poster text, all figures; live reference code/theme/profile/latest commit | Complete |
| Reconciliation | Study type, units, legacy figure wording, heat-map uncertainty | Complete |
| Learning design | 15 topics; 41 terms; 56 cards; 30 questions; evidence map | Complete |
| Implementation | Static source code, themes, lessons, recall, questions, viewers, notes, source tracking | Complete |
| Checks | Core logic, simulated DOM, static asset/source/contrast checks | Run and recorded in tests |
| Real-browser QA | Desktop/mobile, keyboard, fullscreen/share/clipboard, actual file-origin storage | Outstanding |
| Deployment | Private repo/access-protected hosting as appropriate | Not performed |

## Updating science

1. Retain the exact new source version before editing.
2. Compare changes against the current source map.
3. Update research.json and any affected figure/slide assets; document unresolved differences.
4. Run the normal content build; do not rerun the initial seed over manual editorial changes.
5. Run automated checks, then relevant browser checks.
6. Preserve local-state compatibility or provide an explicit migration. Do not silently reset notes.
7. Regenerate a complete ZIP rather than a patch.

## Future scope

A second study can be added by extending the content schema and navigation, with an explicit per-study state namespace. Cross-device synchronization or authentication would require a deliberately selected backend; neither is needed or claimed for this version. Do not add paid AI services or public publication as an assumed maintenance step.
''')
write('TESTING_CHECKLIST.md','''# Testing checklist

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
''')
write('AI_BUILD_PROMPT.md','''# AI-assisted maintenance prompt

Work on the extracted Chromosome 9 Study Desk project, preserving its working features. Read README.md, App_Preferences.md, APP_SPECIFICATION.md, APP_DESIGN_SYSTEM.md, LEARNING_ARCHITECTURE.md, SOURCE_CONTENT_MAP.md and PROJECT_STATUS.md before changes.

This is a personal app for Progress Ajayi’s manuscript “Chromosome 9 Variant Annotation Profiles Across Public Acute Leukemia Sequencing Datasets”. The actual design is a secondary descriptive analysis of six public sequencing runs across four BioSamples; the three ALL runs share REH SAMN13831871. Do not call it a review or a clinical cohort. Manuscript.docx is the scientific authority; Oral_Presentation.pptx guides rehearsal, Poster.pptx guides concise communication, and App_Preferences.md governs design.

Inspect actual code and latest reference when relevant: https://appendicitis-learning-hub.vercel.app/ and https://github.com/ajayiprogress04-ctrl/appendicitis-learning-hub. Never modify that reference project. Use the actual published developer biography/portrait rather than unrelated account memory. Retain local Source Sans 3, Cormorant Garamond, ruby/navy/bronze/green accents, rich contrast in Light/Dark/Colour, collapsible desktop sidebar/mobile drawer, grouped topic dropdowns, one lesson at a time, concise WHY explanations and expandable detail.

Do not add a landing progress bar, flat objectives button row, extra lesson-card index, right-side progress/bookmark panel or six-button lesson toolbar. Preserve Quick guide, Share app and explicit Copy link together. Preserve Previous/Next top reset, term-history navigation, precise glossary/diagram return and End review without clearing work.

Keep science in content/research.json; rebuild content/content.js with scripts/build-content.cjs. source-extract.json retains original paragraphs and source summaries. Preserve all seven figures/eight panels, the two substantive tables, ten oral previews and poster preview. Do not change original evidence pixels to make the results more impressive. No allele coordinates, p-values, CIs, causal mechanisms or biomarker claims may be invented. Record discrepancy/uncertainty instead of merging versions silently. Calling P-values are not group-comparison tests; 0.8% coverage is not 91.4% identity; annotation records are not automatically independent somatic variants.

Use vanilla HTML/CSS/JavaScript and static hosting unless the requested feature genuinely requires more. Core behavior must not depend on a paid API or a backend. Preserve localStorage version 1, notes, ratings and answers through compatible updates. Escape user text and validate backups. Simple scheduling is a transparent heuristic, not a validated mastery algorithm. Short answers are self-assessed. No public deployment or commit of private research is authorized by this maintenance prompt.

Implement the requested change in source code, update documentation, run npm test and relevant real-browser checks when supported. Distinguish static/simulated tests from actual browser evidence. Do not claim publishing, pushing or visual verification without evidence. Update App_Preferences.md only for new reusable user corrections, keeping app-specific choices separate. Deliver one complete updated project ZIP, setup instructions, concrete test results and remaining limits.
''')
write('PROJECT_STATUS.md','''# Project status

Version 1.0.0 · 17 October 2026

## Complete

- Four source roles confirmed; manuscript and source presentations inspected.
- Reference live HTML/CSS/JS and latest GitHub commit inspected; live/reference biography matched.
- Complete buildless app, source files and local assets included.
- 15 lessons, 41 glossary terms, 56 cards, 30 questions, five comparisons and eight supported concept relationships.
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
''')
write('CHANGELOG.md','''# Change notes

## 1.0.0

Created the complete local learning project from the supplied manuscript, oral presentation, poster and App_Preferences.md. Added structured science and a compact three-theme interface in the reference design family. No reference-app files or source presentations were modified. No network service is needed for the core app. Static and simulated-DOM tests are included, with remaining browser checks stated explicitly.

Significant files: index.html; styles.css; app.js; core.js; content/research.json; content/source-extract.json; content/content.js; assets/; sources/; tests/; scripts/.
''')
write('docs/REFERENCE_INSPECTION.md','''# Reference inspection record

Inspected 17 October 2026. Sources:

- https://appendicitis-learning-hub.vercel.app/
- https://github.com/ajayiprogress04-ctrl/appendicitis-learning-hub
- Latest inspected commit: 81ebc624a2ae96248645c6cf7299b6ef90124b63 (Upgrade 5, 2026-10-16T15:07:19Z).

Actual files inspected: index.html, styles.css, colored-mode.css, about.js/about.css, sidebar.js, navigation-history.js, public-sharing.js, package.json, vercel.json. The published about.js and repository about.js matched. Source Sans 3, Cormorant Garamond, ruby/navy/bronze/green tokens, dark-theme rules, compact navigation and sharing patterns informed this separate app. Clinical variables/statistical workflows were not imported. The source reference project was not changed.

Progress Ajayi’s published portrait and approved profile wording were reused as requested. Original reference-specific dedication was not repurposed. Source font binaries are local; their Google Fonts upstream OFL licence copies are included. Local chromosome icon is new, not copied institutional branding. Scientific assets are extracted unchanged from the user-supplied manuscript; oral/poster previews come from the generated, inspected companion files.

This is code/content inspection, not a browser visual audit or a claim that every live interaction was exercised. It does not establish any external product-name/domain uniqueness.
''')
write('ASSET_CREDITS.md','''# Asset credits and scope

- Manuscript, scientific figures, oral presentation and poster: supplied user research materials and companion outputs, bundled for the requested personal learning purpose. This bundle grants no new public redistribution right.
- Progress Ajayi portrait and biography: published reference Hub, retrieved 17 October 2026, reused following the user’s explicit app-preference instruction. Contact links are taken from that profile.
- Source Sans 3 / Cormorant Garamond font binaries: reference Hub local font assets. Upstream SIL Open Font License texts are included as assets/sourcesans3-OFL.txt and assets/cormorantgaramond-OFL.txt.
- Chromosome app icon: new code-native SVG created for this project, not an institutional or FASCON logo.
- The app is a separate original implementation informed by the reference’s specified design patterns; no wholesale clinical/statistical reference code was bundled.

Review privacy and rights before any public deployment. The delivered app has not been published.
''')
# Tool-friendly light schema; actual cross-link validation is executable in core.js.
schema={'$schema':'https://json-schema.org/draft/2020-12/schema','title':'Chromosome 9 learning content','type':'object','required':['version','name','topics','terms','flashcards','questions','figures','slides','relationships'],'properties':{'version':{'const':1},'name':{'type':'string'}}}
for field in ['topics','terms','flashcards','questions','figures','slides']:
 schema['properties'][field]={'type':'array','minItems':1,'items':{'type':'object','required':['id','source'],'properties':{'id':{'type':'string','minLength':1},'source':{'type':'string','minLength':1}}}}
schema['properties']['relationships']={'type':'array','items':{'type':'array','minItems':4,'maxItems':4,'items':{'type':'string'}}}
(R/'content/schema.json').write_text(json.dumps(schema,indent=2))
print('Wrote complete project handover documentation.')
