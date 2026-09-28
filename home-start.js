(function(){
"use strict";
if(window.__pcpHome)return; window.__pcpHome=true;
if(location.hash||/[?&](id|top)=/.test(location.search))return;   /* ?top=1 pour rester tout en haut */
try{ if("scrollRestoration" in history)history.scrollRestoration="manual"; }catch(e){}

var touched=false;
["touchstart","wheel","keydown","mousedown"].forEach(function(ev){
  window.addEventListener(ev,function(e){
    var t=e.target;
    if(t&&t.closest&&t.closest("#pcp-splash"))return;
    touched=true;
  },{passive:true,capture:true});
});

function norm(t){
  t=(t||"").toLowerCase();
  try{ t=t.normalize("NFD").replace(/[\u0300-\u036f]/g,""); }catch(e){}
  return t.replace(/\s+/g," ").trim();
}
function findHeading(){
  var els=document.querySelectorAll("h1,h2,h3,h4,h5,div,span,p"), i, e;
  for(i=0;i<els.length;i++){
    e=els[i];
    if(e.childElementCount>0)continue;
    if(/^nos realisations$/.test(norm(e.textContent)))return e;
  }
  return null;
}
var SEL='[id*="partner" i],[class*="partner" i],[id*="sponsor" i],[class*="sponsor" i],[id*="partenaire" i],[class*="partenaire" i]';
function findBanner(h){
  var list=document.querySelectorAll(SEL), best=null, i, e, r;
  for(i=0;i<list.length;i++){
    e=list[i];
    if(e.contains(h)||h.contains(e))continue;
    if(!(e.compareDocumentPosition(h)&Node.DOCUMENT_POSITION_FOLLOWING))continue;
    r=e.getBoundingClientRect();
    if(r.height<20||r.width<100)continue;
    best=e;
  }
  while(best&&best.parentElement&&best.parentElement.matches&&best.parentElement.matches(SEL)&&!best.parentElement.contains(h)){
    best=best.parentElement;
  }
  return best;
}
function headerBottom(){
  var max=0, vh=window.innerHeight, els=document.body.querySelectorAll("*"), i, e, cs, r;
  for(i=0;i<els.length;i++){
    e=els[i];
    if(e.id==="pcp-splash"||(e.closest&&e.closest("#pcp-splash")))continue;
    cs=getComputedStyle(e);
    if(cs.position!=="fixed"&&cs.position!=="sticky")continue;
    r=e.getBoundingClientRect();
    if(r.height<30||r.width<window.innerWidth*0.6)continue;
    if(r.top<-5||r.top>vh*0.35)continue;
    if(r.bottom<vh*0.5&&r.bottom>max)max=r.bottom;
  }
  return max;
}
function place(){
  if(touched)return;
  var h=findHeading(); if(!h)return;
  var target=findBanner(h)||h;
  var hb=headerBottom();
  var y=target.getBoundingClientRect().top+(window.pageYOffset||0)-hb-12;
  y=Math.max(0,Math.round(y));
  if(Math.abs((window.pageYOffset||0)-y)<4)return;
  try{ window.scrollTo({top:y,left:0,behavior:"instant"}); }catch(e){ window.scrollTo(0,y); }
}
[150,700,1500,2600,4000,5300].forEach(function(ms){ setTimeout(place,ms); });
window.addEventListener("load",function(){ setTimeout(place,100); });
})();
