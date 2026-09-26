import re

with open("profil.html", "r", encoding="utf-8") as f:
    c = f.read()

old = '.card{background:var(--surface); border:1px solid var(--border); border-radius:var(--radius); padding:24px; margin-bottom:20px;}'
new = '''.card{background:linear-gradient(180deg,#ffffff,#f4fffb);border:1px solid var(--border);border-radius:var(--radius);padding:24px;margin-bottom:20px;position:relative;overflow:hidden;}
  .card::before{content:"";position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg,var(--teal),var(--pink));}
  .card h2{color:#0e9488;}'''
c, n = re.subn(re.escape(old), new, c, count=1)
if n != 1: raise SystemExit(f"ERREUR card ({n})")

with open("profil.html", "w", encoding="utf-8") as f:
    f.write(c)
print("OK profil.html couleurs")
