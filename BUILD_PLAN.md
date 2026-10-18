# Build plan and maintenance milestones

| Stage | Result | State |
|---|---|---|
| Intake | All four source roles confirmed | Complete |
| Inspection | Manuscript, oral/poster text, all figures; live reference code/theme/profile/latest commit | Complete |
| Reconciliation | Study type, units, legacy figure wording, heat-map uncertainty | Complete |
| Learning design | 15 topics; 105 terms; 56 cards; 30 questions; evidence map | Complete |
| Implementation | Static source code, themes, lessons, recall, questions, viewers, notes, source tracking | Complete |
| Checks | Core logic, simulated DOM, static asset/source/contrast checks | Run and recorded in tests |
| Real-browser QA | Desktop/mobile, keyboard, fullscreen/share/clipboard, actual file-origin storage | Outstanding |
| Deployment | Private repo/access-protected hosting as appropriate | Not performed |

## Updating science

1. Retain the exact new source version before editing.
2. Compare changes against the current source map.
3. Update research.json and any affected figure/slide assets; document unresolved differences.
4. Run the content build after editing the primary JSON; do not overwrite editorial changes from an older release.
5. Run automated checks, then relevant browser checks.
6. Preserve local-state compatibility or provide an explicit migration. Do not silently reset notes.
7. Regenerate a complete ZIP rather than a patch.

## Future scope

A second study can be added by extending the content schema and navigation, with an explicit per-study state namespace. Cross-device synchronization or authentication would require a deliberately selected backend; neither is needed or claimed for this version. Do not add paid AI services or public publication as an assumed maintenance step.

## Version 2.3.0 — simpler app built around examples

The start page immediately shows the saved objective concept and its example/practice sequence. Five primary dropdown destinations replace the large main menu: Start, Objectives, Worked Examples, Glossary and Figures/Tables. Supporting tools remain under More practice and reference; documents, long notes and source-gallery previews remain available in collapsed reference sections.

Thirty authored hypothetical worked cases (two per topic) add 90 tasks. There are now 175 worked-example units and 525 authored practice tasks. The Worked Examples library filters by objective, saves its selected example and filter, and requires the three-task sequence before sequential Next. Each glossary entry can switch between its own term example and two clearly labelled related topic cases. All other instructional components use the same three-task sequence. The original question bank remains a separate source-linked practice bank with demonstrated examples.

New cases cover scope, causal overclaims, biological provenance, sequence processing, identity/coverage, calling filters, annotation units, summary statistics, predicted coding consequences, coordinate context, set overlap, clustering, heat-map scaling and conclusions. All new numbers and invented labels are hypothetical, not new study findings. Existing figures, tables, source files, themes, sharing and backups are retained.

Old objective cursors at final checks enter the new cases before the final checks; previous answers, notes and completed-step identifiers are preserved. Returning from the glossary refreshes any shared activity’s phase while restoring the previous view and scroll.

Objective task slots (including repeated final checks) are: {'o1': 86, 'o2': 185, 'o3': 20, 'o4': 71, 'o5': 59, 'o6': 29}. These slots reuse saved concepts across views and are not a count of unique findings or validated mastery. Free responses remain explicitly self-assessed. No deployment or real-browser desktop/mobile visual verification was performed.
