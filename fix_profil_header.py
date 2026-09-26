import re
with open("profil.html", "r", encoding="utf-8") as f:
    c = f.read()

old1 = '<span class="bell" id="profil-bell"'
new1 = '<span class="head-right"><span class="bell" id="profil-bell"'
c, n = re.subn(re.escape(old1), new1, c, count=1)
if n != 1: raise SystemExit(f"ERREUR open head-right ({n})")

old2 = '<button id="btn-logout">D\u00e9connexion</button>'
new2 = '<button id="btn-logout">D\u00e9connexion</button></span>'
c, n = re.subn(re.escape(old2), new2, c, count=1)
if n != 1: raise SystemExit(f"ERREUR close head-right ({n})")

old3 = 'header .brand{flex:1; text-align:center;}'
new3 = 'header .brand{flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;text-align:center;}\n  .head-right{display:flex;align-items:center;gap:8px;flex-shrink:0;}'
c, n = re.subn(re.escape(old3), new3, c, count=1)
if n != 1: raise SystemExit(f"ERREUR brand css ({n})")

old4 = 'padding:8px 14px;\n    font-size:13px; cursor:pointer; color:var(--muted);'
new4 = 'padding:8px 10px;\n    font-size:12px; cursor:pointer; color:var(--muted);'
c2, n = re.subn(re.escape(old4), new4, c, count=1)
if n == 1:
    c = c2
else:
    print("Info: bouton padding non modifie (format different), pas bloquant")

with open("profil.html", "w", encoding="utf-8") as f:
    f.write(c)
print("OK fix_profil_header termine")
