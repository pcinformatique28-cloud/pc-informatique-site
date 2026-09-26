import re

with open("index.html", "r", encoding="utf-8") as f:
    c = f.read()

# 1) Nouvelles règles CSS (rangée flex + order)
old_css = ".navlinks{display:flex;gap:10px;flex-wrap:wrap;justify-content:center;width:100%;}"
new_css = old_css + """
.header-row{display:flex;align-items:center;width:100%;gap:8px;padding-top:env(safe-area-inset-top,0px);}
.header-row #btn-menu{order:1;}
.header-row .brand{order:2;flex:1 1 auto;min-width:0;justify-content:flex-start;text-align:left;}
.header-row .brand b{overflow:hidden;text-overflow:ellipsis;white-space:nowrap;}
.header-row #notif-bell{order:3;}
.header-row #auth-icon{order:4;}"""
c, n = re.subn(re.escape(old_css), new_css, c, count=1)
if n != 1: raise SystemExit(f"ERREUR css ({n})")

# 2) Ouvre header-row + nettoie btn-menu
old_menu = '<button class="icon-btn" id="btn-menu" style="position:absolute;left:14px;top:calc(14px + env(safe-area-inset-top,0px));" aria-label="Menu">&#9776;</button>'
new_menu = '<div class="header-row">\n    <button class="icon-btn" id="btn-menu" aria-label="Menu">&#9776;</button>'
c, n = re.subn(re.escape(old_menu), new_menu, c, count=1)
if n != 1: raise SystemExit(f"ERREUR btn-menu ({n})")

# 3) Nettoie auth-icon
old_auth = '<a href="connexion.html" class="icon-btn" id="auth-icon" style="position:absolute;right:14px;top:calc(14px + env(safe-area-inset-top,0px));" aria-label="Connexion">&#128273;</a>'
new_auth = '<a href="connexion.html" class="icon-btn" id="auth-icon" aria-label="Connexion">&#128273;</a>'
c, n = re.subn(re.escape(old_auth), new_auth, c, count=1)
if n != 1: raise SystemExit(f"ERREUR auth-icon ({n})")

# 4) Nettoie notif-bell (garde position:relative pour le badge)
old_bell = '<span class="icon-btn" id="notif-bell" style="display:none;position:absolute;right:56px;top:calc(14px + env(safe-area-inset-top,0px));cursor:pointer;" title="Notifications">&#128276;<span id="notif-bell-badge" style="display:none;position:absolute;top:-4px;right:-6px;background:#ff4fa3;color:#fff;font-size:.6rem;font-weight:800;border-radius:10px;padding:1px 5px;line-height:1;"></span></span>'
new_bell = '<span class="icon-btn" id="notif-bell" style="display:none;position:relative;cursor:pointer;" title="Notifications">&#128276;<span id="notif-bell-badge" style="display:none;position:absolute;top:-4px;right:-6px;background:#ff4fa3;color:#fff;font-size:.6rem;font-weight:800;border-radius:10px;padding:1px 5px;line-height:1;"></span></span>'
c, n = re.subn(re.escape(old_bell), new_bell, c, count=1)
if n != 1: raise SystemExit(f"ERREUR notif-bell ({n})")

# 5) Ferme header-row juste après le titre (sans toucher au logo)
old_close = '<b>PC-INFORMATIQUE</b></div>'
new_close = '<b>PC-INFORMATIQUE</b></div>\n  </div>'
c, n = re.subn(re.escape(old_close), new_close, c, count=1)
if n != 1: raise SystemExit(f"ERREUR fermeture header-row ({n})")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(c)
print("OK index.html header flex 3 zones")
