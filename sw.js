const CACHE_NAME = "pc-informatique-v1791714503";
const CORE_ASSETS = ["./guide-widget.js", 
  "./index.html",
  "./images/icon-192.png",
  "./images/icon-512.png"
];

self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => cache.addAll(CORE_ASSETS))
  );
  self.skipWaiting();
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys().then((names) =>
      Promise.all(names.filter((n) => n !== CACHE_NAME).map((n) => caches.delete(n)))
    )
  );
  self.clients.claim();
});

self.addEventListener("fetch", (event) => {
  if (event.request.method !== "GET") return;
  event.respondWith(
    caches.match(event.request).then((cached) => {
      return cached || fetch(event.request).catch(() => cached);
    })
  );
});

// --- Notifications push (relais Cloudflare + Firebase Cloud Messaging)
self.addEventListener('push', (event) => {
  let p = {}
  try { p = event.data ? event.data.json() : {} } catch (e) { p = {} }
  const d = p.data || p.notification || p
  const title = d.title || 'PC-INFORMATIQUE'
  const ICON = './images/icon-192.png'
  event.waitUntil(self.clients.matchAll({ type: 'window', includeUncontrolled: true }).then((list) => {
    if (list.some((c) => c.visibilityState === 'visible')) return
    return self.registration.showNotification(title, {
      body: d.body || '', tag: d.tag || undefined, renotify: !!d.tag,
      icon: ICON || undefined, badge: ICON || undefined, data: { link: d.link || '' },
    })
  }))
})
self.addEventListener('notificationclick', (event) => {
  event.notification.close()
  const link = (event.notification.data && event.notification.data.link) || self.registration.scope
  event.waitUntil(self.clients.matchAll({ type: 'window', includeUncontrolled: true }).then((list) => {
    for (const c of list) {
      if ('navigate' in c) return c.navigate(link).then((x) => (x || c).focus()).catch(() => self.clients.openWindow(link))
    }
    return self.clients.openWindow(link)
  }))
})
