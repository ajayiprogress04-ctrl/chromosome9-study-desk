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
