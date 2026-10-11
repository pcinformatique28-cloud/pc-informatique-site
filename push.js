/* push.js - alertes telephone (Firebase Cloud Messaging + relais Cloudflare) */
(function () {
  'use strict';
  var VAPID = 'BL0aobUE5AnXVACgncB6TIJRNzlmw1dwD1y_qH4wzVJrbfmMaBdiqT8jw_cXbrYAZplhu3ZHnEQno6mYHsiWeAQ';
  var RELAY = 'https://pcinfo-relais.pcinformatique28.workers.dev';
  var LS = 'pcinfoPushTok';
  var btn = null;
  var user = null;

  function ping(route, id) {
    try {
      fetch(RELAY + route, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ id: id }),
        keepalive: true
      }).catch(function () {});
    } catch (e) {}
  }
  window.pingRelais = ping;

  // Appels au relais : nouvelle demande, projet cree, projet modifie ou decide.
  // Le relais relit l'etat reel dans Firestore et n'envoie qu'une fois par element.
  function hookFirestore() {
    try {
      var F = firebase.firestore;
      var C = F.CollectionReference.prototype;
      var D = F.DocumentReference.prototype;
      if (C.__pcHook) return;
      C.__pcHook = true;
      var add = C.add;
      C.add = function () {
        var p = add.apply(this, arguments);
        var path = this.path;
        if (path === 'demandes' || path === 'projets') {
          p.then(function (ref) {
            ping(path === 'demandes' ? '/notify-demande' : '/notify-projet', ref.id);
          }, function () {});
        }
        return p;
      };
      var upd = D.update;
      D.update = function () {
        var p = upd.apply(this, arguments);
        var parts = String(this.path).split('/');
        if (parts[0] === 'projets' && parts.length === 2) {
          p.then(function () { ping('/notify-projet', parts[1]); }, function () {});
        }
        return p;
      };
    } catch (e) { console.warn('push: hook firestore', e); }
  }

  function supported() {
    try {
      return 'Notification' in window && 'serviceWorker' in navigator &&
        'PushManager' in window && !!firebase.messaging &&
        firebase.messaging.isSupported();
    } catch (e) { return false; }
  }

  function getTok() {
    return navigator.serviceWorker.ready.then(function (reg) {
      return firebase.messaging().getToken({ vapidKey: VAPID, serviceWorkerRegistration: reg });
    });
  }

  function save(tok) {
    return firebase.firestore().collection('pushTokens').doc(tok)
      .set({ uid: user.uid, createdAt: Date.now() })
      .then(function () {
        try { localStorage.setItem(LS, tok); } catch (e) {}
        return tok;
      });
  }

  function ensureBtn() {
    if (btn) return btn;
    btn = document.createElement('button');
    btn.type = 'button';
    btn.style.cssText = 'position:fixed;left:12px;bottom:12px;z-index:9998;padding:9px 14px;' +
      'border-radius:20px;border:1px solid rgba(255,255,255,.25);background:#0f2a3a;color:#fff;' +
      'font:600 13px system-ui,sans-serif;box-shadow:0 2px 10px rgba(0,0,0,.35);cursor:pointer;display:none';
    btn.onclick = function () {
      btn.disabled = true;
      activate().then(function () { btn.disabled = false; });
    };
    document.body.appendChild(btn);
    return btn;
  }

  function show(text, autoHide) {
    var b = ensureBtn();
    b.textContent = text;
    b.style.display = 'block';
    if (autoHide) setTimeout(function () { b.style.display = 'none'; }, 3500);
  }

  function hide() { if (btn) btn.style.display = 'none'; }

  function activate() {
    if (!user) return Promise.resolve();
    return Notification.requestPermission().then(function (perm) {
      if (perm !== 'granted') {
        show(perm === 'denied' ? 'Alertes bloqu\u00e9es (r\u00e9glages du navigateur)' : '\uD83D\uDD14 Activer les alertes t\u00e9l\u00e9phone', perm === 'denied');
        return;
      }
      return getTok().then(function (tok) {
        if (!tok) throw new Error('jeton vide');
        return save(tok);
      }).then(function () { show('\u2713 Alertes t\u00e9l\u00e9phone activ\u00e9es', true); });
    }).catch(function (e) {
      console.warn('push:', e);
      show('Alertes indisponibles ici', true);
    });
  }

  function onLogin(u) {
    user = u;
    if (!u || !supported()) { hide(); return; }
    var perm = Notification.permission;
    if (perm === 'granted') {
      hide();
      getTok().then(function (tok) { if (tok) return save(tok); }).catch(function (e) { console.warn('push:', e); });
    } else if (perm === 'default') {
      show('\uD83D\uDD14 Activer les alertes t\u00e9l\u00e9phone');
    } else {
      hide();
    }
  }

  // A la deconnexion : supprimer le jeton (2 s maximum pour ne pas bloquer)
  function patchSignOut(a) {
    if (a.__pcSO) return;
    a.__pcSO = true;
    var orig = a.signOut.bind(a);
    a.signOut = function () {
      var tok = null;
      try { tok = localStorage.getItem(LS); } catch (e) {}
      try { localStorage.removeItem(LS); } catch (e) {}
      var del = tok
        ? firebase.firestore().collection('pushTokens').doc(tok).delete().catch(function () {})
        : Promise.resolve();
      return Promise.race([del, new Promise(function (r) { setTimeout(r, 2000); })])
        .then(function () { return orig(); });
    };
  }

  function boot() {
    var n = 0;
    var t = setInterval(function () {
      n++;
      if (window.firebase && firebase.apps && firebase.apps.length && firebase.auth) {
        clearInterval(t);
        try {
          var a = firebase.auth();
          patchSignOut(a);
          a.onAuthStateChanged(onLogin);
        } catch (e) { console.warn('push: auth', e); }
      } else if (n > 100) {
        clearInterval(t);
      }
    }, 300);
  }

  hookFirestore();
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot);
  else boot();
})();
