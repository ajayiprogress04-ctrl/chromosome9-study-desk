# Chromosome 9 Study Desk

A personal learning workspace for **Chromosome 9 Variant Annotation Profiles Across Public Acute Leukemia Sequencing Datasets**. Subtitle: **Understand the evidence. Explain the study.**

The name identifies the chromosome focus and the personal study purpose. It is a descriptive project name; trademark or product-name uniqueness is not claimed. Repository identifier: `chromosome9-study-desk`.

## Start using it

1. Extract the complete ZIP into one folder.
2. Open `index.html` in a modern browser. The pre-generated content script and local assets are included; there are no CDNs or paid services.
3. Choose a learning objective or open Quick guide. No login or API key is needed.

For a consistent local address, open a terminal in the extracted folder and run `python3 -m http.server 8000` (Windows: `py -m http.server 8000`). Open `http://localhost:8000`. Browser-local storage on file URLs is browser-dependent; the local-server option is recommended for repeat use. The content does not use `fetch`, so local-file loading does not depend on JSON CORS access.

## Included learning tools

- 15 source-linked lessons under six numbered learning objectives in two expandable classes.
- Concise WHY explanations, expandable details, misconceptions and evidence.
- 102 glossary entries with related terms and context-preserving return.
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

Edit science in `content/research.json`, then rebuild `content/content.js`. `content/source-extract.json` contains manuscript paragraphs, the two substantive tables and extracted slide/poster text. `core.js` contains reusable validation/storage/review/search logic. `app.js` contains the interface. All scientific images are local.

## GitHub and Vercel

This deliverable has **not** been committed, pushed or deployed. It includes manuscript and presentation source files. Use a **private GitHub repository by default**; do not publish confidential research or personal learning backups.

1. Create your intended private GitHub repository.
2. Upload the **extracted folder contents**, with index.html at the repository root. Do not upload the ZIP as the application.
3. In Vercel, import that repository, choose Other, keep the build command from vercel.json (`node scripts/build-content.cjs && node scripts/configure-sharing.cjs`), and set the output directory to `.`. Enable access to Vercel System Environment Variables so the production address can be written into sharing metadata during the build.
4. Configure appropriate access protection before relying on the site as private. A private GitHub repository alone does **not** make its deployed website private. Review hosting access controls and the included research material before deployment.
5. Open the returned real address. Optionally put your actual clean production URL in config.js. No domain is reserved or configured by this project.
6. Export a progress backup before changing origin, then import it on the new address.

There is no backend or authentication in this ZIP. Sharing copies an address, not notes. No analytics or external scientific API is called. Developer contact links open external services only when clicked.

## Verification limits

The handover includes automated core tests, simulated-DOM workflow checks, asset checks and computed contrast checks. It does not claim a real-browser visual, responsive, fullscreen, native-share or clipboard-permission audit. The environment did not expose the supported browser QA capability, so no preview server or alternate browser automation was used. Check those items before relying on a deployed version. Original DOCX layout is not rendered by the app; the reading view is extracted text. Slides and poster use image previews and downloadable editable originals.

See TESTING_CHECKLIST.md and tests/verification-report.json. Font licences are in assets. Biography and portrait follow the published reference Hub, not unrelated account memory.

## Sharing image and app icon

A 1200 × 630 PNG sharing card contains the existing chromosome icon and app title. Static Open Graph and Twitter Card tags are in index.html, with PNG favicon/apple-touch/home-screen variants. On Vercel, the build script uses VERCEL_PROJECT_PRODUCTION_URL (or an explicit STUDY_DESK_PRODUCTION_URL environment variable) to generate absolute image/canonical URLs before a crawler requests the page. Browser JavaScript is not relied on for social metadata.

For another host, after obtaining your actual production address, run `node scripts/configure-sharing.cjs YOUR_ACTUAL_HTTPS_ADDRESS` and upload the resulting files. Do not type that instruction placeholder as a real domain. If no deployment address is available, local development keeps relative PNG metadata and does not invent a production URL.

After deployment, inspect the raw page source for an absolute og:image URL, open that image address, and test an actual shared message. A platform may cache an earlier preview, apply a crop, suppress a card or fail to retrieve protected pages. Do not remove access protections merely to force a preview. If needed, a separately accessible generic landing page/card can be discussed while keeping study content protected. No universal logo-display guarantee is made, and live preview behavior has not been tested.
