D="https://www.sancture.in"  # replace with your custom domain
EMAIL="hello@sancture.in"; PHONE="+91 00000 00000"; WA="910000000000"
NAV=[("index.html","Home"),("services.html","Services"),("pricing.html","Pricing"),("blogs.html","Blogs"),("contact.html","Contact us")]
def head(page,title,desc,extra=""):
    nav="".join('<li><a href="%s"%s>%s</a></li>'%(h,' aria-current="page"' if h==page else '',t) for h,t in NAV[:-1])
    return f'''<!DOCTYPE html>
<html lang="en-IN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{D}/{'' if page=='index.html' else page}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:type" content="website"><meta property="og:url" content="{D}/{page}">
<meta name="theme-color" content="#0E2246"><script>document.documentElement.className+=" js"</script>
<link rel="icon" href="assets/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,650;12..96,700&family=Instrument+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css"><link rel="stylesheet" href="css/theme.css">{extra}
</head><body>
<a class="skip" href="#main">Skip to content</a><div class="progress" aria-hidden="true"></div>
<header class="nav"><div class="wrap"><a class="brand" href="index.html" aria-label="Sancture home"><img src="assets/logo.png" alt="" width="40" height="40">Sancture</a>
<button class="burger" aria-label="Menu" aria-expanded="false"><span></span><span></span><span></span></button>
<ul class="links">{nav}<li><a class="btn" href="contact.html">Book a consultation</a></li></ul></div></header>
<main id="main">'''
FOOT=f'''</main>
<footer><div class="wrap"><div class="cols">
<div><a class="brand" href="index.html"><img src="assets/logo.png" alt="" width="40" height="40">Sancture</a><p>GST and income tax return filing, notices and litigation support for businesses and individuals across India.</p></div>
<div><h3>Services</h3><a href="services.html#gst-registration">GST Registration</a><a href="services.html#gst-returns">GST return filing</a><a href="services.html#itr">Income tax return filing</a><a href="services.html#gst-litigation">GST litigation</a><a href="services.html#it-litigation">Income tax litigation</a></div>
<div><h3>Company</h3><a href="pricing.html">Pricing</a><a href="blogs.html">Blogs</a><a href="contact.html">Contact us</a></div>
<div><h3>Reach us</h3><a href="mailto:{EMAIL}">{EMAIL}</a><a href="tel:{PHONE.replace(' ','')}">{PHONE}</a></div>
</div><small>&copy; 2026 Sancture. All rights reserved. Information on this site is general and not a substitute for professional advice on your specific case.</small></div></footer>
<a class="wa" href="https://wa.me/{WA}" rel="noopener">Chat on WhatsApp</a>
<script src="js/main.js"></script>
'''
import re
def cap(h):
    def t(s):
        s=re.sub(r'\b[Ii]ncome [Tt]ax\b','Income Tax',s)
        s=re.sub(r'\b(GST|Income Tax|[Tt]ax) (return)(s?)\b',lambda k:('Tax' if k.group(1).lower()=='tax' else k.group(1))+' Return'+k.group(3),s)
        s=s.replace('Return filing','Return Filing')
        return re.sub(r'\b[Ll]itigation\b','Litigation',s)
    h=re.sub(r'>([^<]+)<',lambda m:'>'+t(m.group(1))+'<',h)
    return re.sub(r'content="([^"]*)"',lambda m:'content="'+t(m.group(1))+'"',h)
def w(n,s):
    if n.endswith('.html'): s=cap(s)
    open(n,"w",encoding="utf-8").write(s)

# ---------- HOME ----------
P_FILE='<path d="M7 3h7l4 4v14H7z"/><path d="M9 14l2.5 2.5L16 12"/>'
P_SHIELD='<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/>'
def svg(p): return '<svg viewBox="0 0 24 24" aria-hidden="true">'+p+'</svg>'
def cp(h,p,extra=''): return '<div class="cap"><h2>%s</h2><p>%s</p>%s</div>'%(h,p,extra)
def flowhtml(key,title,span,lead,ctas,chips,caps):
    pr='true' if key=='returns' else 'false'; pa='false' if key=='returns' else 'true'
    return ('<section class="flow" id="flow-%s" aria-label="%s"><div class="pin night">'
    '<div class="blobs" aria-hidden="true"></div><div class="gridbg" aria-hidden="true"></div>'
    '<div class="mode" role="group" aria-label="Choose a service"><button data-mode="returns" aria-pressed="%s">Tax Returns</button><button data-mode="assessments" aria-pressed="%s">Tax Assessments</button></div>'
    '<div class="world" aria-hidden="true"><svg></svg><div class="packet"><span></span></div></div>'
    '<div class="hero-copy"><h2 class="t">%s <span>%s</span></h2><p class="kicker">GST AND INCOME TAX</p><p>%s</p><div class="cta">%s</div><ul class="chips">%s</ul></div>%s</div></section>')%(key,title,pr,pa,title,span,lead,ctas,chips,caps)
ld='''<script type="application/ld+json">{"@context":"https://schema.org","@type":"ProfessionalService","name":"Sancture","url":"%s","logo":"%s/assets/logo.png","description":"GST and Income Tax return filing, assessments, notices, appeals and Litigation support.","areaServed":"IN","serviceType":["GST Registration","GST Return Filing","Income Tax Return Filing","GST Litigation","Income Tax Litigation"]}</script>'''%(D,D)
home=head("index.html","Sancture | Filed Right. Defended Well. GST & Income Tax Returns, Assessments and Litigation","Sancture files GST and Income Tax Returns and handles assessments, notices, appeals and Litigation. Transparent pricing, on-time filing and expert representation for businesses and individuals in India.",ld)
# hero
home+='''<section class="hero" id="top"><div class="aurora" aria-hidden="true"></div><div class="hgrid" aria-hidden="true"></div>
<div class="wrap hero-in"><div class="hero-text">
<a class="pill" href="pricing.html"><i></i>Free GST Registration with a two-month Growth plan</a>
<h1>Filed right.<br><span class="grad">Defended well.</span></h1>
<p class="kicker">GST AND INCOME TAX</p>
<p class="sub">Sancture files your GST and Income Tax Returns and stands with you in Assessments, notices and Litigation. One expert team, fixed and published pricing.</p>
<div class="cta"><a class="btn" href="#choose">Explore our services</a><a class="btn ghost" href="contact.html">Book a consultation</a></div>
<ul class="mini"><li><b>3+</b>Years of experience</li><li><b>250+</b>Clients served</li><li><b>&#8377;375Cr+</b>Supplies processed</li></ul></div>
<div class="hero-vis" aria-hidden="true"><div class="orbit o1"><i></i></div><div class="orbit o2"><i></i><i></i></div>
<div class="core"><img src="assets/logo.png" alt=""></div>
<div class="fc fc1"><span class="ck"></span><div><b>GSTR-3B filed</b><small>Acknowledgment generated</small></div></div>
<div class="fc fc2"><span class="rg"></span><div><b>Notice reply</b><small>Draft approved</small></div></div>
<div class="fc fc3"><small>Monthly turnover (sample)</small><div class="bars2"><i></i><i></i><i></i><i></i><i></i><i></i><i></i></div></div>
<div class="fc fc4"><span class="ck"></span><div><b>ITR e-verified</b><small>Refund summary ready</small></div></div></div></div>
<span class="scrollcue" aria-hidden="true"></span></section>
<div class="marq-wrap" aria-hidden="true"><div class="marq"><div class="track">'''
items=['GST Registration','GST Returns','Income Tax Returns','Tax Assessments','Notice Replies','Appeals','Litigation']
home+=''.join('<span>%s</span>'%i for i in items*2)+'</div></div></div>'
# chooser
home+='<section class="choose" id="choose"><div class="wrap"><h2>What are you looking for?</h2><p class="lead">Sancture files GST and Income Tax Returns and represents you in Tax Assessments, notices and Litigation. Pick one to see how we work.</p><div class="picks">'
home+='<button class="pick pick-a" data-mode="returns"><span class="pk-ic">'+svg(P_FILE)+'</span><h3>Tax Returns</h3><p>GST and Income Tax Returns filed accurately and on time.</p><span class="pk-go">See how Returns work<i class="arr"></i></span></button>'
home+='<button class="pick pick-b" data-mode="assessments"><span class="pk-ic">'+svg(P_SHIELD)+'</span><h3>Tax Assessments</h3><p>Notices, assessments, appeals and Litigation handled for you.</p><span class="pk-go">See how Assessments work<i class="arr"></i></span></button></div></div></section>'
home+=flowhtml('returns','Tax Returns and Compliance','filed right with ease.','Sancture files your GST and Income Tax Returns and defends you when a notice arrives. Send your documents once and we handle the filing, reconciliation and representation.',
 '<a class="btn" href="contact.html">Get a free consultation</a><a class="btn ghost" href="pricing.html">See pricing</a>',
 '<li>GST Returns</li><li>Income Tax Returns</li><li>Notice Replies</li><li>Litigation</li>',
 cp('You issue the invoices. We take over the compliance.','Share sales invoices, purchase bills and bank statements by email or WhatsApp. Our team confirms receipt the same day and tells you exactly what is missing.')
 +cp('Fixed fees, paid upfront.','Every plan is published. Pay by UPI or bank transfer and we start work on your documents straight away.','<div class="cta"><a class="btn" href="pricing.html">View pricing</a></div>')
 +cp('Every document is checked before it reaches a return.','Four services, one workflow, handled by qualified professionals.','<ul class="chips"><li>GST Returns</li><li>Income Tax Returns</li></ul><div class="cta"><a class="btn" href="services.html">Explore services</a></div>')
 +cp('Filed on time. Acknowledged in writing.','A reviewer signs off on every return before it is filed. You receive the acknowledgment with a plain summary of the tax payable or the refund due.'))
home+=flowhtml('assessments','Tax Assessments and Notices','handled with confidence.','Sancture prepares replies, represents you before the authorities and manages appeals in GST and Income Tax Assessments and Litigation. Share the notice and we plan the response.',
 '<a class="btn" href="contact.html">Talk to an expert</a><a class="btn ghost" href="pricing.html">See pricing</a>',
 '<li>GST Assessments</li><li>Income Tax Assessments</li><li>Appeals</li><li>Litigation</li>',
 cp('Share the notice and your documents.','Send the notice or order along with whatever supporting papers you have. We note the reply deadline the same day and tell you what else is needed.')
 +cp('Reply drafted, then reviewed.','We prepare a reply covering the facts, the law and the evidence. A senior professional reviews the draft before it reaches you for approval.')
 +cp('Filed on time, with representation.','We file the reply, attend hearings where required and keep you updated at every stage.','<div class="cta"><a class="btn light" href="contact.html">Talk to an expert</a></div>'))
# pricing orbs
home+='''
<section class="sec s-vivid curve"><div class="wrap">
<div class="head center rv"><h2>Simple pricing, published upfront</h2><p>Plans for every stage, from Nil Returns to full Litigation support.</p></div>
<div class="orbs rv">
<a class="orb o-a" href="pricing.html"><small>GST Returns</small><b>&#8377;349</b><span>per month, from</span></a>
<a class="orb o-b" href="pricing.html"><small>Income Tax Returns</small><b>&#8377;999</b><span>per return, from</span></a>
<a class="orb o-c" href="pricing.html"><small>Litigation</small><b>&#8377;3,999</b><span>notice replies, from</span></a>
<a class="orb o-d" href="pricing.html"><small>GST Registration</small><b>Free</b><span>with a two-month Growth plan</span></a></div>
<p class="plink"><a class="btn light" href="pricing.html">Compare all plans</a></p></div></section>
<section class="sec s-ink curve" style="overflow:hidden"><div class="stars" aria-hidden="true"></div><div class="wrap">
<div class="head center rv"><h2>Trusted by clients</h2><p>Our clients range from first-time filers to growing GST-registered businesses.</p></div>
<div class="gauges rv"><svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs><linearGradient id="gg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#7cc0f2"/><stop offset="1" stop-color="#2fd0e0"/></linearGradient></defs></svg>
<div class="gauge"><svg viewBox="0 0 120 120"><circle class="gtrack" cx="60" cy="60" r="52"/><circle class="gfill" cx="60" cy="60" r="52" pathLength="100"/></svg><div class="gnum"><strong data-to="3" data-suf="+">3+</strong></div><span>Years of experience</span></div>
<div class="gauge"><svg viewBox="0 0 120 120"><circle class="gtrack" cx="60" cy="60" r="52"/><circle class="gfill" cx="60" cy="60" r="52" pathLength="100"/></svg><div class="gnum"><strong data-to="250" data-suf="+">250+</strong></div><span>Clients served</span></div>
<div class="gauge"><svg viewBox="0 0 120 120"><circle class="gtrack" cx="60" cy="60" r="52"/><circle class="gfill" cx="60" cy="60" r="52" pathLength="100"/></svg><div class="gnum"><strong data-to="375" data-pre="&#8377;" data-suf="Cr+">&#8377;375Cr+</strong></div><span>Value of supplies processed</span></div></div>
<ul class="badges rv"><li>Reviewed by qualified professionals</li><li>Deadline-first filing</li><li>Confidential handling</li><li>Published pricing</li></ul></div></section>
<section class="sec lt s-mesh curve"><div class="deco" style="width:420px;height:420px;left:-120px;top:120px;background:rgba(58,155,220,.18)"></div><div class="deco" style="width:300px;height:300px;right:-80px;bottom:60px;background:rgba(91,108,240,.16)"></div><div class="wrap">
<div class="head center rv"><h2>Why clients choose Sancture</h2><p>Tax work is only as good as the process behind it. Ours is built around deadlines and evidence.</p></div>
<div class="bento">
<article class="bn bn-a rv"><svg class="wm" viewBox="0 0 24 24">'''+P_SHIELD+'''</svg><h3>Reviewed by professionals</h3><p>Every GST and Income Tax Return is checked by a qualified reviewer before it is filed.</p><div class="avs"><i></i><i></i><i></i></div></article>
<article class="bn bn-b rv"><h3>Deadline tracking</h3><p>We track due dates for each client and remind you early, which helps avoid late fees and interest.</p><div class="cal"><i class="on"></i><i class="on"></i><i class="on"></i><i class="due"></i><i></i><i></i><i></i></div></article>
<article class="bn bn-c rv"><h3>Ready for notices</h3><p>Clean records make notices easier to answer. The same team handles the reply.</p><div class="tl"><i></i><i></i><i></i></div></article>
<article class="bn bn-d rv"><h3>Published pricing</h3><p>Know the fee before you begin.</p><div class="pp"><span>&#8377;349</span><span>&#8377;999</span><span>&#8377;1,999</span></div></article></div></div></section>
<section class="sec s-night curve" style="overflow:hidden"><div class="bigq" aria-hidden="true">?</div><div class="wrap split">
<div class="rv"><h2>Common questions about GST and ITR filing</h2><p style="margin-top:14px;color:var(--mute)">Short answers to what new clients ask us most. Need something specific? <a href="contact.html">Ask our team</a>.</p></div>
<div class="rv faq">
<details><summary>Who needs to file GST Returns?</summary><p>Businesses registered under GST file periodic returns such as GSTR-1 and GSTR-3B, including Nil Returns in months with no activity.</p></details>
<details><summary>What happens if I miss a filing deadline?</summary><p>Late fees and interest may apply, and prolonged non-filing can lead to further action such as cancellation of GST registration. Filing late is usually better than not filing.</p></details>
<details><summary>Can you reply to a GST or Income Tax notice?</summary><p>Yes. We review the notice, prepare the reply with supporting documents and represent you where required.</p></details>
<details><summary>Which documents do I need to start?</summary><p>For GST: sales and purchase invoices and your GST portal access. For ITR: PAN, Form 16 or income details, AIS/26AS and investment proofs.</p></details></div></div></section>
<section class="sec s-royal curve"><div class="wrap">
<div class="head center rv"><h2>Fresh from our blog</h2><p>Plain-language guides from the Sancture team.</p></div>
<div class="grid">
<article class="card bc rv"><div class="cover cv1"><span>GST</span></div><div class="pb"><h3>GSTR-1 vs GSTR-3B: what is the difference?</h3><p>Understand what each return reports and why both must match.</p><p><a href="blogs.html">Read more</a></p></div></article>
<article class="card bc rv"><div class="cover cv2"><span>Income Tax</span></div><div class="pb"><h3>Old vs new tax regime: how to choose</h3><p>A simple way to compare both regimes using your own numbers.</p><p><a href="blogs.html">Read more</a></p></div></article>
<article class="card bc rv"><div class="cover cv3"><span>Litigation</span></div><div class="pb"><h3>Got a GST notice? Start here</h3><p>The first steps to take before you reply.</p><p><a href="blogs.html">Read more</a></p></div></article></div></div></section>
<section class="sec s-ink curve" style="padding-bottom:120px"><div class="wrap"><div class="cta-panel rv"><h2>Ready to put your tax filing on autopilot?</h2><p>Book a free consultation and we will suggest the right plan for you.</p><a class="btn light" href="contact.html">Book a consultation</a></div></div></section>
'''+FOOT+'<script src="js/flow.js"></script></body></html>'
w("index.html",home)

# ---------- SERVICES ----------
def svc(i,t,d,items,faq):
    return f'''<section class="svc" id="{i}"><div class="rv"><h2>{t}</h2><p style="margin-top:14px;color:var(--mute)">{d}</p><p style="margin-top:20px"><a class="btn" href="contact.html">Talk to an expert</a></p></div>
<div class="rv"><h3>What is included</h3><ul>{"".join("<li>%s</li>"%x for x in items)}</ul>
<details style="margin-top:20px"><summary>{faq[0]}</summary><p>{faq[1]}</p></details></div></section>'''
s=head("services.html","GST & Income Tax Services | Return Filing, Notices and Litigation | Sancture","Explore Sancture's GST return filing, income tax return filing, GST litigation and income tax litigation services, delivered with a clear process and published pricing.")
s+='''<section class="page-hero"><div class="wrap"><h1>Services built around your filing calendar</h1><p>From monthly GST returns to appeals before tax authorities, one team handles the work end to end.</p></div></section>
<div class="sec" style="padding-top:20px"><div class="wrap">'''
s+=svc("gst-registration","GST Registration","Get registered correctly the first time. Free with a two-month Growth plan.",["Eligibility check and registration-type guidance","Document checklist and application preparation","Application filing and replies to departmental queries","GSTIN, certificate and first-return guidance","Amendments to registration details"],("Who needs GST registration?","Registration is mandatory once turnover crosses the prescribed threshold, and in certain cases regardless of turnover, such as supplying through e-commerce operators. We confirm whether it applies to you."))
s+=svc("gst-returns","GST return filing","Stay compliant every month without chasing invoices or deadlines.",["Monthly and quarterly GSTR-1 and GSTR-3B filing","GSTR-2B reconciliation and input tax credit review","Annual return (GSTR-9) and reconciliation support","New GST registration and amendments","Filing reminders before every due date"],("What do you need from me each month?","Your sales invoices, purchase bills and any credit or debit notes. We tell you early if anything is missing."))
s+=svc("itr","Income tax return filing","Accurate returns for salaried individuals, professionals, businesses and investors.",["Salaried and pensioner returns with regime comparison","Business and professional income with books or presumptive taxation","Capital gains on shares, mutual funds and property","Advance tax computation and planning","Response to intimation notices after filing"],("Which ITR form applies to me?","It depends on your income sources, such as salary, business, capital gains or foreign assets. We select the right form after reviewing your documents."))
s+=svc("gst-litigation","GST litigation","Notices, assessments, appeals and registration matters handled by one team.",["Show cause notice analysis and reply drafting","Personal hearing representation before the proper officer","Appeals and related submissions","Cancellation and revocation of GST registration","Refund claims and rejections"],("I received a GST notice. What should I do first?","Do not ignore it. Note the reply deadline, collect the documents it refers to and share it with us so we can plan your reply."))
s+=svc("it-litigation","Income tax litigation","Defend your position in scrutiny, rectification, penalty and appeal proceedings.",["Reply to notices under the Income-tax Act","Scrutiny assessment support and hearings","Rectification and condonation applications","Appeals before the first appellate authority","Penalty and prosecution-related advisory"],("Can you help if I already filed my return late or incorrectly?","Often yes. Depending on the facts we can file a revised or updated return, or respond to any resulting notice."))
s+='''</div></div>
<section class="sec tint"><div class="wrap"><div class="head rv"><h2>How every engagement works</h2></div>
<div class="grid"><article class="card rv"><div class="ico">1</div><h3>Share documents</h3><p>Upload or send invoices, statements and notices securely.</p></article>
<article class="card rv"><div class="ico">2</div><h3>Verify and reconcile</h3><p>We check data against portal records and flag mismatches.</p></article>
<article class="card rv"><div class="ico">3</div><h3>Review and file</h3><p>A reviewer approves, you confirm, and we file on time.</p></article>
<article class="card rv"><div class="ico">4</div><h3>Acknowledge and follow up</h3><p>You get the acknowledgment and support for any follow-up.</p></article></div></div></section>'''+FOOT+'</body></html>'
w("services.html",s)

# ---------- PRICING ----------
p=head("pricing.html","Pricing | GST Return Filing, ITR Filing and Litigation Fees | Sancture","Transparent pricing for GST return filing, income tax return filing and notice or appeal support. Compare plans and request a custom quote from Sancture.")
p+='''<section class="page-hero"><div class="wrap"><h1>Pricing you can read in one minute</h1><p>Pick a service, compare plans and start. Prices are fixed for the scope listed.</p></div></section>
<section class="sec" style="padding-top:30px"><div class="wrap">
<div class="offerbar"><b>Offer:</b> GST Registration is free with a two-month Growth plan.<a href="contact.html?plan=Growth">Claim the offer</a></div>
<div class="tabs" role="tablist"><button data-t="gst" role="tab" aria-selected="true">GST Returns</button><button data-t="it" role="tab" aria-selected="false">Income Tax Returns</button><button data-t="lit" role="tab" aria-selected="false">Litigation</button></div>
<div class="bill" id="bill"><span>Monthly</span><button class="sw" role="switch" aria-checked="false" aria-label="Bill yearly"></button><span>Yearly (1 month free)</span></div>
<p class="fine" id="note" style="margin-bottom:30px"></p>
<div class="plans" id="plans" aria-live="polite"></div></div></section>
<section class="sec tint"><div class="wrap split"><div class="rv"><h2>Pricing questions</h2></div><div class="rv">
<details><summary>Are there any hidden charges?</summary><p>No. Government fees and late fees, if any, are charged at actuals and always shared with you in advance.</p></details>
<details><summary>What counts as one invoice in the GST plans?</summary><p>Each sales or purchase invoice reported in the month. Credit and debit notes are counted with them.</p></details>
<details><summary>Can I switch plans later?</summary><p>Yes. You can move up or down at the start of any billing month.</p></details>
<details><summary>How do I pay?</summary><p>By UPI or bank transfer.</p></details></div></div></section>'''+FOOT+'</body></html>'
w("pricing.html",p)

# ---------- BLOGS ----------
posts=[("gst","GST","GSTR-1 vs GSTR-3B: what is the difference?","GSTR-1 reports your outward supplies, while GSTR-3B is the summary return where tax is paid. The two should reconcile, since mismatches are a common reason for notices."),
("gst","GST","Why you should reconcile GSTR-2B every month","GSTR-2B shows the input tax credit available to you. Comparing it with your purchase records each month helps you claim only what is eligible and spot supplier defaults early."),
("it","Income Tax","Old vs new tax regime: how to choose","Compare your total tax under both regimes using your actual deductions. If your eligible deductions are low, the new regime is often simpler; if they are high, the old regime may save more."),
("it","Income Tax","Received an income tax notice? First five steps","Read the notice fully, note the section and deadline, download the related documents from the portal, compare them with your records and then draft a reply that addresses each point."),
("lit","Litigation","Got a GST notice? Start here","Do not ignore it. Check the type of notice, the reply date and the period it covers. Gather supporting invoices and returns, then respond in writing and attend any hearing."),
("gst","GST","Input tax credit: common reasons it gets blocked","Typical causes include supplier non-filing, mismatches between invoices and GSTR-2B, and claims on items where credit is restricted. Regular reconciliation prevents most of them.")]
b=head("blogs.html","Tax Blog | GST and Income Tax Guides and Updates | Sancture","Plain-language guides on GST returns, income tax filing, notices and litigation from the Sancture team.")
b+='''<section class="page-hero"><div class="wrap"><h1>Tax guides in plain language</h1><p>Practical explainers on GST, income tax and notices from the Sancture team.</p></div></section>
<section class="sec" style="padding-top:30px"><div class="wrap"><div class="filters"><button data-c="all" aria-pressed="true">All</button><button data-c="gst" aria-pressed="false">GST</button><button data-c="it" aria-pressed="false">Income Tax</button><button data-c="lit" aria-pressed="false">Litigation</button></div><div class="grid">'''
for c,tag,t,x in posts:
    cv={'gst':'cv1','it':'cv2','lit':'cv3'}[c]
    b+=f'<article class="card post" data-c="{c}"><div class="cover {cv}"><span>{tag}</span></div><div class="pb"><h3>{t}</h3><details><summary>Read article</summary><p>{x}</p><p style="margin-top:10px"><a href="contact.html">Ask us about your case</a></p></details></div></article>'
b+='</div></div></section>'+FOOT+'</body></html>'
w("blogs.html",b)

# ---------- CONTACT ----------
c=head("contact.html","Contact Sancture | Book a GST or Income Tax Consultation","Contact Sancture for GST return filing, income tax filing, notices and litigation support. Send an enquiry or book a consultation.")
c+=f'''<section class="page-hero"><div class="wrap"><h1>Tell us what you need filed or defended</h1><p>Send a short note and a consultant will reply within one business day.</p></div></section>
<section class="sec" style="padding-top:30px"><div class="wrap split" style="align-items:start">
<form id="enquiry" action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
<div class="two"><label>Name<input name="name" required autocomplete="name"></label><label>Phone<input name="phone" type="tel" required autocomplete="tel"></label></div>
<label>Email<input name="email" type="email" required autocomplete="email"></label>
<label>I need help with<select name="topic" id="topic"><option>GST Registration</option><option>GST return filing</option><option>Income tax return filing</option><option>GST notice or litigation</option><option>Income tax notice or litigation</option><option>Nil Return</option><option>Starter</option><option>Growth</option><option>Elite</option><option>Annual Return</option><option>Book Keeping</option><option>Enterprise</option><option>Salaried</option><option>Business and Professional</option><option>Capital Gains and NRI</option><option>Notice Reply</option><option>Appeal and Hearing</option><option>Litigation Retainer</option></select></label>
<label>Message<textarea name="message" id="msg" rows="5"></textarea></label>
<button class="btn" type="submit">Send enquiry</button></form>
<div class="info rv"><div><b>Email</b><a href="mailto:{EMAIL}">{EMAIL}</a></div><div><b>Phone and WhatsApp</b><a href="tel:{PHONE.replace(' ','')}">{PHONE}</a></div><div><b>Office</b>Add your office address here</div><div><b>Hours</b>Monday to Saturday, 10 am to 6 pm</div></div>
</div></section>'''+FOOT+'</body></html>'
w("contact.html",c)

w("sitemap.xml",'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+"".join(f"<url><loc>{D}/{'' if h=='index.html' else h}</loc></url>" for h,_ in NAV)+"</urlset>")
w("robots.txt",f"User-agent: *\nAllow: /\nSitemap: {D}/sitemap.xml\n")
w("CNAME","www.sancture.in\n")
w("README.md","""# Sancture website

Static site for GitHub Pages. No build step needed (build.py only regenerates the HTML).

## Before going live
1. Replace the domain `www.sancture.in` in `CNAME`, `build.py` (D), sitemap.xml and robots.txt, then run `python3 build.py`.
2. Replace placeholder email, phone, WhatsApp number and office address in `build.py`.
3. Create a free form at formspree.io and put its ID in `contact.html` (YOUR_FORM_ID).
4. Replace `assets/logo.png` with a higher resolution logo if you have one.

## Deploy
1. Push this folder to a GitHub repository.
2. Settings > Pages > Deploy from branch (main, root).
3. Add a CNAME DNS record for `www` pointing to `<username>.github.io`, and A records for the apex domain to GitHub Pages IPs (see GitHub docs).
4. Tick Enforce HTTPS.
""")
