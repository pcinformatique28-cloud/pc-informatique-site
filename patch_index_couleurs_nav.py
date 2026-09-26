import re

with open("index.html", "r", encoding="utf-8") as f:
    c = f.read()

old_nav = "nav{position:sticky;top:0;z-index:20;background:linear-gradient(180deg,#fcfcfe 0%,#e7eaf2 55%,#f6f7fb 100%);backdrop-filter:blur(6px);border-bottom:1px solid #d7dbe4;box-shadow:0 1px 0 rgba(255,255,255,.7) inset,0 2px 10px rgba(20,24,40,.08);"
new_nav = "nav{position:sticky;top:0;z-index:20;background:linear-gradient(120deg,#33d9c4 0%,#3a8bff 50%,#ff4fa3 100%);backdrop-filter:blur(6px);border-bottom:1px solid rgba(255,255,255,.25);box-shadow:0 1px 0 rgba(255,255,255,.35) inset,0 2px 14px rgba(20,24,40,.18);"
c, n = re.subn(re.escape(old_nav), new_nav, c, count=1)
if n != 1: raise SystemExit(f"ERREUR nav ({n})")

old_bottom = ".bottom-nav{position:fixed;left:0;right:0;bottom:0;z-index:30;background:linear-gradient(180deg,#f6f7fb 0%,#e7eaf2 100%);backdrop-filter:blur(6px);"
new_bottom = ".bottom-nav{position:fixed;left:0;right:0;bottom:0;z-index:30;background:linear-gradient(120deg,#33d9c4 0%,#3a8bff 50%,#ff4fa3 100%);backdrop-filter:blur(6px);"
c, n = re.subn(re.escape(old_bottom), new_bottom, c, count=1)
if n != 1: raise SystemExit(f"ERREUR bottom-nav ({n})")

old_link = ".bottom-nav a{display:flex;flex-direction:column;align-items:center;gap:3px;color:#6b7280;text-decoration:none;font-size:.64rem;padding:4px 8px;}"
new_link = ".bottom-nav a{display:flex;flex-direction:column;align-items:center;gap:3px;color:rgba(255,255,255,.85);text-decoration:none;font-size:.64rem;padding:4px 8px;}"
c, n = re.subn(re.escape(old_link), new_link, c, count=1)
if n != 1: raise SystemExit(f"ERREUR bottom-nav a ({n})")

old_active = ".bottom-nav a.active{color:#0e9488;}"
new_active = ".bottom-nav a.active{color:#ffffff;font-weight:700;}"
c, n = re.subn(re.escape(old_active), new_active, c, count=1)
if n != 1: raise SystemExit(f"ERREUR active ({n})")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(c)
print("OK index.html couleurs nav")
