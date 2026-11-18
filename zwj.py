import re,glob
for f in glob.glob('/home/claude/work/content/*.txt'):
    t=open(f,encoding='utf-8').read()
    n=re.sub(r'([^න])්(?=[යර])', lambda m: m.group(1)+'්‍', t)
    open(f,'w',encoding='utf-8').write(n)
