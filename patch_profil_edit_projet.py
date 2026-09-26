import re

with open("profil.html", "r", encoding="utf-8") as f:
    c = f.read()

# 1) Rendre l'image cliquable avec data-id + curseur pointer
old1 = "${p.imageURL ? `<img src=\"${p.imageURL}\" alt=\"\">` : ''}"
new1 = "${p.imageURL ? `<img src=\"${p.imageURL}\" alt=\"\" style=\"cursor:pointer;\" data-edit-id=\"${p.id}\">` : ''}"
c, n = re.subn(re.escape(old1), new1, c, count=1)
if n != 1: raise SystemExit(f"ERREUR image ({n})")

# 2) Ajouter le listener de clic sur l'image, apres le bloc btn-danger existant
old2 = """  list.querySelectorAll('.btn-danger').forEach(btn=>{
    btn.addEventListener('click', async ()=>{
      if(!confirm('Supprimer ce projet ?')) return;
      await db.collection('projets').doc(btn.dataset.id).delete();
      loadProjets();
    });
  });
}"""
new2 = """  list.querySelectorAll('.btn-danger').forEach(btn=>{
    btn.addEventListener('click', async ()=>{
      if(!confirm('Supprimer ce projet ?')) return;
      await db.collection('projets').doc(btn.dataset.id).delete();
      loadProjets();
    });
  });

  list.querySelectorAll('img[data-edit-id]').forEach(img=>{
    img.addEventListener('click', ()=>{
      const p = projets.find(x => x.id === img.dataset.editId);
      if(!p) return;
      editingProjetId = p.id;
      document.getElementById('p-titre').value = p.titre || '';
      document.getElementById('p-type').value = p.type || 'personnel';
      document.getElementById('p-desc').value = p.description || '';
      document.getElementById('p-lien').value = p.lien || '';
      document.getElementById('btn-add-projet').textContent = 'Enregistrer les modifications';
      document.getElementById('p-titre').scrollIntoView({behavior:'smooth', block:'center'});
    });
  });
}"""
c, n = re.subn(re.escape(old2), new2, c, count=1)
if n != 1: raise SystemExit(f"ERREUR listener image ({n})")

# 3) Variable editingProjetId, avant currentUser
old3 = "let currentUser = null;"
new3 = "let currentUser = null;\nlet editingProjetId = null;"
c, n = re.subn(re.escape(old3), new3, c, count=1)
if n != 1: raise SystemExit(f"ERREUR var editing ({n})")

# 4) Modifier le handler btn-add-projet: gerer add ou update selon editingProjetId
old4 = """    let imageURL = "";
    if(fileInput.files[0]){
      imageURL = await uploadToCloudinary(fileInput.files[0]);
    }
    await db.collection('projets').add({
      membreId: currentUser.uid,
      titre, description, type, lien, imageURL,
      statut: 'en_attente',
      createdAt: firebase.firestore.FieldValue.serverTimestamp()
    });
    showMsg(msg, "Projet envoyé, en attente de validation par l'admin.", true);
    document.getElementById('p-titre').value = '';
    document.getElementById('p-desc').value = '';
    document.getElementById('p-lien').value = '';"""
new4 = """    let imageURL = "";
    if(fileInput.files[0]){
      imageURL = await uploadToCloudinary(fileInput.files[0]);
    }
    if(editingProjetId){
      const update = { titre, description, type, lien };
      if(imageURL) update.imageURL = imageURL;
      await db.collection('projets').doc(editingProjetId).update(update);
      showMsg(msg, "Projet mis à jour.", true);
      editingProjetId = null;
      document.getElementById('btn-add-projet').textContent = 'Envoyer pour validation';
    } else {
      await db.collection('projets').add({
        membreId: currentUser.uid,
        titre, description, type, lien, imageURL,
        statut: 'en_attente',
        createdAt: firebase.firestore.FieldValue.serverTimestamp()
      });
      showMsg(msg, "Projet envoyé, en attente de validation par l'admin.", true);
    }
    document.getElementById('p-titre').value = '';
    document.getElementById('p-desc').value = '';
    document.getElementById('p-lien').value = '';"""
c, n = re.subn(re.escape(old4), new4, c, count=1)
if n != 1: raise SystemExit(f"ERREUR handler add/update ({n})")

with open("profil.html", "w", encoding="utf-8") as f:
    f.write(c)
print("OK profil.html edition projet")
