def patch(content, anchor, new, label):
    count = content.count(anchor)
    if count != 1:
        raise SystemExit(f"ERREUR ancre '{label}': trouvee {count} fois (attendu 1).")
    return content.replace(anchor, new, 1)

with open("profil.html", "r", encoding="utf-8") as f:
    c = f.read()

old = """  }catch(err){
    alert("Impossible d'envoyer la photo. Réessaie.");
  }finally{"""
new = """  }catch(err){
    console.error(err);
    alert("Erreur upload: " + (err && err.message ? err.message : err));
  }finally{"""
c = patch(c, old, new, "photo-error")

with open("profil.html", "w", encoding="utf-8") as f:
    f.write(c)
print("OK")
