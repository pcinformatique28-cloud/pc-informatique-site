(function(){
  function norm(s){return (s||'').toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g,'').replace(/[^a-z0-9]/g,'');}
  function nameOf(it){var im=it.querySelector('img'),sp=it.querySelector('.pn');return (sp&&sp.textContent)||(im&&(im.alt||im.title))||it.getAttribute('title')||'';}
  function collect(w){
    var half=w.querySelector('.pcp-half')||w,seen={},out=[];
    [].slice.call(half.querySelectorAll('.pcp-i')).forEach(function(it,i){
      var im=it.querySelector('img'),k=norm(nameOf(it))||(im&&im.src)||('i'+i);
      if(!seen[k]){seen[k]=1;out.push(it);}
    });
    return out;
  }
  function headOf(c){return c.querySelector(':scope > .card-head h3')||c.querySelector(':scope > h3')||c.querySelector('h3');}
  function bodyOf(c){return c.querySelector(':scope > .card-body')||c.querySelector(':scope > .card-details')||c.querySelector('.card-body')||c;}
  function findCard(nm){
    var n=norm(nm);if(!n)return null;
    if(n.indexOf('gabonsport')>-1){var g=document.querySelector('.card.gsc, #card-gsc');if(g)return g;}
    var list=[].slice.call(document.querySelectorAll('.card')),i,h;
    for(i=0;i<list.length;i++){h=headOf(list[i]);if(h&&norm(h.textContent)===n)return list[i];}
    for(i=0;i<list.length;i++){h=headOf(list[i]);if(h){var hn=norm(h.textContent);if(hn&&(hn.indexOf(n)>-1||n.indexOf(hn)>-1))return list[i];}}
    return null;
  }
  function openSheet(card,nm){
    var old=document.getElementById('apps-sheet');if(old)old.remove();
    var h=headOf(card),o=document.createElement('div'),b=document.createElement('div'),x=document.createElement('button'),t=document.createElement('h3');
    o.id='apps-sheet';o.className='apps-sheet';b.className='apps-sheet-box';
    x.type='button';x.className='apps-sheet-x';x.textContent='\u00d7';
    t.textContent=nm||(h?h.textContent:'');
    b.appendChild(x);b.appendChild(t);b.appendChild(bodyOf(card).cloneNode(true));
    o.appendChild(b);document.body.appendChild(o);
    function close(){o.remove();}
    x.onclick=close;o.addEventListener('click',function(e){if(e.target===o)close();});
  }
  function build(w,uniq){
    var box=document.createElement('div'),g=document.createElement('div');
    box.className='apps-grid-box';g.className='apps-grid';
    uniq.forEach(function(it){
      var nm=nameOf(it),b=document.createElement('button'),im=it.querySelector('img');
      b.type='button';b.className='apps-tile';b.setAttribute('aria-label',nm);
      if(im){var c=document.createElement('img');c.src=im.src;c.alt=nm;b.appendChild(c);}else{b.textContent=nm;}
      b.addEventListener('click',function(){var card=findCard(nm);if(card)openSheet(card,nm);});
      g.appendChild(b);
    });
    box.appendChild(g);
    w.parentNode.insertBefore(box,w);
    document.body.classList.add('apps-grid-on');
    setTimeout(function(){
      if(document.documentElement.scrollHeight<1200){
        document.body.classList.remove('apps-grid-on');box.remove();
      }
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
