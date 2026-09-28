(function(){
if(document.getElementById("qrw"))return;
var IMG="qr-pc-informatique.png";
var st=document.createElement("style");
st.textContent="#qrw{max-width:520px;margin:0 auto 64px;padding:8px 16px;text-align:center;color:#fff}#qrw h3{margin:0 0 10px;font-size:16px}#qrw .box{display:inline-block;background:#fff;padding:8px;border-radius:12px;cursor:pointer}#qrw img{display:block;image-rendering:pixelated}#qrw p{font-size:14px;opacity:.9;margin:10px 0}#qrw a.b,#qrfs a.b{display:inline-block;margin:4px;padding:10px 14px;border-radius:12px;background:linear-gradient(135deg,#2dd4bf,#ec4899);color:#000;font-weight:700;text-decoration:none}#qrfs{position:fixed;inset:0;z-index:9999;background:rgba(10,12,30,.96);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:14px;padding:16px;color:#fff;text-align:center}#qrfs .big{background:#fff;padding:14px;border-radius:16px}#qrfs img{display:block;width:min(80vw,60vh);height:min(80vw,60vh);image-rendering:pixelated}#qrfs button{padding:10px 18px;border-radius:12px;border:0;background:#ffffff26;color:#fff;font:inherit;font-weight:700;cursor:pointer}";
document.head.appendChild(st);
var w=document.createElement("div"); w.id="qrw"; document.body.appendChild(w);
function full(){
var o=document.createElement("div"); o.id="qrfs";
o.innerHTML='<div class="big"><img src="'+IMG+'" alt="QR"></div><div>Scanne pour ouvrir le site PC-INFORMATIQUE</div><div><a class="b" href="qr.html">Formats &amp; impression</a><button type="button" id="qrx">Fermer</button></div>';
document.body.appendChild(o);
function close(){ if(o.parentNode)o.parentNode.removeChild(o); }
o.onclick=function(e){ if(e.target===o)close(); };
document.getElementById("qrx").onclick=close;
}
function anon(){
w.innerHTML='<h3>Code QR PC-INFORMATIQUE</h3><div class="box" id="qrm"><img src="'+IMG+'" width="56" height="56" alt="QR"></div><p id="qrmsg" style="display:none"></p>';
document.getElementById("qrm").onclick=function(){
var m=document.getElementById("qrmsg"); m.style.display="block";
m.innerHTML='Inscris-toi pour voir ce code.<br><a class="b" href="inscription.html">S\'inscrire</a><a class="b" href="connexion.html">Connexion</a>';
};
}
function ok(){
w.innerHTML='<h3>Code QR PC-INFORMATIQUE</h3><div class="box" id="qrm"><img src="'+IMG+'" width="200" height="200" alt="QR"></div><p>Notre site en un scan. Touche le code pour l\'agrandir.</p>';
document.getElementById("qrm").onclick=full;
}
anon();
var n=0, t=setInterval(function(){
n++; if(n>40){clearInterval(t);return;}
try{
if(typeof firebase==="undefined")return;
if(!firebase.apps.length){
if(typeof firebaseConfig!=="undefined")firebase.initializeApp(firebaseConfig); else return;
}
clearInterval(t);
firebase.auth().onAuthStateChanged(function(u){ if(u&&!u.isAnonymous)ok(); else anon(); });
}catch(e){clearInterval(t);}
},250);
})();
