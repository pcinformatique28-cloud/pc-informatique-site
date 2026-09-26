import re

with open("admin.html", "r", encoding="utf-8") as f:
    c = f.read()

old_navwrap = '.navwrap{max-width:640px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;gap:10px;}'
new_navwrap = old_navwrap + '\n.navwrap b{flex:1 1 auto;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;}\n.navwrap .headright{display:flex;align-items:center;gap:10px;flex-shrink:0;}\n#count{background:rgba(255,255,255,.06);padding:3px 9px;border-radius:20px;}'
c, n = re.subn(re.escape(old_navwrap), new_navwrap, c, count=1)
if n != 1: raise SystemExit(f"ERREUR navwrap ({n})")

old_head = '<nav><div class="navwrap"><b>🔧 PC-INFORMATIQUE — Admin</b><span style="display:flex;align-items:center;gap:12px;"><span id="count" style="font-size:.75rem;color:var(--sub)"></span><span class="bell" id="admin-bell" title="Notifications">&#128276;<span class="bell-badge" id="admin-bell-badge" style="display:none;"></span></span></span></div></nav>'
new_head = '<nav><div class="navwrap"><b>🔧 PC-INFORMATIQUE — Admin</b><span class="headright"><span id="count" style="font-size:.75rem;color:var(--sub)"></span><span class="bell" id="admin-bell" title="Notifications">&#128276;<span class="bell-badge" id="admin-bell-badge" style="display:none;"></span></span></span></div></nav>'
c, n = re.subn(re.escape(old_head), new_head, c, count=1)
if n != 1: raise SystemExit(f"ERREUR head markup ({n})")

with open("admin.html", "w", encoding="utf-8") as f:
    f.write(c)
print("OK admin.html header aligne")
