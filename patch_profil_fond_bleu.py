import re

with open("profil.html", "r", encoding="utf-8") as f:
    c = f.read()

old = "body{background:linear-gradient(160deg,#eafbf8 0%,#fdeef6 100%) !important;}"
new = "body{background:linear-gradient(160deg,#eaf2ff 0%,#dce8ff 100%) !important;}"
c, n = re.subn(re.escape(old), new, c, count=1)
if n != 1: raise SystemExit(f"ERREUR fond ({n})")

with open("profil.html", "w", encoding="utf-8") as f:
    f.write(c)
print("OK profil.html fond bleu")
