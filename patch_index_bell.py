import re

with open("index.html", "r", encoding="utf-8") as f:
    c = f.read()

# 1) CSS: ajouter le style de la cloche. On l'insere juste avant </style> serait fragile,
# donc on l'ajoute apres la regle .icon-btn si elle existe, sinon on la place en dur inline.
# On utilise un point d'ancrage sur le nav existant a la place: on ajoute un <style> local juste avant </nav>.
old_nav_open = '<a href="connexion.html" class="icon-btn" id="auth-icon" style="position:absolute;right:14px;top:calc(14px + env(safe-area-inset-top,0px));" aria-label="Connexion">&#128273;</a>'
new_nav_open = old_nav_open.replace(
    '</a>',
    '</a>\n  <span class="icon-btn" id="notif-bell" style="display:none;position:absolute;right:56px;top:calc(14px + env(safe-area-inset-top,0px));cursor:pointer;" title="Notifications">&#128276;<span id="notif-bell-badge" style="display:none;position:absolute;top:-4px;right:-6px;background:#ff4fa3;color:#fff;font-size:.6rem;font-weight:800;border-radius:10px;padding:1px 5px;line-height:1;"></span></span>'
)
c, n = re.subn(re.escape(old_nav_open), new_nav_open, c, count=1)
if n != 1: raise SystemExit(f"ERREUR nav bell ({n})")

# 2) JS: dans le if(user){...}, afficher la cloche + demarrer l'ecoute
old_if = "dAvatar.src = user.photoURL || 'images/logo-pc-informatique.png';"
new_if = old_if + "\n      document.getElementById('notif-bell').style.display = 'inline-flex';\n      startIndexNotifs(user.uid);"
c, n = re.subn(re.escape(old_if), new_if, c, count=1)
if n != 1: raise SystemExit(f"ERREUR if(user) ({n})")

# 3) JS: dans le else {...}, cacher la cloche
old_else = "dProfil.style.display = 'none';"
new_else = old_else + "\n      document.getElementById('notif-bell').style.display = 'none';"
c, n = re.subn(re.escape(old_else), new_else, c, count=1)
if n != 1: raise SystemExit(f"ERREUR else ({n})")

# 4) JS: fonctions + listener, ajoutees avant le dernier </script>
js_block = '''
<script>
(function(){
  function startIndexNotifs(uid){
    var db = firebase.firestore();
    db.collection('projets').where('membreId','==',uid).where('vu','==', false)
      .onSnapshot(function(snap){
        var badge = document.getElementById('notif-bell-badge');
        if(!badge) return;
        if(snap.size>0){ badge.textContent = snap.size; badge.style.display='inline-block'; }
        else{ badge.style.display='none'; }
      });
  }
  window.startIndexNotifs = startIndexNotifs;
  document.getElementById('notif-bell').addEventListener('click', function(){
    location.href = 'profil.html';
  });
})();
</script>
'''
idx = c.rfind("</body>")
if idx == -1: raise SystemExit("ERREUR: </body> non trouve")
c = c[:idx] + js_block + c[idx:]

with open("index.html", "w", encoding="utf-8") as f:
    f.write(c)
print("OK index.html cloche")
