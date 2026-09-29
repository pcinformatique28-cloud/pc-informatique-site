(function(){
if(window.__pwdEye)return; window.__pwdEye=true;
var EYE='<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M1 12s4-7 11-7 11 7 11 7-4 7-11 7S1 12 1 12z"/><circle cx="12" cy="12" r="3"/></svg>';
var OFF='<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M17.94 17.94A10.94 10.94 0 0 1 12 19c-7 0-11-7-11-7a19.8 19.8 0 0 1 5.06-5.94M9.9 4.24A10.9 10.9 0 0 1 12 4c7 0 11 7 11 7a19.7 19.7 0 0 1-3.17 4.19M14.12 14.12A3 3 0 1 1 9.88 9.88"/><path d="M1 1l22 22"/></svg>';
var st=document.createElement("style");
st.textContent=".pe-wrap{position:relative;display:block;width:100%}.pe-wrap>input{width:100%;box-sizing:border-box;padding-right:48px!important}.pe-btn{position:absolute!important;right:4px!important;top:50%!important;transform:translateY(-50%)!important;width:34px!important;height:34px!important;min-width:0!important;border:0!important;background:transparent!important;color:#475569!important;cursor:pointer;padding:0!important;display:flex!important;align-items:center!important;justify-content:center!important;border-radius:8px!important;box-shadow:none!important}.pe-btn:active{background:rgba(0,0,0,.08)}";
document.head.appendChild(st);
function add(inp){
if(inp.getAttribute("data-pe")||(inp.closest&&inp.closest(".pwrap")))return;
inp.setAttribute("data-pe","1");
var cs=getComputedStyle(inp);
var wrap=document.createElement("span");
wrap.className="pe-wrap";
wrap.style.margin=cs.margin;
inp.style.margin="0";
inp.parentNode.insertBefore(wrap,inp);
wrap.appendChild(inp);
var b=document.createElement("button");
b.type="button"; b.className="pe-btn";
b.setAttribute("aria-label","Afficher le mot de passe");
b.innerHTML=EYE;
b.onclick=function(){
var show=inp.type==="password";
inp.type=show?"text":"password";
b.innerHTML=show?OFF:EYE;
b.setAttribute("aria-label",show?"Masquer le mot de passe":"Afficher le mot de passe");
try{inp.focus();}catch(e){}
};
wrap.appendChild(b);
}
function scan(){
var l=document.querySelectorAll('input[type="password"]');
for(var i=0;i<l.length;i++)add(l[i]);
}
scan();
try{
new MutationObserver(scan).observe(document.body,{childList:true,subtree:true});
}catch(e){}
})();
