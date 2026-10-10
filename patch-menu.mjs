import{readFileSync,writeFileSync,copyFileSync,readdirSync}from'node:fs';
const RANK=[
 ['accueil',l=>/href="index\.html"/.test(l)],
 ['profil',l=>/id="drawer-profil"|href="profil\.html"/.test(l)],
 ['admin',l=>/id="drawer-admin"|href="admin\.html"/.test(l)],
 ['real',l=>/index\.html#realisations/.test(l)],
 ['demande',l=>/index\.html#demande/.test(l)],
 ['notif',l=>/notif-sheet/.test(l)],
 ['about',l=>/about-sheet/.test(l)],
 ['lang',l=>/lang-sheet/.test(l)],
 ['login',l=>/id="drawer-login"|href="connexion\.html"/.test(l)],
 ['logout',l=>/id="drawer-logout"/.test(l)],
 ['theme',l=>/theme-toggle-btn|toggleTheme/.test(l)]
];
const re=/(<nav class="d-links">\s*\n)([\s\S]*?)(\n\s*<\/nav>)/;
for(const F of readdirSync('.').filter(f=>f.endsWith('.html'))){
  let s=readFileSync(F,'utf8');const m=s.match(re);
  if(!m){console.log(F+' : menu absent du fichier (genere par script ?), ignore');continue}
  const lines=m[2].split('\n').filter(l=>l.trim());
  const rk=lines.map(l=>RANK.findIndex(r=>r[1](l)));
  if(rk.includes(-1)||new Set(rk).size!==rk.length){console.log(F+' : liens non reconnus ou en double, ignore');continue}
  const sorted=lines.map((l,i)=>[rk[i],l]).sort((a,b)=>a[0]-b[0]).map(x=>x[1]);
  if(sorted.join('\n')===lines.join('\n')){console.log(F+' : deja dans le bon ordre');continue}
  copyFileSync(F,F+'.bak-menu');
  s=s.replace(re,(x,a,b,c)=>a+sorted.join('\n')+c);
  writeFileSync(F,s);console.log(F+' : OK ('+lines.length+' liens reordonnes)');
}
