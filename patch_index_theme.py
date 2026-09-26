def patch(content, anchor, new, label):
    count = content.count(anchor)
    if count != 1:
        raise SystemExit(f"ERREUR ancre '{label}': trouvee {count} fois (attendu 1).")
    return content.replace(anchor, new, 1)

with open("index.html", "r", encoding="utf-8") as f:
    c = f.read()

# 1) Empeche Chrome de forcer un theme different (corrige le drawer blanc)
old_head = "<head>"
new_head = """<head>
<meta name="color-scheme" content="dark">"""
c = patch(c, old_head, new_head, "head")

# 2) Renforce au niveau CSS
old_root = ":root{\n  --bg:#0d0f16; --card:#141826; --text:#f2f3f7; --sub:#9aa1b4;"
new_root = ":root{\n  color-scheme: dark;\n  --bg:#0d0f16; --card:#141826; --text:#f2f3f7; --sub:#9aa1b4;"
c = patch(c, old_root, new_root, "root-css")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(c)
print("OK: index.html patche avec succes.")
