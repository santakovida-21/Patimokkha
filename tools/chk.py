import re,sys
s=open(sys.argv[1]).read()
parts=re.split(r'^@(pac\d+)\s*$',s,flags=re.M)
for k in range(1,len(parts),2):
    rid,b=parts[k],parts[k+1]
    si,en=b.split('\n#si\n')[1].split('\n#en\n')
    f=lambda x:[re.match(r'## (\{\w+\})',l).group(1) for l in x.split('\n') if l.startswith('## ')]
    rom=[w for w in re.findall(r'[A-Za-zāīūṃṅñṭḍṇḷ]{3,}',si) if w not in('story','att','kkv','src','pn','short','long')]
    print(rid,len(f(si)),len(f(en)),f(si)==f(en),rom[:5], 'longpali:',sum(1 for l in b.split('\n') if l.startswith('> ') and len(l)>200))
