/* ---------- data: index + per-category detail files (data/<cat>.js) ---------- */
const D=window.PM_INDEX;
const LOADED={},WAIT={},REQ={};
function pmAdd(cat,secs){for(const id in secs){if(R[id])R[id].secs=secs[id]}LOADED[cat]=true;(WAIT[cat]||[]).forEach(f=>f(true));delete WAIT[cat]}
function need(cat){return new Promise(res=>{
 if(LOADED[cat])return res(true);
 (WAIT[cat]=WAIT[cat]||[]).push(res);
 if(REQ[cat])return;REQ[cat]=1;
 const sc=document.createElement('script');sc.src='data/'+cat+'.js';sc.async=true;
 sc.onerror=()=>{REQ[cat]=0;(WAIT[cat]||[]).forEach(f=>f(false));delete WAIT[cat]};
 document.head.appendChild(sc);})}
const R={};D.rules.forEach((r,i)=>{r.i=i;R[r.id]=r});
const C={};D.cats.forEach(c=>C[c.id]=c);
/* category files call PM_Q.push([cat,secs]) — works whether they load before or after this script */
(function(){const q=window.PM_Q||[];window.PM_Q={push:a=>pmAdd(a[0],a[1])};q.forEach(a=>pmAdd(a[0],a[1]))})();
const CATCOL={par:'#B42318',sd:'#C2410C',ani:'#7C3AED',np:'#B7791F',pac:'#A16207',pd:'#1D4ED8',sk:'#475569',as:'#047857'};
let S={lang:'en',theme:'lemon',fs:17,script:'roman'};
const SKEY='pm-settings-v3';
try{Object.assign(S,JSON.parse(localStorage.getItem(SKEY)||'{}'))}catch(e){}
function save(){try{localStorage.setItem(SKEY,JSON.stringify(S))}catch(e){}}
const $=s=>document.querySelector(s);
const L=o=>o==null?'':(typeof o==='string'?o:(o[S.lang]||(S.lang==='zh'?o.en:'')||o.si||o.en||''));
const T=(si,en)=>S.lang==='si'?si:ZT(en);
const esc=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const IC={
 swap:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M7 4 3 8l4 4"/><path d="M3 8h13a4 4 0 0 1 4 4"/><path d="m17 20 4-4-4-4"/><path d="M21 16H8a4 4 0 0 1-4-4"/></svg>',
 pada:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 7V5h16v2"/><path d="M12 5v14"/><path d="M9 19h6"/></svg>',
 cmt:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/><path d="M8 9h8M8 13h5"/></svg>',
 att:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 4h6a4 4 0 0 1 4 4v13a3 3 0 0 0-3-3H2z"/><path d="M22 4h-6a4 4 0 0 0-4 4v13a3 3 0 0 1 3-3h7z"/></svg>',
 img:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"><rect x="3" y="4" width="18" height="16" rx="2"/><circle cx="9" cy="10" r="2"/><path d="M21 17l-5-5-9 8"/></svg>',
 chev:'<svg class="chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M9 6l6 6-6 6"/></svg>',
 book:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20V3H6.5A2.5 2.5 0 0 0 4 5.5z"/><path d="M4 19.5A2.5 2.5 0 0 0 6.5 22H20v-5"/></svg>',
 scale:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v18M7 21h10M5 7h14M5 7l-3 7a3 3 0 0 0 6 0zM19 7l-3 7a3 3 0 0 0 6 0z"/></svg>',
 check:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M8 12l3 3 5-6"/></svg>',
 list:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M9 6h11M9 12h11M9 18h11"/><circle cx="4.5" cy="6" r="1.3"/><circle cx="4.5" cy="12" r="1.3"/><circle cx="4.5" cy="18" r="1.3"/></svg>',
 grid:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M3 15h18M9 3v18"/></svg>',
 doc:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"/><path d="M14 3v6h6M8 13h8M8 17h6"/></svg>',
 key:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="8" cy="15" r="4"/><path d="M11 12l9-9M17 6l3 3"/></svg>',
 origin:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"/><path d="M12 2v4M12 18v4M2 12h4M18 12h4"/></svg>',
 grid4:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"><rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/></svg>',
 home:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 11l9-7 9 7"/><path d="M5 10v10h14V10"/></svg>',
 table:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"><rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 10h18M3 15h18M10 4v16"/></svg>',
 expand:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M7 10l5 5 5-5"/><path d="M7 4l5 5 5-5"/></svg>'
};
/* ---------- labels ---------- */
const UI={
 app:['ප්‍රාතිමෝක්ෂ අධ්‍යයනය','Pātimokkha Study'],
 appS:['භික්ඛු පාතිමොක්ඛ · ශික්ෂාපද 227','Bhikkhu Pātimokkha · 227 training rules'],
 menu:['පටුන','Contents'],set:['සැකසුම්','Settings'],search:['ශික්ෂාපදයක් සොයන්න…','Search a rule…'],
 lang:['භාෂාව','Language'],theme:['වර්ණ තේමාව','Colour theme'],fsz:['අකුරු ප්‍රමාණය','Text size'],script:['පාළි අක්ෂර','Pāli script'],
 sinh:['සිංහල','Sinhala'],rom:['රෝම','Roman'],
 home:['මුල් පිටුව','Home'],others:['අනෙකුත් කරුණු','Other topics'],
 r17:['සප්තදශාකාරය (ආකාර 17)','The seventeen aspects'],rsamu:['සමුට්ඨාන (6 හා 13)','Origins (6 and 13)'],rap:['ආපත්ති වර්ග 7','Seven classes of offence'],rall:['ශික්ෂාපද 227 සාරාංශ වගුව','Summary table of all 227'],figs:['රූප සටහන්','Illustrations'],
 rule:['ශික්ෂාපදය','Training rule'],pali:['පාළි පාඨය','Pāli text'],trans:['අර්ථය','Meaning'],
 s17:['සප්තදශාකාරය','The 17 aspects'],openAll:['සියල්ල විවෘත කරන්න','Open all'],closeAll:['සියල්ල වසන්න','Close all'],
 prev:['පෙර','Previous'],next:['ඊළඟ','Next'],rules:['ශික්ෂාපද','rules'],nores:['ප්‍රතිඵල නැත','No results'],
 tip:['ඉඟිය: ශික්ෂාපදයක විස්තර බැලීමට ඉහළ බොත්තම් ඔබන්න. එක් එක් කොටස වෙන වෙනම විවෘත වේ.','Tip: tap the buttons to open each part of the explanation. Each part opens separately.'],
 nodata:['මෙම ශික්ෂාපදයේ විස්තර තවම එකතු කර නැත.','Details for this rule have not been added yet.'],
 cont:['අවසන් වරට බැලූ ශික්ෂාපදය','Continue where you left off'],
 cats:['ශික්ෂාපද කොටස්','Sections of the Pātimokkha'],
 all:['සියල්ල','All']
};
const u=k=>UI[k][S.lang==='si'?0:1];
const AP={PR:['r','පාරාජික','Pārājika'],SD:['o','සංඝාදිසේස','Saṅghādisesa'],TH:['p','ථුල්ලච්චය','Thullaccaya'],NP:['y','නිස්සග්ගිය පාචිත්තිය','Nissaggiya pācittiya'],PC:['y','පාචිත්තිය','Pācittiya'],PD:['b','පාටිදේසනීය','Pāṭidesanīya'],DK:['g','දුක්කට','Dukkaṭa'],DB:['g','දුබ්භාසිත','Dubbhāsita']};
const tag=c=>AP[c]?`<span class="tag ${AP[c][0]}">${S.lang==='si'?AP[c][1]:AP[c][2]}</span>`:'';
const SIX=[['කාය','Body'],['වාචා','Speech'],['කාය+වාචා','Body+speech'],['කාය+චිත්ත','Body+mind'],['වාචා+චිත්ත','Speech+mind'],['කාය+වාචා+චිත්ත','Body+speech+mind']];
const SM={p1:['පඨමපාරාජික සමුට්ඨාන','Paṭhamapārājika-samuṭṭhāna',[4]],ad:['අදින්නාදාන සමුට්ඨාන','Adinnādāna-samuṭṭhāna',[4,5,6]],sc:['සඤ්චරිත්ත සමුට්ඨාන','Sañcaritta-samuṭṭhāna',[1,2,3,4,5,6]],sb:['සමනුභාසන සමුට්ඨාන','Samanubhāsana-samuṭṭhāna',[6]],kt:['කථින සමුට්ඨාන','Kathina-samuṭṭhāna',[3,6]],el:['එළකලෝම සමුට්ඨාන','Eḷakaloma-samuṭṭhāna',[1,4]],pd:['පදසෝධම්ම සමුට්ඨාන','Padasodhamma-samuṭṭhāna',[2,5]],ah:['අද්ධාන සමුට්ඨාන','Addhāna-samuṭṭhāna',[1,3,4,6]],ts:['ථෙය්‍යසත්ථ සමුට්ඨාන','Theyyasattha-samuṭṭhāna',[4,6]],dd:['ධම්මදේසනා සමුට්ඨාන','Dhammadesanā-samuṭṭhāna',[5]],bh:['භූතාරෝචන සමුට්ඨාන','Bhūtārocana-samuṭṭhāna',[1,2,3]],cv:['චෝරීවුට්ඨාපන සමුට්ඨාන','Corīvuṭṭhāpana-samuṭṭhāna',[5,6]],an:['අනනුඤ්ඤාත සමුට්ඨාන','Ananuññāta-samuṭṭhāna',[2,3,5,6]]};
const KR={K:['කිරියා — කිරීමෙන් ඇවැත් වේ','Kiriyā — arises by doing'],A:['අකිරියා — නොකිරීමෙන් ඇවැත් වේ','Akiriyā — arises by not doing'],KA:['කිරියාකිරියා — කිරීමෙන් හා නොකිරීමෙන්','Kiriyākiriyā — by doing and not doing'],KoA:['සියා කිරියා, සියා අකිරියා','Sometimes by doing, sometimes by not doing'],KoKA:['සියා කිරියා, සියා කිරියාකිරියා','Sometimes by doing, sometimes by doing-and-not-doing']};
const SV={S:['සඤ්ඤාවිමොක්ඛ — වීතික්කම සංඥාව නැතිනම් නිදහස්','Saññāvimokkha — free of offence without perception of transgression'],N:['නොසඤ්ඤාවිමොක්ඛ — සංඥාව නැතත් ඇවැත් වේ','No-saññāvimokkha — offence even without that perception']};
const CI={S:['සචිත්තක — සිත සහිතව පමණි','Sacittaka — only with intention'],A:['අචිත්තක — සිතක් නැතිවත් වේ','Acittaka — even without intention']};
const VJ={L:['ලෝකවජ්ජ — ලෝකයා ද වරදක් ලෙස සලකයි','Lokavajja — blameworthy by the world'],P:['පණ්ණත්තිවජ්ජ — පැනවීම නිසා පමණක් වරද','Paṇṇattivajja — blameworthy by the rule only']};
const KM={K:['කායකම්ම','Bodily action'],V:['වචීකම්ම','Verbal action'],KV:['කායකම්ම, වචීකම්ම','Bodily and verbal action']};
const CIT={A:['අකුසල චිත්ත (එක සිතයි)','Unwholesome mind only (one)'],'2':['කුසල, අබ්‍යාකත (ද්විචිත්ත)','Wholesome or indeterminate (two)'],'3':['තිචිත්ත — කුසල, අකුසල, අබ්‍යාකත','Ticitta — wholesome, unwholesome, indeterminate']};
const VED={D:['දුක්ඛ වේදනා පමණි','Painful feeling only'],'2':['ද්විවේදන — සුඛ, උපේක්ෂා','Two feelings — pleasant, neutral'],'3':['තිවේදන — සුඛ, දුක්ඛ, උපේක්ෂා','Three feelings — pleasant, painful, neutral']};
const VP={sila:['සීලවිපත්ති','Failure in virtue'],silacara:['සීලවිපත්ති හෝ ආචාරවිපත්ති (පිළිගන්නා ඇවත අනුව)','Failure in virtue or in conduct (by the offence admitted)'],acara:['ආචාරවිපත්ති','Failure in conduct'],ditthi:['දිට්ඨිවිපත්ති','Failure in view'],ajiva:['ආජීවවිපත්ති','Failure in livelihood']};
const pick=(m,k)=>m[k]?m[k][S.lang==='si'?0:1]:'—';
const ROWS=[
 ['නිදානය','Nidāna','Origin place'],['පුද්ගලයා','Puggala','Person'],['වස්තුව','Vatthu','Matter'],['ප්‍රඥප්ති විධිය','Paññattividhi','Kind of promulgation'],['ආණත්තිය','Āṇatti','Command'],['ආපත්තිය','Āpatti','Offences'],['අනාපත්තිය','Anāpatti','Non-offence'],['විපත්තිය','Vipatti','Failure'],['අංග','Aṅga','Factors'],['සමුට්ඨානය','Samuṭṭhāna','Origination'],['ක්‍රියාව','Kiriyā','Doing'],['සංඥාව','Saññā','Perception'],['චිත්තය','Citta','Intention'],['වජ්ජය','Vajja','Blame'],['කර්මය','Kamma','Action'],['කුසල ත්‍රිකය','Kusalattika','State of mind'],['වේදනා ත්‍රිකය','Vedanāttika','Feeling']
];
function vipOf(r){const s=r.s17||{};if(s.vp)return s.vp;return (r.cat==='par'||r.cat==='sd')?'sila':'acara'}
function sixGrid(code){const g=SM[code];if(!g)return'';return '<div class="six">'+SIX.map((x,i)=>`<span class="${g[2].includes(i+1)?'on':''}">${i+1}. ${S.lang==='si'?x[0]:x[1]}</span>`).join('')+'</div>'}
function table17(r){
 const s=r.s17||{};const si=S.lang==='si';
 const pf=[];pf.push(si?'ප්‍රඥප්ති 1':ZT('One promulgation'));
 if(s.anu&&+s.anu>0)pf.push(si?`අනුප්‍රඥප්ති ${s.anu}`:S.lang==='zh'?`随制 ${s.anu} 条`:`${s.anu} supplementary rule${s.anu>1?'s':''}`);
 if(s.sd)pf.push(s.sd==='s'?(si?'සාධාරණ (භික්ෂුණීන්ට ද පොදු)':ZT('Shared (also binds bhikkhunīs)')):(si?'අසාධාරණ (භික්ෂූන්ට පමණි)':ZT('Not shared (bhikkhus only)')));
 const an=s.an?(s.an==='s'?(si?'සාණත්තික — අනුන් ලවා කරවීමෙන් ද ඇවැත් වේ':ZT('Sāṇattika — offence also by ordering another')):(si?'අනාණත්තික — අනුන් ලවා කරවීමෙන් මෙම ඇවැත නොවේ':ZT('Anāṇattika — no offence by ordering another'))):'—';
 let ag='—';if(s.ag){ag=`<b>${s.ag}</b> `+(si?'ක්':ZT(''));const lst=s.ags&&(s.ags[S.lang]||(S.lang==='zh'&&s.ags.en)||s.ags.si);ag=`<b>${s.ag}</b>`+(lst?'<ol class="ul" style="margin:.3rem 0 0">'+lst.map(x=>`<li>${x.replace(/\*\*(.+?)\*\*/g,'$1')}</li>`).join('')+'</ol>':'')}
 const sm=SM[s.sm]?`<b>${si?SM[s.sm][0]:SM[s.sm][1]}</b>${sixGrid(s.sm)}`:'—';
 const vals=[L(s.n)||'—',L(s.p)||'—',L(s.v)||'—',pf.join(' · '),an,(s.ap||[]).map(tag).join(' ')||'—',L(s.z)||'—',pick(VP,vipOf(r)),ag,sm,pick(KR,s.kr),pick(SV,s.sv),pick(CI,s.ci),pick(VJ,s.vj),pick(KM,s.km),pick(CIT,s.cit),pick(VED,s.ved)];
 return '<div class="scroll"><table class="t17"><tr><th>#</th><th>'+(si?'ආකාරය':ZT('Aspect'))+'</th><th>'+(si?'මෙම ශික්ෂාපදයෙහි':ZT('In this rule'))+'</th></tr>'+ROWS.map((x,i)=>`<tr><td>${i+1}</td><td>${si?x[0]:x[2]+`<small>${x[1]}</small>`}</td><td>${vals[i]}</td></tr>`).join('')+'</table></div>';
}
function iconFor(t){t=t||'';
 if(/කථා|Story/i.test(t))return IC.book;
 if(/අනාපත්ති|No offence|Non-offence/i.test(t))return IC.check;
 if(/ආපත්ති|Division|offences|Offence/i.test(t))return IC.scale;
 if(/අංග|Factors/i.test(t))return IC.list;
 if(/සමුට්ඨාන|Origin/i.test(t))return IC.origin;
 if(/ප්‍රඥප්ති|laying down/i.test(t))return IC.key;
 return IC.doc}
/* ---------- tree ---------- */
function vgName(c,v){return v.si?(L(v)):null}
function ruleLabel(r){return L(r.title)}
function numLabel(r){return r.n}
function buildTree(){
 const el=$('#tree');
 const cur=curRule();
 let h='';
 D.cats.forEach(c=>{
  const isOpen=openCats.has(c.id);
  h+=`<div class="tcat ${isOpen?'open':''}" data-c="${c.id}"><button class="tbtn" data-tog="${c.id}">${IC.chev}<span class="cnum" style="background:${CATCOL[c.id]}">${c.vaggas.reduce((a,v)=>a+v.ids.length,0)}</span><span>${esc(L(c))}<small>${esc((S.lang==='si'?c.sub_si:(S.lang==='zh'&&c.sub_zh)||c.sub_en))}</small></span></button><div class="tkids">`;
  c.vaggas.forEach((v,vi)=>{
   const rl=v.ids.map(id=>{const r=R[id];return `<a class="trule ${cur===id?'cur':''} ${r.has?'':'nodata'}" href="#r-${id}"><span class="tn">${r.n}</span><span>${esc(ruleLabel(r))}</span></a>`}).join('');
   if(v.si){const k=c.id+'-'+vi;h+=`<div class="tvg ${openVg.has(k)?'open':''}"><button class="tbtn" data-tog="${k}">${IC.chev}<span>${esc(L(v))}</span><span class="vc">${v.ids.length}</span></button><div class="tkids">${rl}</div></div>`}
   else h+=rl;
  });
  h+='</div></div>';
 });
 el.innerHTML=h;
 $('#more').innerHTML=MORE.map(x=>`<a class="tlink${location.hash==='#'+x[0]?' cur':''}" href="#${x[0]}"><i>${x[1]}</i><span>${u(x[2])}</span></a>`).join('');
 buildNtabs();
}
/* ---------- navigation pane tabs: home · contents · other topics ---------- */
const MORE=[['ref-17',IC.grid,'r17'],['ref-samu',IC.origin,'rsamu'],['ref-apatti',IC.scale,'rap'],['all',IC.table,'rall'],['figs',IC.img,'figs']];
let NTAB=null;
function buildNtabs(){
 const h=location.hash.slice(1);
 if(!NTAB)NTAB=MORE.some(x=>x[0]===h)?'more':'toc';
 const T3=[['home',IC.home,'home'],['toc',IC.list,'menu'],['more',IC.grid4,'others']];
 const onHome=!h||h==='home';
 $('#ntabs').innerHTML=T3.map(t=>`<button class="ntab${t[0]===NTAB||(t[0]==='home'&&onHome)?' on':''}${t[0]==='home'?' nhome':''}" data-ntab="${t[0]}" role="tab" aria-selected="${t[0]===NTAB}"><i>${t[1]}</i><span>${u(t[2])}</span></button>`).join('');
 $('#tree').hidden=NTAB!=='toc';$('#more').hidden=NTAB!=='more';
 $('#dT').textContent=u(NTAB==='more'?'others':'menu');
}
$('#ntabs').addEventListener('click',e=>{const b=e.target.closest('[data-ntab]');if(!b)return;const k=b.dataset.ntab;
 if(k==='home'){closeSearch(true);if(location.hash&&location.hash!=='#home')location.hash='home';else route(false);if(!isPinned())closeAll();return}
 NTAB=k;buildNtabs()});
$('#more').addEventListener('click',e=>{if(e.target.closest('a')&&!isPinned())closeAll()});

const openCats=new Set(),openVg=new Set();
$('#tree').addEventListener('click',e=>{
 const b=e.target.closest('[data-tog]');
 if(b){const k=b.dataset.tog;const set=k.includes('-')?openVg:openCats;set.has(k)?set.delete(k):set.add(k);b.parentElement.classList.toggle('open');return}
 if(e.target.closest('a')&&!isPinned())closeAll();
});
function fold(x){return x.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g,'').replace(/\u200d/g,'')}
function runSearch(){
 const raw=$('#q').value.trim();const box=$('#sresults');$('.hsearch').classList.toggle('has',!!raw);
 if(!raw){box.hidden=true;box.innerHTML='';return}
 const q=fold(raw);
 const res=D.rules.filter(r=>fold([r.title.si,r.title.en,r.pn,r.pnr,r.pt,r.ptr,(C[r.cat].en+' '+r.n),(C[r.cat].si+' '+r.n),String(r.g)].join(' ')).includes(q)).slice(0,80);
 box.innerHTML=res.length?res.map(r=>`<a class="trule" href="#r-${r.id}"><span class="tn">${r.n}</span><span>${esc(ruleLabel(r))}<br><span class="mini">${esc(L(C[r.cat]))}</span></span></a>`).join(''):`<div class="empty">${u('nores')}</div>`;
 box.hidden=false;
}
function closeSearch(clear){$('#sresults').hidden=true;if(clear){$('#q').value='';$('.hsearch').classList.remove('has')}}
$('#q').addEventListener('input',runSearch);
$('#q').addEventListener('focus',()=>{if($('#q').value.trim())runSearch()});
$('#qClear').addEventListener('click',()=>{closeSearch(true);$('#q').focus()});
$('#sresults').addEventListener('click',e=>{if(e.target.closest('a')){closeSearch(true);$('#q').blur()}});
document.addEventListener('click',e=>{if(!e.target.closest('#top'))closeSearch(false)});
function setHH(){document.documentElement.style.setProperty('--hh',$('#top').offsetHeight+'px')}
addEventListener('resize',setHH);
/* ---------- drawer / sheet ---------- */
function isPinned(){return document.body.classList.contains('pin')&&innerWidth>=1180}
function openDrawer(){if(innerWidth>=1180){document.body.classList.toggle('pin');try{localStorage.setItem('pm-pin',document.body.classList.contains('pin')?'1':'0')}catch(e){}return}$('#drawer').classList.add('on');$('#scrim').classList.add('on')}
function openSheet(){renderSettings();$('#sheet').classList.add('on');$('#scrim').classList.add('on')}
function closeAll(){$('#drawer').classList.remove('on');$('#sheet').classList.remove('on');$('#scrim').classList.remove('on')}
$('#menuBtn').onclick=openDrawer;$('#setBtn').onclick=openSheet;$('#scrim').onclick=closeAll;$('#dClose').onclick=closeAll;$('#sClose').onclick=closeAll;
$('#brand').onclick=()=>{location.hash='home'};
document.addEventListener('keydown',e=>{if(e.key==='Escape'){closeAll();closeSearch(false)}
 if(e.target.tagName==='INPUT')return;const r=R[curRule()];if(!r)return;
 if(e.key==='ArrowRight'&&D.rules[r.i+1])location.hash='r-'+D.rules[r.i+1].id;
 if(e.key==='ArrowLeft'&&D.rules[r.i-1])location.hash='r-'+D.rules[r.i-1].id;});
/* ---------- settings ---------- */
const THEMES=[['sky','ලා නිල්','Light blue','#7DB8E8'],['lemon','ලා කහ','Light yellow','#F3DE7A'],['mint','මින්ට්','Mint','#8FD9BE'],['cream','ක්‍රීම්','Cream','#E9D9B8'],['forest','වන හරිත','Forest','#1F5132'],['saffron','කාෂාය','Saffron','#A9561A'],['ocean','නිල් සාගර','Ocean','#1E4E8C'],['lotus','රත් පියුම','Lotus','#8E2433'],['night','අඳුරු','Dark','#0D1412']];
function renderSettings(){
 $('#sT').textContent=u('set');
 $('#sbody').innerHTML=`
 <div class="sgroup"><h4>${u('lang')}</h4><div class="seg"><button data-lang="si" class="${S.lang==='si'?'on':ZT('')}">සිංහල</button><button data-lang="en" class="${S.lang==='en'?'on':''}">English</button><button data-lang="zh" class="${S.lang==='zh'?'on':''}">中文</button></div></div>
 <div class="sgroup"><h4>${u('theme')}</h4><div class="themes">${THEMES.map(t=>`<button class="sw ${S.theme===t[0]?'on':''}" data-theme="${t[0]}"><span style="background:${t[0]==='night'?'linear-gradient(135deg,#0D1412 50%,#5DBB86 50%)':t[3]}"></span>${S.lang==='si'?t[1]:t[2]}</button>`).join('')}</div></div>
 <div class="sgroup"><h4>${u('fsz')}</h4><div class="fsrow"><button data-fs="-1" aria-label="smaller">A−</button><input type="range" min="13" max="26" step="1" value="${S.fs}" id="fsr"><button data-fs="1" aria-label="larger" style="font-size:1.15rem">A+</button></div><div class="fsval">${Math.round(S.fs/17*100)}%</div><div class="preview">${T('යො පන භික්ඛු… — ශික්ෂාපදයක පෙළ මෙලෙස දිස් වේ.','Yo pana bhikkhu… — rule text will look like this.')}</div></div>
 ${S.lang==='si'?'':`<div class="sgroup"><h4>${u('script')}</h4><div class="seg"><button data-script="native" class="${S.script==='native'?'on':''}">${T('සිංහල අකුරෙන්','Sinhala script')}</button><button data-script="roman" class="${S.script==='roman'?'on':''}">${T('රෝම අකුරෙන්','Roman script')}</button></div><p class="mini" style="margin-top:.5rem">${T('පාළි පාඨ පෙන්වන අක්ෂර ක්‍රමය.','The script used to show Pāli text.')}</p></div>`}`;
}
$('#sbody').addEventListener('click',e=>{
 const b=e.target.closest('button');if(!b)return;
 if(b.dataset.lang){S.lang=b.dataset.lang;if(S.lang==='en'&&!S._scriptSet)S.script='roman';if(S.lang==='si'&&!S._scriptSet)S.script='native';if(S.lang==='zh'&&!S._scriptSet)S.script='roman'}
 if(b.dataset.theme)S.theme=b.dataset.theme;
 if(b.dataset.fs)S.fs=Math.min(26,Math.max(13,S.fs+ +b.dataset.fs));
 if(b.dataset.script){S.script=b.dataset.script;S._scriptSet=true}
 save();apply();renderSettings();
});
$('#sbody').addEventListener('input',e=>{if(e.target.id==='fsr'){S.fs=+e.target.value;save();apply();$('.fsval').textContent=Math.round(S.fs/17*100)+'%'}});
function apply(full=true){
 document.documentElement.dataset.theme=S.theme;document.documentElement.style.setProperty('--fs',S.fs+'px');document.documentElement.lang=S.lang==='zh'?'zh-Hans':S.lang;zhify();document.documentElement.dataset.script=scr();document.documentElement.dataset.story=S.story||'long';document.documentElement.dataset.pali=S.pali?'1':'';
 const m=document.querySelector('meta[name=theme-color]');
 $('#brandT').textContent=u('app');$('#dT').textContent=u('menu');$('#q').placeholder=u('search');setHH();if($('#q').value.trim())runSearch();
 if(full){buildTree();route(true)}
}
/* ---------- 3D diagrams (three.js loaded only when a diagram becomes visible) ---------- */
const SCR={};
function loadJS(n){return SCR[n]||(SCR[n]=new Promise((res,rej)=>{const sc=document.createElement('script');const emb=document.getElementById('src-'+n);
 sc.src=emb?URL.createObjectURL(new Blob([emb.textContent],{type:'text/javascript'})):'js/'+n+'.js';sc.onload=res;sc.onerror=()=>{SCR[n]=null;rej()};document.head.appendChild(sc)}))}
let DIO=null;
function initDiagrams(){
 if(window.PMD)PMD.disposeAll();
 const figs=[...document.querySelectorAll('#main figure.dgm')];if(!figs.length)return;
 if(DIO)DIO.disconnect();
 DIO=new IntersectionObserver(es=>{es.forEach(e=>{if(!e.isIntersecting)return;const f=e.target;DIO.unobserve(f);
  const st=f.querySelector('.dgm-stage');st.innerHTML='<div class="dgm-load"><span class="spin"></span></div>';
  loadJS('three.min').then(()=>loadJS('diagrams')).then(()=>PMD.mount(f,f.dataset.dgm,S.lang)).catch(()=>{st.innerHTML='<div class="dgm-load">'+T('රූප සටහන පූරණය කළ නොහැකි විය.','Could not load the diagram.')+'</div>'})})},{rootMargin:'120px'});
 figs.forEach(f=>DIO.observe(f));
}
/* ---------- views ---------- */
function curRule(){const h=location.hash.slice(1);return h.startsWith('r-')?h.slice(2):null}
function scr(){return S.lang==='si'?'native':S.script}
function pt(r){return scr()==='roman'?`<div class="ptext rom">${esc(r.ptr)}</div>`:`<div class="ptext">${esc(r.pt)}</div>`}
function tnotes(r){const n=(r.tnotes||[]).filter(x=>S.lang==='si'?x.note:x.note_en);if(!n.length)return'';return '<div class="tnotes">'+n.map(x=>`<div>${x.at&&x.at.length>1?`<b>${esc(x.at)}</b> — `:''}${esc(S.lang==='si'?x.note:x.note_en)}</div>`).join('')+'</div>'}
function vgOf(r){const c=C[r.cat];const v=c.vaggas[r.vg];return v&&v.si?(L(v)):null}
/* ---------- four-tab rule layout: story · padabhājanīya · Kaṅkhāvitaraṇī · 17 aspects ---------- */
const TABS=[['story','book','පෙළ','Pāḷi text'],['att','att','අට්ඨකථාව','Aṭṭha\u00ADkathā'],['kkv','cmt','කඞ්ඛාවිතරණී','Kaṅkhā\u00ADvitaraṇī'],['s17','grid','සප්තදශාකාරය','17 aspects'],['tbl','grid','අධිකරණ හා සමථ','Issues & settlements']];
/* ---------- 中文 (简体) interface dictionary: English → Chinese ---------- */
const ZH={
'17 aspects':'十七相','Issues & settlements':'诤事与灭诤','Acittaka — even without intention':'无心 (acittaka) — 无意亦犯','Action':'业','Addhāna-samuṭṭhāna':'道路等起 (Addhāna)','Adinnādāna-samuṭṭhāna':'不与取等起 (Adinnādāna)','Akiriyā — arises by not doing':'不作 (akiriyā) — 因不作而犯','All':'全部','Ananuññāta-samuṭṭhāna':'未许可等起 (Ananuññāta)','Anāpatti':'Anāpatti','Anāṇattika':'无教令 (anāṇattika)','Anāṇattika — no offence by ordering another':'无教令 (anāṇattika) — 教他人作不犯此罪','Aspect':'相','Aṅga':'Aṅga','Bhikkhu Pātimokkha · 227 training rules':'比丘波提木叉 · 227 条学处','Bhūtārocana-samuṭṭhāna':'说实等起 (Bhūtārocana)','Blame':'罪性','Bodily action':'身业','Bodily and verbal action':'身业、语业','Body':'身','Body+mind':'身+心','Body+speech':'身+语','Body+speech+mind':'身+语+心','Citta':'Citta','Close all':'全部收起','Colour theme':'颜色主题','Command':'教令','Shared (also binds bhikkhunīs)':'共通制 (比丘尼亦同)','Contents':'目录','Continue where you left off':'继续上次浏览的学处','Corīvuṭṭhāpana-samuṭṭhāna':'度贼女等起 (Corīvuṭṭhāpana)','Could not load the data file. Please try again.':'无法载入数据文件，请重试。','Could not load the diagram.':'无法载入示意图。','Cream':'米色','Dark':'深色','Details for this rule have not been added yet.':'此学处的详细内容尚未加入。','Dhammadesanā-samuṭṭhāna':'说法等起 (Dhammadesanā)','Doing':'作','Drag to turn a diagram. Tap the link under each one to open its rule.':'拖动可旋转示意图；点按下方链接可打开相应学处。','Dubbhāsita':'恶说','Dukkaṭa':'突吉罗','Eḷakaloma-samuṭṭhāna':'羊毛等起 (Eḷakaloma)','Factors':'构成支分','Failure':'失坏','Failure in conduct':'行仪失坏','Failure in livelihood':'活命失坏','Failure in view':'见失坏','Failure in virtue':'戒失坏','Failure in virtue or in conduct (by the offence admitted)':'戒失坏或行仪失坏 (依所犯之罪)','Feeling':'受','Forest':'森林','Home':'首页','Illustrations':'示意图','In this rule':'本学处','Intention':'心','Kamma':'Kamma','Kathina-samuṭṭhāna':'迦絺那等起 (Kathina)','Kaṅkhā­vitaraṇī':'疑惑度脱','Key aspects of the seventeen — at a glance':'十七相要点一览','Kind of promulgation':'制定方式','Kiriyā':'Kiriyā','Kiriyā — arises by doing':'作 (kiriyā) — 因作而犯','Kiriyākiriyā — by doing and not doing':'作不作 (kiriyākiriyā) — 因作与不作而犯','Kusalattika':'Kusalattika','Language':'语言','Light blue':'浅蓝','Light yellow':'浅黄','Loading…':'载入中…','Lokavajja — blameworthy by the world':'世间罪 (lokavajja) — 世人亦认为是过失','Lotus':'莲花','Matter':'事由','Meaning':'意义','Mind':'心','Mint':'薄荷','Next':'下一条','Nidāna':'Nidāna','Nissaggiya pācittiya':'尼萨耆波逸提','No results':'没有结果','No-saññāvimokkha — offence even without that perception':'非想解脱 (no-saññāvimokkha) — 即使无此想亦犯','Non-offence':'不犯','Not shared (bhikkhus only)':'不共通制 (仅比丘)','Number':'编号','Ocean':'海洋','Offence':'罪','Offences':'所犯之罪','One promulgation':'一次制定','Open all':'全部展开','Origin':'等起','Origin place':'缘起地点','Origin, doing, intention etc. in one table':'等起、作、心等一表总览','Origination':'等起','Origins (6 and 13)':'等起 (六种与十三种)','Other topics':'其他主题','Padasodhamma-samuṭṭhāna':'句法等起 (Padasodhamma)','Painful':'苦','Painful feeling only':'唯苦受','Paññattividhi':'Paññattividhi','Paṇṇattivajja — blameworthy by the rule only':'制罪 (paṇṇattivajja) — 仅因制戒而成过失','Paṭhamapārājika-samuṭṭhāna':'第一波罗夷等起 (Paṭhamapārājika)','Perception':'想','Person':'人物','Previous':'上一条','Puggala':'Puggala','Pācittiya':'波逸提','Pāli script':'巴利文字','Pāli text':'巴利原文','Pārājika':'波罗夷','Pātimokkha Study':'波提木叉研读','Pāḷi text':'巴利原文','Pāṭidesanīya':'波罗提提舍尼','Roman':'罗马字','Roman script':'罗马字','Rule':'学处','Sacittaka — only with intention':'有心 (sacittaka) — 唯有意时犯','Saffron':'橘黄','Samanta­pāsādikā':'善见律注','Aṭṭha­kathā':'义注','Samanubhāsana-samuṭṭhāna':'随顺劝谏等起 (Samanubhāsana)','Samuṭṭhāna':'Samuṭṭhāna','Sañcaritta-samuṭṭhāna':'媒合等起 (Sañcaritta)','Saññā':'Saññā','Saññāvimokkha — free of offence without perception of transgression':'想解脱 (saññāvimokkha) — 无违犯之想则不犯','Saṅghādisesa':'僧残','Search a rule…':'搜索学处…','Sections of the Pātimokkha':'波提木叉各部','Settings':'设置','Seven classes of offence':'七种罪类','Sinhala':'僧伽罗文','Sinhala script':'僧伽罗文字','Sometimes by doing, sometimes by doing-and-not-doing':'有时因作，有时因作不作','Sometimes by doing, sometimes by not doing':'有时因作，有时因不作','Sources: Dvemātikāpāḷi, Kaṅkhāvitaraṇī commentary, the Vinaya Piṭaka and sub-commentaries':'依据：两部论母巴利、疑惑度脱注、律藏及其复注','Speech':'语','Speech+mind':'语+心','State of mind':'心之三法','Summary table of all 227':'227 条学处总表','Sāṇattika':'有教令 (sāṇattika)','Sāṇattika — offence also by ordering another':'有教令 (sāṇattika) — 教他人作亦犯','Text size':'字体大小','The 17 aspects':'十七相','The 3D diagrams included in the rules — by topic':'学处中的 3D 示意图 — 按主题','The 3D diagrams included in the rules, grouped by topic':'学处中的 3D 示意图，按主题分组','The Bhikkhu Pātimokkha — with the Kaṅkhāvitaraṇī commentary':'比丘波提木叉 — 依疑惑度脱注','The doors by which offences arise, and their groups':'罪由何门生起及其分组','The origin story, explanation of terms, division of offences, non-offences, factors and the seventeen aspects.':'缘起故事、字义解释、罪的分别、不犯、构成支分与十七相。','The script used to show Pāli text.':'显示巴利原文所用的文字。','The seventeen aspects':'十七相','The seventeen ways each rule is analysed':'每条学处的十七种分析','The weight of each offence and its remedy':'各罪的轻重及出罪方法','Theyyasattha-samuṭṭhāna':'贼队等起 (Theyyasattha)','Three':'三','Three feelings — pleasant, painful, neutral':'三受 — 乐、苦、不苦不乐','Thullaccaya':'偷兰遮','Ticitta — wholesome, unwholesome, indeterminate':'三心 — 善、不善、无记','Tip: tap the buttons to open each part of the explanation. Each part opens separately.':'提示：点按按钮可打开各部分解释，每部分单独展开。','Training rule':'学处','Two':'二','Two feelings — pleasant, neutral':'二受 — 乐、不苦不乐','Unwholesome':'不善','Unwholesome mind only (one)':'唯不善心 (一心)','Vajja':'Vajja','Vatthu':'Vatthu','Vedanāttika':'Vedanāttika','Verbal action':'语业','Vipatti':'Vipatti','Wholesome or indeterminate (two)':'善或无记 (二心)','Yo pana bhikkhu… — rule text will look like this.':'Yo pana bhikkhu… — 学处原文将如此显示。','Āpatti':'Āpatti','Āṇatti':'Āṇatti',
'Sections':'各部','rules':'条学处','Rule ':'学处 ','Number ':'编号 '
};
const ZT=e=>S.lang==='zh'?(ZH[e]||e):e;
/* swap the English slot of label tables for Chinese when the language is zh */
function zhify(){
 const sw=(tbl,i)=>{for(const k in tbl){const a=tbl[k];if(!Array.isArray(a))continue;if(a._e===undefined)a._e=a[i];a[i]=S.lang==='zh'?(ZH[a._e]||a._e):a._e}};
 [UI,SIX,SM,KR,SV,CI,VJ,KM,CIT,VED,VP].forEach(t=>sw(t,1));sw(AP,2);sw(ROWS,2);sw(TABS,3);
 if(typeof THEMES!=='undefined')sw(THEMES,2);
}
let TAB='story';
function plfabCheck(){const f=document.querySelector('.plfab');if(!f)return;const b=document.querySelector('.thd .plbtn');const top=(document.querySelector('header.top,.topbar,#top')||{getBoundingClientRect:()=>({bottom:0})}).getBoundingClientRect().bottom;const off=!b||b.getBoundingClientRect().bottom<top+4;f.classList.toggle('show',off)}
addEventListener('scroll',plfabCheck,{passive:true});addEventListener('resize',plfabCheck);
const PV=r=>!!(r&&r.pi);
const plab=()=>S.pali?(S.lang==='si'?'සිංහල':S.lang==='zh'?'中文':'English'):(S.lang==='si'?'පාළි':'Pāḷi');
const pitxt=o=>o?(S.lang==='si'||scr()==='native'?o.si:o.ro):'';
const pih=o=>o?(o[S.lang]||o.en||o.si):'';
const LP=(a,b)=>`<span class="lv">${a}</span><span class="pv">${b}</span>`;
const LPB=(a,b)=>`<div class="lv">${a}</div><div class="pv">${b}</div>`;
function tabView(r,secs,head){
 const grp={};secs.forEach(s=>{(grp[s.g||'kkv']=grp[s.g||'kkv']||[]).push(s)});
 if(r.s17&&r.cat!=='as')grp.s17=[{k:'s17',t:u('s17'),h:(PV(r)&&r.pi17)?LPB(table17(r),pih(r.pi17).replace('<table>','<table class="t17">')):table17(r),ic:IC.grid,solo:1}];
 const tabs=TABS.filter(t=>grp[t[0]]);if(!tabs.length)return'';
 const cur=grp[TAB]?TAB:tabs[0][0];
 let h=(head||'')+`<div class="rtabs" role="tablist" style="--n:${tabs.length}">${tabs.map(t=>`<button role="tab" class="rtab${t[0]===cur?' on':''}" data-tab="${t[0]}" aria-selected="${t[0]===cur}">${IC[t[1]]}<span>${S.lang==='si'?t[2]:t[3]}</span></button>`).join('')}</div>`;
 h+=tabs.map(t=>`<div class="tpanel${t[0]===cur?' on':''}" data-panel="${t[0]}" role="tabpanel">${grp[t[0]].map(s=>s.solo?`<div class="sec open solo">${s.h}</div>`:`<div class="sec" id="${s.k}"><button class="sech" data-sec="${s.k}"><span class="ic">${s.ic||(t[0]==='story'&&/වස්තුව|Matter|Story/.test(s.t)?IC.book:iconFor(s.t))}</span><span class="tt">${s.pt!=null?LP(esc(s.t),esc(s.pt)):esc(s.t)}</span>${IC.chev}</button><div class="secb">${s.ph!=null?LPB(s.h,s.ph):s.h}</div></div>`).join('')}</div>`).join('');
 return h}
function thead(r){const c=C[r.cat],vg=vgOf(r);return `<header class="thd"><div class="num" aria-label="${T('අංකය','Number')} ${r.n}">${r.n}</div><div class="tx"><div class="tcrumb"><a href="#c-${c.id}">${esc(L(c))}</a>${vg?`<span class="dot">·</span><span>${esc(vg)}</span>`:''}<span class="dot">·</span><span>${T('ශික්ෂාපද','Rule')} ${r.g} / 227</span></div><h2>${PV(r)?LP(esc(L(r.title)),esc(pitxt(r.pi))):esc(L(r.title))}</h2></div></header>`}
function viewRule(id){
 const r=R[id];if(!r)return viewHome();
 try{localStorage.setItem('pm-last',id)}catch(e){}
 const c=C[r.cat];const vg=vgOf(r);
 const prev=D.rules[r.i-1],next=D.rules[r.i+1];
 let h=r.tabs?thead(r):`<section class="rhead"><div class="rtop"><div class="num">${r.n}</div><div class="crumb"><a href="#c-${c.id}">${esc(L(c))}</a>${vg?' · '+esc(vg):''}<br>${T('ශික්ෂාපද','Rule')} ${r.g} / 227</div></div>
 <div class="rtag">${esc(scr()==='roman'?r.pnr:r.pn)}</div><h2>${esc(L(r.title))}</h2>
 <div class="pill"><span class="lbl">${u('pali')}</span>${pt(r)}${r.tr?`<div class="trn"><span class="lbl">${u('trans')}</span>${esc(L(r.tr))}${tnotes(r)}</div>`:''}</div></section>`;
 if(r.has&&!LOADED[r.cat]){h+=`<div class="loading" style="margin-top:1rem"><span class="spin"></span>${T('පූරණය වෙමින්…','Loading…')}</div>`;need(r.cat).then(ok=>{if(curRule()!==id)return;if(ok)viewRule(id);else{const l=document.querySelector('.loading');if(l)l.outerHTML=`<div class="missing" style="margin-top:1rem">${T('දත්ත ගොනුව පූරණය කළ නොහැකි විය. නැවත උත්සාහ කරන්න.','Could not load the data file. Please try again.')}</div>`}})}
 else if(!r.secs||!r.secs.length){h+=`<div class="missing" style="margin-top:1rem">${u('nodata')}</div>`}
 else{
  const secs=r.secs.map((s,i)=>({k:'s'+i,t:L(s.t)||s.t.si,h:L(s.h)||s.h.si,g:s.g,pt:PV(r)&&s.pt?pitxt(s.pt):null,ph:PV(r)&&s.ph?pih(s.ph):null}));
  if(secs.some(s=>s.g)){h=tabView(r,secs,thead(r))}else{
  if(r.s17&&r.cat!=='as')secs.push({k:'s17',t:u('s17'),h:table17(r),ic:IC.grid});
  h+=`<div class="chips">${secs.map(s=>`<button class="chip" data-open="${s.k}">${s.ic||iconFor(s.t)}<span>${esc(shortT(s.t))}</span></button>`).join('')}<button class="chip all" data-open="__all">${IC.expand}<span>${u('openAll')}</span></button></div>`;
  h+=secs.map(s=>`<div class="sec" id="${s.k}"><button class="sech" data-sec="${s.k}"><span class="ic">${s.ic||iconFor(s.t)}</span><span class="tt">${esc(s.t)}</span>${IC.chev}</button><div class="secb">${s.h}</div></div>`).join('');}
 }
 h+=`<nav class="pn">${prev?`<a href="#r-${prev.id}"><small>‹ ${u('prev')}</small><b>${esc(L(prev.title))}</b></a>`:'<span class="dis"></span>'}${next?`<a class="nx" href="#r-${next.id}"><small>${u('next')} ›</small><b>${esc(L(next.title))}</b></a>`:'<span class="dis"></span>'}</nav>`;
 if(PV(r)&&r.secs&&r.secs.length)h+=`<button type="button" class="plfab" data-plbtn aria-pressed="${!!S.pali}" aria-label="${S.lang==='si'?'පාළි / සිංහල මාරු කරන්න':'Switch Pāḷi / translation'}">${IC.swap}<span>${plab()}</span></button>`;
 $('#main').innerHTML=h;
 plfabCheck();
 initDiagrams();
}
function shortT(t){return t.replace(/^\([^)]{1,3}\)\s*/,'').replace(/\s*—\s*(කඞ්ඛාවිතරණී අනුව|according to the Kaṅkhāvitaraṇī)$/,'').replace(/\s*\(=.*\)$/,'').slice(0,46)}
$('#main').addEventListener('click',e=>{
 const pb=e.target.closest('[data-plbtn]');if(pb){const tb=(document.querySelector('.rtabs')||document.querySelector('#top')).getBoundingClientRect().bottom;const an=[...document.querySelectorAll('.tpanel.on .sec')].find(x=>x.getBoundingClientRect().bottom>tb+8);const t0=an?an.getBoundingClientRect().top:0;S.pali=!S.pali;save();document.documentElement.dataset.pali=S.pali?'1':'';document.querySelectorAll('[data-plbtn]').forEach(b=>{b.setAttribute('aria-pressed',S.pali);b.querySelector('span').textContent=plab()});if(an&&pb.classList.contains('plfab')){const t1=an.getBoundingClientRect().top;scrollBy(0,t0<tb?t1-tb-6:t1-t0)}plfabCheck();return}
 const slb=e.target.closest('[data-sl]');if(slb){S.story=slb.dataset.sl;save();document.documentElement.dataset.story=S.story;return}
 const tb=e.target.closest('[data-tab]');
 if(tb){TAB=tb.dataset.tab;document.querySelectorAll('.rtab').forEach(b=>{const on=b===tb;b.classList.toggle('on',on);b.setAttribute('aria-selected',on)});document.querySelectorAll('.tpanel').forEach(p=>p.classList.toggle('on',p.dataset.panel===TAB));
  const bar=document.querySelector('.rtabs');if(bar&&bar.getBoundingClientRect().top<0)bar.scrollIntoView({block:'start'});tb.scrollIntoView({inline:'nearest',block:'nearest'});initDiagrams();return}
 const pa=e.target.closest('[data-pall]');
 if(pa){const p=pa.closest('.tpanel');const ss=[...p.querySelectorAll('.sec:not(.solo)')];const any=ss.some(x=>!x.classList.contains('open'));ss.forEach(x=>x.classList.toggle('open',any));pa.querySelector('span').textContent=any?u('closeAll'):u('openAll');return}
 const ch=e.target.closest('[data-open]');
 if(ch){const k=ch.dataset.open;
  if(k==='__all'){const secs=[...document.querySelectorAll('.sec')];const any=secs.some(s=>!s.classList.contains('open'));secs.forEach(s=>s.classList.toggle('open',any));document.querySelectorAll('.chip[data-open]').forEach(c=>{if(c.dataset.open!=='__all')c.classList.toggle('on',any)});ch.querySelector('span').textContent=any?u('closeAll'):u('openAll');return}
  const s=document.getElementById(k);const wasOpen=s.classList.contains('open');s.classList.toggle('open',!wasOpen);ch.classList.toggle('on',!wasOpen);if(!wasOpen)s.scrollIntoView({behavior:'smooth',block:'start'});return}
 const sh=e.target.closest('[data-sec]');
 if(sh){const s=sh.parentElement;s.classList.toggle('open');const tp=s.closest('.tpanel');if(tp){const b=tp.querySelector('[data-pall] span');if(b){const any=[...tp.querySelectorAll('.sec:not(.solo)')].some(x=>!x.classList.contains('open'));b.textContent=any?u('openAll'):u('closeAll')}}const c=document.querySelector(`.chip[data-open="${s.id}"]`);if(c)c.classList.toggle('on',s.classList.contains('open'))}
 const f=e.target.closest('[data-filter]');
 if(f){allFilter=f.dataset.filter;viewAll()}
});
function catCard(c){const n=c.vaggas.reduce((a,v)=>a+v.ids.length,0);return `<a class="ccard" href="#c-${c.id}" style="--cc:${CATCOL[c.id]}"><div class="row"><div class="big">${n}</div><div><h3>${esc(L(c))}</h3><small>${esc((S.lang==='si'?c.sub_si:(S.lang==='zh'&&c.sub_zh)||c.sub_en))}</small>${S.lang==='si'?`<span class="pe">${esc(c.en)}</span>`:''}</div></div></a>`}
function viewHome(){
 let last=null;try{last=localStorage.getItem('pm-last')}catch(e){}
 let h=`<header class="hero"><h1>${u('app')}</h1><p class="sub">${T('භික්ඛු පාතිමොක්ඛය — කඞ්ඛාවිතරණී අට්ඨකථාව ඇසුරින්','The Bhikkhu Pātimokkha — with the Kaṅkhāvitaraṇī commentary')}</p><p class="lede">${T('කථා වස්තුව, පද විවරණය, ආපත්ති භේදය, අනාපත්ති, අංග හා සප්තදශාකාරය.','The origin story, explanation of terms, division of offences, non-offences, factors and the seventeen aspects.')}</p><div class="stats">${D.cats.map(c=>`<span>${esc(L(c))} ${c.vaggas.reduce((a,v)=>a+v.ids.length,0)}</span>`).join('')}</div></header>`;
 if(last&&R[last])h+=`<div class="note">${u('cont')}: <a href="#r-${last}"><b>${esc(L(R[last].title))}</b></a> <span class="mini">(${esc(L(C[R[last].cat]))} ${R[last].n})</span></div>`;
 h+=`<div class="h"><b>≡</b><span>${u('cats')}</span></div><div class="grid">${D.cats.map(catCard).join('')}</div>`;
 h+=`<div class="h"><b>+</b><span>${u('others')}</span></div><div class="grid">
 <a class="ccard" href="#ref-17"><div class="row"><div class="big">17</div><div><h3>${u('r17')}</h3><small>${T('එක් එක් ශික්ෂාපදය විග්‍රහ කරන ආකාර දාහත','The seventeen ways each rule is analysed')}</small></div></div></a>
 <a class="ccard" href="#ref-samu"><div class="row"><div class="big">13</div><div><h3>${u('rsamu')}</h3><small>${T('ඇවැත් හටගන්නා ද්වාර හා ඒවායේ කාණ්ඩ','The doors by which offences arise, and their groups')}</small></div></div></a>
 <a class="ccard" href="#ref-apatti"><div class="row"><div class="big">7</div><div><h3>${u('rap')}</h3><small>${T('ඇවැත්වල බරපතලකම හා පිළියම්','The weight of each offence and its remedy')}</small></div></div></a>
 <a class="ccard" href="#all"><div class="row"><div class="big">227</div><div><h3>${u('rall')}</h3><small>${T('සමුට්ඨාන, ක්‍රියා, චිත්ත ආදිය එක් වගුවකින්','Origin, doing, intention etc. in one table')}</small></div></div></a>
 <a class="ccard" href="#figs"><div class="row"><div class="big">${(D.figs||[]).reduce((a,g)=>a+g.figs.length,0)}</div><div><h3>${u('figs')}</h3><small>${T('ශික්ෂාපදවලට ඇතුළත් කළ ත්‍රිමාණ රූප සටහන්, මාතෘකා අනුව','The 3D diagrams included in the rules, grouped by topic')}</small></div></div></a></div>`;
 h+=`<div class="note">${u('tip')}</div><div class="foot">${T('මූලාශ්‍ර: ද්වෙමාතිකාපාළි, කඞ්ඛාවිතරණී අට්ඨකථාව, විනය පිටකය හා ටීකා','Sources: Dvemātikāpāḷi, Kaṅkhāvitaraṇī commentary, the Vinaya Piṭaka and sub-commentaries')}</div>`;
 $('#main').innerHTML=h;
}
function viewCat(id){
 const c=C[id];if(!c)return viewHome();
 const n=c.vaggas.reduce((a,v)=>a+v.ids.length,0);
 let h=`<header class="hero"><h1>${esc(L(c))}</h1><p class="sub">${esc((S.lang==='si'?c.sub_si:(S.lang==='zh'&&c.sub_zh)||c.sub_en))}</p>${S.lang==='si'?`<p class="lede">${esc(c.en)}</p>`:''}</header>`;
 c.vaggas.forEach((v,vi)=>{
  if(v.si)h+=`<div class="h"><b>${vi+1}</b><span>${esc(L(v))}</span></div>`;else h+='<div style="height:1rem"></div>';
  h+='<div class="rlist">'+v.ids.map(id=>{const r=R[id];return `<a class="ritem" href="#r-${id}"><span class="rn">${r.n}</span><span class="rt"><b>${esc(L(r.title))}</b><small>${esc(scr()==='roman'?r.pnr:r.pn)}</small></span><span class="go">›</span></a>`}).join('')+'</div>';
 });
 $('#main').innerHTML=h;
}
let allFilter='all';
function viewAll(){
 const si=S.lang==='si';
 let h=`<header class="hero"><h1>${u('rall')}</h1><p class="sub">${T('සප්තදශාකාරයේ ප්‍රධාන ආකාර — එක් බැල්මෙන්','Key aspects of the seventeen — at a glance')}</p></header>`;
 h+=`<div class="toolbar"><button class="fbtn ${allFilter==='all'?'on':''}" data-filter="all">${u('all')}</button>${D.cats.map(c=>`<button class="fbtn ${allFilter===c.id?'on':''}" data-filter="${c.id}">${esc(L(c))}</button>`).join('')}</div>`;
 const rows=D.rules.filter(r=>r.cat!=='as'&&(allFilter==='all'||r.cat===allFilter));
 const sh=(m,k)=>m[k]?(si?m[k][0]:m[k][1]).split(' — ')[0]:'—';
 h+='<div class="scroll"><table class="alltab"><tr><th>#</th><th>'+(si?'ශික්ෂාපදය':ZT('Rule'))+'</th><th>'+(si?'ආපත්ති':ZT('Offence'))+'</th><th>'+(si?'සමුට්ඨාන':ZT('Origin'))+'</th><th>'+(si?'ක්‍රියා':ZT('Doing'))+'</th><th>'+(si?'සංඥා':ZT('Perception'))+'</th><th>'+(si?'චිත්ත':ZT('Intention'))+'</th><th>'+(si?'වජ්ජ':ZT('Blame'))+'</th><th>'+(si?'කර්ම':ZT('Action'))+'</th><th>'+(si?'චිත්ත ත්‍රික':ZT('Mind'))+'</th><th>'+(si?'වේදනා':ZT('Feeling'))+'</th><th>'+(si?'ආණත්ති':ZT('Command'))+'</th></tr>'+rows.map(r=>{const s=r.s17||{};return `<tr><td>${r.g}</td><td><a href="#r-${r.id}">${esc(L(r.title))}</a></td><td>${(s.ap||[]).slice(0,1).map(tag).join('')}</td><td>${SM[s.sm]?(si?SM[s.sm][0]:SM[s.sm][1]).replace(/ සමුට්ඨාන|-samuṭṭhāna/,''):'—'}</td><td>${sh(KR,s.kr)}</td><td>${sh(SV,s.sv)}</td><td>${sh(CI,s.ci)}</td><td>${sh(VJ,s.vj)}</td><td>${sh(KM,s.km)}</td><td>${s.cit?{A:si?'අකුසල':ZT('Unwholesome'),'2':si?'ද්විචිත්ත':ZT('Two'),'3':si?'තිචිත්ත':ZT('Three')}[s.cit]:'—'}</td><td>${s.ved?{D:si?'දුක්ඛ':ZT('Painful'),'2':si?'ද්විවේදන':ZT('Two'),'3':si?'තිවේදන':ZT('Three')}[s.ved]:'—'}</td><td>${s.an?(s.an==='s'?(si?'සාණත්තික':ZT('Sāṇattika')):(si?'අනාණත්තික':ZT('Anāṇattika'))):'—'}</td></tr>`}).join('')+'</table></div>';
 $('#main').innerHTML=h;
}
function viewFigs(){
 const si=S.lang==='si',G=D.figs||[];
 let h=`<header class="hero"><h1>${u('figs')}</h1><p class="sub">${T('ශික්ෂාපදවලට ඇතුළත් කළ ත්‍රිමාණ රූප සටහන් — මාතෘකා අනුව','The 3D diagrams included in the rules — by topic')}</p><p class="lede">${T('ඇඟිල්ලෙන් ඇදීමෙන් කරකැවිය හැකිය. එක් එක් රූපය අයත් ශික්ෂාපදයට යාමට පහත සබැඳිය ඔබන්න.','Drag to turn a diagram. Tap the link under each one to open its rule.')}</p></header>`;
 h+='<nav class="fignav">'+G.map((g,i)=>`<a href="#figs" data-fg="${g.id}"><b>${i+1}</b>${esc(si?g.si:(S.lang==='zh'&&g.zh)||g.en)} <span>${g.figs.length}</span></a>`).join('')+'</nav>';
 G.forEach((g,i)=>{
  h+=`<div class="h" id="fg-${g.id}"><b>${i+1}</b><span>${esc(si?g.si:(S.lang==='zh'&&g.zh)||g.en)}</span></div>`;
  const d=si?g.dsi:(S.lang==='zh'&&g.dzh)||g.den;if(d)h+=`<p class="figdesc">${esc(d)}</p>`;
  h+='<div class="figgrid">'+g.figs.map(f=>`<figure class="dgm" data-dgm="${f.d}"><div class="dgm-stage"></div><figcaption>${si?(f.si||f.en):(f.en||f.si)}<div class="figrules">${f.rules.filter(id=>R[id]).map(id=>{const r=R[id];return `<a href="#r-${id}">${esc(L(C[r.cat]))} ${r.n} — ${esc(L(r.title))} ›</a>`}).join('')}</div></figcaption></figure>`).join('')+'</div>';
 });
 $('#main').innerHTML=h;
 $('#main').querySelectorAll('[data-fg]').forEach(x=>x.onclick=e=>{e.preventDefault();const t=document.getElementById('fg-'+x.dataset.fg);if(t)window.scrollTo({top:t.getBoundingClientRect().top+scrollY-(parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--hh'))||60)-10,behavior:'smooth'})});
 initDiagrams();
}
const REF17=[
 ['නිදානය','Nidāna','ශික්ෂාපදය පැනවූ ස්ථානය. සියලු ශික්ෂාපද පැනවූයේ වේසාලි, රාජගහ, සාවත්ථි, ආළවි, කොසම්බි, සක්ක (ශාක්‍ය ජනපදය) හා භග්ග යන ස්ථාන සතෙහි ය.','The place where the rule was laid down. All rules were laid down in one of seven places: Vesālī, Rājagaha, Sāvatthī, Āḷavī, Kosambī, the Sakyan country and the Bhagga country.'],
 ['පුද්ගලයා','Puggala','යම් භික්ෂුවක් හෝ භික්ෂු පිරිසක් අරබයා ශික්ෂාපදය පැනවී ද, ඒ පුද්ගලයා (ආදිකම්මිකයා).','The person (or group) because of whom the rule was laid down — the first offender.'],
 ['වස්තුව','Vatthu','ඒ පුද්ගලයා කළ අජ්ඣාචාරය — එනම් ශික්ෂාපදය පැනවීමට හේතු වූ ක්‍රියාව.','The misconduct of that person — the act that led to the rule being laid down.'],
 ['ප්‍රඥප්ති විධිය','Paññattividhi','ප්‍රඥප්ති, අනුප්‍රඥප්ති, අනුප්පන්න ප්‍රඥප්ති, සබ්බත්ථ/පදේස ප්‍රඥප්ති, සාධාරණ/අසාධාරණ ප්‍රඥප්ති, එකතෝ/උභතෝ ප්‍රඥප්ති යනුවෙන් නව ආකාරයකි. ප්‍රායෝගිකව බලනුයේ අනුප්‍රඥප්ති ඇති නැති බව හා සාධාරණ (භික්ෂුණීන්ට ද පොදු) ද අසාධාරණ ද යන්නයි.','Nine kinds: the basic rule, supplementary rules, rules laid down before the fault arose, rules for everywhere or for some regions, rules common or not common to nuns, and rules for one or both Saṅghas. In practice we note whether there are supplementary rules and whether the rule is common to nuns.'],
 ['ආණත්තිය','Āṇatti','අනුන්ට අණ කොට කරවීමෙන් ද ඇවැත් වේ නම් සාණත්තික ය; තමා ම කළහොත් පමණක් ඇවැත් වේ නම් අනාණත්තික ය.','If the offence also arises by ordering someone else to do the act, the rule is sāṇattika; if only by doing it oneself, anāṇattika.'],
 ['ආපත්තිය','Āpatti','පූර්ව ප්‍රයෝග ආදිය අනුව එම ශික්ෂාපදය යටතේ ලැබෙන ඇවැත් වර්ග (පාරාජික, ථුල්ලච්චය, පාචිත්තිය, දුක්කට ආදිය).','The classes of offence that arise under the rule, according to the preliminary effort and so on (pārājika, thullaccaya, pācittiya, dukkaṭa, etc.).'],
 ['අනාපත්තිය','Anāpatti','නොදැනීම, නොසිතීම, උමතු බව, ආදිකම්මික බව වැනි ඇවැත් නොවන අවස්ථා.','The cases where there is no offence — not knowing, not intending, insanity, being the first offender and so on.'],
 ['විපත්තිය','Vipatti','සීල විපත්ති, ආචාර විපත්ති, දිට්ඨි විපත්ති, ආජීව විපත්ති යන සතරින් කුමක් ද යන්න. පාරාජික හා සංඝාදිසේස සීල විපත්තියට ද, සෙසු ඇවැත් ආචාර විපත්තියට ද අයත් ය.','Which of the four failures it belongs to: virtue, conduct, view or livelihood. Pārājika and saṅghādisesa are failures in virtue; the rest are failures in conduct.'],
 ['අංග','Aṅga','ඇවැත සම්පූර්ණ වීමට අවශ්‍ය කරුණු. සියලු අංග සම්පූර්ණ වූ විට පමණක් ප්‍රධාන ඇවැත වේ.','The factors that must all be present for the full offence.'],
 ['සමුට්ඨානය','Samuṭṭhāna','ඇවැත හටගන්නා ද්වාර: කාය, වාචා, කාය-වාචා, කාය-චිත්ත, වාචා-චිත්ත, කාය-වාචා-චිත්ත යන සය. මේවායේ සංයෝග අනුව සමුට්ඨාන කාණ්ඩ දහතුනකි.','The doors by which an offence arises: body; speech; body+speech; body+mind; speech+mind; body+speech+mind. Their combinations form thirteen groups.'],
 ['ක්‍රියාව','Kiriyā','කිරීමෙන් (කිරියා), නොකිරීමෙන් (අකිරියා), කිරීමෙන් හා නොකිරීමෙන් (කිරියාකිරියා), සමහර විට කිරීමෙන් සමහර විට නොකිරීමෙන් ආදී වශයෙන් පස් ආකාරයකි.','Five kinds: arising by doing, by not doing, by doing and not doing together, sometimes by doing and sometimes by not doing, and sometimes by doing and sometimes by doing-and-not-doing.'],
 ['සංඥාව','Saññā','වීතික්කම සංඥාව නැති විට ඇවැතින් මිදේ නම් සඤ්ඤාවිමොක්ඛ ය; එසේ නොමිදේ නම් නොසඤ්ඤාවිමොක්ඛ ය.','If one is freed from the offence when there is no perception of transgression, it is saññāvimokkha; otherwise no-saññāvimokkha.'],
 ['චිත්තය','Citta','සිතක් සහිතව පමණක් හටගන්නා ඇවැත් සචිත්තක ය; සිතක් නැතිව ද හටගන්නා ඇවැත් අචිත්තක ය.','Offences arising only with intention are sacittaka; those which can arise without it are acittaka.'],
 ['වජ්ජය','Vajja','සචිත්තක පක්ෂයේ සිත අකුසල ම නම් ලෝකවජ්ජ ය; සෙස්ස පණ්ණත්තිවජ්ජ ය.','If, when committed with intention, the mind is always unwholesome, it is lokavajja (blamable by the world); otherwise paṇṇattivajja (blamable by the rule).'],
 ['කර්මය','Kamma','කාය ද්වාරයෙන් ද, වචී ද්වාරයෙන් ද, දෙකෙන් ම ද ඇවැත් වේ ද යන්න. මනෝ ද්වාරයෙන් ඇවැත් නොවේ.','Whether the offence is a bodily action, a verbal action, or both. There is no offence by mind alone.'],
 ['කුසල ත්‍රිකය','Kusalattika','ඇවැතට පත් වන සිත අකුසල පමණක් ද, කුසල-අබ්‍යාකත ද, තුනම (තිචිත්ත) ද යන්න.','Whether the mind at the time of the offence is only unwholesome, wholesome or indeterminate, or any of the three.'],
 ['වේදනා ත්‍රිකය','Vedanāttika','දුක්ඛ වේදනාව පමණක් ද, සුඛ-උපේක්ෂා (ද්විවේදන) ද, තුනම (තිවේදන) ද යන්න.','Whether the feeling is only painful, pleasant or neutral (two), or any of the three.']
];
const APC=[
 ['PR','පාරාජික','Pārājika','පරාජයට පත් කරවයි; භික්ෂු භාවය අහිමි වේ. පිළියමක් නැත — නැවත මේ ආත්මයේ උපසම්පදාව නොලැබේ.','Entails defeat: one is no longer a monk. There is no remedy; one cannot be re-ordained in this life.'],
 ['SD','සංඝාදිසේස','Saṅghādisesa','මානත්ත, පරිවාස, අබ්භාන යන කර්මවලදී මුල සිට අවසානය දක්වා සංඝයා අවශ්‍ය වේ. බරපතල (ගරුක) ඇවතකි.','A heavy offence: the Saṅgha is needed at the beginning and end of the rehabilitation (parivāsa, mānatta, abbhāna).'],
 ['TH','ථුල්ලච්චය','Thullaccaya','බරපතල ඇවතකි; පාරාජික හෝ සංඝාදිසේසයට ආසන්න ප්‍රයෝග ආදියෙහි වේ. භික්ෂුවක් ඉදිරියේ දේශනා කළ යුතුය.','A grave offence, usually an attempt at a pārājika or saṅghādisesa. It is confessed to another monk.'],
 ['NP','නිස්සග්ගිය පාචිත්තිය','Nissaggiya pācittiya','අකැප ලෙස ලද වස්තුව සංඝයාට, ගණයට හෝ පුද්ගලයෙකුට අත්හැර (නිස්සජ්ජනය කොට), පසුව ඇවත දේශනා කළ යුතුය.','The item must first be forfeited to the Saṅgha, a group or an individual, then the offence is confessed.'],
 ['PC','පාචිත්තිය','Pācittiya','කුසලය නසන ඇවතකි; භික්ෂුවක් ඉදිරියේ දේශනා කිරීමෙන් පිරිසිදු වේ.','An offence that burns up wholesome states; cleared by confessing it to another monk.'],
 ['PD','පාටිදේසනීය','Pāṭidesanīya','"ගාරය්හං ආවුසෝ ධම්මං ආපජ්ජිං…" ආදී විශේෂ වාක්‍යයෙන් ප්‍රතිදේශනය කළ යුතු ඇවතකි.','Acknowledged with the special formula, “I have fallen into a blameworthy, unsuitable thing that should be acknowledged…”.'],
 ['DK','දුක්කට','Dukkaṭa','නරක ලෙස කළ දෙය; සැහැල්ලු ඇවතකි. සේඛිය ශික්ෂාපද කඩ කිරීම ද මීට අයත් ය.','Wrong-doing; a light offence. Breaking a sekhiya rule falls here.'],
 ['DB','දුබ්භාසිත','Dubbhāsita','නරක ලෙස කීම; ඔමසවාද ආදියෙහි සමහර අවස්ථාවල ලැබෙන ඉතා සැහැල්ලු වචී ඇවතකි.','Wrong speech; a very light verbal offence found in cases such as the abuse rule.']
];
function viewRef(k){
 const si=S.lang==='si';let h='';
 if(k==='17'){
  h=`<header class="hero"><h1>${u('r17')}</h1><p class="sub">${T('ලක්ඛණං සත්තරසධා — කඞ්ඛාවිතරණී','Lakkhaṇaṃ sattarasadhā — Kaṅkhāvitaraṇī')}</p><p class="lede">${T('කඞ්ඛාවිතරණී අට්ඨකථාව එක් එක් ශික්ෂාපදය නිදානයේ සිට වේදනා ත්‍රිකය දක්වා ආකාර දාහතකින් විග්‍රහ කරයි. සෑම ශික්ෂාපදයකම "සප්තදශාකාරය" බොත්තම මඟින් මෙම වගුව බලාගත හැක.','The Kaṅkhāvitaraṇī analyses every rule in seventeen ways, from the place of origin to the triad of feeling. Each rule page has a “17 aspects” button showing this table for that rule.')}</p></header>`;
  h+=`<div class="note"><span class="pali" style="display:block;margin:0;border:0;background:none;padding:0">නිදානං පුග්ගලං වත්ථුං, පඤ්ඤත්තිවිධිමෙව ච;<br>ආණත්තාපත්තිනාපත්ති, විපත්තිඤ්චඞ්ගමෙව ච…</span></div>`;
  h+='<div class="scroll"><table class="t17"><tr><th>#</th><th>'+(si?'ආකාරය':'Aspect')+'</th><th>'+(si?'විස්තරය':'Explanation')+'</th></tr>'+REF17.map((x,i)=>`<tr><td>${i+1}</td><td>${si?x[0]:ROWS[i][2]+`<small>${x[1]}</small>`}</td><td>${si?x[2]:x[3]}</td></tr>`).join('')+'</table></div>';
 } else if(k==='samu'){
  const cnt={};D.rules.forEach(r=>{const s=r.s17&&r.s17.sm;if(s)cnt[s]=(cnt[s]||0)+1});
  h=`<header class="hero"><h1>${u('rsamu')}</h1><p class="sub">${T('ඇවැත් හටගන්නා ආකාරය','How offences originate')}</p></header>`;
  h+=`<div class="h"><b>6</b><span>${T('සමුට්ඨාන සය','The six origins')}</span></div><div class="scroll"><table><tr><th>#</th><th>${T('සමුට්ඨානය','Origin')}</th><th>${T('සිත','Mind')}</th></tr>${SIX.map((x,i)=>`<tr><td>${i+1}</td><td><b>${si?x[0]:x[1]}</b></td><td>${i<3?T('අචිත්තක','Without mind'):T('සචිත්තක','With mind')}</td></tr>`).join('')}</table></div>`;
  h+=`<p class="mini">${T('පළමු තුන අචිත්තක ය; පසු තුන සචිත්තක ය. ඇවැත් එකකින්, දෙකකින්, තුනකින්, සතරකින් හෝ සයෙන් ම හටගනී; පහකින් හටගන්නා ඇවැත් නැත.','The first three are without mind, the last three with mind. Offences arise from one, two, three, four or all six; none arises from exactly five.')}</p>`;
  h+=`<div class="h"><b>13</b><span>${T('සමුට්ඨාන ශීර්ෂ දහතුන','The thirteen origin-groups')}</span></div><div class="scroll"><table><tr><th>#</th><th>${T('කාණ්ඩය','Group')}</th><th>${T('සමුට්ඨාන','Origins')}</th><th>${T('ශික්ෂාපද','Rules')}</th></tr>${Object.keys(SM).map((k2,i)=>`<tr><td>${i+1}</td><td><b>${si?SM[k2][0]:SM[k2][1]}</b></td><td>${sixGrid(k2)}</td><td>${cnt[k2]||0}</td></tr>`).join('')}</table></div>`;
 } else if(k==='apatti'){
  h=`<header class="hero"><h1>${u('rap')}</h1><p class="sub">${T('සත්ත ආපත්තික්ඛන්ධා','Satta āpattikkhandhā')}</p></header>`;
  h+='<div class="scroll"><table><tr><th>'+T('ඇවැත','Offence')+'</th><th>'+T('ස්වභාවය හා පිළියම','Nature and remedy')+'</th></tr>'+APC.map(x=>`<tr><td>${tag(x[0])}</td><td>${si?x[3]:x[4]}</td></tr>`).join('')+'</table></div>';
  h+=`<div class="note">${T('<b>ගරුකාපත්ති</b> — පාරාජික හා සංඝාදිසේස. <b>ලහුකාපත්ති</b> — සෙසු ඇවැත් පස. ථුල්ලච්චය හා දුබ්භාසිත පාතිමොක්ඛයේ ශික්ෂාපද වශයෙන් නොව, විභංගයේ දැක්වෙන ඇවැත් ය.','<b>Heavy offences</b> — pārājika and saṅghādisesa. <b>Light offences</b> — the other five. Thullaccaya and dubbhāsita are not rules of the Pātimokkha; they appear in the analysis (vibhaṅga).')}</div>`;
 } else return viewHome();
 $('#main').innerHTML=h;
}

function route(keep){
 if(window.PMD)PMD.disposeAll();
 const h=location.hash.slice(1)||'home';
 if(h.startsWith('r-'))viewRule(h.slice(2));
 else if(h.startsWith('c-'))viewCat(h.slice(2));
 else if(h==='all')viewAll();
 else if(h==='figs')viewFigs();
 else if(h.startsWith('ref-')&&typeof viewRef==='function')viewRef(h.slice(4));
 else viewHome();
 const r=R[curRule()];if(r){openCats.add(r.cat);if(C[r.cat].vaggas[r.vg].si)openVg.add(r.cat+'-'+r.vg)}
 buildTree();
 if(!keep)window.scrollTo(0,0);
 const cur=document.querySelector('.trule.cur');if(cur&&isPinned())cur.scrollIntoView({block:'nearest'});
}
addEventListener('hashchange',()=>route(false));

try{if(localStorage.getItem('pm-pin')!=='0')document.body.classList.add('pin')}catch(e){document.body.classList.add('pin')}
apply(false);route(false);
/* fetch the remaining category files quietly in the background */
(function(){const ids=D.cats.map(c=>c.id);let i=0;const nx=()=>{if(i>=ids.length)return;const c=ids[i++];need(c).then(()=>setTimeout(nx,60))};setTimeout(nx,900)})();
