import re

with open("profil.html", "r", encoding="utf-8") as f:
    c = f.read()

# CSS
old_css = ".btn-danger:hover{background:#fef2f2;}"
new_css = old_css + "\n  .bell{position:relative;font-size:1.05rem;color:#0e9488;cursor:pointer;display:inline-flex;}\n  .bell-badge{position:absolute;top:-6px;right:-10px;background:var(--danger);color:#fff;font-size:.6rem;font-weight:800;border-radius:10px;padding:1px 5px;line-height:1;}"
c, n = re.subn(re.escape(old_css), new_css, c, count=1)
if n != 1: raise SystemExit(f"ERREUR css ({n})")

# HTML header
old_btn = '<button id="btn-logout">Déconnexion</button>'
new_btn = '<span class="bell" id="profil-bell" title="Notifications">&#128276;<span class="bell-badge" id="profil-bell-badge" style="display:none;"></span></span>\n  <button id="btn-logout">Déconnexion</button>'
c, n = re.subn(re.escape(old_btn), new_btn, c, count=1)
if n != 1: raise SystemExit(f"ERREUR header ({n})")

# JS: vu:true a la creation d'un projet
old_add = "await db.collection('projets').add({\n        membreId: currentUser.uid,\n        titre, description, type, lien, imageURL,\n        statut: 'en_attente',\n        createdAt: firebase.firestore.FieldValue.serverTimestamp()\n      });"
new_add = "await db.collection('projets').add({\n        membreId: currentUser.uid,\n        titre, description, type, lien, imageURL,\n        statut: 'en_attente',\n        vu: true,\n        createdAt: firebase.firestore.FieldValue.serverTimestamp()\n      });"
c, n = re.subn(re.escape(old_add), new_add, c, count=1)
if n != 1: raise SystemExit(f"ERREUR add-projet ({n})")

# JS: demarrer l'ecoute de notifs apres le chargement du profil
old_auth = "await loadProjets();\n    document.getElementById('loading').style.display = 'none';"
new_auth = "await loadProjets();\n    startMemberNotifs();\n    document.getElementById('loading').style.display = 'none';"
c, n = re.subn(re.escape(old_auth), new_auth, c, count=1)
if n != 1: raise SystemExit(f"ERREUR onAuthStateChanged ({n})")

# JS: fonctions de notif, ajoutees avant le dernier </script>
js_block = '''
let unseenNotifCount = 0;
function startMemberNotifs(){
  db.collection('projets').where('membreId','==',currentUser.uid).where('vu','==', false)
    .onSnapshot(snap=>{
      unseenNotifCount = snap.size;
      updateProfilBell();
    });
}
function updateProfilBell(){
  const badge = document.getElementById('profil-bell-badge');
  if(!badge) return;
  if(unseenNotifCount>0){ badge.textContent = unseenNotifCount; badge.style.display='inline-block'; }
  else{ badge.style.display='none'; }
}
document.getElementById('profil-bell').addEventListener('click', async ()=>{
  const snap = await db.collection('projets').where('membreId','==',currentUser.uid).where('vu','==', false).get();
  const batch = db.batch();
  snap.forEach(doc=> batch.update(doc.ref, { vu:true }));
  if(!snap.empty) await batch.commit();
  document.getElementById('projets-list').scrollIntoView({behavior:'smooth', block:'start'});
});
'''
idx = c.rfind("</script>")
if idx == -1: raise SystemExit("ERREUR: </script> non trouve")
c = c[:idx] + js_block + c[idx:]

with open("profil.html", "w", encoding="utf-8") as f:
    f.write(c)
print("OK profil.html cloche")
