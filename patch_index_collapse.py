import re
with open("index.html", "r", encoding="utf-8") as f:
    c = f.read()

old_visitbtn_css = ".visit-btn{display:inline-flex;align-items:center;gap:6px;margin-top:10px;font-size:.74rem;font-weight:700;color:var(--teal);}"
new_visitbtn_css = old_visitbtn_css + """
.card-head{display:flex;align-items:center;justify-content:space-between;padding:14px 18px;cursor:pointer;}
.card-head h3{margin:0;font-size:1.02rem;}
.chevron{color:var(--sub);transition:transform .2s ease;font-size:.9rem;}
.card.expanded .chevron{transform:rotate(180deg);}
.card-details{display:none;}
.card.expanded .card-details{display:block;}"""
c, n = re.subn(re.escape(old_visitbtn_css), new_visitbtn_css, c, count=1)
if n != 1: raise SystemExit(f"ERREUR css ({n})")

pattern = re.compile(
    r'<a class="card-link" href="(?P<href>[^"]+)" target="_blank" rel="noopener">\s*'
    r'<div class="card (?P<cls>\w+)">\s*'
    r'(?P<shot><div class="shot">.*?</div>)\s*'
    r'<div class="card-body"><h3>(?P<title>[^<]+)</h3><p>(?P<desc>[^<]+)</p>'
    r'<div class="visit-btn"(?P<vbtnattr>[^>]*)>(?P<vbtn>[^<]+)</div></div>\s*'
    r'</div>\s*</a>',
    re.DOTALL
)

def build(m):
    return (
        f'<div class="card {m.group("cls")}" id="card-{m.group("cls")}">\n'
        f'  <div class="card-head" onclick="toggleCard(\'{m.group("cls")}\')">\n'
        f'    <h3>{m.group("title")}</h3>\n'
        f'    <span class="chevron">&#9662;</span>\n'
        f'  </div>\n'
        f'  <div class="card-details">\n'
        f'    {m.group("shot")}\n'
        f'    <div class="card-body"><p>{m.group("desc")}</p>'
        f'<a class="visit-btn"{m.group("vbtnattr")} href="{m.group("href")}" target="_blank" rel="noopener">{m.group("vbtn")}</a></div>\n'
        f'  </div>\n'
        f'</div>'
    )

c, n = pattern.subn(build, c)
if n != 4: raise SystemExit(f"ERREUR cartes transformees ({n} au lieu de 4)")

old_anchor = '<div class="section-title" id="demande">'
new_anchor = "<script>\nfunction toggleCard(id){\n  var el = document.getElementById('card-'+id);\n  if(el) el.classList.toggle('expanded');\n}\n</script>\n\n" + old_anchor
c, n = re.subn(re.escape(old_anchor), new_anchor, c, count=1)
if n != 1: raise SystemExit(f"ERREUR script insertion ({n})")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(c)
print("OK index.html cartes repliables")
