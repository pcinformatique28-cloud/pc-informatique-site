(function(){
  function norm(s){return (s||'').toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g,'').replace(/[^a-z0-9]/g,'');}
  function nameOf(it){
    var im=it.querySelector('img'), sp=it.querySelector('.pn');
    return (sp&&sp.textContent)||(im&&(im.alt||im.title))||it.getAttribute('title')||'';
  }
  function collect(w){
    var half=w.querySelector('.pcp-half')||w, seen={}, out=[];
    [].slice.call(half.querySelectorAll('.pcp-i')).forEach(function(it,i){
      var im=it.querySelector('img');
      var k=norm(nameOf(it))||(im&&im.src)||('i'+i);
      if(!seen[k]){seen[k]=1;out.push(it);}
    });
    return out;
  }
  function findCard(nm){
    var n=norm(nm); if(!n) return null;
    var cards=[].slice.call(document.querySelectorAll('[id^="card-"], .card.pcinfo-self'));
    var heads=cards.map(function(c){var h=c.querySelector('h3');return norm(h?h.textContent:'');});
    var i=heads.indexOf(n);
    if(i<0){for(i=0;i<heads.length;i++){if(heads[i]&&(heads[i].indexOf(n)>-1||n.indexOf(heads[i])>-1))break;}if(i>=heads.length)i=-1;}
    return i>-1?cards[i]:null;
  }
  function openSheet(card,nm){
    var old=document.getElementById('apps-sheet'); if(old) old.remove();
    var h=card.querySelector('h3');
    var body=card.querySelector('.card-details')||card.querySelector('.card-body')||card;
    var o=document.createElement('div'); o.id='apps-sheet'; o.className='apps-sheet';
    var b=document.createElement('div'); b.className='apps-sheet-box';
    var x=document.createElement('button'); x.type='button'; x.className='apps-sheet-x'; x.textContent='\u00d7';
    var t=document.createElement('h3'); t.textContent=h?h.textContent:nm;
    b.appendChild(x); b.appendChild(t); b.appendChild(body.cloneNode(true));
    o.appendChild(b); document.body.appendChild(o);
    function close(){o.remove();}
    x.onclick=close;
    o.addEventListener('click',function(e){if(e.target===o)close();});
  }
  function build(w,uniq){
    var box=document.createElement('div'); box.className='apps-grid-box';
    var g=document.createElement('div'); g.className='apps-grid';
    uniq.forEach(function(it){
      var nm=nameOf(it), b=document.createElement('button');
      b.type='button'; b.className='apps-tile'; b.setAttribute('aria-label',nm);
      var im=it.querySelector('img');
      if(im){var c=document.createElement('img'); c.src=im.src; c.alt=nm; b.appendChild(c);} else {b.textContent=nm;}
      b.addEventListener('click',function(){var card=findCard(nm); if(card) openSheet(card,nm);});
      g.appendChild(b);
    });
    box.appendChild(g);
    w.parentNode.insertBefore(box,w);
    document.body.classList.add('apps-grid-on');
  }
  var tries=0,t=setInterval(function(){
    tries++;
    var w=document.querySelector('.pc-partners');
    if(w){
      var u=collect(w);
      if(u.length>=12||(tries>60&&u.length)){clearInterval(t);build(w,u);}
    }
    if(tries>150)clearInterval(t);
  },100);
})();
