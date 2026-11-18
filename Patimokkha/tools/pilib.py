# Shared helpers for the Pāli view: passages are cut VERBATIM from the source texts.
import re,sys
SRC='/home/claude/srcs/'
def load(f,a,b):
    L=open(SRC+f,encoding='utf-8').read().split('\n')[a-1:b]
    t='\n'.join(L)
    t=re.sub(r'\|[^|\n]{1,12}\|','',t)              # page markers |ත්2.0232|
    t=re.sub(r'\s*\*\(var:.*?\)\)?\*','',t)           # variant readings
    t=re.sub(r'\*\*\d+\.\*\*\s*','',t)                # paragraph numbers **89.**
    t=re.sub(r'<!--.*?-->','',t)
    t=re.sub(r'<p align[^>]*>.*?</p>','',t)
    t=re.sub(r'[ \t]+',' ',t)
    return t
class Src:
    def __init__(s,f,a,b): s.t=load(f,a,b)
    def __call__(s,a,b=None,nth=1):
        """exact substring from phrase a (nth occurrence) through phrase b (inclusive)."""
        t=s.t; i=-1
        for _ in range(nth):
            i=t.find(a,i+1)
            if i<0: sys.exit('NOT FOUND start: '+a[:70])
        if b is None: j=i+len(a)
        else:
            j=t.find(b,i)
            if j<0: sys.exit('NOT FOUND end: '+b[:70]+'  (start '+a[:40]+')')
            j+=len(b)
        return re.sub(r'\s*\n\s*',' ',t[i:j].strip())
    def block(s,a,b,nth=1):
        """like __call__ but keeps the source's paragraph breaks -> list of paragraphs."""
        t=s.t; i=-1
        for _ in range(nth):
            i=t.find(a,i+1)
            if i<0: sys.exit('NOT FOUND start: '+a[:70])
        j=t.find(b,i)
        if j<0: sys.exit('NOT FOUND end: '+b[:70])
        j+=len(b)
        return [re.sub(r'[ \t]+',' ',x).strip() for x in t[i:j].split('\n') if x.strip()]
    def gatha(s,a):
        L=s.t.split('\n'); k=[n for n,l in enumerate(L) if a in l][0]; out=[]
        while k<len(L) and L[k].startswith('>'):
            x=L[k].lstrip('> ').rstrip()
            if x: out.append('> '+x)
            k+=1
        return '\n'.join(out)
def has(src,phrase):
    if phrase not in src.t: sys.exit('NOT IN SOURCE: '+phrase)
    return phrase
J=' … '
def s17(o,rows):
    o.append('## {s17} සත්තරසාකාරා')
    o.append('|! # | ආකාරො | ඉමස්මිං සික්ඛාපදෙ')
    for i,(a,b) in enumerate(rows): o.append(f'| {i+1} | **{a}** | {b}')
