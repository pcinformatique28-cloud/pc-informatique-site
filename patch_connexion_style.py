def patch(content, anchor, new, label):
    count = content.count(anchor)
    if count != 1:
        raise SystemExit(f"ERREUR ancre '{label}': trouvee {count} fois (attendu 1, trouve {count}).")
    return content.replace(anchor, new, 1)

with open("connexion.html", "r", encoding="utf-8") as f:
    c = f.read()

old_style_close = "</style>"
new_style_close = """  body{background:linear-gradient(160deg,#eafbf8 0%,#fdeef6 100%) !important;}
  .card{position:relative;overflow:hidden;box-shadow:0 8px 30px rgba(20,24,40,.08) !important;}
  .card::before{content:"";position:absolute;top:0;left:0;right:0;height:4px;background:linear-gradient(90deg,#33d9c4,#ff4fa3);}
  input{background:#f4fbfa !important;}
  input:focus{outline:2px solid #33d9c4 !important;}
  button{background:linear-gradient(90deg,#33d9c4,#ff4fa3) !important;color:#0d0f16 !important;font-weight:700;box-shadow:0 2px 8px rgba(51,217,196,.35);}
  .msg.ok{background:#e6fbf8 !important;color:#0e9488 !important;}
  .msg.err{background:#fdeef1 !important;}
</style>"""
c = patch(c, old_style_close, new_style_close, "style-close")

with open("connexion.html", "w", encoding="utf-8") as f:
    f.write(c)
print("OK connexion.html")
