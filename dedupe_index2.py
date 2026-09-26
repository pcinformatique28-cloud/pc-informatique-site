with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

markers = [
    ".sheet-overlay{",
    "openSheet('about-sheet');return false;",
    'class="about-btn-wrap"',
    'id="sheet-overlay"',
]

for m in markers:
    passes = 0
    while passes < 10:
        idx1 = text.find(m)
        if idx1 == -1:
            break
        idx2 = text.find(m, idx1 + 1)
        if idx2 == -1:
            break
        block_len = idx2 - idx1
        if text[idx1:idx2] == text[idx2:idx2 + block_len]:
            text = text[:idx2] + text[idx2 + block_len:]
            passes += 1
            print(f"Fusion #{passes} pour marqueur: {m[:30]}")
        else:
            break

with open("index.html", "w", encoding="utf-8") as f:
    f.write(text)
print("OK dedupe_index2 termine")
