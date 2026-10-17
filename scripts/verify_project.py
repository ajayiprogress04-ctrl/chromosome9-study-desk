from pathlib import Path
import json,re,sys,hashlib
R=Path(__file__).resolve().parents[1]
data=json.loads((R/'content/research.json').read_text());errors=[];checks=[]
def check(ok,msg):
 (checks if ok else errors).append(msg)
# All science points to actual section labels; numeric examples are tested separately in core.test.cjs.
for section in ['topics','terms','flashcards','questions','figures']:
 for x in data[section]:check(bool(x.get('source')),section+': provenance '+x['id'])
for fig in data['figures']:
 for path in fig['files']:check((R/path).is_file(),'Figure file '+path)
for sl in data['slides']:check((R/sl['image']).is_file(),'Oral preview '+sl['image'])
for path in ['sources/Manuscript.docx','sources/Oral_Presentation.pptx','sources/Poster.pptx','assets/poster/poster.png','assets/progress-ajayi.jpg','assets/source-sans-3-variable.woff','assets/cormorant-garamond-variable.woff','assets/sourcesans3-OFL.txt','assets/cormorantgaramond-OFL.txt']:
 check((R/path).is_file(),'Local source/asset '+path)
html=(R/'index.html').read_text()
for path in re.findall(r'(?:src|href)="([^"#]+)"',html):
 if not path.startswith(('http','mailto:')):check((R/path).is_file(),'HTML dependency '+path)
for path in R.glob('*.js'):
 check(not re.search(r'\b(?:fetch|XMLHttpRequest|sendBeacon|WebSocket)\s*\(',path.read_text()),'No network client in '+path.name)
css=(R/'styles.css').read_text()
# Calculate contrast for normal text and active controls. This is not a browser accessibility audit.
blocks=[(':root',re.search(r':root\{([^}]+)',css)[1])]+[(theme,re.search(r'html\[data-theme='+theme+r'\]\{([^}]+)',css)[1]) for theme in ['dark','colour']]
def lum(hex):
 rgb=[int(hex[i:i+2],16)/255 for i in [1,3,5]];v=[c/12.92 if c<=.04045 else ((c+.055)/1.055)**2.4 for c in rgb];return sum(a*b for a,b in zip(v,[.2126,.7152,.0722]))
def contrast(a,b):
 a,b=sorted([lum(a),lum(b)]);return (b+.05)/(a+.05)
ratios={}
for theme,block in blocks:
 tokens=dict(re.findall(r'--([\w-]+):(#[\da-fA-F]{6})(?:;|$)',block));ratios[theme]={}
 for fg,bg in [('ink','surface'),('ink','bg'),('muted','surface'),('muted','bg'),('accent','surface'),('navy','surface'),('bronze','surface'),('green','surface'),('danger','surface'),('ink','soft'),('muted','soft'),('accent','soft'),('navy','soft'),('bronze','soft'),('green','soft'),('danger','soft'),('on-action','action')]:
  ratio=contrast(tokens[fg],tokens[bg]);ratios[theme][fg+'/'+bg]=round(ratio,2);check(ratio>=4.5,f'{theme} {fg}/{bg} contrast {ratio:.2f} >= 4.5')
 for fg,bg in [('focus','surface'),('line','surface'),('focus','bg'),('line','soft')]:
  ratio=contrast(tokens[fg],tokens[bg]);ratios[theme][fg+'/'+bg]=round(ratio,2);check(ratio>=3,f'{theme} {fg}/{bg} contrast {ratio:.2f} >= 3')
check('@media(max-width:680px)' in css and '@media(max-width:900px)' in css,'Mobile and tablet breakpoint rules present (not visual verification)')
check('prefers-reduced-motion' in css,'Reduced-motion rules')
check('aria-live="polite"' in html and 'Skip to study content' in html,'Live status and skip link')
# Check all handover files exist.
for path in ['README.md','APP_SPECIFICATION.md','APP_DESIGN_SYSTEM.md','LEARNING_ARCHITECTURE.md','SOURCE_CONTENT_MAP.md','CONTENT_SCHEMA.md','BUILD_PLAN.md','TESTING_CHECKLIST.md','AI_BUILD_PROMPT.md','PROJECT_STATUS.md','App_Preferences.md']:
 check((R/path).is_file(),'Handover document '+path)
report={'status':'pass' if not errors else 'fail','passed_checks':len(checks),'errors':errors,'contrast_ratios':ratios,'limitations':['Static checks and simulated DOM only. No real browser visual/responsive/fullscreen/native-share checks were performed.','No deployment performed.']}
(R/'tests/verification-report.json').write_text(json.dumps(report,indent=2));print(json.dumps(report,indent=2));sys.exit(bool(errors))
