import re

with open("index.html", "r", encoding="utf-8") as f:
    c = f.read()

# 1) CSS : sheets, tabs, toggles, notif-rows, ajoutés apres le CSS du drawer-close
old_css_anchor = '.drawer .d-close{position:absolute;top:calc(14px + env(safe-area-inset-top,0px));right:14px;background:none;border:none;color:var(--sub);font-size:1.3rem;cursor:pointer;}'
new_css = old_css_anchor + '''
.sheet-overlay{position:fixed;inset:0;background:rgba(0,0,0,.6);z-index:60;opacity:0;pointer-events:none;transition:opacity .25s ease;}
.sheet-overlay.open{opacity:1;pointer-events:auto;}
.sheet{position:fixed;left:0;right:0;bottom:0;max-height:82vh;background:var(--card);border-radius:20px 20px 0 0;z-index:61;transform:translateY(100%);transition:transform .3s ease;padding:18px 18px calc(20px + env(safe-area-inset-bottom,0px));overflow-y:auto;display:none;}
.sheet.open{display:block;transform:translateY(0);}
.sheet h3{margin:0 22px 12px 0;font-size:1.05rem;}
.sheet-close{position:absolute;top:12px;right:14px;background:none;border:none;color:var(--sub);font-size:1.3rem;cursor:pointer;}
.about-tabs{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:14px;}
.about-tabs button{font-size:.72rem;padding:7px 12px;border-radius:20px;border:1px solid #232841;background:none;color:var(--sub);cursor:pointer;}
.about-tabs button.on{background:linear-gradient(90deg,var(--teal),var(--pink));color:#0d0f16;border:none;font-weight:700;}
.about-pane{display:none;font-size:.85rem;line-height:1.6;color:var(--sub);}
.about-pane.on{display:block;}
.about-pane h4{color:var(--text);margin:14px 0 6px;font-size:.92rem;}
.about-apps{display:flex;flex-direction:column;gap:8px;margin-top:10px;}
.about-apps a{display:flex;align-items:center;justify-content:space-between;padding:10px 12px;border-radius:12px;background:#1a1f33;color:var(--text);text-decoration:none;font-size:.82rem;}
.about-creator{display:flex;align-items:center;gap:12px;margin:4px 0 14px;padding:12px;border-radius:14px;background:#1a1f33;}
.about-creator .ac-avatar{width:52px;height:52px;border-radius:50%;background:linear-gradient(135deg,var(--teal),var(--pink));display:flex;align-items:center;justify-content:center;font-size:1.4rem;flex-shrink:0;}
.about-creator b{color:var(--text);font-size:.88rem;}
.toggle{position:relative;display:inline-block;width:42px;height:24px;flex-shrink:0;}
.toggle input{opacity:0;width:0;height:0;}
.toggle .tg-slider{position:absolute;cursor:pointer;inset:0;background:#2c3350;transition:.2s;border-radius:24px;}
.toggle .tg-slider:before{content:"";position:absolute;height:18px;width:18px;left:3px;bottom:3px;background:#fff;transition:.2s;border-radius:50%;}
.toggle input:checked + .tg-slider{background:linear-gradient(90deg,var(--teal),var(--pink));}
.toggle input:checked + .tg-slider:before{transform:translateX(18px);}
.notif-row{display:flex;align-items:center;justify-content:space-between;gap:12px;padding:12px 0;border-bottom:1px solid #1e2338;}
.notif-row:last-child{border-bottom:none;}
.notif-row .nr-label{font-size:.86rem;color:var(--text);}
.notif-row .nr-sub{font-size:.72rem;color:var(--sub);margin-top:2px;}
.about-btn-wrap{text-align:center;margin:6px 0 30px;}
.about-btn-wrap button{background:none;border:1px solid #232841;color:var(--text);border-radius:20px;padding:10px 18px;font-size:.82rem;cursor:pointer;}'''
c, n = re.subn(re.escape(old_css_anchor), new_css, c, count=1)
if n != 1: raise SystemExit(f"ERREUR css ({n})")

# 2) Liens dans le drawer (avant Connexion)
old_login = '<a href="connexion.html" class="d-link" id="drawer-login"><span class="ic">&#128273;</span>Connexion</a>'
new_login = '<a href="#" class="d-link" onclick="openSheet(\'about-sheet\');return false;"><span class="ic">&#8505;</span>A propos</a>\n    <a href="#" class="d-link" onclick="openSheet(\'notif-sheet\');return false;"><span class="ic">&#128276;</span>Parametres notifications</a>\n    ' + old_login
c, n = re.subn(re.escape(old_login), new_login, c, count=1)
if n != 1: raise SystemExit(f"ERREUR drawer links ({n})")

# 3) Bouton "A propos" visible, juste avant la section "Nouvelle demande"
old_demande = '<div class="section-title" id="demande">'
new_demande = '<div class="about-btn-wrap"><button onclick="openSheet(\'about-sheet\')">&#8505;&nbsp; A propos de PC-INFORMATIQUE</button></div>\n\n' + old_demande
c, n = re.subn(re.escape(old_demande), new_demande, c, count=1)
if n != 1: raise SystemExit(f"ERREUR bouton a propos ({n})")

# 4) Sheets HTML + JS, juste avant </body>
sheets_html = '''
<div class="sheet-overlay" id="sheet-overlay" onclick="closeSheets()"></div>

<div class="sheet" id="about-sheet">
  <button class="sheet-close" onclick="closeSheets()">&times;</button>
  <h3>A propos de PC-INFORMATIQUE</h3>
  <div class="about-tabs">
    <button class="on" data-tab="presentation" onclick="showAboutTab('presentation')">Presentation</button>
    <button data-tab="roles" onclick="showAboutTab('roles')">Roles</button>
    <button data-tab="donnees" onclick="showAboutTab('donnees')">Donnees</button>
    <button data-tab="contact" onclick="showAboutTab('contact')">Contact</button>
    <button data-tab="legal" onclick="showAboutTab('legal')">Legal</button>
  </div>

  <div class="about-pane on" id="about-presentation">
    <div class="about-creator">
      <div class="ac-avatar">&#128187;</div>
      <div>
        <b>KOZANGUE ESSONO PATRICK BERTIN</b><br>
        Informaticien &middot; Fondateur &amp; President de PC-INFORMATIQUE
      </div>
    </div>
    <p>PC-INFORMATIQUE est un studio de developpement base a Libreville, Gabon, specialise dans la creation de sites, d'applications et de PWA sur mesure pour les entreprises et particuliers gabonais.</p>
    <h4>Nos 5 applications</h4>
    <div class="about-apps">
      <a href="index.html">PC-INFORMATIQUE (ce site) <span>&#8594;</span></a>
      <a href="https://ambi2412026-debug.github.io/ambi241" target="_blank" rel="noopener">AMBI241 <span>&#8594;</span></a>
      <a href="https://magerante241-boop.github.io/magerante/" target="_blank" rel="noopener">MAGERANTE <span>&#8594;</span></a>
      <a href="https://malagagabon-dot.github.io/malaga-gabon/" target="_blank" rel="noopener">MALAGA <span>&#8594;</span></a>
      <a href="https://gabon-sport-connect.web.app" target="_blank" rel="noopener">Gabon Sport Connect <span>&#8594;</span></a>
    </div>
  </div>

  <div class="about-pane" id="about-roles">
    <h4>Visiteur (non connecte)</h4>
    <p>Acces en lecture seule aux realisations, au formulaire de demande de projet et aux informations publiques du site.</p>
    <h4>Membre (compte gratuit)</h4>
    <p>Creation de profil, suivi de ses demandes et de ses projets soumis, reception des notifications liees a son dossier.</p>
    <h4>Administrateur</h4>
    <p>Acces complet au tableau de bord : validation ou refus des demandes et des projets membres, moderation des contenus.</p>
  </div>

  <div class="about-pane" id="about-donnees">
    <h4>Donnees collectees</h4>
    <p>Identifiant, email, informations de contact et details du projet transmis via le formulaire de demande.</p>
    <h4>Stockage</h4>
    <p>Les donnees sont hebergees via Firebase (Authentification, Firestore) et securisees selon les regles d'acces standard de la plateforme.</p>
    <h4>Usage</h4>
    <p>Ces informations servent uniquement au traitement de votre demande et au fonctionnement du site. Elles ne sont ni vendues ni partagees avec des tiers.</p>
  </div>

  <div class="about-pane" id="about-contact">
    <h4>Nous contacter</h4>
    <p>&#128231; pcinformatique28@gmail.com<br>&#128222; +241 60 14 19 24</p>
    <p>Pour toute question, signalement ou demande d'assistance concernant l'une de nos 5 applications, contactez l'administration PC-INFORMATIQUE.</p>
  </div>

  <div class="about-pane" id="about-legal">
    <h4>Mentions legales &amp; CGU</h4>
    <p><b>Editeur :</b> PC-INFORMATIQUE, studio de developpement, Libreville, Gabon.</p>
    <p><b>Objet :</b> ce site presente nos realisations et permet de soumettre une demande de creation de site, application ou PWA.</p>
    <p><b>Contenu :</b> les projets et informations soumis via le formulaire restent la propriete de leurs auteurs et sont traites uniquement dans le cadre de la demande.</p>
    <p><b>Acces mineurs :</b> l'utilisation du formulaire de demande de projet suppose d'etre majeur ou d'avoir l'accord d'un representant legal.</p>
  </div>
</div>

<div class="sheet" id="notif-sheet">
  <button class="sheet-close" onclick="closeSheets()">&times;</button>
  <h3>Parametres notifications</h3>
  <div class="notif-row">
    <div><div class="nr-label">Suivi de mes demandes</div><div class="nr-sub">Statut valide / refuse de vos demandes de projet</div></div>
    <label class="toggle"><input type="checkbox" id="notif-demandes" onchange="saveNotifPref('demandes', this.checked)"><span class="tg-slider"></span></label>
  </div>
  <div class="notif-row">
    <div><div class="nr-label">Suivi de mes projets membres</div><div class="nr-sub">Validation ou refus de vos projets soumis</div></div>
    <label class="toggle"><input type="checkbox" id="notif-projets" onchange="saveNotifPref('projets', this.checked)"><span class="tg-slider"></span></label>
  </div>
  <div class="notif-row">
    <div><div class="nr-label">Actualites PC-INFORMATIQUE</div><div class="nr-sub">Nouveautes et informations du studio</div></div>
    <label class="toggle"><input type="checkbox" id="notif-actus" onchange="saveNotifPref('actus', this.checked)"><span class="tg-slider"></span></label>
  </div>
  <div class="notif-row">
    <div><div class="nr-label">Rappels</div><div class="nr-sub">Echeances et relances liees a vos demandes</div></div>
    <label class="toggle"><input type="checkbox" id="notif-rappels" onchange="saveNotifPref('rappels', this.checked)"><span class="tg-slider"></span></label>
  </div>
</div>

<script>
function openSheet(id){
  document.getElementById('sheet-overlay').classList.add('open');
  document.getElementById(id).classList.add('open');
}
function closeSheets(){
  document.getElementById('sheet-overlay').classList.remove('open');
  document.querySelectorAll('.sheet').forEach(function(s){ s.classList.remove('open'); });
}
function showAboutTab(name){
  document.querySelectorAll('.about-tabs button').forEach(function(b){ b.classList.toggle('on', b.dataset.tab===name); });
  document.querySelectorAll('.about-pane').forEach(function(p){ p.classList.toggle('on', p.id==='about-'+name); });
}
var NOTIF_KEYS = ['demandes','projets','actus','rappels'];
function loadNotifPrefs(){
  var saved = {};
  try{ saved = JSON.parse(localStorage.getItem('notif_prefs') || '{}'); }catch(e){}
  NOTIF_KEYS.forEach(function(k){
    var el = document.getElementById('notif-'+k);
    if(el) el.checked = saved[k] !== false;
  });
}
function saveNotifPref(key, val){
  var saved = {};
  try{ saved = JSON.parse(localStorage.getItem('notif_prefs') || '{}'); }catch(e){}
  saved[key] = val;
  localStorage.setItem('notif_prefs', JSON.stringify(saved));
}
loadNotifPrefs();
</script>
'''
old_body_close = '</body>'
c, n = re.subn(re.escape(old_body_close), sheets_html + '\n</body>', c, count=1)
if n != 1: raise SystemExit(f"ERREUR insertion sheets ({n})")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(c)
print("OK index.html : A propos + parametres notifications ajoutes")
