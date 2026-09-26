import re

with open("index.html", "r", encoding="utf-8") as f:
    c = f.read()

old_meta = '<meta charset="UTF-8">'
new_meta = old_meta + '\n<link rel="manifest" href="manifest.json">\n<meta name="theme-color" content="#0d0f16">\n<link rel="apple-touch-icon" href="images/icon-192.png">'
c, n = re.subn(re.escape(old_meta), new_meta, c, count=1)
if n != 1: raise SystemExit(f"ERREUR meta ({n})")

sw_block = '''
<script>
if ("serviceWorker" in navigator) {
  window.addEventListener("load", () => {
    navigator.serviceWorker.register("sw.js").catch(err => console.error("SW error:", err));
  });
}
</script>
'''
idx = c.rfind("</body>")
if idx == -1: raise SystemExit("ERREUR: </body> non trouve")
c = c[:idx] + sw_block + c[idx:]

with open("index.html", "w", encoding="utf-8") as f:
    f.write(c)
print("OK index.html PWA")
