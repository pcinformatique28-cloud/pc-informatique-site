import re

with open("index.html", "r", encoding="utf-8") as f:
    c = f.read()

# 1) Lien "Tableau de bord" dans le drawer, juste après "Mon profil"
old1 = '<a href="profil.html" class="d-link" id="drawer-profil" style="display:none;"><span class="ic">&#128100;</span>Mon profil</a>'
new1 = old1 + '\n    <a href="admin.html" class="d-link" id="drawer-admin" style="display:none;"><span class="ic">&#9881;</span>Tableau de bord</a>'
c, n1 = re.subn(re.escape(old1), new1, c, count=1)
if n1 != 1:
    raise SystemExit(f"ERREUR: ancre drawer-profil non trouvee ({n1})")

# 2) Declaration JS: ADMIN_UID + var dAdmin
old2 = "var dLogout = document.getElementById('drawer-logout');"
new2 = "var dLogout = document.getElementById('drawer-logout');\n  var dAdmin = document.getElementById('drawer-admin');\n  var ADMIN_UID = \"QFC18HxRAZabqYD85S5eA7VLC5D3\";"
c, n2 = re.subn(re.escape(old2), new2, c, count=1)
if n2 != 1:
    raise SystemExit(f"ERREUR: ancre dLogout non trouvee ({n2})")

# 3) Dans le if(user){...}: afficher/masquer selon ADMIN_UID
old3 = "dLogin.style.display = 'none';\n      dLogout.style.display = 'flex';"
new3 = "dLogin.style.display = 'none';\n      dLogout.style.display = 'flex';\n      dAdmin.style.display = (user.uid === ADMIN_UID) ? 'flex' : 'none';"
c, n3 = re.subn(re.escape(old3), new3, c, count=1)
if n3 != 1:
    raise SystemExit(f"ERREUR: ancre bloc if(user) non trouvee ({n3})")

# 4) Dans le else {...}: masquer aussi
old4 = "dProfil.style.display = 'none';\n      dLogin.style.display = 'flex';"
new4 = "dProfil.style.display = 'none';\n      dAdmin.style.display = 'none';\n      dLogin.style.display = 'flex';"
c, n4 = re.subn(re.escape(old4), new4, c, count=1)
if n4 != 1:
    raise SystemExit(f"ERREUR: ancre bloc else non trouvee ({n4})")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(c)
print("OK index.html")
