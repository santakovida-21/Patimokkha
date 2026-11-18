# Verifies that every Pāli passage in content/17_pi.txt is a verbatim substring of the sources.
import re,sys
sys.path.insert(0,'/home/claude/work/tools')
from pilib import load
norm=lambda s:re.sub(r'\s+',' ',s.replace('**','').replace('==','').replace('‍','')).strip()
SRC=norm(' '.join(load(f,1,10**7) for f in ('pac_pali.md','pac_att.md','kkv.md')))
SRC2=SRC.replace('‘‘','').replace('’’','')
bad=0;n=0;rid='?'
for ln in open('/home/claude/work/content/17_pi.txt',encoding='utf-8'):
    ln=ln.rstrip('\n')
    if ln.startswith('@pac'): rid=ln[1:]; continue
    if not ln or ln.startswith(('#','T:',':::','!pn:','@ ','|!')): continue
    if ln.startswith('> ') and len(ln)<200: continue           # rule text (same as Sinhala tab) / verse
    if ln.startswith('|'):
        cell=ln.split('|')[-1].strip(); pieces=[cell]
    else:
        t=re.sub(r'^(- |> |!src: )','',ln); pieces=[p for p in re.split(r' … | — ',t)]
    for p in pieces:
        p=norm(p).rstrip(' …')
        if not p: continue
        n+=1
        if p in SRC or p.replace('‘‘','').replace('’’','') in SRC2: continue
        # 17-fold cells may join two cuts with '; ' or end with a resolved 'ං'
        if all(norm(x) in SRC or norm(x)[:-1] in SRC for x in p.split('; ')): continue
        bad+=1; print('NOT VERBATIM',rid,':',p[:120])
print('checked',n,'passages; problems',bad)
