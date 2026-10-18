/* Example -> dropdown question -> concise feedback. Legacy written responses remain in backups. */
(function(root,factory){if(typeof module==='object'&&module.exports)module.exports=factory;else root.createLearningSystem=factory;})(typeof globalThis!=='undefined'?globalThis:this,function({data,core,getState,escape:E,onChange,notice}){
core.validateLearning(data,data.learning);
const units=new Map(data.learning.units.map(u=>[u.id,u])),views=new Map(),phases=['practice','retry','mastery'];
const key=(id,phase)=>id+':choice:'+phase,answerId=(id,phase)=>'learn-answer-'+id+':'+phase;
function savedPhase(id){const p=getState().notes['choice-phase-'+id];return phases.includes(p)?p:'practice';}
function view(id){if(!views.has(id))views.set(id,{phase:savedPhase(id)});return views.get(id);}
function question(id){return units.get(id)?.simplePractice[phases.indexOf(view(id).phase)];}
function button(action,id,label,extra=''){return `<button type="button" data-action="learn-${action}" data-unit="${E(id)}"${extra}>${E(label)}</button>`;}
function render(id,options={}){const u=units.get(id);if(!u)return '';const v=view(id),q=question(id),k=key(id,v.phase),r=getState().learning?.[k],draft=getState().notes['learn-'+k]??r?.response??'';
return `<section class="learning-flow" data-learning-unit="${E(id)}"><div class="informational-example"><h3>One example</h3><p class="tiny muted">${u.id.startsWith('case:')?'Hypothetical teaching example':u.id.startsWith('figure:')?'Manuscript figure example':'Teaching example'}</p><p>${E(u.worked.scenario)}</p><p><strong>Demonstrated answer:</strong> ${E(u.worked.answer)}</p><p><strong>Why:</strong> ${E(u.worked.why)}</p><p><strong>Remember:</strong> ${E(u.worked.principle)}</p></div><div class="application-task" data-learning-stage="${E(v.phase)}"><h3>Your turn</h3><p>${E(q.prompt)}</p><label for="${E(answerId(id,v.phase))}">Choose your answer</label><select id="${E(answerId(id,v.phase))}" data-learning-draft="${E('learn-'+k)}"><option value="">Choose an option…</option>${q.options.map((x,i)=>`<option value="${i}"${draft===String(i)?' selected':''}>${E(x)}</option>`).join('')}</select>${button('submit',id,'Submit my answer',' class="primary"')}${r?`<div class="answer learning-feedback" id="${E('learning-feedback-'+k)}" role="status" tabindex="-1"><strong>${r.outcome==='correct'?'Correct.':r.outcome==='assisted-correct'?'Correct after feedback.':'Review this answer.'}</strong><p><strong>Answer:</strong> ${E(q.answer)}</p><p><strong>Why:</strong> ${E(q.why)}</p></div><div class="toolbar">${button('next-practice',id,'Another question')}${options.nextLabel?button('continue',id,options.nextLabel,` data-next="${E(options.next||'')}"`):''}</div>`:''}</div></section>`;
}
function handle(action,el){if(!action.startsWith('learn-'))return false;const id=el.dataset.unit;if(!units.has(id))return true;const v=view(id),q=question(id),k=key(id,v.phase),state=getState();
if(action==='learn-submit'){const response=String(document.getElementById(answerId(id,v.phase))?.value??state.notes['learn-'+k]??'').trim();let result;try{result=core.assessApplication(q,response);}catch{notice('Choose an answer first.');return true;}state.learning||={};const old=state.learning[k];state.notes['learn-'+k]=response;state.learning[k]={response,outcome:result.correct&&old?.attempts?'assisted-correct':result.outcome,at:Date.now(),attempts:(old?.attempts||0)+1};onChange({focusId:'learning-feedback-'+k});}
else if(action==='learn-next-practice'){v.phase=phases[(phases.indexOf(v.phase)+1)%phases.length];state.notes['choice-phase-'+id]=v.phase;onChange({focusId:answerId(id,v.phase)});}
else if(action==='learn-continue'&&canContinue(id))onChange({next:el.dataset.next,unit:id,advance:true});
return true;
}
function canContinue(id){return !!getState().learning?.[key(id,view(id).phase)]?.attempts;}
function captureInput(el){if(el.dataset.learningDraft){getState().notes[el.dataset.learningDraft]=String(el.value||'').slice(0,50000);return true;}return false;}
return {render,handle,captureInput,canContinue,canFinish:canContinue,savedPhase,reset(){views.clear();},setPhase(id,phase){view(id).phase=phases.includes(phase)?phase:savedPhase(id);},getUnit:id=>units.get(id),getQuestion:question,getView:view};
});
