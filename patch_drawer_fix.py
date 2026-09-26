def patch(content, anchor, new, label):
    count = content.count(anchor)
    if count != 1:
        raise SystemExit(f"ERREUR ancre '{label}': trouvee {count} fois (attendu 1).")
    return content.replace(anchor, new, 1)

with open("index.html", "r", encoding="utf-8") as f:
    c = f.read()

old = "nav.d-links{display:flex;flex-direction:column;gap:4px;}"
new = "nav.d-links{display:flex;flex-direction:column;gap:4px;background:none;backdrop-filter:none;box-shadow:none;border-bottom:none;position:static;}"
c = patch(c, old, new, "nav-dlinks-fix")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(c)
print("OK index.html")
