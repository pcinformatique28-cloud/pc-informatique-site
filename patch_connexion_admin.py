def patch(content, anchor, new, label):
    count = content.count(anchor)
    if count != 1:
        raise SystemExit(f"ERREUR ancre '{label}': trouvee {count} fois (attendu 1, trouve {count}).")
    return content.replace(anchor, new, 1)

with open("connexion.html", "r", encoding="utf-8") as f:
    c = f.read()

old1 = "const auth = firebase.auth();"
new1 = 'const auth = firebase.auth();\nconst ADMIN_UID = "QFC18HxRAZabqYD85S5eA7VLC5D3";'
c = patch(c, old1, new1, "auth-const")

old2 = """    await auth.signInWithEmailAndPassword(email, pass);
    location.href = 'profil.html';"""
new2 = """    const cred = await auth.signInWithEmailAndPassword(email, pass);
    location.href = (cred.user.uid === ADMIN_UID) ? 'admin.html' : 'profil.html';"""
c = patch(c, old2, new2, "signin-redirect")

old3 = """auth.onAuthStateChanged(user=>{
  if(user) location.href = 'profil.html';
});"""
new3 = """auth.onAuthStateChanged(user=>{
  if(user) location.href = (user.uid === ADMIN_UID) ? 'admin.html' : 'profil.html';
});"""
c = patch(c, old3, new3, "already-logged")

with open("connexion.html", "w", encoding="utf-8") as f:
    f.write(c)
print("OK connexion.html")
