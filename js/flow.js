(function(){
  var root=document.documentElement,reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
  var ic=function(d){return '<svg viewBox="0 0 24 24" aria-hidden="true">'+d+'</svg>'};
  var I={
    doc:'<path d="M7 3h7l4 4v14H7z"/><path d="M14 3v4h4M9.5 12h5M9.5 16h5"/>',
    send:'<path d="M3 11l18-8-8 18-2-8z"/>',
    scan:'<path d="M4 8V4h4M16 4h4v4M20 16v4h-4M8 20H4v-4M7 12h10"/>',
    shield:'<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/>',
    swap:'<path d="M4 7h11M11 3l4 4-4 4M20 17H9M13 13l-4 4 4 4"/>',
    user:'<circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 4-6 8-6s8 2 8 6"/>',
    file:'<path d="M7 3h7l4 4v14H7z"/><path d="M9 14l2.5 2.5L16 12"/>',
    rupee:'<path d="M7 5h10M7 9h10M7 5c6 0 6 8 0 8l8 6"/>'
  };
  var chip=function(a,b){return '<div class="chip"><span>'+a+'</span><span>'+b+'</span></div>'};
  var rgb=function(h){return [1,3,5].map(function(i){return parseInt(h.substr(i,2),16)})};
  var K={sky:[58,155,220],royal:[33,88,166],aqua:[60,196,214],ind:[96,112,226]};
  var CFG={
    returns:{
      nodes:[
        {t:'Issue invoice',s:'Business \u00B7 Sales',i:'doc',b:chip('INV-1042','\u20B948,500')+'<div class="bars"><i></i><i></i><i></i></div>'},
        {t:'Send documents',s:'Email or WhatsApp to Sancture',i:'send',b:chip('Invoices.pdf','Sent')+chip('Bank.csv','Sent')+chip('Purchases.xlsx','Sent')},
        {t:'Payment received',s:'UPI or bank transfer',i:'rupee',b:chip('Service fee','Paid')+chip('Work','Started')},
        {t:'Scan documents',s:'Read invoice data',i:'scan',b:'<div class="meter"><i></i></div>'+chip('Invoices read','128')},
        {t:'Verify entries',s:'GSTIN, HSN and tax rates',i:'shield',b:chip('GSTIN','Valid')+chip('Tax rates','Match')},
        {t:'Reconcile',s:'GSTR-2B and AIS matching',i:'swap',b:'<div class="meter"><i></i></div>'+chip('Mismatches','Resolved')},
        {t:'Professional review',s:'Checked before filing',i:'user',b:chip('Reviewer sign-off','Approved')},
        {t:'File return',s:'GST Returns \u00B7 Income Tax Returns',i:'file',b:chip('Acknowledgment','Generated')+chip('Tax payable','Summarised')}
      ],
      labels:['Invoices','Documents received','Payment confirmed','Data extracted','Entries verified','Reconciled','Approved return'],
      caps:[.8,1.6,2.6,5.4],night:-1,
      pal:['#091a3d','#0c2c63','#0a4160','#142f73','#232a7a','#0a4b66','#0f3a7d','#0b1a38'],
      blobs:[['sky','royal','sky'],['royal','sky','aqua'],['aqua','sky','royal'],['sky','aqua','ind'],['ind','sky','royal'],['royal','ind','sky'],['sky','royal','ind'],['royal','sky','aqua']]
    },
    assessments:{
      nodes:[
        {t:'Send notice and documents',s:'Notice, order and supporting papers',i:'send',b:chip('Notice.pdf','Received')+chip('Supporting documents','Received')},
        {t:'Prepare reply',s:'Facts, law and evidence',i:'doc',b:'<div class="meter"><i></i></div>'+chip('Reply deadline','Tracked')},
        {t:'Review draft',s:'Senior professional review',i:'user',b:chip('Reviewer sign-off','Approved')+chip('Your approval','Confirmed')},
        {t:'Filing',s:'Reply filed on the portal',i:'file',b:chip('Reply','Filed')+chip('Acknowledgment','Generated')}
      ],
      labels:['Notice and papers','Draft reply','Approved draft'],
      caps:[.8,1.7,2.5],night:-1,
      pal:['#091a3d','#0a4160','#232a7a','#0b1a38'],
      blobs:[['sky','royal','sky'],['aqua','sky','royal'],['ind','sky','royal'],['royal','sky','aqua']]
    }
  };
  var cl=function(v,a,b){return Math.min(Math.max(v,a),b)},ss=function(x){return x*x*(3-2*x)};
  var mix=function(a,b,t){return a.map(function(v,i){return Math.round(v+(b[i]-v)*t)})};

  function Flow(el,key){
    var cfg=CFG[key],N=cfg.nodes,n=N.length,pal=cfg.pal.map(rgb);
    var $=function(s){return el.querySelector(s)},pin=$('.pin'),world=$('.world'),svg=$('svg'),pack=$('.packet'),plabel=pack.querySelector('span'),
        grid=$('.gridbg'),blobs=$('.blobs'),hero=$('.hero-copy'),caps=[].slice.call(el.querySelectorAll('.cap'));
    var nodes=N.map(function(d){
      var e=document.createElement('div');e.className='node';
      e.innerHTML='<div class="nh"><span class="ic">'+ic(I[d.i])+'</span><div><h3>'+d.t+'</h3><p>'+d.s+'</p></div><span class="st" data-s="idle"></span></div><div class="nb">'+d.b+'</div>';
      world.appendChild(e);return e;
    });
    var sts=nodes.map(function(e){return e.querySelector('.st')});
    var api={el:el,layout:function(){},frame:function(){}};
    if(reduce){
      el.classList.add('static');
      sts.forEach(function(s){s.dataset.s='done'});
      nodes.forEach(function(e){e.classList.add('go')});
      return api;
    }
    el.style.height=((n-1)*95+100)+'vh';
    var NS='http://www.w3.org/2000/svg',base=[],prog=[],ports=[],len=[];
    function mk(t,c){var e=document.createElementNS(NS,t);if(c)e.setAttribute('class',c);svg.appendChild(e);return e}
    for(var i=0;i<n-1;i++){base.push(mk('path','base'));prog.push(mk('path','prog'))}
    for(i=0;i<(n-1)*2;i++)ports.push(mk('circle','port'));

    var vw,vh,mob,anchor,cx=[],cyv=[],W=[];
    api.layout=function(){
      if(el.offsetParent===null)return;
      vw=innerWidth;vh=innerHeight;mob=vw<860;
      var nw=mob?230:280,gap=mob?70:120,cy=vh*(mob?.73:.52),
          yo=[0,-60,50,-50,50,-40,40,-30,30].slice(0,n).map(function(v){return v*(mob?.55:1)});
      anchor=vw*(mob?.5:.66);
      var c=anchor,right=0;
      nodes.forEach(function(e,i){
        W[i]=nw;if(i)c+=nw+gap;
        cx[i]=c;e.style.width=nw+'px';e.style.left=(c-nw/2)+'px';
        var hh=e.offsetHeight;cyv[i]=cy+yo[i];e.style.top=(cyv[i]-hh/2)+'px';right=c+nw/2;
      });
      var tot=right+vw;
      world.style.width=tot+'px';svg.setAttribute('width',tot);svg.setAttribute('height',vh);
      for(var i=0;i<n-1;i++){
        var x1=cx[i]+W[i]/2,y1=cyv[i],x2=cx[i+1]-W[i+1]/2,y2=cyv[i+1],dx=(x2-x1)*.5,
            d='M'+x1+' '+y1+' C'+(x1+dx)+' '+y1+' '+(x2-dx)+' '+y2+' '+x2+' '+y2;
        base[i].setAttribute('d',d);prog[i].setAttribute('d',d);
        len[i]=prog[i].getTotalLength();prog[i].style.strokeDasharray=len[i];
        [[ports[i*2],x1,y1],[ports[i*2+1],x2,y2]].forEach(function(p){p[0].setAttribute('cx',p[1]);p[0].setAttribute('cy',p[2]);p[0].setAttribute('r',5)});
      }
    };
    var h=0,lastSeg=-1,lastCap=-2,lastNight=null;
    api.frame=function(){
      if(el.offsetParent===null||!len.length)return;
      var r=el.getBoundingClientRect();
      if(r.bottom<-50||r.top>vh+50)return;
      var p=cl(-r.top/(r.height-vh),0,1),target=p*(n-1);
      h+=(target-h)*.14;if(Math.abs(target-h)<.0005)h=target;
      var seg=cl(Math.floor(h),0,n-2),f=cl(h-seg,0,1),e=ss(f);
      var pt=prog[seg].getPointAtLength(len[seg]*e);
      pack.style.transform='translate3d('+pt.x+'px,'+pt.y+'px,0)';
      pack.style.opacity=h>.04&&h<n-1.02?1:0;
      plabel.style.opacity=ss(cl((f-.12)/.2,0,1))*ss(cl((.88-f)/.2,0,1));
      if(seg!==lastSeg){plabel.textContent=cfg.labels[seg];lastSeg=seg}
      var headX=cx[seg]+(cx[seg+1]-cx[seg])*e,pan=Math.max(0,headX-anchor);
      world.style.transform='translate3d('+(-pan)+'px,0,0)';
      grid.style.backgroundPosition=(-pan)+'px 0';
      blobs.style.transform='translate3d('+(-pan*.3)+'px,0,0)';
      // background changes with every step
      var bg=mix(pal[seg],pal[seg+1],e);
      pin.style.backgroundColor='rgb('+bg.join(',')+')';
      for(var k=0;k<3;k++)pin.style.setProperty('--b'+(k+1),mix(K[cfg.blobs[seg][k]],K[cfg.blobs[seg+1][k]],e).join(','));
      nodes.forEach(function(nd,i){
        var rv=i?ss(cl(h-i+1.4,0,1)):1,st=h>i+.5?'done':(h>i-.15?'run':'idle');
        nd.style.opacity=rv;nd.style.transform='translateY('+((1-rv)*30)+'px) scale('+(.95+.05*rv)+')';
        if(sts[i].dataset.s!==st){sts[i].dataset.s=st;nd.classList.toggle('go',st!=='idle')}
      });
      for(var i=0;i<prog.length;i++)prog[i].style.strokeDashoffset=len[i]*(1-cl(h-i,0,1));
      var ho=1-cl((h-.15)/.55,0,1);
      hero.style.opacity=ho;hero.style.transform=(mob?'':'translateY(-50%) ')+'translateX('+(-40*(1-ho))+'px)';
      hero.style.pointerEvents=ho>.5?'auto':'none';
      var ci=-1;cfg.caps.forEach(function(t,k){if(h>=t)ci=k});
      if(ci!==lastCap){caps.forEach(function(c,k){c.classList.toggle('on',k===ci)});lastCap=ci}
      var night=h>cfg.night;if(night!==lastNight){pin.classList.toggle('night',night);lastNight=night}
    };
    return api;
  }

  var flows={returns:Flow(document.getElementById('flow-returns'),'returns'),assessments:Flow(document.getElementById('flow-assessments'),'assessments')};
  var cur=null;
  function activate(m){
    var first=cur===null;cur=m;root.setAttribute('data-mode',m);
    [].forEach.call(document.querySelectorAll('.mode button'),function(b){b.setAttribute('aria-pressed',b.dataset.mode===m)});
    var f=flows[m];f.layout();
    scrollTo({top:f.el.getBoundingClientRect().top+scrollY,behavior:first&&!reduce?'smooth':'auto'});
  }
  [].forEach.call(document.querySelectorAll('[data-mode]'),function(b){b.addEventListener('click',function(){activate(b.dataset.mode)})});
  addEventListener('resize',function(){if(cur)flows[cur].layout()});
  if(document.fonts&&document.fonts.ready)document.fonts.ready.then(function(){if(cur)flows[cur].layout()});
  (function loop(){requestAnimationFrame(loop);if(cur&&!document.hidden)flows[cur].frame()})();
  var hm=location.hash.slice(1);if(flows[hm])activate(hm);
})();
