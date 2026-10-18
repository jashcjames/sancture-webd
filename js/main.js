(function(){
  var $=function(s,c){return (c||document).querySelector(s)},$$=function(s,c){return [].slice.call((c||document).querySelectorAll(s))};
  var reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;

  // nav
  var nav=$('.nav'),bar=$('.progress'),links=$('.links'),burger=$('.burger');
  function onScroll(){
    nav.classList.toggle('solid',scrollY>30);
    var h=document.documentElement.scrollHeight-innerHeight;
    if(bar)bar.style.transform='scaleX('+(h>0?scrollY/h:0)+')';
  }
  addEventListener('scroll',onScroll,{passive:true});onScroll();
  if(burger)burger.addEventListener('click',function(){
    var o=links.classList.toggle('open');burger.setAttribute('aria-expanded',o);
  });
  $$('.links a').forEach(function(a){a.addEventListener('click',function(){links.classList.remove('open')})});

  // hero parallax
  var hero=$('.hero');
  if(hero&&!reduce&&matchMedia('(pointer:fine)').matches)hero.addEventListener('pointermove',function(e){
    var r=hero.getBoundingClientRect();
    hero.style.setProperty('--mx',((e.clientX-r.left)/r.width-.5).toFixed(3));
    hero.style.setProperty('--my',((e.clientY-r.top)/r.height-.5).toFixed(3));
  });

  // reveal
  var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{threshold:.15});
  $$('.rv').forEach(function(el){io.observe(el)});

  // counters
  function count(el){
    var to=parseFloat(el.dataset.to),suf=el.dataset.suf||'',pre=el.dataset.pre||'',t0=null;
    if(reduce){el.textContent=pre+to+suf;return}
    (function step(t){
      if(!t0)t0=t;var p=Math.min((t-t0)/1800,1),e=1-Math.pow(1-p,3);
      el.textContent=pre+Math.round(to*e)+suf;
      if(p<1)requestAnimationFrame(step);
    })(performance.now());
  }
  var co=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){count(e.target);co.unobserve(e.target)}})},{threshold:.6});
  $$('[data-to]').forEach(function(el){co.observe(el)});

  // pricing
  var box=$('#plans');
  if(box){
    var P=function(n,p,d,f,o){o=o||{};o.n=n;o.p=p;o.d=d;o.f=f;return o};
    var data={
      gst:{note:'GST compliance plans.',bill:true,plans:[
        P('Nil Return',349,'For months with no sales or purchases',['Nil GSTR-1 and GSTR-3B filing','Filing reminders every month','Email and WhatsApp support','Acknowledgment shared on filing'],{m:1}),
        P('Starter',999,'For small traders and service providers',['GSTR-1 and GSTR-3B filing','Up to 25 sales invoices a month','Email and WhatsApp support','Monthly filing reminders'],{m:1}),
        P('Growth',1999,'For growing businesses with regular sales',['Everything in Starter','Up to 200 sales invoices a month','GSTR-2B reconciliation and ITC review','Quarterly compliance health report','Free GST Registration with a two-month plan'],{m:1,pop:1}),
        P('Elite',3499,'For high-volume businesses',['Everything in Growth','Up to 350 sales invoices a month','Priority support and turnaround','Monthly review call'],{m:1}),
        P('Annual Return',3999,'Yearly GST annual return',['GSTR-9 annual return filing','Books-to-portal reconciliation','Mismatch and liability review','Acknowledgment on filing'],{u:'/ annual return'}),
        P('Book Keeping',0,'Accounts maintained for you',['Monthly bookkeeping and ledgers','Bank and invoice entries','Financial statements on request','Priced on transaction volume']),
        P('Enterprise',0,'For multiple GSTINs and large teams',['Multiple GSTINs and entities','Very high invoice volumes','Dedicated team and service levels','Custom scope and reporting'])]},
      it:{note:'One-time fee per return.',bill:false,plans:[
        P('Salaried',999,'For salaried individuals and pensioners',['Form 16 and AIS/26AS matching','Old vs new regime comparison','Deductions and HRA review','E-verification support'],{u:'/ return'}),
        P('Business and Professional',2999,'For proprietors, freelancers and professionals',['Presumptive or books-based filing','Profit and loss with balance sheet','Advance tax computation','Expense and deduction planning'],{u:'/ return',pop:1}),
        P('Capital Gains and NRI',4999,'For investors, property sellers and NRIs',['Shares, mutual funds and property gains','Foreign income and DTAA review','Schedule FA guidance','Priority turnaround'],{u:'/ return'})]},
      lit:{note:'Fees depend on the notice and the amount in dispute.',bill:false,plans:[
        P('Notice Reply',3999,'For a single GST or Income Tax notice',['Notice review and strategy call','Drafted reply with supporting documents','Online submission on the portal','One follow-up response'],{u:'onwards'}),
        P('Appeal and Hearing',15000,'For orders, appeals and personal hearings',['Appeal drafting and filing','Representation before the authority','Case law and statutory research','Status updates at every stage'],{u:'onwards',pop:1}),
        P('Litigation Retainer',0,'For businesses with ongoing disputes',['Multiple notices and proceedings','Assessment and audit support','Priority access to a senior consultant','Custom quote based on scope'])]}
    };
    var cur='gst',annual=false;
    var fmt=function(n){return '\u20B9'+n.toLocaleString('en-IN')};
    function render(){
      var d=data[cur];
      $('#note').textContent=d.note;$('#bill').hidden=!d.bill;
      box.innerHTML=d.plans.map(function(p){
        var price,unit='',ct=!p.p,yr=d.bill&&annual&&p.m;
        if(ct)price='Contact for pricing';
        else if(yr){price=fmt(p.p*11);unit='/ year'}
        else{price=fmt(p.p);unit=p.u||(p.m?'/ month':'')}
        return '<article class="plan'+(p.pop?' pop':'')+'">'+(p.pop?'<span class="badge">Most chosen</span>':'')+
          '<h3>'+p.n+'</h3><p class="fine">'+p.d+'</p><div class="price'+(ct?' ct':'')+'">'+price+' <small>'+unit+'</small></div>'+
          (yr?'<p class="fine">One month free, billed yearly</p>':'<p class="fine">&nbsp;</p>')+
          '<ul>'+p.f.map(function(x){return '<li>'+x+'</li>'}).join('')+'</ul>'+
          '<a class="btn'+(p.pop?' light':'')+'" href="contact.html?plan='+encodeURIComponent(p.n)+'">'+(ct?'Contact us':'Get started')+'</a></article>';
      }).join('');
    }
    $$('.tabs button').forEach(function(b){b.addEventListener('click',function(){
      cur=b.dataset.t;$$('.tabs button').forEach(function(x){x.setAttribute('aria-selected',x===b)});render();
    })});
    $('.sw').addEventListener('click',function(e){annual=!annual;e.currentTarget.setAttribute('aria-checked',annual);render()});
    render();
  }

  // blog filter
  $$('.filters button').forEach(function(b){b.addEventListener('click',function(){
    $$('.filters button').forEach(function(x){x.setAttribute('aria-pressed',x===b)});
    $$('.post').forEach(function(p){p.hidden=!(b.dataset.c==='all'||p.dataset.c===b.dataset.c)});
  })});

  // contact
  var f=$('#enquiry');
  if(f){
    var q=new URLSearchParams(location.search).get('plan');
    if(q){var s=$('#topic');for(var i=0;i<s.options.length;i++)if(s.options[i].text===q)s.selectedIndex=i;$('#msg').value='I am interested in the '+q+' plan.'}
    f.addEventListener('submit',function(e){
      e.preventDefault();
      var btn=f.querySelector('button');btn.disabled=true;btn.textContent='Sending...';
      fetch(f.action,{method:'POST',body:new FormData(f),headers:{Accept:'application/json'}}).then(function(r){
        if(!r.ok)throw 0;f.innerHTML='<p class="ok">Thank you. We have received your enquiry and will reply within one business day.</p>';
      }).catch(function(){btn.disabled=false;btn.textContent='Send enquiry';
        f.insertAdjacentHTML('beforeend','<p class="fine">We could not send your message. Please email us or call directly.</p>')});
    });
  }
})();
