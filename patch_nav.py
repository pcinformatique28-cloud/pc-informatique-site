import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

def patch(content, anchor, insertion, where="after", label=""):
    count = content.count(anchor)
    if count != 1:
        raise SystemExit(f"ERREUR: ancre '{label}' trouvée {count} fois (attendu 1). Abandon sans modification.")
    if where == "after":
        return content.replace(anchor, anchor + insertion, 1)
    else:
        return content.replace(anchor, insertion + anchor, 1)

# 1) CSS - ajout après une règle existante unique
css_anchor = '.navlinks a .ic{font-size:.85rem;line-height:1;}'
css_insert = """
.icon-btn{background:none;border:1px solid #232841;color:var(--sub);width:34px;height:34px;border-radius:50%;
  display:inline-flex;align-items:center;justify-content:center;font-size:1rem;cursor:pointer;text-decoration:none;}
.icon-btn:hover{color:var(--teal);border-color:var(--teal);}
.drawer-overlay{position:fixed;inset:0;background:rgba(0,0,0,.55);z-index:40;opacity:0;pointer-events:none;transition:opacity .25s ease;}
.drawer-overlay.open{opacity:1;pointer-events:auto;}
.drawer{position:fixed;top:0;left:0;bottom:0;width:78%;max-width:300px;background:var(--card);border-right:1px solid #1e2338;
  z-index:50;transform:translateX(-100%);transition:transform .28s ease;padding:calc(20px + env(safe-area-inset-top,0px)) 18px 20px;overflow-y:auto;}
.drawer.open{transform:translateX(0);}
.drawer .d-user{display:flex;align-items:center;gap:12px;margin-bottom:20px;padding-bottom:16px;border-bottom:1px solid #1e2338;}
.drawer .d-user img{width:46px;height:46px;border-radius:50%;object-fit:cover;background:#232841;}
.drawer .d-user .d-name{font-weight:700;font-size:.92rem;}
.drawer .d-user .d-email{color:var(--sub);font-size:.74rem;}
.drawer nav.d-links{display:flex;flex-direction:column;gap:4px;}
.drawer a.d-link{display:flex;align-items:center;gap:12px;padding:11px 10px;border-radius:10px;color:var(--text);text-decoration:none;font-size:.88rem;}
.drawer a.d-link:hover{background:#1a1f33;}
.drawer a.d-link .ic{width:20px;text-align:center;}
.drawer .d-close{position:absolute;top:calc(14px + env(safe-area-inset-top,0px));right:14px;background:none;border:none;color:var(--sub);font-size:1.3rem;cursor:pointer;}
.bottom-nav{position:fixed;left:0;right:0;bottom:0;z-index:30;background:rgba(13,15,22,.96);backdrop-filter:blur(6px);
  border-top:1px solid #1e2338;padding:8px 6px calc(8px + env(safe-area-inset-bottom,0px));display:flex;justify-content:space-around;}
.bottom-nav a{display:flex;flex-direction:column;align-items:center;gap:3px;color:var(--sub);text-decoration:none;font-size:.64rem;padding:4px 8px;}
.bottom-nav a.active{color:var(--teal);}
.bottom-nav a .ic{font-size:1.15rem;}
body{padding-bottom:70px;}
"""
content = patch(content, "</style>", css_insert + "</style>".replace("</style>","",0) , label="dummy") if False else content
content = content.replace("</style>", css_insert + "</style>", 1)

# 2) Hamburger + icône auth dans le header
nav_anchor = '<nav>\n  <div class="navwrap">'
nav_insert = '''
  <button class="icon-btn" id="btn-menu" style="position:absolute;left:14px;top:calc(14px + env(safe-area-inset-top,0px));" aria-label="Menu">&#9776;</button>
  <a href="connexion.html" class="icon-btn" id="auth-icon" style="position:absolute;right:14px;top:calc(14px + env(safe-area-inset-top,0px));" aria-label="Connexion">&#128273;</a>'''
content = patch(content, nav_anchor, nav_insert, label="nav-open")

# 3) Drawer + overlay + bottom nav apres </nav>
nav_close_anchor = "</nav>"
drawer_insert = '''
<div class="drawer-overlay" id="drawer-overlay"></div>
<aside class="drawer" id="drawer">
  <button class="d-close" id="drawer-close" aria-label="Fermer">&times;</button>
  <div class="d-user" id="drawer-user" style="display:none;">
    <img id="drawer-avatar" src="" alt="">
    <div>
      <div class="d-name" id="drawer-name">&mdash;</div>
      <div class="d-email" id="drawer-email">&mdash;</div>
    </div>
  </div>
  <nav class="d-links">
    <a href="index.html" class="d-link"><span class="ic">&#127968;</span>Accueil</a>
    <a href="index.html#realisations" class="d-link"><span class="ic">&#128193;</span>Realisations</a>
    <a href="index.html#demande" class="d-link"><span class="ic">&#10133;</span>Nouvelle demande</a>
    <a href="profil.html" class="d-link" id="drawer-profil" style="display:none;"><span class="ic">&#128100;</span>Mon profil</a>
    <a href="connexion.html" class="d-link" id="drawer-login"><span class="ic">&#128273;</span>Connexion</a>
    <a href="#" class="d-link" id="drawer-logout" style="display:none;color:#ff6b6b;"><span class="ic">&#128682;</span>Deconnexion</a>
  </nav>
</aside>

<div class="bottom-nav">
  <a href="index.html" class="active"><span class="ic">&#127968;</span><span class="lbl">Accueil</span></a>
  <a href="index.html#realisations"><span class="ic">&#128193;</span><span class="lbl">Projets</span></a>
  <a href="index.html#demande"><span class="ic">&#10133;</span><span class="lbl">Demande</span></a>
  <a href="connexion.html" id="bottom-auth"><span class="ic">&#128273;</span><span class="lbl">Connexion</span></a>
</div>
'''
content = patch(content, nav_close_anchor, drawer_insert, label="nav-close")

# 4) Ajout du SDK firebase-auth-compat apres firebase-app-compat
app_sdk_anchor = '<script src="https://cdn.jsdelivr.net/npm/firebase@10.13.0/firebase-app-compat.js"></script>'
auth_sdk_insert = '\n<script src="https://cdn.jsdelivr.net/npm/firebase@10.13.0/firebase-auth-compat.js"></script>'
content = patch(content, app_sdk_anchor, auth_sdk_insert, label="app-sdk")

# 5) Script de logique auth + drawer, insere apres le SDK firestore
firestore_sdk_anchor = '<script src="https://cdn.jsdelivr.net/npm/firebase@10.13.0/firebase-firestore-compat.js"></script>'
auth_logic_insert = '''
<script>
(function(){
  if(!firebase.apps.length) firebase.initializeApp(firebaseConfig);
  var auth = firebase.auth();

  var drawer = document.getElementById('drawer');
  var overlay = document.getElementById('drawer-overlay');
  function openDrawer(){ drawer.classList.add('open'); overlay.classList.add('open'); }
  function closeDrawer(){ drawer.classList.remove('open'); overlay.classList.remove('open'); }
  document.getElementById('btn-menu').addEventListener('click', openDrawer);
  document.getElementById('drawer-close').addEventListener('click', closeDrawer);
  overlay.addEventListener('click', closeDrawer);

  var authIcon = document.getElementById('auth-icon');
  var bottomAuth = document.getElementById('bottom-auth');
  var dUser = document.getElementById('drawer-user');
  var dName = document.getElementById('drawer-name');
  var dEmail = document.getElementById('drawer-email');
  var dAvatar = document.getElementById('drawer-avatar');
  var dProfil = document.getElementById('drawer-profil');
  var dLogin = document.getElementById('drawer-login');
  var dLogout = document.getElementById('drawer-logout');

  dLogout.addEventListener('click', function(e){
    e.preventDefault();
    auth.signOut().then(function(){ closeDrawer(); location.href='index.html'; });
  });

  auth.onAuthStateChanged(function(user){
    if(user){
      authIcon.href = 'profil.html';
      authIcon.innerHTML = '&#128100;';
      authIcon.setAttribute('aria-label','Mon profil');
      bottomAuth.href = 'profil.html';
      bottomAuth.querySelector('.ic').innerHTML = '&#128100;';
      bottomAuth.querySelector('.lbl').textContent = 'Profil';
      dUser.style.display = 'flex';
      dName.textContent = user.displayName || 'Membre';
      dEmail.textContent = user.email || '';
      dAvatar.src = user.photoURL || 'images/logo-pc-informatique.png';
      dProfil.style.display = 'flex';
      dLogin.style.display = 'none';
      dLogout.style.display = 'flex';
    } else {
      authIcon.href = 'connexion.html';
      authIcon.innerHTML = '&#128273;';
      authIcon.setAttribute('aria-label','Connexion');
      bottomAuth.href = 'connexion.html';
      bottomAuth.querySelector('.ic').innerHTML = '&#128273;';
      bottomAuth.querySelector('.lbl').textContent = 'Connexion';
      dUser.style.display = 'none';
      dProfil.style.display = 'none';
      dLogin.style.display = 'flex';
      dLogout.style.display = 'none';
    }
  });
})();
</script>
'''
content = patch(content, firestore_sdk_anchor, auth_logic_insert, label="firestore-sdk")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("OK: index.html patche avec succes.")
