(function(){
  var n=0,t=setInterval(function(){
    var b=document.querySelector('.pc-partners'),
        s=document.querySelector('.section-title');
    if(b&&s){
      if(b.compareDocumentPosition(s)&Node.DOCUMENT_POSITION_FOLLOWING){
        b.parentNode.insertBefore(s,b);
      }
      clearInterval(t);
    }
    if(++n>100)clearInterval(t);
  },100);
})();
