# Learning architecture

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

## Objective, demonstration, practice and feedback

`learning.js` provides one reusable progressive component. The outcome identifies the parent objective. The worked example explains a concrete scenario with its answer and reasoning. The corresponding “Your turn” question appears immediately after the example. Hints provide guidance; submission opens explanatory feedback, and a separate correction or transfer task provides further practice.

Numeric inputs support direct numbers and percentages under the question's stated unit convention. Arithmetic grading checks the result only; optional written calculations remain learner-reviewed. Multiple-choice grading returns feedback tied to the chosen misconception. Open-ended work has a model and checklist rubric. Accurate/partial/needs-revision labels are explicitly self-assessments, not AI language grades.

The glossary, lessons, source visuals, comparisons and oral rehearsal use the same component. Revision cards use the example/application flow first, with recall wording retained as optional reference; bank questions have a concise matching demonstration before their own question. Existing read markers retain their meaning as reading activity. New attempt records do not imply validated mastery.

## Guided objective cursor and reference separation (2.1)

`research.json.guidedPaths` contains six paths (24, 55, 6, 21, 15 and 7 steps, including two final transfer checks per objective). Repeated lesson/term demonstrations are deduplicated within a path where they teach the same immediate application. Only one step is rendered. A submitted response plus feedback enables Continue; written responses additionally require rubric self-assessment. A reviewed step records process completion, not independently established mastery.

`state.guided[objectiveId]` stores `{index, completed[]}` using the existing version-1 backup. Future step labels are absent from the revisit dropdown until reviewed. Selecting an objective resumes its cursor. Lesson routes open the relevant point in its path; full notes use separate `reference/<topic>` routes. Flexible visual Back restores the guided route, cursor, open sections and scroll.

The glossary begins with an example and question. Definitions and mechanisms support it inside optional reference details. Main comparison/revision/rehearsal surfaces show one concept at a time. Gallery and source views remain reference indexes. Selection groups use native dropdowns; rubric points remain independent checkboxes.

A correct repeated submission after earlier feedback is labelled `assisted-correct` and excluded from the independently scored-correct count. It remains a recorded practice outcome. Hints guide before submission; unattempted application answers cannot be revealed through the component's controls.

## Version 2.2.0 — repeated practical learning

The screenshot-approved example / demonstrated answer / why / remember layout is retained. Every ordinary guided concept and every glossary entry now presents three existing, distinct tasks in sequence: application, correction of a claim, and transfer of reasoning. These follow-ups are part of the normal journey rather than optional buttons. A single answered question cannot enable the main Continue action. Feedback, explicit rubric self-assessment, reviewed-task dropdowns and the selected task are saved locally and included in backups. Previously saved responses remain valid.

All 105 glossary entries have three tasks each (315 existing authored tasks). Objective paths retain their concept steps and two final checks. Task slots by objective are 68, 161, 14, 59, 41 and 17; concepts shared between glossary/objectives reuse the same saved responses, and final checks can revisit transfer prompts. These are practice opportunities, not counts of unique concepts or validated mastery. Return and related-term navigation remain available without forcing completion.

No new scientific findings or external medical advice were added. Written responses remain self-assessed against rubrics. Desktop/mobile visual testing and deployment were not performed.
