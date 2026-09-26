import re

with open("admin.html", "r", encoding="utf-8") as f:
    c = f.read()

old_card = ".card{background:var(--card);border:1px solid #1e2338;border-radius:16px;padding:14px 16px;margin-bottom:12px;cursor:pointer;}"
new_card = ".card{background:var(--card);border:1px solid #1e2338;border-radius:18px;padding:16px 18px;margin-bottom:14px;cursor:pointer;box-shadow:0 2px 10px rgba(0,0,0,.25);transition:transform .15s ease;}\n.card:active{transform:scale(.98);}"
c, n = re.subn(re.escape(old_card), new_card, c, count=1)
if n != 1: raise SystemExit(f"ERREUR card ({n})")

old_h4 = ".card h4{margin:0 0 4px;font-size:.95rem;}"
new_h4 = ".card h4{margin:8px 0 4px;font-size:1rem;font-weight:700;}\n.card p{margin:2px 0;font-size:.82rem;color:var(--sub);}"
c, n = re.subn(re.escape(old_h4), new_h4, c, count=1)
if n != 1: raise SystemExit(f"ERREUR h4 ({n})")

old_actions = ".actions{display:flex;gap:10px;margin-top:18px;}"
new_actions = ".actions{display:flex;gap:10px;margin-top:16px;}\n.actions .btn{flex:1;}"
c, n = re.subn(re.escape(old_actions), new_actions, c, count=1)
if n != 1: raise SystemExit(f"ERREUR actions ({n})")

with open("admin.html", "w", encoding="utf-8") as f:
    f.write(c)
print("OK admin.html tuiles")
