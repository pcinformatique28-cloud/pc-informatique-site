with open("admin.html", "r", encoding="utf-8") as f:
    c = f.read()

replacements = [
    ("--bg:#0d0f16;", "--bg:#fdf6ea;"),
    ("--card:#141826;", "--card:#ffffff;"),
    ("--text:#f2f3f7;", "--text:#2c2416;"),
    ("--sub:#9aa1b4;", "--sub:#8a7a63;"),
    ("--teal:#33d9c4;", "--teal:#EF9F27;"),
    ("--pink:#ff4fa3;", "--pink:#D4537E;"),
    ("--ok:#5ee06a;", "--ok:#15803d;"),
    ("--bad:#ff5c5c;", "--bad:#b91c1c;"),
    ("--wait:#f2c94c;", "--wait:#92400e;"),
    ("background:rgba(13,15,22,.94);backdrop-filter:blur(6px);border-bottom:1px solid #1e2338;",
     "background:rgba(255,255,255,.92);backdrop-filter:blur(6px);border-bottom:1px solid #f0e4c8;"),
    ("#1e2338", "#f0e4c8"),
    ("#1a1f33", "#fdf1dc"),
    ("#232841", "#f5ecd6"),
    ("#0f1220", "#ffffff"),
    ("#262c47", "#e6dcc4"),
    ("#141826", "#ffffff"),
]

for old, new in replacements:
    if old in c:
        c = c.replace(old, new)
    else:
        print(f"NON TROUVE: {old[:60]}")

with open("admin.html", "w", encoding="utf-8") as f:
    f.write(c)
print("OK theme_admin termine")
