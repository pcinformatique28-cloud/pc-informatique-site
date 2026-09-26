def patch(content, anchor, new, label):
    count = content.count(anchor)
    if count != 1:
        raise SystemExit(f"ERREUR ancre '{label}': trouvee {count} fois (attendu 1, trouve {count}).")
    return content.replace(anchor, new, 1)

with open("profil.html", "r", encoding="utf-8") as f:
    c = f.read()

old1 = "let currentUser = null;"
new1 = 'const ADMIN_UID = "QFC18HxRAZabqYD85S5eA7VLC5D3";\nlet currentUser = null;'
c = patch(c, old1, new1, "admin-const")

old2 = '<button id="btn-logout">Déconnexion</button>'
new2 = '''<a href="admin.html" id="btn-admin" style="display:none;align-items:center;gap:6px;text-decoration:none;color:#0d0f16;font-size:13px;background:linear-gradient(90deg,var(--primary),var(--primary-dark));border-radius:8px;padding:8px 12px;font-weight:700;">&#9881; Admin</a>
  <button id="btn-logout">Déconnexion</button>'''
c = patch(c, old2, new2, "admin-link")

old3 = "  currentUser = user;\n  try{"
new3 = "  currentUser = user;\n  if(user.uid === ADMIN_UID){ document.getElementById('btn-admin').style.display = 'inline-flex'; }\n  try{"
c = patch(c, old3, new3, "admin-reveal")

with open("profil.html", "w", encoding="utf-8") as f:
    f.write(c)
print("OK profil.html")
