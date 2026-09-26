import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

orig = html

# 1) Police globale plus grande (scale tout ce qui est en rem)
old = "html,body{margin:0;background:var(--bg);color:var(--text);font-family:-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;}"
new = "html,body{margin:0;background:var(--bg);color:var(--text);font-family:-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;font-size:18px;}"
assert html.count(old) == 1, "html,body rule introuvable"
html = html.replace(old, new)

# 2) Contact visible (texte sombre au lieu de gris-bleu clair)
old = '.contact{display:flex;flex-wrap:wrap;gap:14px;font-size:.82rem;color:#dfe2ee;margin-bottom:10px;justify-content:center;}'
new = '.contact{display:flex;flex-wrap:wrap;gap:14px;font-size:.9rem;color:var(--text);margin-bottom:10px;justify-content:center;font-weight:600;}'
assert html.count(old) == 1, ".contact rule introuvable"
html = html.replace(old, new)

# 3) Menu latéral : couleurs d'origine du logo (navy + teal + rose), ajoutées après les règles .drawer existantes
old = '.drawer .d-close{position:absolute;top:calc(14px + env(safe-area-inset-top,0px));right:14px;background:none;border:none;color:var(--sub);font-size:1.3rem;cursor:pointer;}'
assert html.count(old) == 1, ".d-close rule introuvable"
override = old + """
:root{--logo-navy:#12142b;--logo-navy2:#1b1e3d;--logo-teal:#2dd9c4;--logo-pink:#e0266f;}
.drawer{background:linear-gradient(180deg,var(--logo-navy),var(--logo-navy2));border-right:none;}
.drawer::before{background:linear-gradient(90deg,var(--logo-teal),var(--logo-pink));}
.drawer .d-user{border-bottom:1px solid rgba(255,255,255,.12);}
.drawer .d-user img{border:2px solid var(--logo-teal);}
.drawer .d-user .d-name{color:#fff;}
.drawer .d-user .d-email{color:rgba(255,255,255,.65);}
.drawer a.d-link{background:rgba(255,255,255,.04);color:#f2f3fa;}
.drawer a.d-link:hover{background:linear-gradient(90deg,rgba(45,217,196,.18),rgba(224,38,111,.18));border-left:3px solid var(--logo-teal);}
.drawer a.d-link .ic{background:rgba(255,255,255,.9);}
.drawer .d-close{color:rgba(255,255,255,.75);}
"""
html = html.replace(old, override)

assert html != orig, "Aucun changement appliqué"
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("OK : 3 correctifs appliqués (police, contact, menu).")
