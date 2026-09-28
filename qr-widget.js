(function(){
if(document.getElementById("qrw"))return;
var SVG="qr-pc-informatique.svg";
var st=document.createElement("style");
st.textContent="#qrw{max-width:520px;margin:24px auto 110px;padding:16px;text-align:center;color:#fff}#qrw h3{margin:0 0 10px;font-size:16px}#qrw .box{display:inline-block;background:#fff;padding:8px;border-radius:12px}#qrw img{display:block}#qrw .m{cursor:pointer}#qrw p{font-size:14px;opacity:.9;margin:10px 0}#qrw a.b{display:inline-block;margin:4px;padding:10px 14px;border-radius:12px;background:linear-gradient(135deg,#2dd4bf,#ec4899);color:#000;font-weight:700;text-decoration:none}";
document.head.appendChild(st);
var w=document.createElement("div"); w.id="qrw"; document.body.appendChild(w);
function anon(){
w.innerHTML='<h3>Code QR PC-INFORMATIQUE</h3><div class="box m" id="qrm"><img src="'+SVG+'" width="56" height="56" alt="QR"></div><p id="qrmsg" style="display:none"></p>';
document.getElementById("qrm").onclick=function(){
var m=document.getElementById("qrmsg"); m.style.display="block";
m.innerHTML='Inscris-toi pour voir ce code.<br><a class="b" href="inscription.html">S\'inscrire</a><a class="b" href="connexion.html">Connexion</a>';
};
}
function ok(){
w.innerHTML='<h3>Code QR PC-INFORMATIQUE</h3><div class="box"><img src="'+SVG+'" width="200" height="200" alt="QR"></div><p>Scanne pour ouvrir le site.</p><a class="b" href="qr.html">Formats &amp; impression</a>';
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
