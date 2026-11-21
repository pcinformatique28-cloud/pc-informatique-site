(function(){
  function norm(s){return (s||'').toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g,'').replace(/[^a-z0-9]/g,'');}
  var ORDER=['gsc','neoferme','aneg','lework','mage','ambi','malaga','lav','troc','bijou','pc','gfc'];
  var KEYS=[['gsc',['gabonsport','sportconnect','gsc']],['gfc',['football','gfc']],['neoferme',['neoferme']],['aneg',['aneg']],['lework',['work']],['mage',['mage']],['ambi',['ambi']],['malaga',['malaga']],['lav',['lav']],['troc',['troc']],['bijou',['bijou']],['pc',['pcinfo']]];
  var SEL={gsc:'#card-gsc, .card.gsc',gfc:'#card-gfc, .card.gfc',pc:'.card.pcinfo-self',neoferme:'#card-neoferme',aneg:'#card-aneg',lework:'#card-lework',mage:'#card-mage',ambi:'#card-ambi',malaga:'#card-malaga',lav:'#card-lav',troc:'#card-troc',bijou:'#card-bijou'};
  function nameOf(it){var im=it.querySelector('img'),sp=it.querySelector('.pn');return (sp&&sp.textContent)||(im&&(im.alt||im.title))||it.getAttribute('title')||'';}
  function hay(it){var im=it.querySelector('img'),s=nameOf(it);if(im&&im.src&&im.src.indexOf('data:')!==0)s+=' '+im.src.split('/').pop();return norm(s);}
  function keyOf(it,idx){
    var h=hay(it),i,j;
    for(i=0;i<KEYS.length;i++){for(j=0;j<KEYS[i][1].length;j++){if(h.indexOf(KEYS[i][1][j])>-1)return KEYS[i][0];}}
    return ORDER[idx]||null;
  }
  function collect(w){
    var half=w.querySelector('.pcp-half')||w,seen={},out=[];
    [].slice.call(half.querySelectorAll('.pcp-i')).forEach(function(it,i){
      var im=it.querySelector('img'),k=norm(nameOf(it))||(im&&im.src)||('i'+i);
      if(!seen[k]){seen[k]=1;out.push(it);}
    });
    return out;
  }
  function headOf(c){return c.querySelector('.card-head h3')||c.querySelector('h3');}
  function bodyOf(c){return c.querySelector('.card-details')||c.querySelector('.card-body')||c;}
  function pcBody(card,nm,tileImg,key){
    if(key!=='pc')return bodyOf(card).cloneNode(true);
    var d=document.createElement('div'),s=document.createElement('div'),c=document.createElement('div'),p=document.createElement('p'),a=document.createElement('a');
    d.className='card-details';s.className='shot';c.className='card-body';
    if(tileImg){var i=document.createElement('img');i.src=tileImg.src;i.alt=nm;s.appendChild(i);}
    p.textContent='PC-INFORMATIQUE, startup technologique gabonaise : cr\u00e9atrice et propri\u00e9taire des applications pr\u00e9sent\u00e9es ici. Nous concevons des applications web et mobiles pour les entreprises et les particuliers au Gabon.';
    a.className='visit-btn';a.href='mailto:pcinformatique28@gmail.com';a.textContent='Nous contacter';
    c.appendChild(p);c.appendChild(a);d.appendChild(s);d.appendChild(c);return d;
  }
  function openSheet(card,nm,tileImg,key){
    var old=document.getElementById('apps-sheet');if(old)old.remove();
    var h=headOf(card),o=document.createElement('div'),b=document.createElement('div'),x=document.createElement('button'),t=document.createElement('h3');
    o.id='apps-sheet';o.className='apps-sheet';b.className='apps-sheet-box';
    x.type='button';x.className='apps-sheet-x';x.textContent='\u00d7';
    t.textContent=(h?h.textContent:nm)||nm;
    b.appendChild(x);b.appendChild(t);b.appendChild(pcBody(card,nm,tileImg,key));
    o.appendChild(b);document.body.appendChild(o);
    function close(){o.remove();}
    x.onclick=close;o.addEventListener('click',function(e){if(e.target===o)close();});
  }
  function build(w,uniq){
    var box=document.createElement('div'),g=document.createElement('div');
    box.className='apps-grid-box';g.className='apps-grid';
    uniq.forEach(function(it,idx){
      var nm=nameOf(it),key=keyOf(it,idx),b=document.createElement('button'),im=it.querySelector('img');
      b.type='button';b.className='apps-tile';b.setAttribute('aria-label',nm);
      if(im){var c=document.createElement('img');c.src=im.src;c.alt=nm;b.appendChild(c);}else{b.textContent=nm;}
      b.addEventListener('click',function(){
        var card=key&&SEL[key]?document.querySelector(SEL[key]):null;
        if(card)openSheet(card,nm,im,key);
      });
      g.appendChild(b);
    });
    box.appendChild(g);
    w.parentNode.insertBefore(box,w);
    document.body.classList.add('apps-grid-on');document.documentElement.classList.remove('apps-pre');
    setTimeout(function(){
      if(box.offsetHeight<20){document.body.classList.remove('apps-grid-on');box.remove();}
    },700);
  }
  var tries=0,t=setInterval(function(){
    tries++;
    try{
      var w=document.querySelector('.pc-partners');
      if(w){var u=collect(w);if(u.length>=12||(tries>60&&u.length)){clearInterval(t);build(w,u);}}
    }catch(e){clearInterval(t);}
    if(tries>150)clearInterval(t);
  },100);
})();
