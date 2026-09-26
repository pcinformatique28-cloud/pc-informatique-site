with open("index.html", "r", encoding="utf-8") as f:
    c = f.read()

replacements = [
    ("color-scheme: dark;", "color-scheme: light;"),
    ("--bg:#0d0f16;", "--bg:#fdf6ea;"),
    ("--card:#141826;", "--card:#ffffff;"),
    ("--text:#f2f3f7;", "--text:#2c2416;"),
    ("--sub:#9aa1b4;", "--sub:#8a7a63;"),
    ("--teal:#33d9c4;", "--teal:#EF9F27;"),
    ("--pink:#ff4fa3;", "--pink:#D4537E;"),
    ("background:linear-gradient(120deg,#33d9c4 0%,#3a8bff 50%,#ff4fa3 100%);",
     "background:linear-gradient(120deg,#EF9F27 0%,#F0997B 50%,#D4537E 100%);"),
    ("#1e2338", "#f0e4c8"),
    ("#1a1f33", "#fdf1dc"),
    ("#232841", "#f5ecd6"),
    ("#0f1220", "#ffffff"),
    ("#262c47", "#e6dcc4"),
    ("#141826", "#ffffff"),
    (".drawer a.d-link .ic{width:20px;text-align:center;filter:drop-shadow(0 0 2px rgba(51,217,196,.3));}",
     ".drawer a.d-link .ic{width:30px;height:30px;text-align:center;line-height:30px;background:#fff;border-radius:50%;box-shadow:0 1px 3px rgba(0,0,0,.12);margin-right:2px;}\n"
     ".drawer a.d-link{background:var(--bg);margin-bottom:4px;border-left:none;border-radius:12px;}\n"
     ".drawer a.d-link:hover{background:linear-gradient(90deg,rgba(239,159,39,.15),rgba(212,83,126,.15));}"),
    (".about-pane h4{color:var(--text);margin:14px 0 6px;font-size:.92rem;}",
     ".about-pane h4{color:var(--text);margin:14px 0 6px;font-size:.92rem;text-align:center;}\n"
     ".about-pane p{background:var(--bg);border:1px solid rgba(0,0,0,.06);border-radius:10px;padding:10px 12px;margin:0 0 10px;text-align:left;}"),
    (".sheet h3{margin:0 22px 12px 0;font-size:1.05rem;}",
     ".sheet h3{margin:0 22px 12px 0;font-size:1.05rem;text-align:center;}"),
    (".about-tabs{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:14px;}",
     ".about-tabs{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:14px;justify-content:center;}"),
]

for old, new in replacements:
    if old in c:
        c = c.replace(old, new)
    else:
        print(f"NON TROUVE: {old[:60]}")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(c)
print("OK theme_index termine")
