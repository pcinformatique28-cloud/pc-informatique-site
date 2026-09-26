import re

with open("profil.html", "r", encoding="utf-8") as f:
    c = f.read()

c, n1 = re.subn(r'\s*const ADMIN_UID = "[^"]*";\n?', '\n', c, count=1)
if n1 != 1:
    raise SystemExit(f"ERREUR: ADMIN_UID non trouve ({n1})")

c, n2 = re.subn(r'\s*<a[^>]*id="btn-admin"[^>]*>.*?</a>', '', c, count=1, flags=re.DOTALL)
if n2 != 1:
    raise SystemExit(f"ERREUR: bouton btn-admin non trouve ({n2})")

c, n3 = re.subn(r'\s*if\(user\.uid === ADMIN_UID\)\{[^}]*\}\n?', '\n', c, count=1)
if n3 != 1:
    raise SystemExit(f"ERREUR: bloc reveal non trouve ({n3})")

with open("profil.html", "w", encoding="utf-8") as f:
    f.write(c)
print("OK profil.html (admin retire)")
