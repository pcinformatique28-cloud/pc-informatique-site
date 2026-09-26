def patch(content, anchor, new, label):
    count = content.count(anchor)
    if count != 1:
        raise SystemExit(f"ERREUR ancre '{label}': trouvee {count} fois (attendu 1, trouve {count}).")
    return content.replace(anchor, new, 1)

with open("profil.html", "r", encoding="utf-8") as f:
    c = f.read()

old_style_close = "</style>"
new_style_close = """  body{background:linear-gradient(160deg,#eafbf8 0%,#fdeef6 100%) !important;}
  input[readonly],textarea[readonly]{background:transparent !important;border-color:transparent !important;color:var(--text);cursor:default;}
  .profil-head{display:flex;align-items:center;justify-content:space-between;}
  .edit-icon{background:none;border:none;cursor:pointer;font-size:14px;font-weight:600;color:var(--muted);padding:4px 10px;border-radius:6px;}
  .edit-icon:hover{color:var(--primary);background:#f0fdfb;}
</style>"""
c = patch(c, old_style_close, new_style_close, "style-close")

old_h2 = '    <h2>Mon profil</h2>'
new_h2 = '''    <div class="profil-head">
      <h2>Mon profil</h2>
      <button type="button" id="btn-edit-profil" class="edit-icon" title="Modifier" style="display:none;">Modifier</button>
    </div>'''
c = patch(c, old_h2, new_h2, "h2-wrap")

old_load = """async function loadProfil(){
  const doc = await db.collection('membres').doc(currentUser.uid).get();
  const d = doc.data() || {};
  document.getElementById('nom').value = d.nom || '';
  document.getElementById('bio').value = d.bio || '';
  document.getElementById('avatar').src = d.photoURL || DEFAULT_AVATAR;
}"""
new_load = """async function loadProfil(){
  const doc = await db.collection('membres').doc(currentUser.uid).get();
  const d = doc.data() || {};
  document.getElementById('nom').value = d.nom || '';
  document.getElementById('bio').value = d.bio || '';
  document.getElementById('avatar').src = d.photoURL || DEFAULT_AVATAR;
  setProfilEditMode(!d.nom);
}

function setProfilEditMode(on){
  const nom = document.getElementById('nom');
  const bio = document.getElementById('bio');
  const btnSave = document.getElementById('btn-save-profil');
  const btnEdit = document.getElementById('btn-edit-profil');
  nom.readOnly = !on;
  bio.readOnly = !on;
  btnSave.parentElement.style.display = on ? '' : 'none';
  btnEdit.style.display = on ? 'none' : '';
}

document.getElementById('btn-edit-profil').addEventListener('click', ()=> setProfilEditMode(true));"""
c = patch(c, old_load, new_load, "load-profil")

old_save = '''  try{
    await db.collection('membres').doc(currentUser.uid).set({ nom, bio }, { merge: true });
    showMsg(msg, "Profil mis à jour.", true);
  }catch(err){'''
new_save = '''  try{
    await db.collection('membres').doc(currentUser.uid).set({ nom, bio }, { merge: true });
    showMsg(msg, "Profil mis à jour.", true);
    setProfilEditMode(false);
  }catch(err){'''
c = patch(c, old_save, new_save, "save-lock")

with open("profil.html", "w", encoding="utf-8") as f:
    f.write(c)
print("OK profil.html")
