def patch(content, anchor, new, label):
    count = content.count(anchor)
    if count != 1:
        raise SystemExit(f"ERREUR ancre '{label}': trouvee {count} fois (attendu 1, trouve {count}).")
    return content.replace(anchor, new, 1)

with open("index.html", "r", encoding="utf-8") as f:
    c = f.read()

old = """.drawer{position:fixed;top:0;left:0;bottom:0;width:78%;max-width:300px;background:var(--card);border-right:1px solid #1e2338;
  z-index:50;transform:translateX(-100%);transition:transform .28s ease;padding:calc(20px + env(safe-area-inset-top,0px)) 18px 20px;overflow-y:auto;}
.drawer.open{transform:translateX(0);}
.drawer .d-user{display:flex;align-items:center;gap:12px;margin-bottom:20px;padding-bottom:16px;border-bottom:1px solid #1e2338;}
.drawer .d-user img{width:46px;height:46px;border-radius:50%;object-fit:cover;background:#232841;}
.drawer .d-user .d-name{font-weight:700;font-size:.92rem;}
.drawer .d-user .d-email{color:var(--sub);font-size:.74rem;}
.drawer nav.d-links{display:flex;flex-direction:column;gap:4px;}
.drawer a.d-link{display:flex;align-items:center;gap:12px;padding:11px 10px;border-radius:10px;color:var(--text);text-decoration:none;font-size:.88rem;}
.drawer a.d-link:hover{background:#1a1f33;}
.drawer a.d-link .ic{width:20px;text-align:center;}"""

new = """.drawer{position:fixed;top:0;left:0;bottom:0;width:78%;max-width:300px;background:var(--card);border-right:1px solid #1e2338;
  z-index:50;transform:translateX(-100%);transition:transform .28s ease;padding:calc(20px + env(safe-area-inset-top,0px)) 18px 20px;overflow-y:auto;
  box-shadow:4px 0 24px rgba(0,0,0,.4);}
.drawer::before{content:"";position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg,var(--teal),var(--pink));}
.drawer.open{transform:translateX(0);}
.drawer .d-user{display:flex;align-items:center;gap:12px;margin-bottom:20px;padding-bottom:16px;border-bottom:1px solid #1e2338;}
.drawer .d-user img{width:46px;height:46px;border-radius:50%;object-fit:cover;background:#232841;border:2px solid var(--teal);}
.drawer .d-user .d-name{font-weight:700;font-size:.92rem;color:var(--text);}
.drawer .d-user .d-email{color:var(--sub);font-size:.74rem;}
.drawer nav.d-links{display:flex;flex-direction:column;gap:4px;}
.drawer a.d-link{display:flex;align-items:center;gap:12px;padding:11px 10px;border-radius:10px;color:var(--text);text-decoration:none;font-size:.88rem;border-left:3px solid transparent;}
.drawer a.d-link:hover{background:#1a1f33;border-left:3px solid var(--teal);}
.drawer a.d-link .ic{width:20px;text-align:center;filter:drop-shadow(0 0 2px rgba(51,217,196,.3));}"""

c = patch(c, old, new, "drawer-css")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(c)
print("OK")
