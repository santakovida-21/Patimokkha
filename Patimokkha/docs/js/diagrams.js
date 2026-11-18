/* Pātimokkha Study — cartoon 3D diagrams (three.js r129, global THREE)
   Units: 1 = one ratana / hattha (cubit, ≈ 46 cm). A standing person is ≈ 3.8 units tall.
   PMD.mount(figureEl, id, lang) builds a small interactive scene; drag to turn it. */
(function(){
const T=window.THREE;
const C={skin:0xE9B48A,robe:0xE57B17,robeD:0xB95A0A,shirt:0xF3F1EA,pants:0x34405A,saree:0x7D4FA5,hair:0x2A2018,
 wood:0xA8703F,woodD:0x7A4E28,ground:0xDCE8C8,mat:0xC9A36A,leaf:0x4E9A3A,trunk:0x8C6A45,wall:0xE9C9A0,roof:0xB0452F,
 line:0xD7263D,ok:0x1F9D55,bad:0xD7263D,bowl:0x6B4A2E};
let GRAD=null;
function grad(){if(GRAD)return GRAD;const d=new Uint8Array([90,170,255]);GRAD=new T.DataTexture(d,3,1,T.LuminanceFormat);GRAD.minFilter=GRAD.magFilter=T.NearestFilter;GRAD.needsUpdate=true;return GRAD}
const MATS={};
function mat(c){return MATS[c]||(MATS[c]=new T.MeshToonMaterial({color:c,gradientMap:grad()}))}
const OUT=new T.MeshBasicMaterial({color:0x1d1a17,side:T.BackSide});
const EDGE=new T.LineBasicMaterial({color:0x1d1a17});
function mesh(geo,c,outline=true){const m=new T.Mesh(geo,mat(c));if(outline){if(geo.type==='BoxGeometry'){m.add(new T.LineSegments(new T.EdgesGeometry(geo),EDGE))}else{const o=new T.Mesh(geo,OUT);o.scale.setScalar(1.06);m.add(o)}}return m}
function limb(len,r,c){ // cylinder hanging down from origin, rounded ends
 const g=new T.Group();const cyl=mesh(new T.CylinderGeometry(r,r*0.92,len,14),c);cyl.position.y=-len/2;g.add(cyl);
 const s=mesh(new T.SphereGeometry(r,14,10),c,false);g.add(s);const e=mesh(new T.SphereGeometry(r*0.92,14,10),c,false);e.position.y=-len;g.add(e);return g}
function box(w,h,d,c,ol=true){return mesh(new T.BoxGeometry(w,h,d),c,ol)}
const deg=a=>a*Math.PI/180;

/* ---------- people ---------- */
const D={thigh:0.95,shin:0.92,torso:1.2,ua:0.68,fa:0.62,headR:0.3,foot:0.12};
function person(kind){
 const col=kind==='monk'?{t:C.robe,ul:C.robe,ur:C.skin,fa:C.skin,leg:C.robe,shin:C.robeD}:
           kind==='woman'?{t:C.saree,ul:C.saree,ur:C.saree,fa:C.skin,leg:C.saree,shin:C.saree}:
           {t:C.shirt,ul:C.shirt,ur:C.shirt,fa:C.skin,leg:C.pants,shin:C.pants};
 const root=new T.Group();const J={root};
 const torsoP=new T.Group();root.add(torsoP);J.torso=torsoP;
 const tor=mesh(new T.CylinderGeometry(0.36,0.33,D.torso,16),col.t);tor.position.y=D.torso/2;torsoP.add(tor);
 const hips=mesh(new T.SphereGeometry(0.34,16,10),col.leg,false);hips.scale.y=0.6;root.add(hips);
 if(kind==='monk'){const sash=mesh(new T.CylinderGeometry(0.375,0.375,0.16,16,1,true),C.robeD,false);sash.position.y=D.torso*0.55;sash.rotation.z=deg(28);torsoP.add(sash)}
 const neck=mesh(new T.CylinderGeometry(0.11,0.12,0.2,10),C.skin,false);neck.position.y=D.torso+0.08;torsoP.add(neck);
 const headP=new T.Group();headP.position.y=D.torso+0.18+D.headR;torsoP.add(headP);J.head=headP;
 const head=mesh(new T.SphereGeometry(D.headR,20,16),C.skin);headP.add(head);J.headMesh=head;
 if(kind!=='monk'){const hair=mesh(new T.SphereGeometry(D.headR*1.04,20,12,0,Math.PI*2,0,Math.PI*0.55),C.hair,false);hair.rotation.x=deg(-18);headP.add(hair);
  if(kind==='woman'){const bun=mesh(new T.SphereGeometry(0.14,12,10),C.hair,false);bun.position.set(0,0.05,-0.3);headP.add(bun)}}
 for(const s of [-1,1]){const e=mesh(new T.SphereGeometry(0.035,8,6),0x222222,false);e.position.set(s*0.1,0.05,D.headR*0.93);headP.add(e)}
 const nose=mesh(new T.SphereGeometry(0.05,8,6),C.skin,false);nose.position.set(0,-0.02,D.headR);headP.add(nose);
 for(const s of [-1,1]){ // arms
  const sh=new T.Group();sh.position.set(s*0.45,D.torso-0.12,0);torsoP.add(sh);
  const u=limb(D.ua,0.12,s>0?col.ur:col.ul);sh.add(u);
  const el=new T.Group();el.position.y=-D.ua;sh.add(el);const f=limb(D.fa,0.105,col.fa);el.add(f);
  const hand=mesh(new T.SphereGeometry(0.13,12,8),C.skin,false);hand.position.y=-D.fa-0.08;el.add(hand);
  J[s>0?'shR':'shL']=sh;J[s>0?'elR':'elL']=el;J[s>0?'handR':'handL']=hand;}
 for(const s of [-1,1]){ // legs
  const hp=new T.Group();hp.position.set(s*0.18,0,0);root.add(hp);
  const th=limb(D.thigh,0.17,col.leg);hp.add(th);
  const kn=new T.Group();kn.position.y=-D.thigh;hp.add(kn);const sn=limb(D.shin,0.14,col.shin);kn.add(sn);
  const ft=box(0.22,D.foot*2,0.42,kind==='monk'?C.skin:(kind==='woman'?C.skin:0x2b2b2b));ft.position.set(0,-D.shin-0.06,0.1);kn.add(ft);
  J[s>0?'hipR':'hipL']=hp;J[s>0?'kneeR':'kneeL']=kn;J[s>0?'footR':'footL']=ft;}
 if(kind==='woman'){const sk=mesh(new T.CylinderGeometry(0.36,0.62,D.thigh+D.shin*0.9,18,1,true),C.saree);sk.material=sk.material.clone();sk.material.side=T.DoubleSide;sk.position.y=-(D.thigh+D.shin*0.9)/2;root.add(sk);J.skirt=sk}
 if(kind==='monk'){const sk=mesh(new T.CylinderGeometry(0.37,0.5,D.thigh*0.9,18,1,true),C.robe);sk.material=sk.material.clone();sk.material.side=T.DoubleSide;sk.position.y=-D.thigh*0.45;root.add(sk);J.skirt=sk}
 root.userData.J=J;return root}
function pose(p,o){const J=p.userData.J;const set=(k,x=0,y=0,z=0)=>{if(J[k])J[k].rotation.set(deg(x),deg(y),deg(z))};
 for(const k of ['torso','head','shL','shR','elL','elR','hipL','hipR','kneeL','kneeR'])set(k);
 if(J.skirt)J.skirt.visible=!(o.hideSkirt);
 for(const k in o)if(Array.isArray(o[k]))set(k,...o[k]);
 p.updateMatrixWorld(true);return p}
const P={
 stand:{shL:[0,0,6],shR:[0,0,-6]},
 sitChair:{hipL:[-90,0,4],hipR:[-90,0,-4],kneeL:[90],kneeR:[90],shL:[-35,0,8],shR:[-35,0,-8],elL:[-35],elR:[-35],hideSkirt:true},
 sitGround:{hipL:[-88,0,32],hipR:[-88,0,-32],kneeL:[150,0,0],kneeR:[150,0,0],shL:[-30,0,10],shR:[-30,0,-10],elL:[-50],elR:[-50],hideSkirt:true},
 squat:{torso:[22],hipL:[-125,0,10],hipR:[-125,0,-10],kneeL:[145],kneeR:[145],shL:[-60,0,6],shR:[-75,0,-6],elL:[-40],elR:[-35],hideSkirt:true},
 bendOffer:{torso:[58],head:[-30],shL:[-62,0,10],shR:[-62,0,-10],elL:[-28],elR:[-28]},
 lie:{hipL:[-25],hipR:[-35],kneeL:[40],kneeR:[50],shL:[-50,0,0],shR:[-70,0,0],elL:[-60],elR:[-40],hideSkirt:true},
 kneelReach:{torso:[62],head:[-35],hipL:[0],hipR:[0],kneeL:[90],kneeR:[90],shL:[-110,0,8],shR:[-118,0,-8],elL:[-10],elR:[-10],hideSkirt:true},
 climb:{hipL:[-45,0,30],hipR:[-35,0,-30],kneeL:[80],kneeR:[70],shL:[-170,0,-10],shR:[-150,0,10],hideSkirt:true},
 ladder:{torso:[8],head:[30],hipL:[-35],hipR:[-5],kneeL:[60],kneeR:[10],shL:[-165,0,-5],shR:[-150,0,5],elL:[-10],elR:[-15]},
 lookUp:{head:[35],shL:[-150,0,-8],shR:[-140,0,8],elL:[-20],elR:[-20]},
 teach:{hipL:[-88,0,32],hipR:[-88,0,-32],kneeL:[150],kneeR:[150],shL:[-30,0,10],shR:[-60,0,-25],elL:[-50],elR:[-70],hideSkirt:true},
 sitLow:{hipL:[-100,0,6],hipR:[-100,0,-6],kneeL:[140],kneeR:[140],shL:[-30,0,8],shR:[-60,0,-20],elL:[-40],elR:[-70],hideSkirt:true},
 standTeach:{shL:[0,0,6],shR:[-60,0,-20],elR:[-60]},
};
function feetY(p){const J=p.userData.J,v=new T.Vector3();J.footL.getWorldPosition(v);return v.y-D.foot}

/* ---------- props ---------- */
function chair(h=1.05){const g=new T.Group();const seat=box(1.05,0.12,1.0,C.wood);seat.position.y=h;g.add(seat);
 for(const[x,z]of[[-.45,-.42],[.45,-.42],[-.45,.42],[.45,.42]]){const l=box(0.09,h,0.09,C.woodD);l.position.set(x,h/2,z);g.add(l)}
 const back=box(1.05,1.25,0.1,C.wood);back.position.set(0,h+0.62,-0.47);g.add(back);g.userData.depth=1.0;return g}
function bed(){const g=new T.Group();const b=box(1.7,0.75,4.6,C.wood);b.position.y=0.55;g.add(b);const m=box(1.6,0.22,4.4,0xF2EEE4);m.position.y=1.03;g.add(m);
 const pil=box(0.9,0.2,0.5,0xffffff);pil.position.set(0,1.24,-1.8);g.add(pil);g.userData.top=1.14;return g}
function bowl(){const g=new T.Group();const b=mesh(new T.SphereGeometry(0.26,18,10,0,Math.PI*2,Math.PI/2,Math.PI/2),C.bowl);b.material=b.material.clone();b.material.side=T.DoubleSide;g.add(b);
 const rice=mesh(new T.CircleGeometry(0.24,18),0xffffff,false);rice.rotation.x=-Math.PI/2;rice.position.y=-0.02;g.add(rice);return g}
function mat2(w,d){const m=box(w,0.05,d,C.mat,false);m.position.y=0.025;return m}
function ground(r=9){const g=new T.Mesh(new T.CircleGeometry(r,48),new T.MeshToonMaterial({color:C.ground,gradientMap:grad()}));g.rotation.x=-Math.PI/2;g.position.y=-0.005;return g}
function coconut(h=9){const g=new T.Group();const tr=mesh(new T.CylinderGeometry(0.22,0.32,h,12),C.trunk);tr.position.y=h/2;g.add(tr);
 for(let i=0;i<8;i++){const f=mesh(new T.ConeGeometry(0.28,2.6,6),C.leaf);f.scale.x=0.3;const a=i/8*Math.PI*2;f.position.set(Math.cos(a)*1.1,h+0.1,Math.sin(a)*1.1);f.lookAt(Math.cos(a)*3,h-0.8,Math.sin(a)*3);f.rotateX(deg(90));g.add(f)}
 for(let i=0;i<4;i++){const n=mesh(new T.SphereGeometry(0.2,10,8),0x6b8e23,false);n.position.set(Math.cos(i*1.6)*0.32,h-0.25,Math.sin(i*1.6)*0.32);g.add(n)}
 g.userData.h=h;return g}
function house(h=5.2){const g=new T.Group();const w=box(5,h,3.4,C.wall);w.position.set(0,h/2,0);g.add(w);
 const r=box(5.6,0.3,4.2,C.roof);r.position.set(0,h+0.15,0.3);g.add(r);const door=box(1,2.2,0.05,C.woodD,false);door.position.set(-1.2,1.1,1.72);g.add(door);g.userData.h=h+0.3;return g}
function ladderObj(len=6,ang=16){const g=new T.Group();for(const x of[-.35,.35]){const r=box(0.08,len,0.1,C.woodD);r.position.set(x,len/2,0);g.add(r)}
 for(let y=0.4;y<len;y+=0.55){const s=box(0.7,0.06,0.07,C.wood,false);s.position.set(0,y,0);g.add(s)}g.rotation.x=deg(-ang);return g}

/* ---------- measurement & labels ---------- */
function labelSprite(text,color='#D7263D',scale=0.42){
 const fs=getComputedStyle(document.body).fontFamily||'sans-serif';
 const c=document.createElement('canvas');const ctx=c.getContext('2d');const px=64;ctx.font=`700 ${px}px ${fs}`;
 const w=Math.ceil(ctx.measureText(text).width)+48;c.width=w;c.height=px+40;
 ctx.font=`700 ${px}px ${fs}`;ctx.fillStyle='rgba(255,255,255,.93)';const r=24;
 ctx.beginPath();ctx.moveTo(r,0);ctx.arcTo(w,0,w,c.height,r);ctx.arcTo(w,c.height,0,c.height,r);ctx.arcTo(0,c.height,0,0,r);ctx.arcTo(0,0,w,0,r);ctx.fill();
 ctx.strokeStyle=color;ctx.lineWidth=5;ctx.stroke();ctx.fillStyle=color;ctx.textBaseline='middle';ctx.fillText(text,24,c.height/2+3);
 const tex=new T.CanvasTexture(c);tex.anisotropy=4;const sp=new T.Sprite(new T.SpriteMaterial({map:tex,depthTest:false,transparent:true}));
 sp.scale.set(scale*w/c.height,scale,1);sp.renderOrder=10;return sp}
function seg(a,b,color,r=0.035){const d=new T.Vector3().subVectors(b,a);const len=d.length();const m=new T.Mesh(new T.CylinderGeometry(r,r,len,8),new T.MeshBasicMaterial({color,depthTest:false,transparent:true,opacity:.95}));
 m.position.copy(a).addScaledVector(d,0.5);m.quaternion.setFromUnitVectors(new T.Vector3(0,1,0),d.clone().normalize());m.renderOrder=9;return m}
function dashed(a,b,color){const g=new T.BufferGeometry().setFromPoints([a,b]);const l=new T.Line(g,new T.LineDashedMaterial({color,dashSize:0.18,gapSize:0.12,depthTest:false,transparent:true}));l.computeLineDistances();l.renderOrder=8;return l}
function dot(p,color){const m=new T.Mesh(new T.SphereGeometry(0.07,12,8),new T.MeshBasicMaterial({color,depthTest:false}));m.position.copy(p);m.renderOrder=11;return m}
function dimension(scene,a,b,text,{color=C.line,guides=null,labelOff=new T.Vector3(0,0.35,0)}={}){
 const hex='#'+color.toString(16).padStart(6,'0');
 scene.add(seg(a,b,color));scene.add(dot(a,color));scene.add(dot(b,color));
 const dir=new T.Vector3().subVectors(b,a).normalize();const perp=Math.abs(dir.y)>0.9?new T.Vector3(0.18,0,0):new T.Vector3(0,0.18,0);
 for(const p of[a,b])scene.add(seg(p.clone().sub(perp),p.clone().add(perp),color,0.03));
 if(guides)for(const [p,q] of guides)scene.add(dashed(p,q,color));
 const s=labelSprite(text,hex);s.position.copy(a).add(b).multiplyScalar(0.5).add(labelOff);scene.add(s);return s}
function tag(scene,p,text,color='#333',scale=0.3){const s=labelSprite(text,color,scale);s.position.copy(p);scene.add(s);return s}
function wp(o,dx=0,dy=0,dz=0){const v=new T.Vector3();o.getWorldPosition(v);v.x+=dx;v.y+=dy;v.z+=dz;return v}


/* ---------- alms bowls (enlarged; R = bowl radius) ---------- */
const BP=[[0,0],[0.42,0.03],[0.72,0.14],[0.92,0.34],[1.0,0.56],[0.97,0.76],[0.9,0.92],[0.86,1.0],[0.865,1.03]];
function bowlR(y){for(let i=1;i<BP.length;i++){if(y<=BP[i][1]){const[a,b]=[BP[i-1],BP[i]];return a[0]+(b[0]-a[0])*(y-a[1])/(b[1]-a[1])}}return BP[BP.length-1][0]}
function almsBowl(R=1,color=0x2F2A26){const g=new T.Group();
 const pts=BP.map(([r,y])=>new T.Vector2(r*R,y*R));const geo=new T.LatheGeometry(pts,48);
 const m=new T.Mesh(geo,new T.MeshToonMaterial({color,gradientMap:grad(),side:T.DoubleSide}));g.add(m);
 const o=new T.Mesh(geo,OUT);o.scale.set(1.025,1.0,1.025);g.add(o);
 const lip=new T.Mesh(new T.TorusGeometry(0.865*R,0.025*R,8,48),mat(color));lip.rotation.x=Math.PI/2;lip.position.y=1.03*R;g.add(lip);
 g.userData.R=R;return g}
const RIM=0.9; // the lower line under the mouth (heṭṭhima-rāji), as a fraction of R
function rimLine(b,color=0xD7263D){const R=b.userData.R;const t=new T.Mesh(new T.TorusGeometry(bowlR(RIM)*R+0.012*R,0.018*R,6,64),new T.MeshBasicMaterial({color}));t.rotation.x=Math.PI/2;t.position.y=RIM*R;b.add(t);return t}
function riceMound(b,topFrac,dome=0.12){const R=b.userData.R;const g=new T.Group();
 const fill=topFrac-dome;const rr=Math.min(bowlR(Math.max(0,fill-0.04)),bowlR(Math.min(1,fill+0.08)))*R*0.95;
 const d=new T.Mesh(new T.CylinderGeometry(rr,rr*0.9,0.08*R,40),mat(0xFFFDF4));d.position.y=fill*R-0.04*R;g.add(d);
 const h=(topFrac-fill)*R;const cap=new T.Mesh(new T.SphereGeometry(1,32,12,0,Math.PI*2,0,Math.PI/2),mat(0xFFFDF4));cap.scale.set(rr,h,rr);cap.position.y=fill*R;g.add(cap);
 const curry=new T.Mesh(new T.SphereGeometry(1,20,8,0,Math.PI*2,0,Math.PI/2),mat(0xD9A33A));curry.scale.set(rr*0.38,h*0.45+0.02*R,rr*0.38);curry.position.set(rr*0.3,fill*R+h*0.62,rr*0.12);g.add(curry);
 b.add(g);return g}
function surf(b,theta,y,out=0.02){const R=b.userData.R;const r=bowlR(y/R)*R+out*R;return new T.Vector3(Math.sin(theta)*r,y,Math.cos(theta)*r)}
function crack(b,theta,lenY){ // a crack running down from the mouth along the outer wall
 const R=b.userData.R;const pts=[];const y0=1.0*R;const n=10;for(let i=0;i<=n;i++){const y=y0-lenY*i/n;pts.push(surf(b,theta+(i%2?0.025:-0.02),y,0.012))}
 const l=new T.Line(new T.BufferGeometry().setFromPoints(pts),new T.LineBasicMaterial({color:0xFFE15A}));b.add(l);
 const tube=new T.Mesh(new T.TubeGeometry(new T.CatmullRomCurve3(pts),40,0.012*R,5,false),new T.MeshBasicMaterial({color:0xFFE15A}));b.add(tube);
 return pts[pts.length-1]}
function stitch(b,theta,y){ // a binding across the crack at its lower end
 const R=b.userData.R;const a=surf(b,theta-0.13,y,0.03),c=surf(b,theta+0.13,y,0.03),a2=surf(b,theta-0.13,y-0.07*R,0.03),c2=surf(b,theta+0.13,y-0.07*R,0.03);
 const th=0xFFFFFF;const mk=(p,q)=>{const d=new T.Vector3().subVectors(q,p);const m=new T.Mesh(new T.CylinderGeometry(0.018*R,0.018*R,d.length(),6),new T.MeshBasicMaterial({color:th}));m.position.copy(p).addScaledVector(d,.5);m.quaternion.setFromUnitVectors(new T.Vector3(0,1,0),d.normalize());b.add(m)};
 mk(a,c2);mk(c,a2);for(const p of[a,c,a2,c2]){const h=new T.Mesh(new T.SphereGeometry(0.022*R,8,6),new T.MeshBasicMaterial({color:0x111111}));h.position.copy(p);b.add(h)}}

/* ---------- scenes ---------- */
const TXT={
 hp:{si:'රියන් 2½',en:'2½ cubits'},
 seatBack:{si:'ආසනයේ පසු කෙළවර',en:'back edge of seat'},
 heel:{si:'විළුඹ',en:'heel'},
 head:{si:'හිස',en:'head'},
 knee:{si:'දණහිස',en:'knee'},
 back:{si:'සැතපුණු පැත්තේ පිටත කෙළවර',en:'far edge of the side he lies on'},
 sole:{si:'පතුල',en:'sole'},
 foot:{si:'පය',en:'foot'},
 headG:{si:'හිස',en:'head'},
 no:{si:'✕ නොකළ යුතුයි',en:'✕ not to be done'},
 ill:{si:'නොගිලන් අසන්නා',en:'listener, not ill'},
 teacher:{si:'දේශකයා',en:'teacher'},
 uk:{si:'උක්කට්ඨ · නැළි 2',en:'large · 2 nāḷi'},
 mj:{si:'මජ්ඣිම · නැළි 1',en:'medium · 1 nāḷi'},
 om:{si:'ඔමක · නැළි ½',en:'small · ½ nāḷi'},
 rim:{si:'මුව දාරයට පහළ රේඛාව',en:'line below the rim'},
 lvEq:{si:'සම → උක්කට්ඨ ✓',en:'level → ukkaṭṭha ✓'},
 lvUp:{si:'ගොඩ → උක්කට්ඨොමක ✓',en:'heaped → ukkaṭṭhomaka ✓'},
 lvDn:{si:'අඩු → අපත්ත ✕',en:'below → not a bowl ✕'},
 mk0:{si:'බැඳුම් 0',en:'0 mends'},
 ttOk:{si:'සමතිත්තික ✓',en:'level ✓'},ttNo:{si:'ථූපීකත ✕',en:'heaped ✕'},ttLn:{si:'මුව ඇතුළත දාර රේඛාව',en:'inner rim line'},
 mk1:{si:'බැඳුම් 1',en:'1 mend'},
 mk5:{si:'බැඳුම් 5 → අපත්ත',en:'5 mends → not a bowl'},
 mkNo:{si:'✕ ඉල්ලිය නොහැක',en:'✕ may not ask'},
 mkOk:{si:'✓ ඉල්ලිය හැක',en:'✓ may ask'},
};
const L=(k,lang)=>TXT[k][lang]||TXT[k].en;
const S={
 'hp-seated'(sc,lang){ // monk on chair, giver standing bent
  const ch=chair();sc.add(ch);const m=pose(person('monk'),P.sitChair);m.position.set(0,1.05+0.12+0.17,-0.05);sc.add(m);
  const g=pose(person('man'),P.bendOffer);g.rotation.y=Math.PI;sc.add(g);g.position.set(3,0,0);g.updateMatrixWorld(true);g.position.y-=feetY(g);
  const bw=bowl();g.userData.J.handL.add(bw);bw.position.set(0.1,-0.12,0.05);
  // receiver faces +z; giver stands in front (+z) facing -z
  g.position.set(0,g.position.y,0);g.updateMatrixWorld(true);
  const seatBack=new T.Vector3(0,1.17,-0.5);let hz=wp(g.userData.J.headMesh).z-D.headR;g.position.z+=seatBack.z+2.5-hz;g.updateMatrixWorld(true);
  const head=wp(g.userData.J.headMesh,0,0,-D.headR);const y=0.25;const a=new T.Vector3(1.0,y,seatBack.z),b=new T.Vector3(1.0,y,head.z);
  dimension(sc,a,b,L('hp',lang),{guides:[[new T.Vector3(1.0,y,seatBack.z),new T.Vector3(0.52,1.11,seatBack.z)],[new T.Vector3(1.0,y,head.z),head]]});
  tag(sc,new T.Vector3(1.3,1.9,seatBack.z-0.4),L('seatBack',lang),'#7a4e28');tag(sc,head.clone().add(new T.Vector3(0.9,0.55,0)),L('head',lang),'#1F6FB2');
  return{cam:[7.5,4.2,2.4],tgt:[0,1.6,1.0]}},
 'hp-standing'(sc,lang){
  const m=pose(person('monk'),P.stand);sc.add(m);m.updateMatrixWorld(true);m.position.y-=feetY(m);
  const g=pose(person('man'),P.bendOffer);g.rotation.y=Math.PI;sc.add(g);g.updateMatrixWorld(true);g.position.y-=feetY(g);
  const bw=bowl();g.userData.J.handL.add(bw);bw.position.set(0.1,-0.12,0.05);g.updateMatrixWorld(true);
  const heel=new T.Vector3(0,0,-0.12);const hz=wp(g.userData.J.headMesh).z-D.headR;g.position.z+=heel.z+2.5-hz;g.updateMatrixWorld(true);
  const head=wp(g.userData.J.headMesh,0,0,-D.headR);const y=0.12,x=0.9;
  dimension(sc,new T.Vector3(x,y,heel.z),new T.Vector3(x,y,head.z),L('hp',lang),{guides:[[new T.Vector3(0.15,0.02,heel.z),new T.Vector3(x,y,heel.z)],[new T.Vector3(x,y,head.z),head]]});
  tag(sc,new T.Vector3(1.1,0.6,heel.z-0.3),L('heel',lang),'#7a4e28');tag(sc,head.clone().add(new T.Vector3(0.9,0.55,0)),L('head',lang),'#1F6FB2');
  return{cam:[7.2,3.6,2.2],tgt:[0,1.6,1.0]}},
 'hp-lying'(sc,lang){ // monk lying on his right side on a bed, facing the giver (+x); giver squatting
  const b=bed();sc.add(b);
  const m=pose(person('monk'),P.lie);m.rotation.x=deg(-90);
  const lay=new T.Group();lay.add(m);lay.rotation.z=deg(-90);lay.position.set(-0.15,1.14+0.58,0.25);sc.add(lay);lay.updateMatrixWorld(true);
  const backX=wp(m.userData.J.torso).x-0.37;
  const g=pose(person('man'),P.squat);g.rotation.y=-Math.PI/2;sc.add(g);g.updateMatrixWorld(true);g.position.y-=feetY(g);g.position.z=0.2;g.updateMatrixWorld(true);
  const kx=()=>Math.min(wp(g.userData.J.kneeL).x,wp(g.userData.J.kneeR).x)-0.17;g.position.x+=backX+2.5-kx();g.updateMatrixWorld(true);
  const knee=wp(g.userData.J.kneeL);knee.x=kx();const y=0.15,z=2.7;
  dimension(sc,new T.Vector3(backX,y,z),new T.Vector3(knee.x,y,z),L('hp',lang),{guides:[[new T.Vector3(backX,y,z),new T.Vector3(backX,1.75,0.2)],[new T.Vector3(knee.x,y,z),knee]]});
  tag(sc,new T.Vector3(backX-0.5,2.6,0.2),L('back',lang),'#7a4e28');tag(sc,knee.clone().add(new T.Vector3(0.7,0.8,0.5)),L('knee',lang),'#1F6FB2');
  return{cam:[2.6,4.8,8.6],tgt:[0.8,1.1,0.6]}},
 'hp-roof'(sc,lang){
  const h=house();sc.add(h);const top=h.userData.h;
  const m=pose(person('monk'),P.kneelReach);m.rotation.y=0;sc.add(m);m.updateMatrixWorld(true);
  // knees on roof edge; the monk faces +z (out over the edge)
  m.position.set(0.6,top+D.shin*0+0.95,1.7);m.updateMatrixWorld(true);
  const kneeY=Math.min(wp(m.userData.J.kneeL).y,wp(m.userData.J.kneeR).y)-0.17;m.position.y+=top-kneeY;m.updateMatrixWorld(true);
  const g=pose(person('man'),P.ladder);g.rotation.y=Math.PI;sc.add(g);
  const ld=ladderObj(6.2,14);ld.position.set(0.6,0,3.15);sc.add(ld);
  g.position.set(0.6,0,3.1);g.updateMatrixWorld(true);
  // lowest part of the person above (excluding the hand) — knee / shin on the roof edge, the "sole" in the book's figure
  const sole=Math.min(wp(m.userData.J.footL).y,wp(m.userData.J.kneeL).y-0.17,top);
  const hy=wp(g.userData.J.headMesh).y+D.headR;g.position.y+=sole-2.5-hy;g.updateMatrixWorld(true);
  const head=wp(g.userData.J.headMesh,0,D.headR,0);const x=2.2;
  dimension(sc,new T.Vector3(x,head.y,head.z),new T.Vector3(x,sole,head.z),L('hp',lang),{labelOff:new T.Vector3(0.9,0,0),guides:[[new T.Vector3(x,head.y,head.z),head],[new T.Vector3(x,sole,head.z),new T.Vector3(0.6,sole,1.75)]]});
  tag(sc,new T.Vector3(x+0.6,sole+0.45,head.z),L('sole',lang),'#7a4e28');tag(sc,new T.Vector3(x+0.6,head.y-0.45,head.z),L('headG',lang),'#1F6FB2');
  return{cam:[11,6.5,10],tgt:[0.6,3.4,2.0]}},
 'hp-tree'(sc,lang){
  const t=coconut(8.6);t.position.set(0,0,0);sc.add(t);
  const g=pose(person('man'),P.climb);g.rotation.y=Math.PI;sc.add(g);g.position.set(0,0,0.42);g.updateMatrixWorld(true);
  const m=pose(person('monk'),P.lookUp);m.rotation.y=Math.PI;sc.add(m);m.position.set(0.15,0,1.3);m.updateMatrixWorld(true);m.position.y-=feetY(m);m.updateMatrixWorld(true);
  const hy=wp(m.userData.J.headMesh).y+D.headR;const fy=Math.min(wp(g.userData.J.footL).y,wp(g.userData.J.footR).y)-D.foot;g.position.y+=hy+2.5-fy;g.updateMatrixWorld(true);
  const foot=Math.min(wp(g.userData.J.footL).y,wp(g.userData.J.footR).y)-D.foot;const x=1.6,z=1.0;
  dimension(sc,new T.Vector3(x,hy,z),new T.Vector3(x,foot,z),L('hp',lang),{labelOff:new T.Vector3(0.9,0,0),guides:[[new T.Vector3(x,hy,z),wp(m.userData.J.headMesh,0,D.headR,0)],[new T.Vector3(x,foot,z),new T.Vector3(0.2,foot,0.6)]]});
  tag(sc,new T.Vector3(x+0.7,foot+0.45,z),L('foot',lang),'#7a4e28');tag(sc,new T.Vector3(x+0.7,hy-0.45,z),L('headG',lang),'#1F6FB2');
  return{cam:[11,6,8.5],tgt:[0.4,4.4,0.8]}},
 'pt-sizes'(sc,lang){ // three sizes; volumes 4:2:1 → linear 1 : .794 : .63
  const R0=1.0;const sz=[[R0,'uk',-2.25,0],[R0*0.794,'mj',0,1],[R0*0.63,'om',1.95,0]];
  for(const[R,k,x,hi] of sz){const b=almsBowl(R);b.position.x=x;sc.add(b);rimLine(b);riceMound(b,RIM);
   tag(sc,new T.Vector3(x,R*1.05+0.45+hi*0.55,0),L(k,lang),'#7a4e28',0.32)}
  return{cam:[0,3.2,6.2],tgt:[0,0.75,0],fitW:3.35}},
 'pt-levels'(sc,lang){ // same bowl, rice of 2 nāḷi + curry: level vs. the line below the rim
  const R=0.95;const lv=[[RIM+0.34,0.36,'lvUp',-2.2,'#B95A0A',1],[RIM,0.12,'lvEq',0,'#1F9D55',0],[RIM-0.22,0.1,'lvDn',2.2,'#D7263D',1]];
  for(const[t,dm,k,x,c,hi] of lv){const b=almsBowl(R);b.position.x=x;sc.add(b);rimLine(b);riceMound(b,t,dm);tag(sc,new T.Vector3(x*0.85,R*1.05+0.65+hi*0.6,0),L(k,lang),c,0.3)}
  tag(sc,new T.Vector3(0,-0.15,R+0.75),L('rim',lang),'#D7263D',0.28);
  return{cam:[0,3.2,5.8],tgt:[0,0.85,0.2],fitW:3.5}},
 'pt-mends'(sc,lang){ // clay bowls: cracks and mends (enlarged; 1 finger ≈ R/6.5)
  const R=0.95,ag=R/6.5;const xs=[-2.2,0,2.2];const bs=xs.map(x=>{const b=almsBowl(R,0xB5652F);b.position.x=x;sc.add(b);return b});
  crack(bs[0],0,ag*1.3);
  const e1=crack(bs[1],0,ag*2);stitch(bs[1],0,e1.y+0.02*R);
  for(const th of[-0.9,-0.45,0,0.45,0.9]){const e=crack(bs[2],th,ag*2);stitch(bs[2],th,e.y+0.02*R)}
  const ty=R*1.05+0.45;
  tag(sc,new T.Vector3(xs[0],ty,0),L('mk0',lang),'#7a4e28',0.3);tag(sc,new T.Vector3(xs[1],ty+0.6,0),L('mk1',lang),'#7a4e28',0.3);tag(sc,new T.Vector3(xs[2],ty,0),L('mk5',lang),'#1F9D55',0.3);
  tag(sc,new T.Vector3(-1.1,-0.15,R+0.8),L('mkNo',lang),'#D7263D',0.28);tag(sc,new T.Vector3(2.2,-0.15,R+0.8),L('mkOk',lang),'#1F9D55',0.28);
  return{cam:[0,2.5,6.0],tgt:[0,0.7,0.3],fitW:3.35}},
 'sk-tittika'(sc,lang){ // sekhiya 30: level with the inner rim line vs. heaped
  const R=0.95;const lv=[[RIM,0.12,'ttOk',-1.25,'#1F9D55',0],[RIM+0.4,0.4,'ttNo',1.25,'#D7263D',1]];
  for(const[t,dm,k,x,c,hi] of lv){const b=almsBowl(R);b.position.x=x;sc.add(b);rimLine(b);riceMound(b,t,dm);tag(sc,new T.Vector3(x*0.9,R*1.05+0.65+hi*0.5,0),L(k,lang),c,0.32)}
  tag(sc,new T.Vector3(0,-0.15,R+0.75),L('ttLn',lang),'#7a4e28',0.28);
  return{cam:[0,3.0,5.6],tgt:[0,0.55,0.3],fitW:3.0}},
 'sk-ground'(sc,lang){teachScene(sc,lang,'ground');return{cam:[6.5,3.6,5.2],tgt:[0,1.2,0]}},
 'sk-lowseat'(sc,lang){teachScene(sc,lang,'low');return{cam:[6.5,3.6,5.2],tgt:[0,1.2,0]}},
 'sk-standing'(sc,lang){teachScene(sc,lang,'stand');return{cam:[6.5,3.8,5.2],tgt:[0,1.6,0]}},
};
function teachScene(sc,lang,kind){
 // listener (not ill) sits on a chair; the teacher is lower: on the ground / a low seat / standing
 const ch=chair();ch.position.set(-1.3,0,0);ch.rotation.y=Math.PI/2;sc.add(ch);
 const l=pose(person('man'),P.sitChair);l.rotation.y=Math.PI/2;l.position.set(-1.3+0.05,1.05+0.12+0.17,0);sc.add(l);
 let t;
 if(kind==='ground'){const mt=mat2(1.6,1.6);mt.position.x=1.4;sc.add(mt);t=pose(person('monk'),P.teach);t.rotation.y=-Math.PI/2;sc.add(t);t.position.set(1.4,0.42,0)}
 else if(kind==='low'){const st=box(1.1,0.5,1.0,C.wood);st.position.set(1.4,0.25,0);sc.add(st);t=pose(person('monk'),P.sitLow);t.rotation.y=-Math.PI/2;sc.add(t);t.position.set(1.4,0.5+0.17,0);}
 else {t=pose(person('monk'),P.standTeach);t.rotation.y=-Math.PI/2;sc.add(t);t.updateMatrixWorld(true);t.position.set(1.5,0,0);t.updateMatrixWorld(true);t.position.y-=feetY(t)}
 tag(sc,new T.Vector3(-1.3,4.6,0),L('ill',lang),'#1F6FB2',0.3);tag(sc,new T.Vector3(1.5,kind==='stand'?4.8:(kind==='low'?3.9:3.4),0),L('teacher',lang),'#7a4e28',0.3);
 tag(sc,new T.Vector3(0.1,0.35,1.6),L('no',lang),'#D7263D',0.38);
}

/* ---------- mount ---------- */
const LIVE=new Set();
function mount(el,id,lang){
 const def=S[id];const stage=el.querySelector('.dgm-stage')||el;if(!def){stage.textContent='?';return}
 if(el._pmd)return;
 const w=stage.clientWidth||600,h=Math.round(Math.min(420,Math.max(260,w*0.7)));
 const r=new T.WebGLRenderer({antialias:true,alpha:true});r.setPixelRatio(Math.min(2,window.devicePixelRatio||1));r.setSize(w,h);
 stage.innerHTML='';stage.appendChild(r.domElement);r.domElement.style.touchAction='pan-y';
 const sc=new T.Scene();const world=new T.Group();sc.add(world);
 sc.add(new T.HemisphereLight(0xffffff,0x8a7f6a,0.75));const dl=new T.DirectionalLight(0xffffff,0.75);dl.position.set(5,10,7);sc.add(dl);
 world.add(ground(id==='hp-roof'||id==='hp-tree'?10:7.5));
 const cfg=def(world,lang);
 const cam=new T.PerspectiveCamera(38,w/h,0.1,200);const tgt=new T.Vector3(...cfg.tgt);
 const base=new T.Vector3(...cfg.cam).sub(tgt);const base0=base.length();
 function fitK(asp){if(!cfg.fitW)return 1;const vf=Math.tan(deg(19));const hf=vf*asp;return Math.max(1,(cfg.fitW/hf)/base0)}
 base.multiplyScalar(fitK(w/h));const sph=new T.Spherical().setFromVector3(base);const s0={th:sph.theta,ph:sph.phi};
 function place(){const v=new T.Vector3().setFromSpherical(sph).add(tgt);cam.position.copy(v);cam.lookAt(tgt)}
 place();let dirty=true;
 function frame(){if(!el.isConnected){dispose();return}if(dirty){r.render(sc,cam);dirty=false}el._raf=requestAnimationFrame(frame)}
 let drag=null;const cv=r.domElement;
 cv.addEventListener('pointerdown',e=>{drag={x:e.clientX,y:e.clientY,th:sph.theta,ph:sph.phi};cv.setPointerCapture(e.pointerId)});
 cv.addEventListener('pointermove',e=>{if(!drag)return;sph.theta=drag.th-(e.clientX-drag.x)*0.008;sph.phi=Math.max(0.35,Math.min(1.45,drag.ph-(e.clientY-drag.y)*0.006));place();dirty=true});
 const up=()=>{drag=null};cv.addEventListener('pointerup',up);cv.addEventListener('pointercancel',up);
 cv.addEventListener('dblclick',()=>{sph.theta=s0.th;sph.phi=s0.ph;place();dirty=true});
 const ro=new ResizeObserver(()=>{const W=stage.clientWidth;if(!W)return;const H=Math.round(Math.min(420,Math.max(260,W*0.7)));r.setSize(W,H);cam.aspect=W/H;cam.updateProjectionMatrix();if(cfg.fitW){sph.radius=base0*fitK(W/H);place()}dirty=true});ro.observe(stage);
 function dispose(){cancelAnimationFrame(el._raf);ro.disconnect();sc.traverse(o=>{if(o.geometry)o.geometry.dispose();if(o.material&&o.material.map)o.material.map.dispose()});r.dispose();r.forceContextLoss&&r.forceContextLoss();LIVE.delete(dispose);el._pmd=null}
 el._pmd={dispose};LIVE.add(dispose);frame();
 const hint=document.createElement('div');hint.className='dgm-hint';hint.textContent=lang==='si'?'⟲ ඇදීමෙන් කරකවන්න · දෙවරක් තට්ටු කර යළි සකසන්න':'⟲ Drag to turn · double-tap to reset';el.insertBefore(hint,stage.nextSibling);
}
function disposeAll(){[...LIVE].forEach(f=>f())}
window.PMD={mount,disposeAll,ids:Object.keys(S)};
})();
