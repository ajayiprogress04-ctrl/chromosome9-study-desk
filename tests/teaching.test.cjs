const assert=require('node:assert/strict'),fs=require('node:fs');
const d=require('../content/research.json'),app=fs.readFileSync('app.js','utf8');
const sourced=d.terms.filter(t=>t.backgroundSources);
assert.equal(sourced.length,41);
for(const t of sourced){assert.ok(t.plain.length>20);assert.ok(t.mechanism.length>60);assert.ok(t.example.length>20);for(const s of t.backgroundSources)assert.match(s.url,/^https:\/\/(www\.(genome.gov|ncbi.nlm.nih.gov|illumina.com|cancer.gov)|docs.scipy.org)\//);}
assert.ok(d.terms.every(t=>!t.origin.includes('manuscript does not provide a historical')));
assert.match(app,/Teaching example, not an additional study result/);
assert.match(app,/Established background · sources/);
assert.match(d.terms.find(t=>t.id==='q30').mechanism,/does not guarantee/);
assert.match(d.terms.find(t=>t.id==='gene-ddx31').plain,/does not establish/);
assert.match(d.terms.find(t=>t.id==='gene-ankrd18b').plain,/does not provide/);
console.log('PASS Sourced background, examples, honest uncertainty, and distinct study context.');
