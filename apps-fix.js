(function(){
  var n=0,t=setInterval(function(){
    var box=document.querySelector('.apps-grid-box');
    if(box){
      clearInterval(t);
      var host=box.parentNode;
      [].slice.call(document.querySelectorAll('[id^="card-"], .card.pcinfo-self')).forEach(function(c){
        var el=c;
        while(el.parentNode && el.parentNode!==host && el.parentNode!==document.body){ el=el.parentNode; }
        if(el!==box && !el.contains(box)) el.style.setProperty('display','none','important');
      });
    }
    if(++n>150)clearInterval(t);
  },100);
})();
