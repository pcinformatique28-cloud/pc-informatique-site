import re

with open("admin.html", "r", encoding="utf-8") as f:
    c = f.read()

# 1) CSS: badge pour statut "en_attente" (projets)
old_css = ".b-refuse{background:rgba(255,92,92,.15);color:var(--bad);}"
new_css = old_css + "\n.b-en_attente{background:rgba(242,201,76,.15);color:var(--wait);}"
c, n = re.subn(re.escape(old_css), new_css, c, count=1)
if n != 1: raise SystemExit(f"ERREUR css ({n})")

# 2) HTML: mode switcher + ouverture section demandes, avant .tabs
old_tabs_open = '<div class="tabs">'
new_tabs_open = '''<div class="modebar" style="display:flex;gap:8px;margin:14px 0;">
    <div class="tab on" id="mode-demandes">Demandes</div>
    <div class="tab" id="mode-projets">Projets membres</div>
  </div>
  <div id="sec-demandes">
  <div class="tabs">'''
c, n = re.subn(re.escape(old_tabs_open), new_tabs_open, c, count=1)
if n != 1: raise SystemExit(f"ERREUR tabs-open ({n})")

# 3) HTML: fermeture section demandes + section projets, apres #list
old_list = '<div id="list"></div>'
new_list = '''<div id="list"></div>
  </div>
  <div id="sec-projets" style="display:none">
    <div class="tabs">
      <div class="tab on" data-fp="en_attente">En attente</div>
      <div class="tab" data-fp="valide">Valides</div>
      <div class="tab" data-fp="refuse">Refuses</div>
      <div class="tab" data-fp="all">Tous</div>
    </div>
    <div id="list-projets"></div>
  </div>'''
c, n = re.subn(re.escape(old_list), new_list, c, count=1)
if n != 1: raise SystemExit(f"ERREUR list ({n})")

# 4) JS: appeler loadProjets() en plus de loadList()
old_load = "loadList();"
new_load = "loadList();\n    loadProjets();"
c, n = re.subn(re.escape(old_load), new_load, c, count=1)
if n != 1: raise SystemExit(f"ERREUR loadList ({n})")

# 5) JS: ajouter toute la logique projets avant le dernier </script>
js_block = '''
let ALLP = []; let filterP = 'en_attente';
function loadProjets(){
  if(!db) return;
  db.collection('projets').orderBy('createdAt','desc').onSnapshot(snap=>{
    ALLP = snap.docs.map(doc=>({id:doc.id, ...doc.data()}));
    renderProjets();
  });
}
function renderProjets(){
  const list = document.getElementById('list-projets');
  const items = filterP==='all' ? ALLP : ALLP.filter(p=>p.statut===filterP);
  if(!items.length){ list.innerHTML = '<div class="empty">Aucun projet ici pour le moment.</div>'; return; }
  list.innerHTML = items.map(p=>`
    <div class="card">
      <span class="badge b-${p.statut}">${p.statut}</span>
      <h4>${p.titre||'Sans titre'}</h4>
      <p>${p.type||'-'}</p>
      <p>${p.description||''}</p>
      ${p.imageURL ? `<div class="thumbs"><img src="${p.imageURL}"></div>` : ''}
      ${p.lien ? `<p><a href="${p.lien}" target="_blank" style="color:var(--teal)">${p.lien}</a></p>` : ''}
      ${p.statut==='en_attente' ? `
        <div class="actions">
          <button class="btn primary" onclick="decideProjet('${p.id}','valide')">Valider</button>
          <button class="btn bad" onclick="decideProjet('${p.id}','refuse')">Refuser</button>
        </div>` : ''}
    </div>`).join('');
}
document.querySelectorAll('#sec-projets .tab').forEach(t=>t.addEventListener('click',()=>{
  document.querySelectorAll('#sec-projets .tab').forEach(x=>x.classList.remove('on')); t.classList.add('on');
  filterP = t.dataset.fp; renderProjets();
}));
function decideProjet(id, status){
  db.collection('projets').doc(id).update({ statut: status, decidedAt: new Date().toISOString() });
}
document.getElementById('mode-demandes').addEventListener('click', ()=>{
  document.getElementById('mode-demandes').classList.add('on');
  document.getElementById('mode-projets').classList.remove('on');
  document.getElementById('sec-demandes').style.display='block';
  document.getElementById('sec-projets').style.display='none';
});
document.getElementById('mode-projets').addEventListener('click', ()=>{
  document.getElementById('mode-projets').classList.add('on');
  document.getElementById('mode-demandes').classList.remove('on');
  document.getElementById('sec-demandes').style.display='none';
  document.getElementById('sec-projets').style.display='block';
});
'''

idx = c.rfind("</script>")
if idx == -1: raise SystemExit("ERREUR: aucune balise </script> trouvee")
c = c[:idx] + js_block + c[idx:]

with open("admin.html", "w", encoding="utf-8") as f:
    f.write(c)
print("OK admin.html")
