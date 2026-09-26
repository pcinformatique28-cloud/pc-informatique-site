import re
with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

markers = [
    ".sheet-overlay{",
    "openSheet('about-sheet');return false;",
    'class="about-btn-wrap"',
    'id="sheet-overlay"',
]

for m in markers:
    idx1 = text.find(m)
    if idx1 == -1:
        continue
    idx2 = text.find(m, idx1 + 1)
    if idx2 == -1:
        continue
    block_len = idx2 - idx1
    if text[idx1:idx2] == text[idx2:idx2 + block_len]:
        text = text[:idx2] + text[idx2 + block_len:]
        print(f"Doublon supprime pour marqueur: {m[:30]}")
    else:
        print(f"ATTENTION: pas de doublon exact detecte pour: {m[:30]}")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(text)
print("OK dedupe_index termine")
