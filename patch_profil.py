def patch(content, anchor, new, label):
    count = content.count(anchor)
    if count != 1:
        raise SystemExit(f"ERREUR ancre '{label}': trouvee {count} fois (attendu 1).")
    return content.replace(anchor, new, 1)

with open("profil.html", "r", encoding="utf-8") as f:
    c = f.read()

# 1) Header : ajout bouton retour
old_header = """<header>
  <div class="brand">PC-INFORMATIQUE · Espace membre</div>
  <button id="btn-logout">Déconnexion</button>
</header>"""
new_header = """<header>
  <a href="index.html" id="btn-back" style="display:inline-flex;align-items:center;gap:6px;text-decoration:none;color:var(--muted);font-size:13px;border:1px solid var(--border);border-radius:8px;padding:8px 12px;">&larr; Accueil</a>
  <div class="brand">PC-INFORMATIQUE · Espace membre</div>
  <button id="btn-logout">Déconnexion</button>
</header>"""
c = patch(c, old_header, new_header, "header")

# 2) Header flex : repartir sur 3 elements
old_header_css = """header{
    background:var(--surface); border-bottom:1px solid var(--border);
    padding:14px 20px; display:flex; justify-content:space-between; align-items:center;
  }"""
new_header_css = """header{
    background:var(--surface); border-bottom:1px solid var(--border);
    padding:14px 20px; display:flex; justify-content:space-between; align-items:center; gap:10px;
  }
  header .brand{flex:1; text-align:center;}"""
c = patch(c, old_header_css, new_header_css, "header-css")

# 3) Ajout try/catch pour afficher les erreurs reelles au lieu de bloquer sur "Chargement..."
old_auth = """auth.onAuthStateChanged(async user=>{
  if(!user){ location.href = 'connexion.html'; return; }
  currentUser = user;
  await loadProfil();
  await loadProjets();
  document.getElementById('loading').style.display = 'none';
  document.getElementById('app').style.display = 'block';
});"""
new_auth = """auth.onAuthStateChanged(async user=>{
  if(!user){ location.href = 'connexion.html'; return; }
  currentUser = user;
  try{
    await loadProfil();
    await loadProjets();
    document.getElementById('loading').style.display = 'none';
    document.getElementById('app').style.display = 'block';
  }catch(err){
    console.error(err);
    document.getElementById('loading').textContent = "Erreur: " + (err && err.message ? err.message : err);
  }
});"""
c = patch(c, old_auth, new_auth, "auth-state")

# 4) Deconnexion fiable
old_logout = "document.getElementById('btn-logout').addEventListener('click', ()=> auth.signOut());"
new_logout = """document.getElementById('btn-logout').addEventListener('click', async ()=>{
  const btn = document.getElementById('btn-logout');
  btn.disabled = true;
  btn.textContent = 'Déconnexion...';
  try{
    await auth.signOut();
    location.href = 'index.html';
  }catch(err){
    console.error(err);
    btn.disabled = false;
    btn.textContent = 'Déconnexion';
    alert("Erreur lors de la déconnexion, réessaie.");
  }
});"""
c = patch(c, old_logout, new_logout, "logout")

with open("profil.html", "w", encoding="utf-8") as f:
    f.write(c)
print("OK: profil.html patche avec succes.")
