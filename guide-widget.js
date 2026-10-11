/* Module « Comment ça marche » — PC-INFORMATIQUE
   Fichier autonome, sans bibliothèque. Tout se règle dans CONFIG. */
(function () {
  'use strict';
  if (window.GuideWidget) return;

  // ===== CONFIG =====
  var CONFIG = {
    homePathRegex: /(\/|index\.html)$/,
    adminPathRegex: /admin/i,
    menu: {
      containers: ['nav.d-links', '.drawer', '.sidebar', '#sideMenu', '.side-menu', '.menu-lateral'],
      label: '\u2753 Comment ça marche'
    },
    toast: { text: 'Comment ça marche ?', delayMs: 1500, durationMs: 7000, oncePerSession: true },
    fab: { text: '\u2753 Comment ça marche' },
    color: { gold: '#D4AF37', ink: '#1a1a1a', ivory: '#fdf8ef', night: '#0b1230' },
    defaultRole: 'visiteur',
    adminRole: 'admin',
    roles: [
      {
        id: 'visiteur', label: '\uD83D\uDD0D Visiteur',
        intro: 'Je découvre le site sans compte.',
        secs: [
          ['\u2705 Ce que je peux faire', ['Voir nos réalisations et nos applications.', 'Remplir le formulaire de nouvelle demande.', 'Lire la page À propos.']],
          ['\u26A0\uFE0F Ce que je dois faire', ['Remplir les champs marqués d\u2019une étoile.', 'Donner un téléphone ou un e-mail joignable.']],
          ['\uD83D\uDD27 Comment faire', ['Touchez \u2630 pour ouvrir le menu.', 'Touchez Nouvelle demande, puis suivez les 6 étapes.', 'Touchez Envoyer ma demande à la fin.']],
          ['\u2B50 Points importants', ['Un compte gratuit permet de suivre vos demandes.', 'Changez de langue avec Langue / Language dans le menu.']]
        ]
      },
      {
        id: 'membre', label: '\uD83D\uDC64 Membre',
        intro: 'J\u2019ai un compte gratuit et je suis connecté.',
        secs: [
          ['\u2705 Ce que je peux faire', ['Me connecter avec mon compte.', 'Créer et modifier mon profil.', 'Suivre mes demandes et mes projets.', 'Recevoir des notifications sur mon dossier.']],
          ['\u26A0\uFE0F Ce que je dois faire', ['Garder mes informations à jour.', 'Régler mes notifications selon mes besoins.']],
          ['\uD83D\uDD27 Comment faire', ['Touchez Connexion, puis saisissez e-mail et mot de passe.', 'Ouvrez Mon profil depuis le menu \u2630.', 'Touchez Paramètres notifications pour choisir vos alertes.']],
          ['\u2B50 Points importants', ['Ne partagez jamais votre mot de passe.', 'Touchez Déconnexion sur un téléphone partagé.']]
        ]
      },
      {
        id: 'admin', label: '\uD83D\uDEE0\uFE0F Admin',
        intro: 'Je traite les demandes et les projets des membres.',
        secs: [
          ['\u2705 Ce que je peux faire', ['Valider ou refuser les demandes de projet.', 'Valider ou refuser les projets des membres.', 'Modérer les contenus.']],
          ['\u26A0\uFE0F Ce que je dois faire', ['Garder l\u2019accès admin confidentiel.', 'Vérifier une demande avant de la valider.']],
          ['\uD83D\uDD27 Comment faire', ['Touchez Tableau de bord dans le menu.', 'Ouvrez la demande ou le projet à traiter.', 'Choisissez Valider ou Refuser.']],
          ['\u2B50 Points importants', ['Le membre est informé de votre décision.', 'Déconnectez-vous après chaque session admin.']]
        ]
      }
    ]
  };
  // ===== FIN CONFIG =====

  var C = CONFIG.color;
  var path = location.pathname;
  var isAdminPage = CONFIG.adminPathRegex.test(path);
  var isHome = CONFIG.homePathRegex.test(path) && !isAdminPage;
  var overlay = null;
  var toastEl = null;

  function h(tag, attrs, kids) {
    var e = document.createElement(tag);
    if (attrs) for (var k in attrs) {
      if (k === 'text') e.textContent = attrs[k];
      else if (k === 'style') e.style.cssText = attrs[k];
      else e.setAttribute(k, attrs[k]);
    }
    (kids || []).forEach(function (c) { if (c) e.appendChild(c); });
    return e;
  }

  function injectCss() {
    if (document.getElementById('gw-css')) return;
    var gold60 = 'rgba(212,175,55,.6)';
    var css =
      '.gw-pill{position:fixed;z-index:99990;background:rgba(11,18,48,.95);border:1px solid ' + C.gold + ';color:' + C.gold + ';box-shadow:0 6px 20px rgba(0,0,0,.4);font-family:inherit}' +
      '.gw-toast{left:12px;right:12px;margin:0 auto;max-width:360px;bottom:calc(96px + env(safe-area-inset-bottom,0px));border-radius:16px;padding:12px 16px;display:flex;align-items:center;gap:12px;cursor:pointer;font-size:14px;transition:opacity .5s,transform .5s}' +
      '.gw-toast.gw-hide{opacity:0;transform:translateY(8px)}' +
      '.gw-fab{left:12px;bottom:calc(96px + env(safe-area-inset-bottom,0px));border-radius:999px;padding:8px 16px;font-size:14px;font-weight:600;cursor:pointer}' +
      '.gw-round{width:36px;height:36px;border-radius:50%;border:1px solid ' + gold60 + ';background:none;color:' + C.gold + ';cursor:pointer;font-size:16px;flex-shrink:0}' +
      '.gw-ov{position:fixed;inset:0;z-index:99995;overflow-y:auto;background:#0b1230;font-family:inherit;-webkit-overflow-scrolling:touch}' +
      '.gw-box{max-width:448px;margin:0 auto;padding:20px 16px 40px;color:' + C.ivory + '}' +
      '.gw-head{display:flex;align-items:center;gap:8px;margin-bottom:16px}' +
      '.gw-title{flex:1;padding-left:36px;text-align:center;font-size:24px;font-weight:500;color:' + C.gold + ';margin:0}' +
      '.gw-tabs{display:grid;gap:8px;margin-bottom:16px}' +
      '.gw-tab{display:flex;align-items:center;justify-content:center;padding:8px 4px;border-radius:12px;font-weight:500;line-height:1.2;cursor:pointer;border:1px solid ' + gold60 + ';background:rgba(255,255,255,.05);color:' + C.ivory + ';font-family:inherit}' +
      '.gw-tab.gw-on{background:' + C.gold + ';border-color:' + C.gold + ';color:' + C.ink + '}' +
      '.gw-col .gw-tab{flex-direction:column;gap:2px;font-size:11px}' +
      '.gw-col .gw-ic{font-size:16px}' +
      '.gw-row .gw-tab{flex-direction:row;gap:6px;font-size:14px}' +
      '.gw-row .gw-ic{font-size:14px}' +
      '.gw-intro{text-align:center;font-size:14px;color:rgba(253,248,239,.8);margin:0 0 16px}' +
      '.gw-card{display:flex;gap:12px;padding:16px;margin-bottom:12px;border-radius:16px;border:1px solid ' + gold60 + ';background:rgba(255,255,255,.05)}' +
      '.gw-num{width:36px;height:36px;flex-shrink:0;border-radius:50%;background:' + C.gold + ';color:' + C.ink + ';display:flex;align-items:center;justify-content:center;font-size:18px;font-weight:600}' +
      '.gw-card h3{margin:0 0 6px;font-size:18px;font-weight:600;color:' + C.gold + '}' +
      '.gw-card ul{list-style:none;margin:0;padding:0;font-size:14px;color:rgba(253,248,239,.9)}' +
      '.gw-card li{display:flex;gap:8px;margin-bottom:4px}' +
      '.gw-card li b{color:' + C.gold + ';font-weight:400}';
    var s = h('style', { id: 'gw-css' });
    s.textContent = css;
    document.head.appendChild(s);
  }

  function visibleRoles() {
    return CONFIG.roles.filter(function (r) { return r.id !== CONFIG.adminRole || isAdminPage; });
  }

  function closeGuide() {
    if (overlay) { overlay.remove(); overlay = null; }
    document.body.style.overflow = '';
  }

  function render(roleId) {
    var roles = visibleRoles();
    var cur = roles.filter(function (r) { return r.id === roleId; })[0] || roles[0];
    var cols = roles.length === 3 ? 3 : (roles.length >= 4 ? 2 : roles.length);
    var tabs = h('div', { 'class': 'gw-tabs ' + (roles.length === 3 ? 'gw-col' : 'gw-row'), style: 'grid-template-columns:repeat(' + cols + ',1fr)' },
      roles.map(function (r) {
        var parts = r.label.split(' ');
        var b = h('button', { 'class': 'gw-tab' + (r.id === cur.id ? ' gw-on' : ''), type: 'button' }, [
          h('span', { 'class': 'gw-ic', 'aria-hidden': 'true', text: parts[0] }),
          h('span', { style: 'white-space:nowrap', text: parts.slice(1).join(' ') })
        ]);
        b.addEventListener('click', function () { render(r.id); });
        return b;
      }));
    var cards = cur.secs.map(function (s, i) {
      return h('div', { 'class': 'gw-card' }, [
        h('span', { 'class': 'gw-num', text: String(i + 1) }),
        h('div', { style: 'flex:1;min-width:0' }, [
          h('h3', { text: s[0] }),
          h('ul', null, s[1].map(function (t) {
            return h('li', null, [h('b', { 'aria-hidden': 'true', text: '\u2022' }), h('span', { text: t })]);
          }))
        ])
      ]);
    });
    var closeBtn = h('button', { 'class': 'gw-round', type: 'button', 'aria-label': 'Fermer', text: '\u2715' });
    closeBtn.addEventListener('click', closeGuide);
    var box = h('div', { 'class': 'gw-box' }, [
      h('div', { 'class': 'gw-head' }, [h('h2', { 'class': 'gw-title', text: 'Comment ça marche' }), closeBtn]),
      tabs,
      h('p', { 'class': 'gw-intro', text: cur.intro })
    ].concat(cards));
    if (!overlay) {
      overlay = h('div', { 'class': 'gw-ov', role: 'dialog', 'aria-modal': 'true' });
      document.body.appendChild(overlay);
    }
    overlay.innerHTML = '';
    overlay.appendChild(box);
    overlay.scrollTop = 0;
  }

  function open(roleId) {
    injectCss();
    hideToast();
    document.body.style.overflow = 'hidden';
    render(roleId || (isAdminPage ? CONFIG.adminRole : CONFIG.defaultRole));
  }

  function hideToast() {
    if (toastEl) { toastEl.remove(); toastEl = null; }
  }

  function showToast() {
    var forced = /[?&]guide=1/.test(location.search);
    if (CONFIG.toast.oncePerSession && !forced) {
      try {
        if (sessionStorage.getItem('gwSeen')) return;
        sessionStorage.setItem('gwSeen', '1');
      } catch (e) { /* ignore */ }
    }
    var x = h('button', { type: 'button', 'class': 'gw-round', 'aria-label': 'Fermer', style: 'width:28px;height:28px', text: '\u2715' });
    toastEl = h('div', { 'class': 'gw-pill gw-toast', role: 'status' }, [
      h('span', { 'aria-hidden': 'true', text: '\u2753' }),
      h('b', { style: 'flex:1;font-weight:500', text: CONFIG.toast.text }),
      x
    ]);
    toastEl.addEventListener('click', function () { open(); });
    x.addEventListener('click', function (e) { e.stopPropagation(); hideToast(); });
    document.body.appendChild(toastEl);
    var t = toastEl;
    setTimeout(function () { if (t === toastEl && t) t.classList.add('gw-hide'); }, CONFIG.toast.durationMs);
    setTimeout(function () { if (t === toastEl) hideToast(); }, CONFIG.toast.durationMs + 500);
  }

  function splashVisible() {
    var e = document.querySelector('[id*="splash"],[class*="splash"]');
    if (!e) return false;
    var cs = getComputedStyle(e);
    return cs.display !== 'none' && cs.visibility !== 'hidden' && parseFloat(cs.opacity) > 0.05 && e.offsetHeight > 0;
  }

  function scheduleToast() {
    var waited = 0;
    function go() { setTimeout(showToast, CONFIG.toast.delayMs); }
    function wait() {
      if (splashVisible() && waited < 12000) { waited += 300; setTimeout(wait, 300); }
      else go();
    }
    if (document.readyState === 'complete') wait();
    else window.addEventListener('load', wait);
  }

  function addMenuLine() {
    if (!CONFIG.menu || document.getElementById('gw-menu-line')) return true;
    var box = null;
    for (var i = 0; i < CONFIG.menu.containers.length && !box; i++) {
      box = document.querySelector(CONFIG.menu.containers[i]);
    }
    if (!box) return false;
    var ref = box.querySelector('a');
    var a = h('a', { href: '#', id: 'gw-menu-line' }, [
      h('span', { 'class': 'ic', 'aria-hidden': 'true', text: '\u2753' }),
      document.createTextNode('Comment ça marche')
    ]);
    if (ref && ref.className) a.className = ref.className;
    a.addEventListener('click', function (e) {
      e.preventDefault();
      e.stopPropagation();
      var c = document.getElementById('drawer-close');
      if (c) c.click();
      open();
    });
    var login = document.getElementById('drawer-login');
    if (login && login.parentNode === box) box.insertBefore(a, login);
    else box.appendChild(a);
    return true;
  }

  function init() {
    injectCss();
    if (!addMenuLine()) setTimeout(addMenuLine, 1500);
    if (isAdminPage) {
      var fab = h('button', { type: 'button', 'class': 'gw-pill gw-fab', text: CONFIG.fab.text });
      fab.addEventListener('click', function () { open(CONFIG.adminRole); });
      document.body.appendChild(fab);
    } else if (isHome) {
      scheduleToast();
    }
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeGuide(); });
  }

  window.GuideWidget = { open: open, close: closeGuide };
  window.addEventListener('guide:open', function () { open(); });

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
