# Source reconciliation and content map

## Supplied/available sources

| File in project | Purpose |
|---|---|
| sources/Manuscript.docx | Primary complete scientific manuscript (uploaded Manuscript(2), byte-identical to Manuscript(1)) |
| sources/Oral_Presentation.pptx | Completed ten-slide ORA presentation |
| sources/Poster.pptx | Completed single-page FASCON poster |
| App_Preferences.md | Interface/development authority |

Manuscript paragraphs, both substantive tables and extracted oral/poster text are retained in content/source-extract.json. The third DOCX table is a figure-layout container with A/B labels, not a third scientific data table; its two actual Figure 5 images are preserved. Section/table/figure provenance is used rather than invented page numbers.

## Reconciliation matrix

| Topic / module | Principal learning point | Manuscript | Oral | Poster | Reconciliation |
|---|---|---|---|---|---|
| Why chromosome 9? / 1 · Foundations | This study describes chromosome 9 annotation patterns across public acute leukemia sequencing runs. | Introduction; Background and Literature Review; §3.2.2 | 2, 5 | Introduction and Objective; Results and Discussion | Manuscript controls scientific detail; companions are compressed. |
| What kind of study is this? / 1 · Foundations | A secondary descriptive analysis of six sequencing runs, not a review article or a recruited patient cohort. | §3.1.1; §3.1.4; §3.2.1 | 3 | Materials and Methods | Manuscript controls scientific detail; companions are compressed. |
| Six runs, four biological sources / 1 · Foundations | The ALL group repeats one REH BioSample. AML inputs differ in biological material and assay purpose. | §3.1.1; Table 1; §3.2.1 | 3 | Materials and Methods | Manuscript controls scientific detail; companions are compressed. |
| From public reads to an alignment / 2 · Methods | Quality assessment, trimming, assembly checks and chromosome-focused alignment precede annotation. | §3.1.2 | 4 | Materials and Methods | Manuscript controls scientific detail; companions are compressed. |
| Identity is not coverage / 2 · Methods | ALL-1 had 91.4% pairwise identity but only 0.8% chromosome 9 reference coverage. | §3.2.1; Discussion | 4 | Materials and Methods | Manuscript controls scientific detail; companions are compressed. |
| Calling thresholds versus group tests / 2 · Methods | Geneious filter settings are not tests of AML–ALL differences. | §3.1.3; §3.1.4 | 4, 5 | Materials and Methods | Manuscript controls scientific detail; companions are compressed. |
| Annotation records versus validated variants / 2 · Methods | An annotation record is an annotated entry used in the summaries, not automatically an independent somatic mutation. | §3.1.3; §3.2.1–§3.2.2; Discussion | 5 | Results and Discussion | Manuscript controls scientific detail; companions are compressed. |
| What do the annotation counts show? / 3 · Results | AML-associated counts had a higher median and wider range, with overlap between groups. | §3.2.2; Figure 1 | 5 | Results and Discussion | Manuscript controls scientific detail; companions are compressed. |
| Protein effects and amino-acid summaries / 3 · Results | Substitutions predominated in both groups. Truncation labels were more prominent in ALL. | §3.2.3–§3.2.4; Figures 3–4 | 6 | Results and Discussion | Manuscript controls scientific detail; companions are compressed. |
| Why pooled positions are not hotspots / 3 · Results | Codon and coding-position labels are pooled across coding sequences, not chromosome coordinates. | §3.2.4; Table 2; Discussion | 6 | Not individually displayed | Manuscript controls scientific detail; companions are compressed. |
| Shared and group-restricted sets / 3 · Results | Few recovered labels or annotation records were shared between the two pooled groups. | §3.2.5; Figure 5; Discussion | 7 | Results and Discussion | Manuscript controls scientific detail; companions are compressed. |
| Why clustering does not separate the groups / 3 · Results | AML and ALL labels intermix. ALL-3 and AML-2 form the closest pair. | §3.1.4; §3.2.6; Figures 6–7 | 8 | Results and Discussion | Manuscript controls scientific detail; companions are compressed. |
| Reading the clustered heat map / 3 · Results | Rows are six runs, columns are genes, and values show the plotted annotation representation. | §3.1.4; §3.2.6; Figure 7 caption | 8 | Clustering summarized; heat map not displayed | Manuscript controls scientific detail; companions are compressed. |
| What the evidence cannot establish / 4 · Appraisal and Defence | The study supports descriptive annotation comparisons, with substantial design and coverage limitations. | Discussion; Conclusion | 9 | Conclusion; Materials and Methods | Manuscript controls scientific detail; companions are compressed. |
| A defensible oral synthesis / 4 · Appraisal and Defence | Different recovered profiles, limited overlap and mixed clustering support further controlled study. | Discussion; Conclusion | 9 | Conclusion | Manuscript controls scientific detail; companions are compressed. |

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

## Learning-objective organisation (inferred, not six author-stated research objectives)

- Objective 1: Explain the study purpose, design and biological sources. Lessons: rationale, design, provenance. Source: Introduction; §3.1.1; Table 1.
- Objective 2: Explain processing, coverage, calling and annotation. Lessons: processing, alignment, calling, annotation. Source: §3.1.2–§3.1.4; §3.2.1.
- Objective 3: Interpret annotation counts and gene assignments. Lessons: counts. Source: §3.2.2; Figures 1–2.
- Objective 4: Compare coding effects and pooled position labels. Lessons: coding, positions. Source: §3.2.3–§3.2.4; Figures 3–4; Table 2.
- Objective 5: Interpret overlap, clustering and heat-map evidence. Lessons: overlap, clustering, heatmap. Source: §3.2.5–§3.2.6; Figures 5–7.
- Objective 6: Appraise limitations and defend the study conclusions. Lessons: limitations, conclusions. Source: Discussion; Conclusion.
