def patch(content, anchor, new, label):
    count = content.count(anchor)
    if count != 1:
        raise SystemExit(f"ERREUR ancre '{label}': trouvee {count} fois (attendu 1, trouve {count}).")
    return content.replace(anchor, new, 1)

with open("profil.html", "r", encoding="utf-8") as f:
    c = f.read()

c = patch(c,
  "--bg:#f5f6f8; --surface:#ffffff; --text:#151824; --muted:#6b7280;\n    --primary:#2454ff; --primary-dark:#173bd1; --border:#e2e5ea;",
  "--bg:#f5f6f8; --surface:#ffffff; --text:#151824; --muted:#6b7280;\n    --teal:#33d9c4; --pink:#ff4fa3;\n    --primary:#0e9488; --primary-dark:#ff4fa3; --border:#e2e5ea;",
  "root-vars")

c = patch(c,
  "header{\n    background:var(--surface); border-bottom:1px solid var(--border);",
  "header{\n    position:relative; background:var(--surface); border-bottom:1px solid var(--border);",
  "header-pos")
c = patch(c,
  "header .brand{flex:1; text-align:center;}\n  header .brand{font-weight:700; font-size:15px;}",
  "header .brand{flex:1; text-align:center;}\n  header .brand{font-weight:700; font-size:15px;}\n  header::before{content:\"\";position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg,var(--teal),var(--pink));}",
  "header-bar")

c = patch(c,
  ".photo-actions label{\n    display:inline-block; background:var(--primary); color:#fff; padding:8px 14px;",
  ".photo-actions label{\n    display:inline-block; background:linear-gradient(90deg,var(--teal),var(--pink)); color:#0d0f16; padding:8px 14px;",
  "photo-btn")

c = patch(c,
  "  .btn{\n    padding:10px 16px; border:none; border-radius:8px; font-size:14px; font-weight:600;\n    cursor:pointer; background:var(--primary); color:#fff;\n  }",
  "  .btn{\n    padding:10px 16px; border:none; border-radius:8px; font-size:14px; font-weight:700;\n    cursor:pointer; background:linear-gradient(90deg,var(--teal),var(--pink)); color:#0d0f16;\n    box-shadow:0 2px 8px rgba(51,217,196,.35);\n  }",
  "btn-main")

c = patch(c,
  "input:focus,textarea:focus,select:focus{outline:2px solid var(--primary); outline-offset:1px; background:#fff;}",
  "input:focus,textarea:focus,select:focus{outline:2px solid var(--teal); outline-offset:1px; background:#fff;}",
  "focus")

c = patch(c,
  ".badge.valide{background:#f0fdf4; color:var(--success);}",
  ".badge.valide{background:#e6fbf8; color:#0e9488;}",
  "badge-valide")
c = patch(c,
  ".badge.type{background:#eef2ff; color:var(--primary-dark); margin-left:6px;}",
  ".badge.type{background:#ffe9f4; color:#c2367f; margin-left:6px;}",
  "badge-type")

with open("profil.html", "w", encoding="utf-8") as f:
    f.write(c)
print("OK profil.html")
