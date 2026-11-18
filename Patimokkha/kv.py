import re,sys
t=open('/home/claude/src/ex/ප්‍රාතිමෝක්ෂ අධ්‍යයනය/ද්වෙමාතිකාපාළි - කඞ්ඛාවිතරණී-අට්ඨකථා.md',encoding='utf-8').read()
L=t.split('\n')[3859:]
secs=[];cur=None
for ln in L:
    m=re.match(r'(#{2,3}) (.+)',ln)
    if m:
        cur=[m.group(2),[]];secs.append(cur);continue
    if cur and ln.strip():
        x=re.sub(r'\|[^|]{1,12}\|','',ln); x=re.sub(r'\s*\*\(var:[^)]*\)\*','',x); x=re.sub(r'\s*\([^()]*\d+[^()]*\)','',x)
        cur[1].append(x.replace('**',''))
i=int(sys.argv[1])
h,b=secs[i]
print(h); print('\n'.join(b))
