import json,re,glob,sys
from lib import roman,cap,md,TAGS,inline,dual
W='/home/claude/work/'
raw=json.load(open(W+'rules_raw.json'))
CATS=[
 dict(id='par',si='පාරාජික',en='Pārājika',sub_si='පරාජයට පත් කරවන ඇවැත් 4',sub_en='Four rules entailing defeat',sec='පාරාජිකුද්දෙසො',vg=[(None,None,4)]),
 dict(id='sd',si='සංඝාදිසේස',en='Saṅghādisesa',sub_si='සංඝයා ඇසුරෙන් පිරිසිදු වන ඇවැත් 13',sub_en='Thirteen rules entailing a meeting of the Saṅgha',sec='සඞ්ඝාදිසෙසුද්දෙසො',vg=[(None,None,13)]),
 dict(id='ani',si='අනියත',en='Aniyata',sub_si='අනියත (නියම නොවූ) ඇවැත් 2',sub_en='Two undetermined rules',sec='අනියතුද්දෙසො',vg=[(None,None,2)]),
 dict(id='np',si='නිස්සග්ගිය පාචිත්තිය',en='Nissaggiya Pācittiya',sub_si='අත්හැරිය යුතු වස්තු සහිත ඇවැත් 30',sub_en='Thirty rules entailing forfeiture and confession',sec='නිස්සග්ගියපාචිත්තියා',
      vg=[('කථින වග්ගය','Kathina-vagga',10),('කෝසිය වග්ගය','Kosiya-vagga',10),('පත්ත වග්ගය','Patta-vagga',10)]),
 dict(id='pac',si='පාචිත්තිය',en='Pācittiya',sub_si='දෙසිය යුතු ඇවැත් 92',sub_en='Ninety-two rules entailing confession',sec='සුද්ධපාචිත්තියා',
      vg=[('මුසාවාද වග්ගය','Musāvāda-vagga',10),('භූතගාම වග්ගය','Bhūtagāma-vagga',10),('ඕවාද වග්ගය','Ovāda-vagga',10),('භෝජන වග්ගය','Bhojana-vagga',10),('අචේලක වග්ගය','Acelaka-vagga',10),('සුරාපාන වග්ගය','Surāpāna-vagga',10),('සප්පාණක වග්ගය','Sappāṇaka-vagga',10),('සහධම්මික වග්ගය','Sahadhammika-vagga',12),('රතන වග්ගය','Ratana-vagga',10)]),
 dict(id='pd',si='පාටිදේසනීය',en='Pāṭidesanīya',sub_si='ප්‍රතිදේශනය කළ යුතු ඇවැත් 4',sub_en='Four rules entailing acknowledgement',sec='පාටිදෙසනීයා',vg=[(None,None,4)]),
 dict(id='sk',si='සේඛිය',en='Sekhiya',sub_si='හික්මිය යුතු පුහුණු 75',sub_en='Seventy-five training rules',sec='සෙඛියා',
      vg=[('පරිමණ්ඩල වග්ගය','Parimaṇḍala-vagga',10),('උජ්ජග්ඝික වග්ගය','Ujjagghika-vagga',10),('ඛම්භකත වග්ගය','Khambhakata-vagga',10),('සක්කච්ච වග්ගය','Sakkacca-vagga',10),('කබළ වග්ගය','Kabaḷa-vagga',10),('සුරුසුරු වග්ගය','Surusuru-vagga',10),('පාදුක වග්ගය','Pāduka-vagga',15)]),
 dict(id='as',si='අධිකරණ සමථ',en='Adhikaraṇa-samatha',sub_si='අධිකරණ සංසිඳවීමේ ක්‍රම 7',sub_en='Seven ways of settling disputes',sec=None,vg=[(None,None,7)]),
]
CATZH={'par':('波罗夷','四条导致失败（他胜）的学处'),'sd':('僧残','十三条需僧团出罪的学处'),'ani':('不定','两条不定法'),
 'np':('尼萨耆波逸提','三十条须舍物并忏悔的学处'),'pac':('波逸提','九十二条须忏悔的学处'),'pd':('波罗提提舍尼','四条须向他人告白的学处'),
 'sk':('众学','七十五条应学习的学处'),'as':('灭诤','七种平息诤事的方法')}
VGZH={'Kathina-vagga':'迦絺那品','Kosiya-vagga':'憍舍耶品','Patta-vagga':'钵品','Musāvāda-vagga':'妄语品','Bhūtagāma-vagga':'草木品',
 'Ovāda-vagga':'教诫品','Bhojana-vagga':'食品','Acelaka-vagga':'裸形品','Surāpāna-vagga':'饮酒品','Sappāṇaka-vagga':'有虫品',
 'Sahadhammika-vagga':'如法品','Ratana-vagga':'宝品','Parimaṇḍala-vagga':'圆整品','Ujjagghika-vagga':'大笑品','Khambhakata-vagga':'叉腰品',
 'Sakkacca-vagga':'恭敬品','Kabaḷa-vagga':'饭团品','Surusuru-vagga':'嗦嗦声品','Pāduka-vagga':'鞋品'}
for _c in CATS: _c['zh'],_c['sub_zh']=CATZH[_c['id']]
SAMATHA=[('සම්මුඛාවිනයො','උප්පන්නුප්පන්නානං අධිකරණානං සමථාය වූපසමාය සම්මුඛාවිනයො දාතබ්බො.'),('සතිවිනයො','සතිවිනයො දාතබ්බො.'),('අමූළ්හවිනයො','අමූළ්හවිනයො දාතබ්බො.'),('පටිඤ්ඤාතකරණං','පටිඤ්ඤාය කාරෙතබ්බං.'),('යෙභුය්‍යසිකා','යෙභුය්‍යසිකා.'),('තස්සපාපියසිකා','තස්සපාපියසිකා.'),('තිණවත්ථාරකො','තිණවත්ථාරකොති.')]
PRESET={
 'P1':dict(sm='p1',kr='K',sv='S',ci='S',vj='L',km='K',cit='A',ved='2'),
 'AD':dict(sm='ad',kr='K',sv='S',ci='S',vj='L',km='KV',cit='A',ved='3'),
 'SC':dict(sm='sc',kr='K',sv='N',ci='A',vj='P',km='KV',cit='3',ved='3'),
 'KT':dict(sm='kt',kr='A',sv='N',ci='A',vj='P',km='KV',cit='3',ved='3'),
 'EL':dict(sm='el',kr='K',sv='N',ci='A',vj='P',km='K',cit='3',ved='3'),
 'PD':dict(sm='pd',kr='K',sv='N',ci='A',vj='P',km='V',cit='3',ved='3'),
 'SB':dict(sm='sb',kr='A',sv='S',ci='S',vj='L',km='KV',cit='A',ved='D'),
 'AH':dict(sm='ah',kr='K',sv='N',ci='A',vj='P',km='KV',cit='3',ved='3'),
 'TS':dict(sm='ts',kr='K',sv='S',ci='S',vj='P',km='KV',cit='3',ved='3'),
 'DD':dict(sm='dd',kr='KA',sv='S',ci='S',vj='L',km='V',cit='A',ved='D'),
 'BH':dict(sm='bh',kr='K',sv='N',ci='A',vj='P',km='KV',cit='2',ved='2'),
 'CV':dict(sm='cv',kr='KA',sv='N',ci='S',vj='L',km='V',cit='A',ved='D'),
 'AN':dict(sm='an',kr='KA',sv='N',ci='A',vj='P',km='V',cit='3',ved='3'),
}
def parse_content(path):
    txt=open(path,encoding='utf-8').read()
    blocks=re.split(r'^@(\S+)\s*$',txt,flags=re.M)
    out={}
    for k in range(1,len(blocks),2):
        rid=blocks[k]; body=blocks[k+1]
        d=dict(head={},si=None,en=None,zh=None)
        parts=re.split(r'^#(si|en|zh|pi)\s*$',body,flags=re.M)
        for ln in parts[0].split('\n'):
            m=re.match(r'([A-Z]{1,2}):\s*(.*)',ln)
            if m: d['head'][m.group(1)]=m.group(2).strip()
        for j in range(1,len(parts),2):
            lang=parts[j]; secs=[]
            for s in re.split(r'^## ',parts[j+1],flags=re.M)[1:]:
                t,_,b=s.partition('\n'); t=t.strip()
                m=re.match(r'\{(\w+)\}\s*',t)
                if m: d.setdefault('grp',{}).setdefault(lang,[]).append(m.group(1)); t=t[m.end():]
                secs.append((t,b))
            d[lang]=secs
        out[rid]=d
    return out
def bi(s):
    if s is None: return None
    a,_,b=s.partition('||'); return dict(si=a.strip(),en=b.strip() or a.strip())
def codes_from(secs_md):
    found=[]
    for t,b in secs_md:
        for m in re.finditer(r'\|\s*([A-Z+/ ]+)\s*$',b,flags=re.M):
            for p in re.split(r'[+/]',m.group(1)):
                p=p.strip()
                if p in TAGS and p not in ('N','AN') and p not in found: found.append(p)
    return found
# --- assemble ---
content={}
for f in sorted(glob.glob(W+'content/*.txt')):
    if f.endswith('_zh.txt') or f.endswith('_pi.txt'): continue
    content.update(parse_content(f))
for f in sorted(glob.glob(W+'content/*_zh.txt')):
    for rid,d in parse_content(f).items():
        if rid not in content: continue
        content[rid]['zh']=d['zh']; content[rid]['headzh']=d['head']
        if d.get('grp',{}).get('zh'): content[rid].setdefault('grp',{})['zh']=d['grp']['zh']
for f in sorted(glob.glob(W+'content/*_pi.txt')):
    for rid,d in parse_content(f).items():
        if rid not in content: continue
        content[rid]['pi']=d['pi']; content[rid]['headpi']=d['head']; content[rid]['grppi']=d.get('grp',{}).get('pi',[])
def picap(h):
    U=lambda m:m.group(1)+m.group(2).upper()
    # first letter of a block (p, li, h3, place, table cell)
    h=re.sub(r'(<(?:p|li|h3 class="vh"|div class="place"|td|th)>(?:<strong>|<mark>)?(?:‘‘|‘)?<span class="p-si">[^<]*</span><span class="p-ro">)([a-zāīūṭḍṇḷṃñṅ])',U,h)
    # sentence starts inside a Roman run
    def run(m):
        t=re.sub(r'([.!?] (?:‘‘|‘)?)([a-zāīūṭḍṇḷṃñṅ])',U,m.group(2))
        return m.group(1)+t+'</span>'
    h=re.sub(r'(<span class="p-ro">)([^<]*)</span>',run,h)
    return h
samples=json.load(open(W+'samples.json'))
TRD=json.load(open(W+'trdata.json'))
SITAG={'පාරාජික':'PR','සංඝාදිසේස':'SD','ථුල්ලච්චය':'TH','පාචිත්තිය':'PC','පචිති':'PC','දුක්කට':'DK','දුබ්භාසිත':'DB'}
rules=[];g=0;missing=[]
bysec={}
for r in raw: bysec.setdefault(r['sec'],[]).append(r)
for c in CATS:
    src=bysec.get(c['sec'],[]) if c['sec'] else [dict(n=i+1,name=n,text=t) for i,(n,t) in enumerate(SAMATHA)]
    c['vaggas']=[];n=0
    for vi,(vsi,ven,cnt) in enumerate(c['vg']):
        ids=[]
        for k in range(cnt):
            n+=1;g+=1; r=src[n-1]; rid=f"{c['id']}{n}"
            ids.append(rid)
            name=r['name'] or ''
            name=re.sub(r'\s*සික්ඛාපදං$','',name).strip()
            name=re.sub(r'සික්ඛාපදං$','',name)
            if c['id']=='as': name=r['name']
            rule=dict(id=rid,cat=c['id'],vg=vi,n=n,g=g,pn=name,pnr=cap(roman(name)) if name else '',pt=r['text'],ptr=cap(roman(r['text'])))
            cd=content.get(rid)
            if not cd: missing.append(rid); rule['secs']=[]; rule['title']=dict(si=name,en=rule['pnr']); rules.append(rule); continue
            h=cd['head']
            rule['title']=bi(h.get('T')) or dict(si=name,en=rule['pnr'])
            rule['tr']=bi(h.get('R'))
            if rid in TRD:
                t=TRD[rid]; rule['tr']=dict(si=t['si'],en=t['en'])
                if t.get('notes'): rule['tnotes']=t['notes']
            secs=[]
            if rid in samples['si'] and not cd.get('grp'):
                ssi=samples['si'][rid]['secs']
                sen=samples['en'][rid]['secs'] if rid in samples['en'] else [(t,md(b,'en')) for t,b in (cd['en'] or [])]
                if sen and isinstance(sen[0],dict): sen=[(x['t'],x['h']) for x in sen]
                if len(sen)!=len(ssi): print('WARN section mismatch',rid,len(ssi),len(sen),file=sys.stderr)
                for i2,x in enumerate(ssi):
                    e=sen[i2] if i2<len(sen) else ('','')
                    secs.append(dict(t=dict(si=x['t'],en=dual(e[0])),h=dict(si=x['h'],en=dual(e[1]))))
                ap=[]
                for x in ssi:
                    for m in re.finditer(r'class="tag [a-z]">([^<]+)<',x['h']):
                        for k2,v in SITAG.items():
                            if m.group(1).strip().startswith(k2) and v not in ap: ap.append(v)
            else:
                si_s=cd['si'] or []; en_s=cd['en'] or []
                if len(si_s)!=len(en_s): print('WARN section mismatch',rid,len(si_s),len(en_s),file=sys.stderr)
                for i2,(t,b) in enumerate(si_s):
                    et,eb=en_s[i2] if i2<len(en_s) else ('','')
                    sd=dict(t=dict(si=t,en=et),h=dict(si=md(b,'si'),en=md(eb,'en')))
                    zs=cd.get('zh') or []
                    if zs and len(zs)==len(si_s):
                        sd['t']['zh']=zs[i2][0]; sd['h']['zh']=md(zs[i2][1],'zh')
                    elif zs and i2==0: print('WARN zh section mismatch',rid,len(si_s),len(zs),file=sys.stderr)
                    if cd.get('grp'): sd['g']=cd['grp']['si'][i2]
                    secs.append(sd)
                ap=codes_from(si_s)
            rule['secs']=secs
            if any(x.get('g') for x in secs): rule['tabs']=1
            if cd.get('pi'):
                ps=[(t,b,g2) for (t,b),g2 in zip(cd['pi'],cd['grppi'])]
                p17=[x for x in ps if x[2]=='s17']; ps=[x for x in ps if x[2]!='s17']
                if len(ps)!=len(secs) or [x[2] for x in ps]!=[x.get('g') for x in secs]:
                    print('WARN pi section mismatch',rid,len(secs),len(ps),file=sys.stderr)
                else:
                    for sd,(t,b,g2) in zip(secs,ps):
                        sd['pt']=dict(si=t,ro=cap(roman(t)))
                        sd['ph']=dict(si=md(b,'si'),en=picap(md(b,'en')),zh=picap(md(b,'zh')))
                    pt=cd['headpi'].get('T','')
                    rule['pi']=dict(si=pt,ro=cap(roman(pt)))
                    if p17: rule['pi17']=dict(si=md(p17[0][1],'si'),en=picap(md(p17[0][1],'en')),zh=picap(md(p17[0][1],'zh')))
            # 17-fold
            k=h.get('K','').split()
            s17={}
            if k and k[0] in PRESET: s17.update(PRESET[k[0]]); k=k[1:]
            for kv in k:
                a,_,b=kv.partition('='); s17[a]=b
            if 'ap' in s17: ap=s17['ap'].split(',')
            MAIN={'par':'PR','sd':'SD','np':'NP','pac':'PC','pd':'PD','sk':'DK'}
            if c['id']=='np' and 'PC' in ap: ap=[x for x in ap if x!='PC']
            if c['id'] in MAIN and MAIN[c['id']] not in ap: ap=[MAIN[c['id']]]+ap
            ORD=['PR','SD','TH','NP','PC','PD','DK','DB']
            ap=sorted(set(ap),key=lambda x:ORD.index(x) if x in ORD else 99)
            s17['ap']=ap
            for key in ('N','P','V','Z'):
                if h.get(key): s17[key.lower()]=bi(h[key])
            # anga
            ags=None
            for lang in ('si','en','zh'):
                for t,b in (cd.get(lang) or []):
                    if re.match(r'(\(.\)\s*)?(අංග|Factors|构成支分)',t):
                        items=[x[2:].strip() for x in b.split('\n') if x.startswith('# ')]
                        if items: ags=ags or {}; ags[lang]=items
            if ags: s17['ags']=ags
            if not ags and rid in samples['en']:
                for x in samples['en'][rid]['secs']:
                    if 'Factors' in x['t'] or 'factors' in x['t']:
                        s17['ag']=x['h'].count('class="fitem"') or None
            if not ags and rid in samples['si'] and not s17.get('ag'):
                for x in samples['si'][rid]['secs']:
                    if 'අංග' in x['t']: s17['ag']=x['h'].count('<li>') or None
            if h.get('G'): s17['ag']=int(h['G']) if h['G'].strip().isdigit() else h['G'].strip()
            elif ags: s17['ag']=len(ags.get('si') or ags.get('en'))
            hz=cd.get('headzh') or {}
            if hz.get('T'): rule['title']['zh']=hz['T']
            if hz.get('R'): rule.setdefault('tr',{})['zh']=hz['R']
            for key in ('N','P','V','Z'):
                if hz.get(key) and key.lower() in s17: s17[key.lower()]['zh']=hz[key]
            rule['s17']=s17
            rules.append(rule)
        c['vaggas'].append(dict(si=vsi,en=ven,zh=VGZH.get(ven),ids=ids))
    c.pop('vg');c.pop('sec')
print('rules',len(rules),'missing',len(missing),file=sys.stderr)
if '-v' in sys.argv: print(missing,file=sys.stderr)
# ---------- figure gallery index ----------
FIGG=[dict(id='hp',si='හත්ථපාසය (අත්පස) මැනීම',en='Measuring arm’s reach (hatthapāsa)',
           dsi='පිළිගැන්වීමේදී දායකයා හා භික්ෂුව අතර රියන් දෙකහමාරේ දුර මනින ආකාරය.',den='How the two and a half cubits between giver and monk are measured when food is offered.',ids=['hp-seated','hp-standing','hp-lying','hp-roof','hp-tree']),
      dict(id='pt',si='පාත්‍රය',en='The bowl',
           dsi='පාත්‍ර ප්‍රමාණ, ආහාර පිරවීමේ මට්ටම් හා පාත්‍රයේ බැඳුම්.',den='Bowl sizes, how full a bowl may be, and mends on a bowl.',ids=['pt-sizes','pt-levels','pt-mends','sk-tittika']),
      dict(id='teach',si='ධර්ම දේශනා ඉරියව්',en='Postures when teaching Dhamma',
           dsi='දේශකයා හා ශ්‍රාවකයා සිටිය යුතු ආකාරය — නොකළ යුතු ඉරියව්.',den='How teacher and listener are placed — postures not to be used.',ids=['sk-ground','sk-lowseat','sk-standing'])]
for _g,(_z,_d) in zip(FIGG,[('测量手臂距离 (hatthapāsa)','供养时施主与比丘之间两肘半距离的测量方法。'),('钵','钵的尺寸、盛食的高度与钵的补缀。'),('说法时的姿势','说法者与听法者应有的位置 — 不应采用的姿势。')]): _g['zh'],_g['dzh']=_z,_d
ruleids={r['id'] for r in rules}
FIG={}
for rid,d in content.items():
    if rid not in ruleids: continue
    for lang in ('si','en'):
        for t,body in (d.get(lang) or []):
            for ln in body.split('\n'):
                m=re.match(r'!dgm:\s*([a-z0-9-]+)(?:\s+(.*))?$',ln.strip())
                if not m: continue
                f=FIG.setdefault(m.group(1),dict(d=m.group(1),rules=[],si='',en=''))
                if rid not in f['rules']: f['rules'].append(rid)
                if not f[lang] and m.group(2): f[lang]=inline(re.sub(r'^\*\*\d+\.\s*',"**",m.group(2).strip()))
known={x for g in FIGG for x in g['ids']}
rest=[k for k in FIG if k not in known]
if rest: FIGG.append(dict(id='other',si='වෙනත්',en='Other',dsi='',den='',ids=rest))
FIGS=[dict({k:v for k,v in g.items() if k!='ids'},figs=[FIG[x] for x in g['ids'] if x in FIG]) for g in FIGG]
print('figs',sum(len(g['figs']) for g in FIGS),file=sys.stderr)
json.dump(dict(cats=CATS,rules=rules,figs=FIGS),open(W+'data.json','w'),ensure_ascii=False,separators=(',',':'))
