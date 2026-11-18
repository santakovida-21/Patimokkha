import re,json,sys
L=open(sys.argv[1],encoding='utf-8').read().split('\n')
L=L[3859:]
def clean(s):
    s=re.sub(r'\|[^|]{1,12}\|','',s); s=re.sub(r'\s*\([^()]*\d+[^()]*\)','',s)
    s=re.sub(r'\s*\*\(var:[^)]*\)\*','',s)
    return re.sub(r'\s+',' ',s.replace('**','')).strip()
secs=[];cur=None;top=None
for ln in L:
    m=re.match(r'(#{2,3}) (.+)',ln)
    if m:
        if m.group(1)=='##': top=m.group(2).strip()
        if m.group(1)=='###' or 'වග්ග' not in m.group(2):
            cur=dict(top=top,h=m.group(2).strip(),body=[]);secs.append(cur)
        continue
    if cur is not None and ln.strip(): cur['body'].append(clean(ln))
out=[]
for s in secs:
    txt=' '.join(s['body'])
    sents=re.split(r'(?<=[.;])\s+',txt)
    pick=lambda k:[x for x in sents if k in x]
    a=pick('ආරබ්භ')[:1]; ag=pick('අඞ්ගානි')[:2]; sm=[x for x in sents if 'සමුට්ඨාන' in x][-2:]
    out.append(dict(top=s['top'],h=s['h'],len=len(txt),arabbha=a,anga=ag,samu=sm))
json.dump(out,open('/home/claude/work/kkv.json','w'),ensure_ascii=False,indent=0)
print(len(out)); 
for o in out: print(o['top'],'|',o['h'],o['len'])
