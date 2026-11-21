(function(){
  var n=0,t=setInterval(function(){
    var s=document.querySelector('#demande .section-title')||document.querySelector('#demande.section-title');
    if(s){
      s.addEventListener('click',function(){
        var w=document.getElementById('wizard')||s;
        w.scrollIntoView({behavior:'smooth',block:'start'});
      });
      clearInterval(t);
    }
    if(++n>100)clearInterval(t);
  },100);
})();
