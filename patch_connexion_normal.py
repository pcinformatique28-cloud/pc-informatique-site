def patch(content, anchor, new, label):
    count = content.count(anchor)
    if count != 1:
        raise SystemExit(f"ERREUR ancre \"{label}\": trouvee {count} fois (attendu 1).")
    return content.replace(anchor, new, 1)

with open("connexion.html", "r", encoding="utf-8") as f:
    c = f.read()

old1 = "location.href = (cred.user.uid === ADMIN_UID) ? 'admin.html' : 'profil.html';"
new1 = "location.href = 'profil.html';"
c = patch(c, old1, new1, "redirect-submit")

old2 = "if(user) location.href = (user.uid === ADMIN_UID) ? 'admin.html' : 'profil.html';"
new2 = "if(user) location.href = 'profil.html';"
c = patch(c, old2, new2, "redirect-authstate")

with open("connexion.html", "w", encoding="utf-8") as f:
    f.write(c)
print("OK connexion.html")
