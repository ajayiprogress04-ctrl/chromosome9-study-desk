/* Write crawler-readable sharing metadata at build time, not through browser JavaScript. */
const fs=require('node:fs'),path=require('node:path');
function normaliseURL(value){if(!value)return '';let raw=value.trim();if(!/^[a-z][a-z\d+.-]*:/i.test(raw))raw='https://'+raw;const url=new URL(raw);if(!['https:','http:'].includes(url.protocol)||url.username||url.password)throw Error('Supply an HTTP(S) production address without credentials.');url.hash='';url.search='';if(!url.pathname.endsWith('/'))url.pathname+='/';return url.href;}
function esc(s){return s.replace(/&/g,'&amp;').replace(/"/g,'&quot;').replace(/</g,'&lt;');}
function metadata(base=''){const card=base?new URL('assets/share-card.png',base).href:'assets/share-card.png';return `<!-- SHARE_METADATA_START -->
<meta property="og:type" content="website">
<meta property="og:site_name" content="Chromosome 9 Study Desk">
<meta property="og:title" content="Chromosome 9 Study Desk">
<meta property="og:description" content="Understand the evidence. Explain the study.">
${base?`<meta property="og:url" content="${esc(base)}">\n<link rel="canonical" href="${esc(base)}">`:''}
<meta property="og:image" content="${esc(card)}">
<meta property="og:image:type" content="image/png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Chromosome 9 Study Desk: cream chromosome icon on a deep burgundy background, with the app title.">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Chromosome 9 Study Desk">
<meta name="twitter:description" content="Understand the evidence. Explain the study.">
<meta name="twitter:image" content="${esc(card)}">
<meta name="twitter:image:alt" content="Chromosome 9 Study Desk app icon and title.">
<!-- SHARE_METADATA_END -->`;}
function configure(root,raw){const base=normaliseURL(raw);if(!base){console.log('Sharing PNG and metadata are present. Absolute addresses will be set when a real deployment URL is available.');return false;}const p=path.join(root,'index.html'),html=fs.readFileSync(p,'utf8');if(!html.includes('<!-- SHARE_METADATA_START -->'))throw Error('Sharing metadata markers are missing.');fs.writeFileSync(p,html.replace(/<!-- SHARE_METADATA_START -->[\s\S]*?<!-- SHARE_METADATA_END -->/,()=>metadata(base)));fs.writeFileSync(path.join(root,'config.js'),'/* Public production address generated at build time. No credentials are stored here. */\nwindow.STUDY_DESK_PRODUCTION_URL = '+JSON.stringify(base)+';\n');console.log('Static sharing metadata and clean app address configured.');return true;}
if(require.main===module){try{configure(path.join(__dirname,'..'),process.argv[2]||process.env.STUDY_DESK_PRODUCTION_URL||process.env.VERCEL_PROJECT_PRODUCTION_URL||'');}catch(e){console.error(e.message);process.exitCode=1;}}
module.exports={normaliseURL,metadata,configure};
