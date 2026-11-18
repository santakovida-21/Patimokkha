import re,glob
SCO_SI='**සඤ්චරිත්ත සමුට්ඨානයි** (ඡසමුට්ඨාන — කාය, වාචා, කාය-වාචා, කාය-චිත්ත, වාචා-චිත්ත, කාය-වාචා-චිත්ත)'
SCO_EN='**Matchmaking (go-between) origin** (six origins — body; speech; body–speech; body–mind; speech–mind; body–speech–mind)'
REST_SI='**නෝසඤ්ඤාවිමොක්ඛයි, අචිත්තකයි, පණ්ණත්තිවජ්ජයි, කාය-වචීකම්මයි, තිචිත්තයි, තිවේදනයි**.'
REST_EN='**no release by perception, without intention, blameworthy by convention, bodily and verbal action, three kinds of mind, three feelings**.'
def sc(kr_si,kr_en,note_si='',note_en=''):
    return (SCO_SI+', '+kr_si+(f' ({note_si})' if note_si else '')+', '+REST_SI, SCO_EN+', '+kr_en+(f' ({note_en})' if note_en else '')+', '+REST_EN)
K_SI,K_EN='**කිරියයි**','**by doing**'
KA_SI,KA_EN='**කිරියාකිරියයි**','**by doing and not doing**'
MAN={
 'ani1':('**පඨමපාරාජික සමුට්ඨානයි** (කාය-චිත්ත), **කිරියයි, සඤ්ඤාවිමොක්ඛයි, සචිත්තකයි, ලෝකවජ්ජයි, කායකම්මයි, අකුසලචිත්තයි, ද්විවේදනයි** (සුඛ, උපේක්ඛා). පිළිගන්නා ඇවත අනුව **සීලවිපත්තිය හෝ ආචාරවිපත්තිය** විය හැකිය.',
         '**First-pārājika origin** (body–mind), **by doing, release by perception, with intention, blameworthy by nature, bodily action, unwholesome mind, two feelings** (pleasant, neutral). Depending on the offence admitted it may be **failure in virtue or failure in conduct**.'),
 'ani2':('**අදින්නාදාන සමුට්ඨානයි** (තිසමුට්ඨාන — කාය-චිත්ත, වාචා-චිත්ත, කාය-වාචා-චිත්ත), **කිරියයි, සඤ්ඤාවිමොක්ඛයි, සචිත්තකයි, ලෝකවජ්ජයි, කාය-වචීකම්මයි, අකුසලචිත්තයි, තිවේදනයි**. පිළිගන්නා ඇවත අනුව **සීලවිපත්තිය හෝ ආචාරවිපත්තිය** විය හැකිය.',
         '**Stealing origin** (three origins — body–mind; speech–mind; body–speech–mind), **by doing, release by perception, with intention, blameworthy by nature, bodily and verbal action, unwholesome mind, three feelings**. Depending on the offence admitted it may be **failure in virtue or failure in conduct**.'),
 'np2':('**කඨින සමුට්ඨානයි** (කාය-වාචා, කාය-වාචා-චිත්ත), **අකිරියයි** (**පච්චුද්ධරණය නොකිරීම**), **නෝසඤ්ඤාවිමොක්ඛයි, අචිත්තකයි, පණ්ණත්තිවජ්ජයි, කාය-වචීකම්මයි, තිචිත්තයි, තිවේදනයි**.',
        '**Kaṭhina origin** (body–speech; body–speech–mind), **by not doing** (**not relinquishing**), **no release by perception, without intention, blameworthy by convention, bodily and verbal action, three kinds of mind, three feelings**.'),
 'np5':sc(KA_SI,KA_EN,'ගැනීම කිරියාව, හුවමාරුව නොදීම අකිරියාව','taking is doing, not giving in exchange is not doing'),
 'np7':sc(K_SI,K_EN),'np8':sc(K_SI,K_EN),'np9':sc(K_SI,K_EN),'np10':sc(K_SI,K_EN),'np12':sc(K_SI,K_EN),
 'np13':sc(KA_SI,KA_EN,'කිරීම කිරියාව; සුදු, දුඹුරු කොටස් නොගැනීම අකිරියාව','making is doing; not taking the white and brown parts is not doing'),
 'np14':sc(KA_SI,KA_EN),'np15':sc(KA_SI,KA_EN),'np17':sc(K_SI,K_EN),
 'np18':sc('**කිරියයි හෝ අකිරියයි**','**by doing or by not doing**','ගැනීමෙන් ඇවැත් වන බැවින් කිරිය; ප්‍රතික්ෂේප නොකිරීමෙන් ඇවැත් වන බැවින් අකිරිය','falling into it by taking is doing; by not refusing, not doing'),
 'np19':sc(K_SI,K_EN),'np20':sc(K_SI,K_EN),
}
REFRX=re.compile(r'හා සමාන|කී පරිදි|මෙනි|මෙන් ම|\bas (for|in|the)\b|\bAs \*\*|\bsame as\b|\bAs the\b|\bas \*\*|— as (in )?the',re.I)
def clean(body,lang):
    lines=body.split('\n')
    out=[]
    for ln in lines:
        s=ln
        if lang=='si':
            s=re.sub(r'^(සමුට්ඨාන ආදිය |සෙසු සියල්ල )?\*\*[^*]*(හා සමාන ය|කී පරිදි ම ය|මෙනි)[^*]*\*\*\s*(—\s*|:\s*)','',s)
            s=re.sub(r'^සමුට්ඨාන ආදිය \*\*([^*]*?)(?: හා සමාන ය| මෙනි)(; එහෙත් [^*]*)?\*\*\s*—\s*','',s)
        else:
            s=re.sub(r'^(Origin and the rest are |The rest )?(As |as )\*\*[^*]*\*\*\s*(—\s*|:\s*)','',s)
            s=re.sub(r'^\*\*As [^*]*\*\*\s*(—\s*|:\s*)','',s)
            s=re.sub(r'\s*—\s*as (in )?the (previous|first)[^.]*\.$','.',s)
        if s and s[0].islower() and lang=='en': s=s[0].upper()+s[1:]
        out.append(s)
    return '\n'.join(out)
changed=0;left=[]
for f in sorted(glob.glob('/home/claude/work/content/[01][0-9]*.txt')):
    if f.endswith('10_sk.txt') or '05_pac01_20' in f: continue
    txt=open(f).read(); new=[]
    for blk in re.split(r'^(?=@[a-z]+\d+\s*$)',txt,flags=re.M):
        m=re.match(r'@(\S+)',blk)
        if not m: new.append(blk); continue
        rid=m.group(1)
        head,_,rest=blk.partition('#si\n'); si,_,en=rest.partition('#en\n')
        def proc(part,lang):
            secs=re.split(r'^(?=## )',part,flags=re.M); res=[]
            for sec in secs:
                if sec.startswith('## ') and ('සමුට්ඨාන' in sec.split('\n')[0] or 'Origin' in sec.split('\n')[0]):
                    t,_,b=sec.partition('\n')
                    tail='\n' if b.endswith('\n') else ''
                    if rid in MAN: nb=MAN[rid][0 if lang=='si' else 1]+(('\n'+'\n'.join(x for x in b.strip().split('\n')[1:] if x.startswith('**විපත්තිය') or x.startswith('**Failure'))) if False else '')+tail
                    else: nb=clean(b,lang)
                    if REFRX.search(nb): left.append((f.split('/')[-1],rid,lang,nb.strip()[:160]))
                    res.append(t+'\n'+nb)
                else: res.append(sec)
            return ''.join(res)
        if '#si\n' in blk: blk=head+'#si\n'+proc(si,'si')+'#en\n'+proc(en,'en')
        new.append(blk)
    nt=''.join(new)
    if nt!=txt: open(f,'w').write(nt); changed+=1
print('files changed',changed)
for x in left: print(*x)
