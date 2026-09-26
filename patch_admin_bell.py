import re

with open("admin.html", "r", encoding="utf-8") as f:
    c = f.read()

# CSS
old_css = ".navwrap b{font-size:.95rem;}"
new_css = old_css + "\n.bell{position:relative;font-size:1.05rem;color:#fff;cursor:default;display:inline-flex;}\n.bell-badge{position:absolute;top:-6px;right:-10px;background:var(--bad);color:#fff;font-size:.6rem;font-weight:800;border-radius:10px;padding:1px 5px;line-height:1;}"
c, n = re.subn(re.escape(old_css), new_css, c, count=1)
if n != 1: raise SystemExit(f"ERREUR css ({n})")

# HTML nav
old_nav = '<nav><div class="navwrap"><b>🔧 PC-INFORMATIQUE — Admin</b><span id="count" style="font-size:.75rem;color:var(--sub)"></span></div></nav>'
new_nav = '<nav><div class="navwrap"><b>🔧 PC-INFORMATIQUE — Admin</b><span style="display:flex;align-items:center;gap:12px;"><span id="count" style="font-size:.75rem;color:var(--sub)"></span><span class="bell" id="admin-bell" title="Notifications">&#128276;<span class="bell-badge" id="admin-bell-badge" style="display:none;"></span></span></span></div></nav>'
c, n = re.subn(re.escape(old_nav), new_nav, c, count=1)
if n != 1: raise SystemExit(f"ERREUR nav ({n})")

# JS: demarrer les compteurs apres le login admin
old_load = "loadList();\n    loadProjets();"
new_load = "loadList();\n    loadProjets();\n    startAdminNotifs();"
c, n = re.subn(re.escape(old_load), new_load, c, count=1)
if n != 1: raise SystemExit(f"ERREUR loadList ({n})")

# JS: ajouter vu:false dans decideProjet
old_decide = "function decideProjet(id, status){\n  db.collection('projets').doc(id).update({ statut: status, decidedAt: new Date().toISOString() });\n}"
new_decide = "function decideProjet(id, status){\n  db.collection('projets').doc(id).update({ statut: status, decidedAt: new Date().toISOString(), vu: false });\n}"
c, n = re.subn(re.escape(old_decide), new_decide, c, count=1)
if n != 1: raise SystemExit(f"ERREUR decideProjet ({n})")

# JS: fonctions de notif, ajoutees avant le dernier </script>
js_block = '''
let notifDemandesCount = 0, notifProjetsCount = 0;
function startAdminNotifs(){
  db.collection('demandes').where('status','==','nouveau').onSnapshot(snap=>{
    notifDemandesCount = snap.size;
    updateAdminBell();
  });
  db.collection('projets').where('statut','==','en_attente').onSnapshot(snap=>{
    notifProjetsCount = snap.size;
    updateAdminBell();
  });
}
function updateAdminBell(){
  const badge = document.getElementById('admin-bell-badge');
  if(!badge) return;
  const total = notifDemandesCount + notifProjetsCount;
  if(total>0){ badge.textContent = total; badge.style.display='inline-block'; }
  else{ badge.style.display='none'; }
}
'''
idx = c.rfind("</script>")
if idx == -1: raise SystemExit("ERREUR: </script> non trouve")
c = c[:idx] + js_block + c[idx:]

with open("admin.html", "w", encoding="utf-8") as f:
    f.write(c)
print("OK admin.html cloche")
