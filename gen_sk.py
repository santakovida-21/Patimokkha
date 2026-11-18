import re
L=open('/home/claude/work/sk_data.txt',encoding='utf-8').read().strip().split('\n')
KM={'P1':'P1','SBK':'SB kr=K','TSL':'TS vj=L cit=A ved=D','DD':'DD'}
out=[]
VN=[('හිඳගත්හ','හිඳීම'),('පිළිගත්හ','පිළිගැනීම'),('ගත්හ','ගැනීම'),('ගියහ','යාම'),('වැළඳූහ','වැළඳීම'),('දේශනා කළහ','දේශනා කිරීම'),('කළහ','කිරීම'),('ඇන්දහ','ඇඳීම'),('පෙරවූහ','පෙරවීම'),('නැගූහ','නැගීම'),('බැලූහ','බැලීම'),('වැසූහ','වැසීම'),('දැමූහ','දැමීම'),('පිරවූහ','පිරවීම')]
EX={68:('!dgm: sk-ground **නොකළ යුතු ඉරියව්ව** — දේශකයා බිම හිඳ, ගිලන් නොවූ අසන්නා ආසනයක හිඳ සිටියදී.','!dgm: sk-ground **A posture not to be used** — the teacher sits on the ground while the listener, not ill, sits on a seat.'),
 69:('!dgm: sk-lowseat **නොකළ යුතු ඉරියව්ව** — දේශකයා පහත් ආසනයක, අසන්නා උස් ආසනයක.','!dgm: sk-lowseat **A posture not to be used** — the teacher on a low seat, the listener on a high one.'),
 70:('!dgm: sk-standing **නොකළ යුතු ඉරියව්ව** — දේශකයා සිටගෙන, අසන්නා හිඳගෙන.','!dgm: sk-standing **A posture not to be used** — the teacher standing, the listener sitting.')}
def verbn(v):
    for a,b in VN:
        if v.endswith(a): return v[:-len(a)]+b
    return v
for ln in L:
    f=[x.strip() for x in ln.split('¦')]
    n=int(f[0]); T,R,V,M,X,K=f[1:7]
    vsi,_,ven=V.partition('||'); vsi=vsi.strip(); ven=ven.strip()
    msi,_,men=M.partition('||'); msi=msi.strip(); men=men.strip()
    xsi,_,xen=X.partition('||'); xsi=xsi.strip(); xen=xen.strip()
    if n==51: N='කොසඹෑ නුවර, ඝෝසිතාරාමය || Kosambī, Ghositārāma'; P='බොහෝ භික්ෂූන් || A number of monks'
    elif n in (55,56): N='භග්ග ජනපදය, සුංසුමාරගිරය || Bhagga country, Suṃsumāragira'; P='බොහෝ භික්ෂූන් || A number of monks'
    else: N='සැවැත් නුවර, ජේතවනය || Sāvatthī, Jetavana'; P='ෂඩ්වර්ගීය භික්ෂූන් || The group-of-six monks'
    nsi,nen=[x.strip() for x in N.split('||')]; psi,pen=[x.strip() for x in P.split('||')]
    zsi='නොසිතා, නොසිහියෙන්, නොදැන, ගිලන්, ආපදා'+(('; '+xsi) if xsi else '')+'; උමතු ආදීන්'
    zen='Unintentionally, unmindfully, not knowing, ill, emergencies'+(('; '+xen) if xen else '')+'; the insane etc.'
    b=[f'@sk{n}',f'T: {T}',f'R: {R}',f'N: {N}',f'P: {P}',f'V: {vsi} || {ven}',f'K: {KM[K]} sd=s an=a anu=0',f'Z: {zsi} || {zen}','#si',
       '## කථා වස්තුව',f'@ {nsi.replace(", "," · ")}',f'**{psi.replace("භික්ෂූන්","භික්ෂූහු")}** =={vsi}==. '+('එය දුටු අල්පේච්ඡ භික්ෂූහු දොස් කීහ' if 57<=n<=72 else 'එය දුටු මිනිස්සු "ගිහි කාමභෝගීන් මෙනි" යි දොස් කීහ')+'. භාග්‍යවතුන් වහන්සේ ශික්ෂාපදය පැනවූහ.']
    if msi: b+=['## පද විවරණය',msi]
    if n in EX: b+=['## රූප සටහන',EX[n][0]]
    b+=['## ආපත්ති භේදය','|! ආකාරය | ඇවැත',f'| අනාදරයෙන් (ගෞරවයක් නැතිව) — {verbn(vsi)} | DK','| නොසිතා, නොසිහියෙන්, නොදැන හෝ ගිලන්ව | N',
        '## අනාපත්ති','# **නොසිතා** (අසඤ්චිච්ච); **නොසිහියෙන්** (අසතියා);','# **නොදැන** (අජානන්ත); **ගිලන්** වූ විට; **ආපදාවකදී**;']
    if xsi: b+=[f'# {xsi};']
    b+=['# උමතු ආදීන්ට හා ආදිකම්මිකයන්ට.','## අංග','# ශික්ෂාපදයේ දැක්වෙන **ක්‍රියාව කිරීම / නොකිරීම**.','# **අනාදරය** (අගෞරවය).','# **අනාපත්ති කරුණක් නොවීම** (ගිලන් බව ආදිය නොමැති වීම).',
        '#en','## The Story',f'@ {nen.replace(", "," · ")}',f'**{pen}** =={ven}==. '+('Monks of few wishes criticised this.' if 57<=n<=72 else 'People criticised this: “Like householders who enjoy sensual pleasures.”')+' The Blessed One laid down the rule.']
    if men: b+=['## Explanation of terms',men]
    if n in EX: b+=['## Illustration',EX[n][1]]
    b+=['## Division of offences','|! Case | Offence',f'| Out of disrespect — {ven} | DK','| Unintentionally, unmindfully, not knowing, or when ill | N',
        '## No offence','# **Unintentionally**; **unmindfully**;','# **Not knowing**; when **ill**; in **emergencies**;']
    if xen: b+=[f'# {xen};']
    b+=['# For the insane and so on, and for the first offenders.','## Factors','# **Doing (or not doing)** what the rule describes.','# **Disrespect** (*anādariya*).','# **No exemption** applies (illness and so on).','']
    out.append('\n'.join(b))
open('/home/claude/work/content/10_sk.txt','w',encoding='utf-8').write('\n'.join(out))
print(len(out))
