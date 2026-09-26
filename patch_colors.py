def patch(content, anchor, new, label):
    count = content.count(anchor)
    if count != 1:
        raise SystemExit(f"ERREUR ancre '{label}': trouvée {count} fois (attendu 1).")
    return content.replace(anchor, new, 1)

with open("index.html", "r", encoding="utf-8") as f:
    c = f.read()

# Header (nav) : fond chrome clair, brillant
old_nav = """nav{position:sticky;top:0;z-index:20;background:rgba(13,15,22,.94);backdrop-filter:blur(6px);border-bottom:1px solid #1e2338;
  padding:calc(14px + env(safe-area-inset-top,0px)) 16px 14px;}"""
new_nav = """nav{position:sticky;top:0;z-index:20;background:linear-gradient(180deg,#fcfcfe 0%,#e7eaf2 55%,#f6f7fb 100%);backdrop-filter:blur(6px);border-bottom:1px solid #d7dbe4;box-shadow:0 1px 0 rgba(255,255,255,.7) inset,0 2px 10px rgba(20,24,40,.08);
  padding:calc(14px + env(safe-area-inset-top,0px)) 16px 14px;}"""
c = patch(c, old_nav, new_nav, "nav")

old_brand = '.brand b{font-size:.95rem;letter-spacing:.02em;}'
new_brand = '.brand b{font-size:.95rem;letter-spacing:.02em;color:#1b2030;}'
c = patch(c, old_brand, new_brand, "brand-b")

old_links = '.navlinks a{display:inline-flex;align-items:center;justify-content:center;gap:6px;text-decoration:none;font-size:.78rem;color:var(--sub);padding:7px 12px;border-radius:20px;border:1px solid #232841;}'
new_links = '.navlinks a{display:inline-flex;align-items:center;justify-content:center;gap:6px;text-decoration:none;font-size:.78rem;color:#55596b;padding:7px 12px;border-radius:20px;border:1px solid #d7dbe4;background:#fff;}'
c = patch(c, old_links, new_links, "navlinks-a")

old_icon = """.icon-btn{background:none;border:1px solid #232841;color:var(--sub);width:34px;height:34px;border-radius:50%;
  display:inline-flex;align-items:center;justify-content:center;font-size:1rem;cursor:pointer;text-decoration:none;}
.icon-btn:hover{color:var(--teal);border-color:var(--teal);}"""
new_icon = """.icon-btn{background:#fff;border:1px solid #d7dbe4;color:#55596b;width:34px;height:34px;border-radius:50%;
  display:inline-flex;align-items:center;justify-content:center;font-size:1rem;cursor:pointer;text-decoration:none;box-shadow:0 1px 2px rgba(20,24,40,.08);}
.icon-btn:hover{color:#0e9488;border-color:#0e9488;}"""
c = patch(c, old_icon, new_icon, "icon-btn")

old_bottom = """.bottom-nav{position:fixed;left:0;right:0;bottom:0;z-index:30;background:rgba(13,15,22,.96);backdrop-filter:blur(6px);
  border-top:1px solid #1e2338;padding:8px 6px calc(8px + env(safe-area-inset-bottom,0px));display:flex;justify-content:space-around;}
.bottom-nav a{display:flex;flex-direction:column;align-items:center;gap:3px;color:var(--sub);text-decoration:none;font-size:.64rem;padding:4px 8px;}
.bottom-nav a.active{color:var(--teal);}"""
new_bottom = """.bottom-nav{position:fixed;left:0;right:0;bottom:0;z-index:30;background:linear-gradient(180deg,#f6f7fb 0%,#e7eaf2 100%);backdrop-filter:blur(6px);
  border-top:1px solid #d7dbe4;box-shadow:0 -2px 10px rgba(20,24,40,.06);padding:8px 6px calc(8px + env(safe-area-inset-bottom,0px));display:flex;justify-content:space-around;}
.bottom-nav a{display:flex;flex-direction:column;align-items:center;gap:3px;color:#6b7280;text-decoration:none;font-size:.64rem;padding:4px 8px;}
.bottom-nav a.active{color:#0e9488;}"""
c = patch(c, old_bottom, new_bottom, "bottom-nav")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(c)
print("OK: couleurs patchees.")
