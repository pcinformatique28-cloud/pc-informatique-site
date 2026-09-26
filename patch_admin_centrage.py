import re
with open("admin.html", "r", encoding="utf-8") as f:
    c = f.read()

old_tabs_css = ".tabs{display:flex;gap:8px;margin:16px 0;flex-wrap:wrap;}"
new_tabs_css = ".tabs{display:flex;gap:8px;margin:16px 0;flex-wrap:wrap;justify-content:center;}"
c, n = re.subn(re.escape(old_tabs_css), new_tabs_css, c, count=1)
if n != 1: raise SystemExit(f"ERREUR tabs css ({n})")

old_modebar = '<div class="modebar" style="display:flex;gap:8px;margin:14px 0;">'
new_modebar = '<div class="modebar" style="display:flex;gap:8px;margin:14px 0;justify-content:center;">'
c, n = re.subn(re.escape(old_modebar), new_modebar, c, count=1)
if n != 1: raise SystemExit(f"ERREUR modebar ({n})")

with open("admin.html", "w", encoding="utf-8") as f:
    f.write(c)
print("OK admin.html tabs centrees")
