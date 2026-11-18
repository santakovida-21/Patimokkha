import re
def blocks(f):
    s=open(f).read(); p=re.split(r'^@(pac\d+)\s*$',s,flags=re.M); return {p[k]:p[k+1] for k in range(1,len(p),2)}
def segs(sec):
    out=[];cur=None
    for ln in sec.split('\n'):
        if ln.startswith('### '): cur=[]; continue
        if ln.startswith('@ ') and cur==[]: continue
        if ln.startswith('!pn:') or ln.startswith('!src:'):
            if cur is not None: out.append('\n'.join(cur)); cur=None
            continue
        if cur is not None: cur.append(ln)
    return out
def story(B,rid,lang):
    b=B[rid]
    if lang=='si': t=b.split('\n#si\n')[1].split('\n#en\n')[0]
    elif lang=='en': t=b.split('\n#en\n')[1]
    else: t=b.split('\n#zh\n')[1]
    return t.split('\n## ')[0]
