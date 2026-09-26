with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

markers = [
    ".sheet-overlay{",
    "openSheet('about-sheet');return false;",
    'class="about-btn-wrap"',
    'id="sheet-overlay"',
]

for m in markers:
    before = text.count(m)
    idx1 = text.find(m)
    if idx1 == -1:
        continue
    idx2 = text.find(m, idx1 + 1)
    if idx2 == -1:
        print(f"OK deja unique: {m[:30]} (count={before})")
        continue
    block_len = idx2 - idx1
    text = text[:idx1] + text[idx1 + block_len:]
    after = text.count(m)
    print(f"Marqueur {m[:30]!r}: avant={before} apres={after} (block_len={block_len})")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(text)
print("OK dedupe_index3 termine")
