def patch(content, anchor, new, label):
    count = content.count(anchor)
    if count != 1:
        raise SystemExit(f"ERREUR ancre '{label}': trouvee {count} fois (attendu 1, trouve {count}).")
    return content.replace(anchor, new, 1)

with open("profil.html", "r", encoding="utf-8") as f:
    c = f.read()

old1 = "await db.collection('membres').doc(currentUser.uid).update({ photoURL: url });"
new1 = "await db.collection('membres').doc(currentUser.uid).set({ photoURL: url }, { merge: true });"
c = patch(c, old1, new1, "photo-update")

old2 = "await db.collection('membres').doc(currentUser.uid).update({ nom, bio });"
new2 = "await db.collection('membres').doc(currentUser.uid).set({ nom, bio }, { merge: true });"
c = patch(c, old2, new2, "profil-update")

with open("profil.html", "w", encoding="utf-8") as f:
    f.write(c)
print("OK")
