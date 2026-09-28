(function(){
"use strict";
if(window.__pcpSplash)return; window.__pcpSplash=true;
var force=/[?&]splash=1/.test(location.search);
try{
  if(!force&&sessionStorage.getItem("pcp_splash"))return;
  sessionStorage.setItem("pcp_splash","1");
}catch(e){}
try{ if(!force&&window.matchMedia&&matchMedia("(prefers-reduced-motion: reduce)").matches)return; }catch(e){}

var MIN=10000, FADE=600, MAXW=10500;
var vw=window.innerWidth||360, vh=window.innerHeight||640;
function rnd(a,b){return a+Math.random()*(b-a);}
function clamp(v,a,b){return v<a?a:(v>b?b:v);}

/* ---------- geometrie ---------- */
var lw=Math.min(vw*0.92,460,vh*0.5*420/295), lh=lw*295/420;
var ly=Math.min(vh*0.56,vh-lh-28), lx=(vw-lw)/2;
var sx=vw/2, sy=ly+lh*112/295;
var ld=Math.min(vw*0.6,vh*0.3,300);
var fx=vw/2, fy=Math.max(vh*0.33,ld/2+56);

/* ---------- racine ---------- */
var root=document.createElement("div");
root.id="pcp-splash"; root.setAttribute("aria-hidden","true");
root.style.cssText="position:fixed;left:0;top:0;width:100%;height:100%;z-index:2147483000;overflow:hidden;background:radial-gradient(ellipse at 50% 36%,#171c38 0%,#0d0f1e 55%,#070810 100%);touch-action:manipulation";
function box(x,y,w,h,extra){
  var d=document.createElement("div");
  d.style.cssText="position:absolute;left:"+x+"px;top:"+y+"px;width:"+w+"px;height:"+h+"px;pointer-events:none;"+(extra||"");
  return d;
}

/* aura derriere le logo */
var aura=box(fx-ld*0.9,fy-ld*0.9,ld*1.8,ld*1.8,"opacity:0;background:radial-gradient(circle,rgba(45,212,191,.28) 0%,rgba(236,72,153,.16) 38%,rgba(0,0,0,0) 68%)");
root.appendChild(aura);

/* ordinateur portable */
function laptopSVG(){
  var s='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 295" width="100%" height="100%">'
  +'<defs>'
  +'<linearGradient id="pcpL" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#373b4d"/><stop offset="1" stop-color="#14161e"/></linearGradient>'
  +'<linearGradient id="pcpB" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#858b9e"/><stop offset="1" stop-color="#454a5b"/></linearGradient>'
  +'<radialGradient id="pcpS" cx="50%" cy="50%" r="70%"><stop offset="0" stop-color="#1d2b63"/><stop offset="1" stop-color="#05070f"/></radialGradient>'
  +'<radialGradient id="pcpG" cx="50%" cy="50%" r="60%"><stop offset="0" stop-color="#cfeaff" stop-opacity=".95"/><stop offset=".45" stop-color="#5fb6ff" stop-opacity=".45"/><stop offset="1" stop-color="#5fb6ff" stop-opacity="0"/></radialGradient>'
  +'<linearGradient id="pcpR" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".10"/><stop offset=".45" stop-color="#fff" stop-opacity="0"/></linearGradient>'
  +'</defs>'
  +'<ellipse cx="210" cy="285" rx="192" ry="9" fill="#000" opacity=".55"/>'
  +'<path d="M60 218 L360 218 L404 268 L16 268 Z" fill="url(#pcpB)"/>'
  +'<path d="M16 268 L404 268 L404 273 Q404 278 398 278 L22 278 Q16 278 16 273 Z" fill="#8f95a8"/>';
  var rows=[224,231,238,245], r, k;
  for(r=0;r<rows.length;r++){
    var y=rows[r], t=(y-218)/50;
    var xl=60-44*t+12, xr=360+44*t-12, n=15, step=(xr-xl)/n;
    for(k=0;k<n;k++){
      s+='<rect x="'+(xl+k*step+1).toFixed(1)+'" y="'+y+'" width="'+(step-2).toFixed(1)+'" height="5" rx="1.2" fill="#2a2e3c"/>';
    }
  }
  s+='<rect x="175" y="253" width="70" height="11" rx="2.5" fill="#2c3040" stroke="#4d5368" stroke-width=".8"/>'
  +'<rect x="52" y="211" width="316" height="8" rx="3" fill="#1a1c26"/>'
  +'<rect x="40" y="8" width="340" height="207" rx="15" fill="url(#pcpL)" stroke="#50556d" stroke-width="1.2"/>'
  +'<rect x="52" y="20" width="316" height="184" rx="6" fill="url(#pcpS)"/>'
  +'<rect id="pcpGlow" x="52" y="20" width="316" height="184" rx="6" fill="url(#pcpG)" opacity="0"/>'
  +'<rect x="52" y="20" width="316" height="184" rx="6" fill="url(#pcpR)"/>'
  +'<circle cx="210" cy="14" r="2.2" fill="#0a0b10" stroke="#3b3f52" stroke-width=".8"/>'
  +'</svg>';
  return s;
}
var lap=box(lx,ly,lw,lh,"");
lap.innerHTML=laptopSVG();
root.appendChild(lap);

/* faisceau lumineux a la sortie de l'ecran */
var bs=ld*1.5;
var beam=box(sx-bs/2,sy-bs/2,bs,bs,"opacity:0;background:radial-gradient(circle,rgba(190,230,255,.75) 0%,rgba(236,72,153,.28) 38%,rgba(0,0,0,0) 70%)");
root.appendChild(beam);

/* poussiere d'etoiles + avatars (canvas) */
var dpr=Math.min(window.devicePixelRatio||1,2);
var cv=document.createElement("canvas");
cv.width=Math.round(vw*dpr); cv.height=Math.round(vh*dpr);
cv.style.cssText="position:absolute;left:0;top:0;width:"+vw+"px;height:"+vh+"px;pointer-events:none";
root.appendChild(cv);
var X=cv.getContext("2d");

/* logo */
function logoSVG(){
  return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="100%" height="100%">'
  +'<circle cx="250" cy="250" r="245" fill="#12152a"/>'
  +'<circle cx="250" cy="250" r="244" fill="none" stroke="#2a2e58" stroke-width="2.5"/>'
  +'<circle cx="250" cy="250" r="228" fill="none" stroke="#23274d" stroke-width="2.5"/>'
  +'<line x1="250" y1="128" x2="250" y2="256" stroke="#ec4899" stroke-width="5"/>'
  +'<line x1="250" y1="256" x2="157" y2="335" stroke="#3a3d5c" stroke-width="5"/>'
  +'<line x1="250" y1="256" x2="343" y2="335" stroke="#3a3d5c" stroke-width="5"/>'
  +'<circle cx="250" cy="128" r="33" fill="#f1f2f7"/>'
  +'<circle cx="157" cy="335" r="28" fill="#ff4fa3"/>'
  +'<circle cx="343" cy="335" r="28" fill="#2dd4bf"/>'
  +'<circle cx="250" cy="256" r="42" fill="#f1f2f7"/>'
  +'<text x="250" y="256" dy=".35em" text-anchor="middle" font-family="Georgia,\'DejaVu Serif\',serif" font-weight="700" font-size="56" fill="#15161c">P</text>'
  +'</svg>';
}
var logo=box(fx-ld/2,fy-ld/2,ld,ld,"opacity:0;filter:drop-shadow(0 0 16px rgba(45,212,191,.35))");
logo.innerHTML=logoSVG();
root.appendChild(logo);

(document.body||document.documentElement).appendChild(root);

/* ---------- particules ---------- */
var AV=[["Cl","#d97757","#fff"],["GP","#10a37f","#fff"],["Ge","#4285f4","#fff"],["Co","#7c4dff","#fff"],["GH","#24292f","#fff"],["VS","#007acc","#fff"],["W","#2b579a","#fff"],["X","#217346","#fff"],["P","#d24726","#fff"],["Ch","#fbbc04","#222"],["WA","#25d366","#fff"],["Fb","#ffa000","#222"],["Py","#3776ab","#ffd43b"],["JS","#f7df1e","#222"],["TG","#229ed9","#fff"],["H5","#e34f26","#fff"]];
var rxMax=vw/2-22;
var ryMax=Math.max(ld/2+40,Math.min(fy-34,ly-fy+40));
var P=[], i;
function orbit(b,dust){
  var lo=ld/2+34;
  b.rx=clamp(rnd(dust?0.4:0.62,1.0)*rxMax,Math.min(lo,rxMax),rxMax);
  b.ry=Math.max(rnd(0.62,1.0)*ryMax,Math.min(ld/2+30,ryMax));
  b.a0=rnd(0,Math.PI*2);
  b.w=(Math.random()<0.5?-1:1)*rnd(dust?0.10:0.14,dust?0.34:0.30);
  b.ph=rnd(0,6.28);
  b.cv=rnd(-60,60);
}
for(i=0;i<AV.length;i++){
  var b={ic:AV[i],dust:false,sz:rnd(12,16)*Math.min(1.25,Math.max(.85,vw/380)),d:rnd(900,2800),du:rnd(1300,1700)};
  orbit(b,false); P.push(b);
}
for(i=0;i<70;i++){
  var q={dust:true,sz:rnd(0.7,2.2),d:rnd(800,3000),du:rnd(1200,1900),tint:Math.random()<0.25?"255,79,163":(Math.random()<0.3?"45,212,191":"255,255,255")};
  orbit(q,true); P.push(q);
}
function easeOut(p){return 1-Math.pow(1-p,3);}
var raf=0, t0=0, ended=false;
function draw(now){
  if(ended)return;
  if(!t0)t0=now;
  var t=now-t0, j, b;
  X.setTransform(dpr,0,0,dpr,0,0);
  X.clearRect(0,0,vw,vh);
  for(j=0;j<P.length;j++){
    b=P[j];
    var p=clamp((t-b.d)/b.du,0,1);
    if(p<=0)continue;
    var e=easeOut(p), a=b.a0+b.w*(t/1000);
    var ox=fx+Math.cos(a)*b.rx+Math.sin(t/700+b.ph)*4;
    var oy=fy+Math.sin(a)*b.ry+Math.cos(t/900+b.ph)*4;
    var x=sx+(ox-sx)*e+Math.sin(Math.PI*p)*b.cv;
    var y=sy+(oy-sy)*e;
    if(b.dust){
      var al=Math.min(1,p*3)*(0.45+0.55*Math.abs(Math.sin(t/380+b.ph)));
      X.fillStyle="rgba("+b.tint+","+al.toFixed(3)+")";
      X.beginPath(); X.arc(x,y,b.sz*(0.4+0.6*e),0,6.2832); X.fill();
    }else{
      var r=b.sz*e;
      X.save();
      X.globalAlpha=Math.min(1,p*2.5);
      X.shadowColor=b.ic[1]; X.shadowBlur=9;
      X.fillStyle=b.ic[1];
      X.beginPath(); X.arc(x,y,r,0,6.2832); X.fill();
      X.shadowBlur=0;
      X.lineWidth=1; X.strokeStyle="rgba(255,255,255,.4)"; X.stroke();
      X.fillStyle=b.ic[2];
      X.font="700 "+(r*0.92).toFixed(1)+"px system-ui,Arial,sans-serif";
      X.textAlign="center"; X.textBaseline="middle";
      X.fillText(b.ic[0],x,y+r*0.04);
      X.restore();
    }
  }
  raf=requestAnimationFrame(draw);
}
raf=requestAnimationFrame(draw);

/* ---------- animations ---------- */
function anim(el,kf,opt){ try{ return el.animate(kf,opt); }catch(e){ return null; } }
var dx=sx-fx, dy=sy-fy;
anim(lap,[{transform:"translateY(46px)",opacity:0},{transform:"translateY(0)",opacity:1}],{duration:900,easing:"cubic-bezier(.2,.8,.2,1)",fill:"both"});
anim(root.querySelector("#pcpGlow"),[{opacity:0},{opacity:.95,offset:.35},{opacity:.4}],{duration:1900,delay:350,fill:"both"});
anim(beam,[{opacity:0,transform:"scale(.3)"},{opacity:1,transform:"scale(.9)",offset:.4},{opacity:0,transform:"scale(1.5)"}],{duration:1300,delay:550,easing:"ease-out",fill:"both"});
anim(aura,[{opacity:0,transform:"scale(.7)"},{opacity:1,transform:"scale(1)"}],{duration:1800,delay:900,easing:"ease-out",fill:"both"});
var lg=anim(logo,[
  {opacity:0,transform:"translate("+dx+"px,"+dy+"px) scale(.08)"},
  {opacity:1,transform:"translate("+(dx*0.55)+"px,"+(dy*0.55)+"px) scale(.45)",offset:.25},
  {opacity:1,transform:"translate(0,0) scale(1.07)",offset:.85},
  {opacity:1,transform:"translate(0,0) scale(1)"}
],{duration:1900,delay:600,easing:"cubic-bezier(.25,.8,.3,1)",fill:"both"});
if(!lg)logo.style.opacity=1;

/* ---------- fin ---------- */
var loaded=document.readyState==="complete", minDone=false;
function cleanup(){
  ended=true;
  if(raf)cancelAnimationFrame(raf);
  if(root.parentNode)root.parentNode.removeChild(root);
}
function end(fast){
  if(ended&&!root.parentNode)return;
  if(root.__ending)return; root.__ending=true;
  var dur=fast?260:FADE;
  var a=anim(root,[{opacity:1},{opacity:0}],{duration:dur,easing:"ease-in",fill:"forwards"});
  anim(logo,[{transform:"translate(0,0) scale(1)"},{transform:"translate(0,0) scale(1.14)"}],{duration:dur,fill:"forwards"});
  if(a)a.onfinish=cleanup;
  setTimeout(cleanup,dur+200);
}
function maybeEnd(){ if(minDone&&loaded)end(false); }
window.addEventListener("load",function(){ loaded=true; maybeEnd(); });
setTimeout(function(){ minDone=true; maybeEnd(); },MIN);
setTimeout(function(){ end(false); },MAXW);
root.addEventListener("click",function(){ end(true); });
root.addEventListener("touchstart",function(){ end(true); },{passive:true});
})();
