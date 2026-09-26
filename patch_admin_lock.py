def patch(content, anchor, new, label):
    count = content.count(anchor)
    if count != 1:
        raise SystemExit(f"ERREUR ancre '{label}': trouvee {count} fois (attendu 1, trouve {count}).")
    return content.replace(anchor, new, 1)

with open("admin.html", "r", encoding="utf-8") as f:
    c = f.read()

old = """// ---- Bascule gate/dash selon l'état de connexion ----
auth.onAuthStateChanged(user=>{
  if(user){
    document.getElementById('gate').style.display='none';
    document.getElementById('dash').style.display='block';
    loadList();
  } else {
    document.getElementById('gate').style.display='block';
    document.getElementById('dash').style.display='none';
  }
});"""
new = """// ---- Bascule gate/dash selon l'état de connexion ----
const ADMIN_UID = "QFC18HxRAZabqYD85S5eA7VLC5D3";
auth.onAuthStateChanged(user=>{
  if(user && user.uid === ADMIN_UID){
    document.getElementById('gate').style.display='none';
    document.getElementById('dash').style.display='block';
    loadList();
  } else if(user){
    auth.signOut();
    gateMsg("Ce compte n'a pas les droits administrateur.", false);
  } else {
    document.getElementById('gate').style.display='block';
    document.getElementById('dash').style.display='none';
  }
});"""
c = patch(c, old, new, "admin-gate")

with open("admin.html", "w", encoding="utf-8") as f:
    f.write(c)
print("OK admin.html")
