<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><title>PitCAD – RassLexx #27772</title>
<style>
:root{--bg:#121916;--p:#18211d;--t:#e8f7ee;--m:#8fa89a;--a:#48E57C;--b:#2a3a32;box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px);color-scheme:dark}
*{box-sizing:border-box}html,body{height:100%;margin:0}
body{background:var(--bg);color:var(--t);font:14px system-ui,-apple-system,Segoe UI,sans-serif;display:flex;flex-direction:column;overflow:hidden}
header{display:flex;flex-wrap:wrap;gap:8px 12px;align-items:center;padding:8px 12px;background:var(--p);border-bottom:1px solid var(--b)}
h1{font-size:17px;margin:0;color:var(--a);letter-spacing:.5px;text-shadow:0 0 12px #48E57C66}h4{margin:10px 0 5px;font-size:11px;text-transform:uppercase;letter-spacing:.8px;color:var(--m)}
label{display:flex;align-items:center;gap:5px;color:var(--m);font-size:12px}
input,button,textarea{font:inherit;color:var(--t);background:var(--bg);border:1px solid var(--b);border-radius:7px;padding:5px 8px}
input[type=color]{padding:0;width:30px;height:26px}input[type=checkbox]{width:auto}input[type=number]{width:62px}
#tn{width:68px}#tm{width:110px}button{cursor:pointer}button:hover{border-color:var(--a)}button.pr{background:var(--a);color:#0b120f;border-color:var(--a);font-weight:600}button:hover{box-shadow:0 0 10px #48E57C55}
main{flex:1;min-height:0;display:grid;grid-template-columns:190px 1fr 240px}
aside{background:var(--p);padding:10px;overflow:auto;border-right:1px solid var(--b)}aside.r{border-right:0;border-left:1px solid var(--b)}
.g{display:grid;grid-template-columns:1fr 1fr;gap:5px}.g button{font-size:12px;padding:7px 3px}
#vw{position:relative;min-width:0;min-height:0}canvas{display:block;width:100%;height:100%;touch-action:none}
#hint{position:absolute;left:8px;bottom:8px;font-size:11px;color:#dcdaf0;background:#121916cc;border:1px solid #2a3a32;padding:4px 8px;border-radius:6px;pointer-events:none}
#zm{position:absolute;right:8px;top:8px;display:flex;flex-direction:column;gap:4px}
.row{display:flex;gap:6px;flex-wrap:wrap;margin:8px 0;align-items:center}textarea{width:100%;height:70px;font-size:11px}#ls{display:flex;flex-direction:column;gap:4px}#ls button{text-align:left;font-size:12px;padding:4px 8px}
#mobileTools,#vb{display:none}
@media(max-width:820px){
html{height:var(--vh,100%)}
body{height:100%;font-size:14px}
header{flex:none;display:flex;gap:8px;padding:6px 12px}
header>*:not(h1){display:none}
header h1{margin:0;font-size:18px}
body.menu header{display:grid;grid-template-columns:1fr 1fr;max-height:55%;overflow:auto;padding:8px 10px;-webkit-overflow-scrolling:touch}
body.menu header h1{grid-column:1/-1}
body.menu header>label{display:flex}
body.menu header>#ex,body.menu header>#cl{display:block}
header label input#tn,header label input#tm{flex:1;min-width:0;width:100%}
main{display:flex;flex-direction:column;flex:1;min-height:0;overflow:hidden}
#vw{order:0;flex:1 1 0;min-height:120px;width:100%}
canvas{width:100%;height:100%;touch-action:none}
#vb{display:flex;position:absolute;left:8px;top:8px;gap:6px;z-index:2}
#vb button{padding:6px 12px;background:#121916e6}
#zm{right:8px;top:8px}#zm button{width:44px;height:44px;font-size:22px;background:#121916e6}
#hint{left:8px;right:8px;bottom:8px;font-size:11px;text-align:center;transition:opacity .6s}
#mobileTools{order:1;display:flex;flex:none;gap:6px;padding:6px 8px;background:var(--p);border-top:1px solid var(--b);margin:0}
#mobileTools button{flex:1}
aside{display:none;order:2;flex:none;height:calc(var(--vh,100vh)*.38);overflow:auto;-webkit-overflow-scrolling:touch;border:0;border-top:1px solid var(--b);padding:10px}
aside.r{border:0;border-top:1px solid var(--b)}
body[data-tab=parts] aside:not(.r){display:block}
body[data-tab=edit] aside.r{display:block}
.g{grid-template-columns:repeat(2,minmax(0,1fr))}.g button{font-size:13px;padding:8px 4px}
input,button,textarea{font-size:16px;min-height:42px}
input[type=checkbox]{min-height:0;width:22px;height:22px}
input[type=color]{width:46px;min-height:42px}
input[type=number]{width:84px}
input[type=range]{min-height:34px}
#ls button{min-height:42px}
#js{min-height:70px}
}
</style></head><body data-tab="parts"><script>function vh(){document.documentElement.style.setProperty("--vh",innerHeight+"px")}vh();addEventListener("resize",vh);addEventListener("orientationchange",vh);window.addEventListener("error",function(e){var h=document.getElementById("hint");if(h){h.style.color="#ff8080";h.textContent="Error: "+e.message}})</script>
<header><h1>▲ PitCAD</h1>
<label>Team #<input id="tn" value="27772"></label><label>Name<input id="tm" value="RassLexx"></label>
<label><input id="st" type="checkbox">Stage mode</label><label><input id="au" type="checkbox">360° spin</label>
<button id="v1">Orbit</button><button id="v2">Top</button><button id="v3">Inside 360°</button>
<button id="ex" class="pr">Example</button><button id="cl">New empty</button></header>
<main>
<aside><div id="items"></div></aside>
<div id="vw"><canvas id="cv"></canvas><div id="vb"><button id="mOrbit">Orbit</button><button id="mTop">Top</button><button id="mInside">360°</button></div><div id="zm"><button id="zi">+</button><button id="zo">−</button></div><div id="hint">Add parts from the left · drag parts · drag empty space to look around 360° · wheel zoom · Q/E/R spin · ↑↓ height · Del remove</div></div>
<div id="mobileTools"><button id="tP" class="pr">Parts</button><button id="tE">Edit</button><button id="tM">Menu</button></div><aside class="r"><div id="sel" style="color:var(--m)">Pit is empty. Add a floor or tent from the left menu, then click a part to edit it.</div>
<div id="ctl" style="display:none"><div id="nm" style="font-weight:600"></div><div id="sz" style="color:var(--m);font-size:12px"></div>
<div class="row"><label>Color<input id="ic" type="color"></label><label id="l2">Color 2<input id="ic2" type="color"></label></div>
<div class="row"><label>X ft<input id="ix" type="number" step=".25"></label><label>Z ft<input id="iz" type="number" step=".25"></label></div>
<div id="fr" style="display:none"><div class="row"><label style="flex:1">Award<input id="ft" style="flex:1;min-width:0"></label></div><div class="row"><label style="flex:1">Regional / event<input id="fe" style="flex:1;min-width:0"></label></div><div class="row"><label style="flex:1">Year / note<input id="fs2" style="flex:1;min-width:0"></label></div><div class="row"><label style="flex:1">Program<input id="fh" style="flex:1;min-width:0"></label></div><div class="row"><label>Stars<input id="fst" type="number" min="0" max="5"></label><label><input id="fp" type="checkbox">Stripes</label><label><input id="fi" type="checkbox">Italic</label></div></div>
<div id="cb" style="display:none"><div class="row"><label style="flex:1">Title<input id="ct" style="flex:1;min-width:0"></label></div><div class="row"><label style="flex:1">Subtitle<input id="cs" style="flex:1;min-width:0"></label></div></div>
<div class="row" id="pr2" style="display:none"><button id="pb">Upload photos…</button><button id="pc">Clear</button><input id="pf" type="file" accept="image/*" multiple hidden></div>
<div class="row" style="flex-direction:column;align-items:stretch;gap:3px"><label>Spin <b id="iao"></b>°<input id="ia" type="range" min="0" max="360" step="1" style="flex:1"></label><label>Height <b id="iyo"></b> ft<input id="iy" type="range" min="0" max="12" step=".25" style="flex:1"></label><label>Tilt <b id="itlo"></b>°<input id="itl" type="range" min="-90" max="90" step="1" style="flex:1"></label></div>
<div class="row"><button id="rt">Rotate</button><button id="dp">Duplicate</button><button id="dl">Delete</button></div></div>
<h4>In your pit</h4><div id="ls"></div>
<h4>Save / share</h4><textarea id="js" placeholder="Layout code appears here"></textarea>
<div class="row"><button id="sv">Export</button><button id="ld">Import</button></div>
<div style="font-size:11px;color:var(--m)">Pit area = 10×10 ft (yellow tape). Autosaves in this browser.</div></aside>
</main>
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script>
const P=(sx,sz,h,t,c,s)=>[[1,1],[1,-1],[-1,1],[-1,-1]].map(([a,b])=>[t,h,t,a*sx,h/2,b*sz,c,s]);
const TR='#c8ccd6';const FP=[[1.4,.1,1.4,0,.05,0,'#222','c'],[.1,6.6,.1,0,3.3,0,'#222','m'],[2.8,.08,.08,0,6.5,0,'#222','m']];
const D={
ftiles:{cat:'Floor',n:'Foam tiles 10×10',c:'#9b6fe0',f:'tiles',w:10,dd:10,d:'5×5 interlocking tiles, 2 colors'},
fcarpet:{cat:'Floor',n:'Carpet 10×10',c:'#3b4a6b',f:'carpet',w:10,dd:10,d:'solid carpet'},
frug:{cat:'Floor',n:'Rug 6×4',c:'#a33b3b',f:'carpet',w:6,dd:4,d:'6 × 4 ft'},
fwood:{cat:'Floor',n:'Wood deck 10×10',c:'#b07a45',f:'wood',w:10,dd:10,d:'plank deck'},
tent:{cat:'Shelter',n:'Pop-up tent 10×10',c:'#2f6fd6',p:[...P(4.9,4.9,7,.18,TR,'m'),[10.6,2.4,10.6,0,8.2,0,null,'p'],[10.6,.7,.05,0,6.65,5.3,null],[10.6,.7,.05,0,6.65,-5.3,null],[.05,.7,10.6,5.3,6.65,0,null],[.05,.7,10.6,-5.3,6.65,0,null]],d:'10×10 ft, 7 ft legs'},
arch:{cat:'Shelter',n:'Truss arch + sign',c:'#2a6fd6',p:[[.35,7,.35,-4.9,3.5,0,TR,'m'],[.35,7,.35,4.9,3.5,0,TR,'m'],[10,.35,.35,0,7,0,TR,'m'],[9.6,1.6,.1,0,6.05,0,null]],s:[9.4,1.5,6.05,.07],d:'10 ft wide, 7 ft tall'},
drape:{cat:'Shelter',n:'Pipe & drape wall',c:'#14141c',p:[[10,7,.06,0,3.5,0,null],[.12,7.2,.12,-5,3.6,0,TR,'m'],[.12,7.2,.12,5,3.6,0,TR,'m'],[10.1,.1,.1,0,7.1,0,TR,'m']],d:'10 × 7 ft'},
banner:{cat:'Shelter',n:'Banner sign',c:'#5b2fb0',p:[[9,2.6,.08,0,5.2,0,null],[.1,4,.1,-4.4,2,0,'#222','m'],[.1,4,.1,4.4,2,0,'#222','m']],s:[8.6,2.2,5.2,.05],d:'9 × 2.6 ft, team sign'},
table:{cat:'Furniture',n:'Table 6 ft',c:'#e9e7f0',p:[[6,.12,2.5,0,2.5,0,null],...P(2.85,1.1,2.45,.12,'#444','m')],d:'6 × 2.5 ft'},
rtable:{cat:'Furniture',n:'Round table',c:'#ffffff',p:[[5,.1,5,0,2.5,0,null,'c'],[.3,2.4,.3,0,1.2,0,'#333','cm'],[2.4,.1,2.4,0,.05,0,'#333','c']],d:'5 ft diameter'},
chair:{cat:'Furniture',n:'Chair',c:'#333333',p:[[1.4,.1,1.4,0,1.4,0,null],[1.4,1.2,.1,0,2.1,-.65,null],...P(.6,.6,1.4,.07,'#222','m')],d:'1.4 × 1.4 ft'},
stool:{cat:'Furniture',n:'Stool',c:'#444444',p:[[1.2,.1,1.2,0,2.1,0,null,'c'],...P(.38,.38,2.05,.06,'#222','m')],d:'bar stool'},
bench:{cat:'Furniture',n:'Bench',c:'#8a6a4a',p:[[6,.15,1.2,0,1.5,0,null],...P(2.8,.45,1.45,.12,'#444','m')],d:'6 × 1.2 ft'},
shelf:{cat:'Storage',n:'Shelf unit',c:'#5b2fb0',p:[...P(1.9,.65,6,.12,'#2b2b33','m'),...[.3,2,3.6,5.2].map(y=>[4,.08,1.5,0,y,0,null])],d:'4 × 1.5 × 6 ft'},
chest:{cat:'Storage',n:'Tool chest',c:'#c0392b',p:[[4,2.4,2,0,1.5,0,null,'m'],[4.1,.1,2.1,0,2.75,0,'#222'],...[1,1.6,2.2].map(y=>[3.8,.04,.03,0,y,1.01,'#111'])],d:'4 × 2 × 3 ft'},
tote:{cat:'Storage',n:'Tote',c:'#222222',p:[[2,1.1,1.4,0,.55,0,null],[2.06,.14,1.46,0,1.17,0,'#e8c020']],d:'2 × 1.4 ft'},
cart:{cat:'Storage',n:'Wire cart',c:'#c9ccd4',p:[...P(1.4,.7,3,.08,'#999','m'),...[.4,1.6,2.9].map(y=>[3,.06,1.5,0,y,0,null,'m'])],d:'3 × 1.5 × 3 ft'},
bin:{cat:'Storage',n:'Trash can',c:'#6b8a7a',p:[[1.1,1.8,1.1,0,.9,0,null,'c']],d:'1.1 ft'},
wall:{cat:'Shelter',n:'Wall 10 ft',c:'#e8e6ef',p:[[10,7,.3,0,3.5,0,null]],d:'10 × 7 ft solid wall'},
wall5:{cat:'Shelter',n:'Wall 5 ft',c:'#e8e6ef',p:[[5,7,.3,0,3.5,0,null]],d:'5 × 7 ft solid wall'},
finsp:{cat:'Flags',n:'Inspire Award',c:'#f2531c',k:'flag',hd:'FIRST TECH CHALLENGE',txt:'Inspire Award',ev:'Almaty FIRST Championship',sub:'Regional Qualifiers',stars:0,pat:0,ital:0,p:FP,d:'award banner, edit every line'},
fcap:{cat:'Flags',n:'Winning Alliance Captain',c:'#ff6a13',k:'flag',hd:'FIRST TECH CHALLENGE',txt:'Winning Alliance Captain Award',ev:'Central Asia FIRST Championship',sub:'2026',stars:5,pat:1,ital:1,p:FP,d:'award banner, edit every line'},
fwin:{cat:'Flags',n:"Champion's Award Winner",c:'#e0261f',k:'flag',hd:'FIRST LEGO LEAGUE CHALLENGE',txt:"Champion's Award Winner",ev:'Almaty Tech Cup',sub:'2025',stars:0,pat:0,ital:1,p:FP,d:'award banner, edit every line'},
fcust:{cat:'Flags',n:'Custom award flag',c:'#0d7a5f',k:'flag',hd:'FIRST ROBOTICS COMPETITION',txt:'Your Award',ev:'Your Regional',sub:'2026',stars:3,pat:0,ital:0,p:FP,d:'award banner, edit every line'},
port:{cat:'Desk items',n:'Portfolio',c:'#1f3a8a',k:'port',sm:1,txt:'Team Portfolio',sub:'27772',p:[[.96,.09,1.36,0,.06,0,'#f4f1ea'],[.98,.015,1.38,0,.0075,0,null],[.98,.015,1.38,0,.1125,0,null],[.03,.12,1.38,-.475,.06,0,null]],d:'binder, custom title + cover image'},
mag:{cat:'Desk items',n:'Magazines',c:'#c0392b',k:'mag',sm:1,txt:'Magazine',sub:'Our season',d:'stack of 3, custom title + cover image'},
mac:{cat:'Desk items',n:'MacBook',c:'#c9ccd4',k:'mac',sm:1,txt:'',sub:'',d:'13-inch laptop, custom screen text + image'},
iflag:{cat:'Flags',n:'Custom image flag',c:'#0d7a5f',k:'iflag',txt:'Your flag image',ar:.667,d:'upload any picture as a banner'},
photog:{cat:'Decor',n:'Photo garland',c:'#ffffff',k:'photog',d:'10 ft string with 7 photo cards, upload your photos'},
garland:{cat:'Decor',n:'Garland fringe',c:'#ff8fc8',k:'garland',p:[[10,.06,.06,0,7.1,0,'#ddd','m']],d:'10 ft tinsel fringe, hangs at 7 ft'},
string:{cat:'Decor',n:'String lights',c:'#ffd27a',k:'string',d:'10 ft bulb string'},
plant:{cat:'Decor',n:'Plant',c:'#2e7d32',p:[[.9,1,.9,0,.5,0,'#a0522d','c'],[1.6,1.6,1.6,0,1.9,0,null,'s']],d:'potted plant'},
stage:{cat:'Lights',n:'Spot light',c:'#00c8ff',p:[[.1,5,.1,0,2.5,0,'#222','m'],[.9,.6,.6,0,5.3,0,'#222','m'],[.6,.1,.6,0,4.98,0,null,'e']],sp:[0,5,0,3,22],d:'tripod spot, glows in stage mode'},
led:{cat:'Lights',n:'LED strip 10 ft',c:'#ff2fd0',p:[[10,.1,.1,0,6.9,0,null,'e']],l:[0,6.6,.3,1.2,14],d:'10 ft glowing bar'},
robot:{cat:'Robot & tech',n:'Robot',c:'#d02a2a',p:[[2.9,.5,2.9,0,.55,0,null],[2.4,1,2.4,0,1.3,0,'#555','m'],[.3,.5,.5,1.1,.3,1.1,'#111'],[.3,.5,.5,-1.1,.3,1.1,'#111'],[.3,.5,.5,1.1,.3,-1.1,'#111'],[.3,.5,.5,-1.1,.3,-1.1,'#111']],d:'~2.9 × 2.9 ft'},
mon:{cat:'Robot & tech',n:'Monitor',c:'#1a3b8a',p:[[.12,2.2,.12,0,1.1,0,'#222','m'],[1.2,.06,1.2,0,.03,0,'#222'],[2.4,1.4,.1,0,2.9,0,null,'e']],d:'2.4 ft screen'}};
const S={tn:'27772',tm:'RassLexx',st:false};let items=[],sel=null,box=null;const $=i=>document.getElementById(i);
// renderer
const cv=$('cv'),R=new THREE.WebGLRenderer({canvas:cv,antialias:true});
R.shadowMap.enabled=true;R.shadowMap.type=THREE.PCFSoftShadowMap;R.outputEncoding=THREE.sRGBEncoding;R.toneMapping=THREE.ACESFilmicToneMapping;
const sc=new THREE.Scene(),cam=new THREE.PerspectiveCamera(42,1,.1,300);sc.fog=new THREE.Fog(0x121916,50,120);
const es=new THREE.Scene(),sg=new THREE.SphereGeometry(50,32,16),pa=sg.attributes.position,cl=[];
for(let i=0;i<pa.count;i++){const t=(pa.getY(i)/50+1)/2;cl.push(.2+t*.8,.22+t*.78,.28+t*.72)}
sg.setAttribute('color',new THREE.Float32BufferAttribute(cl,3));es.add(new THREE.Mesh(sg,new THREE.MeshBasicMaterial({vertexColors:true,side:THREE.BackSide})));
[[0,40,0,20],[30,22,20,10],[-32,20,-8,10]].forEach(([x,y,z,s])=>{const m=new THREE.Mesh(new THREE.PlaneGeometry(s,s),new THREE.MeshBasicMaterial({color:new THREE.Color(7,7,7),side:THREE.DoubleSide}));m.position.set(x,y,z);m.lookAt(0,0,0);es.add(m)});
try{sc.environment=new THREE.PMREMGenerator(R).fromScene(es,.04).texture}catch(e){}
const hemi=new THREE.HemisphereLight(0xdfe8ff,0x40404a,.4),sun=new THREE.DirectionalLight(0xfff4e6,1.5);sun.position.set(9,18,11);sun.castShadow=true;
const smz=/Mobi|iPhone|iPad|Android/i.test(navigator.userAgent)?1024:2048;sun.shadow.mapSize.set(smz,smz);sun.shadow.bias=-.0005;sun.shadow.normalBias=.03;Object.assign(sun.shadow.camera,{left:-14,right:14,top:14,bottom:-14,far:60});sc.add(hemi,sun);
const gnd=new THREE.Mesh(new THREE.PlaneGeometry(200,200),new THREE.MeshStandardMaterial({color:0x2a3a32,roughness:.8}));gnd.rotation.x=-Math.PI/2;gnd.receiveShadow=true;sc.add(gnd);
[[10.12,.12,0,-5],[10.12,.12,0,5],[.12,10.12,-5,0],[.12,10.12,5,0]].forEach(([w,d,x,z])=>{const m=new THREE.Mesh(new THREE.BoxGeometry(w,.02,d),new THREE.MeshBasicMaterial({color:0xffd23a}));m.position.set(x,.012,z);sc.add(m)});
const grp=new THREE.Group();sc.add(grp);const rnd=i=>Math.abs(Math.sin(i*12.9898)*43758.5453)%1;
function sign(it,w,h,y,z){const c=document.createElement('canvas');c.width=1024;c.height=Math.round(1024*h/w);const x=c.getContext('2d'),H=c.height;
x.fillStyle=it.c;x.fillRect(0,0,1024,H);x.fillStyle='#fff';x.textBaseline='middle';x.font=`italic 900 ${H*.62}px sans-serif`;x.fillText(S.tn,30,H*.52);
let f=H*.32;x.textAlign='right';do{x.font=`bold ${f}px sans-serif`;f-=2}while(x.measureText(S.tm).width>512&&f>8);x.fillText(S.tm,1000,H*.52);
const t=new THREE.CanvasTexture(c);t.encoding=THREE.sRGBEncoding;t.anisotropy=8;const m=new THREE.Mesh(new THREE.PlaneGeometry(w,h),new THREE.MeshBasicMaterial({map:t}));m.position.set(0,y,z);return m}
function mkFloor(it,d,g){const c=document.createElement('canvas');c.width=c.height=1024;const x=c.getContext('2d');
if(d.f=='tiles'){const n=5,s=1024/n;for(let i=0;i<n;i++)for(let j=0;j<n;j++){x.fillStyle=(i+j)%2?it.c2:it.c;x.fillRect(i*s,j*s,s,s);x.strokeStyle='#0003';x.lineWidth=3;x.strokeRect(i*s,j*s,s,s)}}
else if(d.f=='wood'){x.fillStyle=it.c;x.fillRect(0,0,1024,1024);for(let k=0;k<16;k++){x.fillStyle=`rgba(0,0,0,${.04+rnd(k)*.1})`;x.fillRect(0,k*64,1024,64);x.fillStyle='#0005';x.fillRect(0,k*64,1024,2)}}
else{x.fillStyle=it.c;x.fillRect(0,0,1024,1024);for(let k=0;k<9000;k++){x.fillStyle=rnd(k)>.5?'#fff1':'#0002';x.fillRect(rnd(k+1)*1024,rnd(k+2)*1024,2,2)}}
const t=new THREE.CanvasTexture(c);t.encoding=THREE.sRGBEncoding;t.anisotropy=R.capabilities.getMaxAnisotropy();
const m=new THREE.Mesh(new THREE.PlaneGeometry(d.w,d.dd),new THREE.MeshStandardMaterial({map:t,roughness:.85}));m.rotation.x=-Math.PI/2;m.position.y=.02+items.filter(i=>D[i.t].f).indexOf(it)*.004;m.receiveShadow=true;g.add(m)}
function mkL(g,U,col,[x,y,z,I,dist]){const l=new THREE.PointLight(col,0,dist,2);l.userData.i=I;l.position.set(x,y,z);g.add(l);U.L.push(l)}
const dr=new THREE.Raycaster();
function settle(it){if(!D[it.t].sm)return;dr.set(new THREE.Vector3(it.x,4,it.z),new THREE.Vector3(0,-1,0));const h=dr.intersectObjects(grp.children.filter(g=>g!==it.g&&!g.userData.np),true).filter(h=>h.object.type=='Mesh')[0];it.y=h?h.point.y:0;applyT(it)}
function applyT(it){const g=it.g;g.rotation.order='YXZ';g.position.set(it.x,it.y,it.z);g.rotation.set(it.tl*Math.PI/180,it.a*Math.PI/180,0)}
function ptex(src){const t=new THREE.Texture(),im=new Image();t.encoding=THREE.sRGBEncoding;im.onload=()=>{t.image=im;t.needsUpdate=true};im.src=src;return t}
function phTex(){const c=document.createElement('canvas');c.width=c.height=128;const x=c.getContext('2d');x.fillStyle='#cfd2dc';x.fillRect(0,0,128,128);x.font='60px sans-serif';x.textAlign='center';x.textBaseline='middle';x.fillText('📷',64,68);const t=new THREE.CanvasTexture(c);t.encoding=THREE.sRGBEncoding;return t}
function wrapT(x,t,f,W,fn){x.font=fn(f);const L=[];let l='';(t||'').split(/\s+/).filter(Boolean).forEach(w=>{const n=l?l+' '+w:w;if(l&&x.measureText(n).width>W){L.push(l);l=w}else l=n});if(l)L.push(l);return L}
function fitT(x,t,f,W,H,lh,fn){let L;for(;f>12;f-=2){L=wrapT(x,t,f,W,fn);if(L.length*f*lh<=H&&L.every(l=>x.measureText(l).width<=W))break}return[L||[],f]}
function dl(x,t,f,W,H,cy,lh,fn,cx){const[L,g]=fitT(x,t,f,W,H,lh,fn);x.font=fn(g);L.forEach((l,i)=>x.fillText(l,cx||x.canvas.width/2,cy+(i-(L.length-1)/2)*g*lh))}
function star(x,cx,cy,R){x.beginPath();for(let i=0;i<10;i++){const r=i%2?R*.45:R,a=-Math.PI/2+i*Math.PI/5;x.lineTo(cx+r*Math.cos(a),cy+r*Math.sin(a))}x.closePath();x.fill()}
function flagTex(it){const c=document.createElement('canvas');c.width=512;c.height=768;const x=c.getContext('2d');x.fillStyle=it.c;x.fillRect(0,0,512,768);
if(it.pat){x.strokeStyle='rgba(0,0,0,.14)';x.lineWidth=14;for(let k=-2;k<9;k++){x.beginPath();x.moveTo(-20,k*110);x.lineTo(256,k*110+150);x.lineTo(540,k*110+40);x.stroke()}}
x.textAlign='center';x.textBaseline='middle';x.fillStyle=x.strokeStyle='#fff';x.lineWidth=7;
x.beginPath();x.arc(256,62,24,0,7);x.stroke();x.beginPath();x.moveTo(190,40);x.lineTo(226,62);x.lineTo(190,84);x.closePath();x.moveTo(322,40);x.lineTo(286,62);x.lineTo(322,84);x.closePath();x.stroke();
const hw=(it.hd||'').toUpperCase().split(/\s+/).filter(Boolean),first=hw[0]=='FIRST';if(first){x.font='italic 900 60px sans-serif';x.fillText('FIRST',256,128)}
dl(x,(first?hw.slice(1):hw).join(' '),44,400,90,first?195:150,1.05,f=>`900 ${f}px sans-serif`);
x.lineWidth=3;[272,548].forEach(y=>{x.beginPath();x.moveTo(70,y);x.lineTo(442,y);x.stroke()});
dl(x,(it.txt||'').toUpperCase(),112,430,250,410,1.06,f=>`${it.ital?'italic ':''}900 ${f}px sans-serif`);
dl(x,(it.ev||'').toUpperCase(),46,430,95,610,1.12,f=>`800 ${f}px sans-serif`);
const n=Math.max(0,Math.min(5,it.stars|0));x.font='400 30px sans-serif';x.fillText(it.sub||'',256,n?684:705);
for(let i=0;i<n;i++)star(x,256+(i-(n-1)/2)*62,738,22);return c}
function rr(x,px,py,w,h,r){x.beginPath();x.moveTo(px+r,py);x.arcTo(px+w,py,px+w,py+h,r);x.arcTo(px+w,py+h,px,py+h,r);x.arcTo(px,py+h,px,py,r);x.arcTo(px,py,px+w,py,r);x.closePath()}
function coverTex(it,W,H,kind){const c=document.createElement('canvas');c.width=W;c.height=H;const x=c.getContext('2d'),t=new THREE.CanvasTexture(c);t.encoding=THREE.sRGBEncoding;t.anisotropy=8;
const paint=im=>{x.shadowBlur=0;if(kind=='scr'){const gr=x.createLinearGradient(0,0,W,H);gr.addColorStop(0,'#1b2a6b');gr.addColorStop(1,'#8a4fe0');x.fillStyle=gr}else x.fillStyle=it.c;x.fillRect(0,0,W,H);
if(im){const s=Math.max(W/im.width,H/im.height),w=im.width*s,h=im.height*s;x.drawImage(im,(W-w)/2,(H-h)/2,w,h)}
if(kind=='scr'){x.fillStyle='rgba(0,0,0,.35)';x.fillRect(0,0,W,22)}
x.textAlign='center';x.textBaseline='middle';x.fillStyle='#fff';x.shadowColor='#000b';x.shadowBlur=im?16:0;const fn=f=>`900 ${f}px sans-serif`,up=(it.txt||'').toUpperCase(),sf=f=>`600 ${f}px sans-serif`;
if(kind=='port'){dl(x,up,90,W*.9,H*.4,H*.42,1.05,fn);dl(x,it.sub||'',40,W*.9,H*.14,H*.9,1.1,sf)}
if(kind=='mag'){dl(x,up,96,W*.92,H*.2,H*.13,1.05,fn);dl(x,it.sub||'',40,W*.9,H*.14,H*.9,1.1,sf)}
if(kind=='scr'){dl(x,it.txt||(S.tn+' '+S.tm),70,W*.8,H*.45,H*.47,1.1,fn);dl(x,it.sub||'',34,W*.8,H*.12,H*.68,1.1,sf)}
if(kind=='img'&&!im)dl(x,up,70,W*.8,H*.5,H*.5,1.1,fn);
t.needsUpdate=true};
paint(null);if(it.ph&&it.ph[0]){const im=new Image();im.onload=()=>paint(im);im.src=it.ph[0]}return t}
function build(it){const d=D[it.t],g=new THREE.Group(),U=g.userData;U.L=[];U.E=[];U.S=[];
if(d.f){mkFloor(it,d,g);U.np=1}
(d.p||[]).forEach(([w,h,dp,x,y,z,c,sh=''])=>{const mt=sh.includes('m'),col=c||it.c;
const ge=sh.includes('c')?new THREE.CylinderGeometry(w/2,w/2,h,32):sh.includes('s')?new THREE.SphereGeometry(w/2,28,18):sh.includes('p')?(()=>{const q=new THREE.ConeGeometry(w*.7071,h,4);q.rotateY(Math.PI/4);return q})():new THREE.BoxGeometry(w,h,dp);
const m=new THREE.MeshStandardMaterial({color:col,roughness:mt?.3:.6,metalness:mt?.85:.05,side:sh.includes('p')?THREE.DoubleSide:THREE.FrontSide});
if(sh.includes('e')){m.emissive=new THREE.Color(col);U.E.push(m)}
const me=new THREE.Mesh(ge,m);me.position.set(x,y,z);me.castShadow=!sh.includes('e');me.receiveShadow=true;g.add(me)});
if(d.s)g.add(sign(it,...d.s));
if(d.l)mkL(g,U,it.c,d.l);
if(d.sp){const q=d.sp,sp=new THREE.SpotLight(it.c,0,q[4],Math.PI/5,.6,1.5);sp.position.set(q[0],q[1],q[2]);sp.target.position.set(q[0],0,q[2]);sp.userData.i=q[3];g.add(sp,sp.target);U.L.push(sp);
const cn=new THREE.Mesh(new THREE.CylinderGeometry(.15,1.8,5,32,1,true),new THREE.MeshBasicMaterial({color:it.c,transparent:true,opacity:.13,blending:THREE.AdditiveBlending,depthWrite:false,side:THREE.DoubleSide}));cn.position.set(q[0],2.5,q[2]);U.S.push(cn);g.add(cn)}
if(d.k=='garland'){const n=90,im=new THREE.InstancedMesh(new THREE.BoxGeometry(.05,1,.012),new THREE.MeshStandardMaterial({color:it.c,metalness:.9,roughness:.2,side:THREE.DoubleSide}),n),o=new THREE.Object3D();
for(let i=0;i<n;i++){const L=1.1+rnd(i)*.8;o.position.set(-4.95+i*10/(n-1),7.1-L/2,(rnd(i+7)-.5)*.08);o.rotation.set(rnd(i+3)*.3,0,(rnd(i+5)-.5)*.14);o.scale.set(1,L,1);o.updateMatrix();im.setMatrixAt(i,o.matrix)}g.add(im)}
if(d.k=='string'){const n=26,bm=new THREE.MeshStandardMaterial({color:0xfff6d0,emissive:new THREE.Color(it.c),roughness:.3}),im=new THREE.InstancedMesh(new THREE.SphereGeometry(.1,14,10),bm,n),o=new THREE.Object3D(),pts=[];U.E.push(bm);
for(let i=0;i<n;i++){const x=-4.9+i*9.8/(n-1),y=7-.7*(1-Math.pow(x/4.9,2));o.position.set(x,y-.12,0);o.updateMatrix();im.setMatrixAt(i,o.matrix);pts.push(new THREE.Vector3(x,y,0))}
g.add(im,new THREE.Line(new THREE.BufferGeometry().setFromPoints(pts),new THREE.LineBasicMaterial({color:0x111111})));[[-3,6.5,.4],[0,6.3,.4],[3,6.5,.4]].forEach(p=>mkL(g,U,it.c,[...p,1.3,12]))}
if(d.k=='flag'){const t=new THREE.CanvasTexture(flagTex(it));t.encoding=THREE.sRGBEncoding;t.anisotropy=8;const mt=new THREE.MeshStandardMaterial({map:t,roughness:.85});[0,1].forEach(s=>{const m=new THREE.Mesh(new THREE.PlaneGeometry(2.4,3.6),mt);m.position.set(0,4.65,s?-.08:.08);m.rotation.y=s*Math.PI;m.castShadow=true;g.add(m)})}
if(d.k=='photog'){const pts=[],ph=it.ph;for(let i=0;i<=24;i++){const x=-4.9+i*9.8/24;pts.push(new THREE.Vector3(x,7-.7*(1-Math.pow(x/4.9,2)),0))}
g.add(new THREE.Line(new THREE.BufferGeometry().setFromPoints(pts),new THREE.LineBasicMaterial({color:0x111111})));
for(let i=0;i<7;i++){const x=-4.2+i*1.4,c=new THREE.Group();c.position.set(x,7-.7*(1-Math.pow(x/4.9,2))-.85,0);c.rotation.z=(rnd(i+9)-.5)*.22;
const fr=new THREE.Mesh(new THREE.BoxGeometry(1.1,1.35,.03),new THREE.MeshStandardMaterial({color:it.c,roughness:.6}));fr.castShadow=true;c.add(fr);
const pp=new THREE.Mesh(new THREE.PlaneGeometry(.95,.95),new THREE.MeshBasicMaterial({map:ph.length?ptex(ph[i%ph.length]):phTex()}));pp.position.set(0,.12,.02);c.add(pp);
const pb=pp.clone();pb.rotation.y=Math.PI;pb.position.z=-.02;c.add(pb);g.add(c)}}
const bx=(w,h,dp,x,y,z,col,m,ro)=>{const o=new THREE.Mesh(new THREE.BoxGeometry(w,h,dp),new THREE.MeshStandardMaterial({color:col,roughness:m?.3:.6,metalness:m?.85:.05}));o.position.set(x,y,z);if(ro)o.rotation.y=ro;o.castShadow=o.receiveShadow=true;g.add(o);return o};
const pl2=(w,h,tex,bs)=>new THREE.Mesh(new THREE.PlaneGeometry(w,h),bs?new THREE.MeshBasicMaterial({map:tex}):new THREE.MeshStandardMaterial({map:tex,roughness:.6}));
if(d.k=='port'){const p=pl2(.94,1.34,coverTex(it,420,580,'port'));p.rotation.x=-Math.PI/2;p.position.y=.1215;g.add(p)}
if(d.k=='mag'){const t=coverTex(it,420,580,'mag');for(let i=0;i<3;i++){const ro=(i-1)*.2,y=.006+i*.013;bx(.72,.012,.95,(i-1)*.03,y,(i-1)*.02,'#eeeeee',0,ro);const p=pl2(.7,.93,t);p.rotation.order='YXZ';p.rotation.set(-Math.PI/2,ro,0);p.position.set((i-1)*.03,y+.0062,(i-1)*.02);g.add(p)}}
if(d.k=='mac'){bx(1,.03,.7,0,.015,0,it.c,1);bx(.9,.004,.3,0,.032,-.12,'#222');bx(.36,.003,.2,0,.0315,.22,'#b5b8c0');
const lid=new THREE.Group();lid.position.set(0,.03,-.35);lid.rotation.x=-.3;g.add(lid);
const lb=new THREE.Mesh(new THREE.BoxGeometry(1,.7,.02),new THREE.MeshStandardMaterial({color:it.c,roughness:.3,metalness:.85}));lb.position.set(0,.35,-.01);lb.castShadow=true;lid.add(lb);
const bz=new THREE.Mesh(new THREE.PlaneGeometry(.97,.67),new THREE.MeshBasicMaterial({color:0x050505}));bz.position.set(0,.35,.0008);lid.add(bz);
const sp=pl2(.93,.6,coverTex(it,640,413,'scr'),1);sp.position.set(0,.36,.0016);lid.add(sp)}
if(d.k=='iflag'){const ar=it.ar||.667,w=Math.min(5,Math.max(1.6,3.6*ar)),t=coverTex(it,720,Math.round(720*3.6/w),'img');bx(1.4,.1,1.4,0,.05,0,'#222');bx(.1,6.6,.1,0,3.3,0,'#222',1);bx(w+.4,.08,.08,0,6.5,0,'#222',1);
[0,1].forEach(q=>{const m=pl2(w,3.6,t);m.position.set(0,4.65,q?-.08:.08);m.rotation.y=q*Math.PI;m.castShadow=true;g.add(m)})}
U.it=it;it.g=g;applyT(it);grp.add(g)}
function stage(){const s=S.st;sun.intensity=s?.04:1.5;hemi.intensity=s?.03:.4;const bg=s?0x040806:0x121916;sc.background=new THREE.Color(bg);sc.fog.color.set(bg);gnd.material.color.set(s?0x0e1511:0x2a3a32);
sc.traverse(o=>{if(o.material&&o.material.envMapIntensity!==undefined)o.material.envMapIntensity=s?.05:1});
items.forEach(i=>{const U=i.g.userData;U.L.forEach(l=>l.intensity=s?l.userData.i:0);U.E.forEach(m=>m.emissiveIntensity=s?3:1);U.S.forEach(m=>m.visible=s)})}
function add(t,x=0,z=0,r=0,c,c2,ex={}){const it={t,x,z,a:ex.a!==undefined?ex.a:r*90,y:ex.y||0,tl:ex.tl||0,c:c||D[t].c,c2:c2||'#f2f2f2',txt:ex.txt!==undefined?ex.txt:(D[t].txt||''),...Object.fromEntries(['ev','sub','hd','stars','pat','ital','ar','st'].map(k=>[k,ex[k]!==undefined?ex[k]:D[t][k]])),ph:ex.ph?[...ex.ph]:[]};items.push(it);build(it);stage();return it}
function rebuild(it){grp.remove(it.g);build(it);stage();if(sel==it)pick2(it)}
function syncP(){if(!sel)return;[['ia',sel.a],['iy',sel.y],['itl',sel.tl]].forEach(([k,v])=>{$(k).value=v;$(k+'o').textContent=Math.round(v*100)/100})}
function list(){const L=$('ls');L.innerHTML='';items.forEach(it=>{const b=document.createElement('button');b.textContent=D[it.t].n;if(it==sel)b.className='pr';b.onclick=()=>pick2(it);L.appendChild(b)})}
function pick2(it){sel=it;if(box){sc.remove(box);box=null}
if(it){box=new THREE.BoxHelper(it.g,0x48e57c);sc.add(box);$('sel').style.display='none';$('ctl').style.display='block';$('nm').textContent=D[it.t].n;$('sz').textContent=D[it.t].d;$('ic').value=it.c;$('l2').style.display=D[it.t].f=='tiles'?'':'none';$('ic2').value=it.c2;$('fr').style.display=D[it.t].k=='flag'?'':'none';$('ft').value=it.txt;$('fe').value=it.ev||'';$('fs2').value=it.sub||'';$('fh').value=it.hd||'';$('fst').value=it.stars|0;$('fp').checked=!!it.pat;$('fi').checked=!!it.ital;{const k=D[it.t].k;$('pr2').style.display=['photog','port','mag','mac','iflag'].includes(k)?'':'none';$('pb').textContent=k=='photog'?'Upload photos…':'Upload image…';$('cb').style.display=['port','mag','mac','iflag'].includes(k)?'':'none';$('ct').value=it.txt;$('cs').value=it.sub||'';}$('ix').value=it.x;$('iz').value=it.z;syncP()}
else{$('sel').style.display='block';$('ctl').style.display='none'}list()}
function save(){const o={S,items:items.map(({t,x,z,a,y,tl,c,c2,txt,ph,ev,sub,hd,stars,pat,ital,ar,st})=>({t,x,z,a,y,tl,c,c2,txt,ph,ev,sub,hd,stars,pat,ital,ar,st}))};try{localStorage.setItem('pitcad4',JSON.stringify(o))}catch(e){}return JSON.stringify(o)}
function load(s){const o=JSON.parse(s);items.forEach(i=>grp.remove(i.g));items=[];Object.assign(S,o.S);$('tn').value=S.tn;$('tm').value=S.tm;$('st').checked=S.st;o.items.filter(i=>D[i.t]).forEach(i=>add(i.t,i.x,i.z,i.r,i.c,i.c2,i));stage();pick2(null)}
function example(){load(JSON.stringify({S:{...S,st:false},items:[{t:'ftiles',x:0,z:0,r:0,c:'#48E57C',c2:'#121916'},{t:'tent',x:0,z:0,r:0,c:'#1c2a24'},{t:'drape',x:0,z:-5,r:0,c:'#14141c'},{t:'banner',x:0,z:-4.6,r:0,c:'#121916'},
{t:'shelf',x:-4.2,z:-2.9,r:1,c:'#121916'},{t:'shelf',x:4.2,z:-2.9,r:1,c:'#121916'},{t:'table',x:0,z:-3.3,r:0,c:'#d9efe2'},{t:'port',x:-2,z:-3.4,y:2.56,a:-8,c:'#121916'},{t:'mag',x:-.2,z:-3.3,y:2.56,a:15,c:'#48E57C'},{t:'mac',x:1.9,z:-3.2,y:2.56,a:0,c:'#c9ccd4'},{t:'chest',x:-2.4,z:.6,r:0,c:'#48E57C'},{t:'robot',x:2,z:1.6,r:0,c:'#2fcf68'},{t:'chair',x:-.2,z:-1.5,r:2,c:'#333333'},{t:'mon',x:4,z:2.8,r:3,c:'#121916'},
{t:'garland',x:0,z:4.95,r:0,c:'#48E57C'},{t:'string',x:0,z:0,r:0,c:'#caffdc'},{t:'fwin',x:-3.6,z:3.2,r:0,c:'#e0261f'},{t:'fcap',x:0,z:3.3,r:0,c:'#ff6a13'},{t:'finsp',x:3.4,z:3.2,r:0,c:'#f2531c'},{t:'photog',x:0,z:-2.2,r:0,c:'#ffffff'},{t:'stage',x:-4.5,z:4.3,r:0,c:'#48E57C'},{t:'stage',x:4.5,z:4.3,r:0,c:'#9dffbf'}]}))}
// menu
const cats={};Object.entries(D).forEach(([k,d])=>(cats[d.cat]=cats[d.cat]||[]).push(k));
for(const c in cats){const h=document.createElement('h4');h.textContent=c;const g=document.createElement('div');g.className='g';cats[c].forEach(k=>{const b=document.createElement('button');b.textContent=D[k].n;b.onclick=()=>{const i=add(k,0,0);settle(i);pick2(i);save()};g.appendChild(b)});$('items').append(h,g)}
['tn','tm'].forEach(k=>$(k).oninput=e=>{S[k]=e.target.value;items.filter(i=>D[i.t].s||D[i.t].k=='flag').forEach(rebuild);save()});
$('st').onchange=e=>{S.st=e.target.checked;stage();save()};$('au').onchange=e=>auto=e.target.checked;
$('ic').oninput=e=>{if(sel){sel.c=e.target.value;rebuild(sel);save()}};$('ic2').oninput=e=>{if(sel){sel.c2=e.target.value;rebuild(sel);save()}};
$('ix').oninput=e=>{if(sel){sel.x=+e.target.value;sel.g.position.x=sel.x;save()}};$('iz').oninput=e=>{if(sel){sel.z=+e.target.value;sel.g.position.z=sel.z;save()}};
[['ia','a'],['iy','y'],['itl','tl']].forEach(([k,p])=>$(k).oninput=e=>{if(sel){sel[p]=+e.target.value;applyT(sel);syncP();save()}});
[['ft','txt'],['fe','ev'],['fs2','sub'],['fh','hd'],['ct','txt'],['cs','sub']].forEach(([k,p])=>$(k).oninput=e=>{if(sel){sel[p]=e.target.value;rebuild(sel);save()}});
$('fst').oninput=e=>{if(sel){sel.stars=Math.max(0,Math.min(5,+e.target.value||0));rebuild(sel);save()}};$('fp').onchange=e=>{if(sel){sel.pat=e.target.checked?1:0;rebuild(sel);save()}};$('fi').onchange=e=>{if(sel){sel.ital=e.target.checked?1:0;rebuild(sel);save()}};$('pb').onclick=()=>$('pf').click();$('pc').onclick=()=>{if(sel){sel.ph=[];rebuild(sel);save()}};
$('pf').onchange=async e=>{if(!sel)return;const it=sel;for(const f of [...e.target.files].slice(0,12)){await new Promise(res=>{const r=new FileReader();r.onload=()=>{const im=new Image();im.onload=()=>{const c=document.createElement('canvas'),g2=c.getContext('2d');if(D[it.t].k=='photog'){const m=Math.min(im.width,im.height);c.width=c.height=320;g2.drawImage(im,(im.width-m)/2,(im.height-m)/2,m,m,0,0,320,320)}else{const q=Math.min(1,(D[it.t].k=='iflag'?1100:700)/Math.max(im.width,im.height));c.width=Math.max(1,im.width*q|0);c.height=Math.max(1,im.height*q|0);g2.drawImage(im,0,0,c.width,c.height);it.ar=im.width/im.height}it.ph.push(c.toDataURL('image/jpeg',.85));res()};im.onerror=res;im.src=r.result};r.readAsDataURL(f)})}
it.ph=D[it.t].k=='photog'?it.ph.slice(-12):it.ph.slice(-1);rebuild(it);save();e.target.value=''};
const rot=(d=90)=>{if(sel){sel.a=((sel.a+d)%360+360)%360;applyT(sel);syncP();save()}},del=()=>{if(sel){grp.remove(sel.g);items=items.filter(i=>i!=sel);pick2(null);save()}};
$('rt').onclick=()=>rot(90);$('dl').onclick=del;$('dp').onclick=()=>{if(sel){pick2(add(sel.t,sel.x+1,sel.z+1,sel.r,sel.c,sel.c2,sel));save()}};
$('cl').onclick=()=>{items.forEach(i=>grp.remove(i.g));items=[];pick2(null);save()};$('ex').onclick=()=>{example();save()};
$('sv').onclick=()=>{$('js').value=save();$('js').select()};$('ld').onclick=()=>{try{load($('js').value);save()}catch(e){alert('Invalid layout code')}};
addEventListener('keydown',e=>{if(/INPUT|TEXTAREA/.test(e.target.tagName))return;if(e.key=='r'||e.key=='R')rot();if(e.key=='q'||e.key=='Q')rot(-15);if(e.key=='e'||e.key=='E')rot(15);if(sel&&(e.key=='ArrowUp'||e.key=='ArrowDown')){e.preventDefault();sel.y=Math.max(0,Math.min(12,sel.y+(e.key=='ArrowUp'?.25:-.25)));applyT(sel);syncP();save()}if(e.key=='Delete'||e.key=='Backspace')del()});
// camera (full 360)
let M='o',th=.6,ph=1,rd=24,yaw=0,pit=0,auto=false,fov=42;const tg=new THREE.Vector3(0,2.5,0);
function cm(){if(auto){M=='o'?th+=.004:yaw+=.004}
if(M=='o'){cam.position.set(tg.x+rd*Math.sin(ph)*Math.sin(th),tg.y+rd*Math.cos(ph),tg.z+rd*Math.sin(ph)*Math.cos(th));cam.lookAt(tg)}
else{cam.position.set(0,5.4,0);cam.lookAt(Math.sin(yaw)*Math.cos(pit),5.4+Math.sin(pit),-Math.cos(yaw)*Math.cos(pit))}
if(cam.fov!=fov){cam.fov=fov;cam.updateProjectionMatrix()}}
const mode=m=>{M=m;fov=m=='e'?80:42};
$('mOrbit')?.addEventListener('click',()=>{mode('o');ph=1;rd=24});$('mTop')?.addEventListener('click',()=>{mode('o');ph=.04;rd=26});$('mInside')?.addEventListener('click',()=>{mode('e');yaw=0;pit=0});
$('v1').onclick=()=>{mode('o');ph=1;rd=24};$('v2').onclick=()=>{mode('o');ph=.04;rd=26};$('v3').onclick=()=>{mode('e');yaw=0;pit=0};
const zoom=k=>{if(M=='o')rd=Math.min(60,Math.max(6,rd+k));else fov=Math.min(100,Math.max(35,fov+k*3))};$('zi').onclick=()=>zoom(-2);$('zo').onclick=()=>zoom(2);
cv.addEventListener('wheel',e=>{e.preventDefault();zoom(e.deltaY*.02)},{passive:false});
const rc=new THREE.Raycaster(),pl=new THREE.Plane(new THREE.Vector3(0,1,0),0),mv=new THREE.Vector2(),v=new THREE.Vector3();let drag=null,orb=null;
function ray(e){const r=cv.getBoundingClientRect();mv.set((e.clientX-r.left)/r.width*2-1,-((e.clientY-r.top)/r.height)*2+1);rc.setFromCamera(mv,cam)}
const pts=new Map();let pinch=null,tapSel=false;cv.addEventListener('contextmenu',e=>e.preventDefault());cv.addEventListener('pointerdown',e=>{cv.setPointerCapture(e.pointerId);pts.set(e.pointerId,{x:e.clientX,y:e.clientY});if(pts.size==2){drag=orb=null;tapSel=false;const[a,b]=[...pts.values()];pinch=Math.hypot(a.x-b.x,a.y-b.y);return}tapSel=true;if(M=='e'){orb={x:e.clientX,y:e.clientY};return}
ray(e);const h=rc.intersectObjects(grp.children.filter(g=>!g.userData.np),true)[0];
if(h){let o=h.object;while(o&&!o.userData.it)o=o.parent;pick2(o.userData.it);rc.ray.intersectPlane(pl,v);drag={ox:o.position.x-v.x,oz:o.position.z-v.z}}else{pick2(null);orb={x:e.clientX,y:e.clientY}}});
cv.addEventListener('pointermove',e=>{if(pts.has(e.pointerId))pts.set(e.pointerId,{x:e.clientX,y:e.clientY});if(pinch!==null&&pts.size>=2){const[a,b]=[...pts.values()],d=Math.hypot(a.x-b.x,a.y-b.y);zoom((pinch-d)*.05);pinch=d;return}if(drag&&sel){ray(e);if(rc.ray.intersectPlane(pl,v)){const q=n=>Math.round(n*4)/4,c=n=>Math.max(-8,Math.min(8,n));
sel.x=c(q(v.x+drag.ox));sel.z=c(q(v.z+drag.oz));if(D[sel.t].sm)settle(sel);else applyT(sel);syncP();$('ix').value=sel.x;$('iz').value=sel.z}}
else if(orb){const dx=e.clientX-orb.x,dy=e.clientY-orb.y;if(M=='o'){th-=dx*.008;ph=Math.max(.04,Math.min(1.5,ph-dy*.006))}else{yaw-=dx*.005;pit=Math.max(-1.3,Math.min(1.3,pit+dy*.005))}orb={x:e.clientX,y:e.clientY}}});
const up=e=>{pts.delete(e.pointerId);if(pts.size<2)pinch=null;if(drag)save();drag=orb=null;if(tapSel&&e.type=='pointerup'&&sel&&mq.matches)setTab('edit');tapSel=false};cv.addEventListener('pointerup',up);cv.addEventListener('pointercancel',up);
function rs(){const r=$('vw').getBoundingClientRect();R.setPixelRatio(Math.min(window.devicePixelRatio||1,1.75));R.setSize(Math.max(1,r.width),Math.max(1,r.height),false);cam.aspect=Math.max(.1,r.width)/Math.max(1,r.height);cam.updateProjectionMatrix()}
new ResizeObserver(rs).observe($('vw'));
(function loop(){requestAnimationFrame(loop);cm();if(box&&sel)box.update();R.render(sc,cam)})();

const mq=matchMedia('(max-width:820px)');let tab='parts',menu=false;
function setTab(t){tab=(tab===t&&arguments[1]!==1)?'':t;ui()}
function ui(){document.body.dataset.tab=tab;document.body.classList.toggle('menu',menu);$('tP').className=tab=='parts'?'pr':'';$('tE').className=tab=='edit'?'pr':'';$('tM').className=menu?'pr':''}
$('tP').onclick=()=>setTab('parts');$('tE').onclick=()=>setTab('edit');$('tM').onclick=()=>{menu=!menu;ui()};
const _sT=setTab;setTab=function(t){if(t=='edit'){tab='edit';ui()}else _sT(t)};
if(mq.matches){$('hint').textContent='Drag a part to move it · drag empty space to look around · pinch to zoom';setTimeout(()=>{const h=$('hint');if(h.style.color!='rgb(255, 128, 128)')h.style.opacity=0},7000)}
ui();
let saved=null;try{saved=localStorage.getItem('pitcad4')}catch(e){}
try{if(saved)load(saved);else example()}catch(e){}stage();rs();
</script></body></html>
