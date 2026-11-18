import re,glob
def blocks(f):
    s=open(f).read(); p=re.split(r'^@(pac\d+)\s*$',s,flags=re.M)
    return {p[k]:p[k+1] for k in range(1,len(p),2)}
base={}
for f in ['/home/claude/work/content/12_tabs.txt','/home/claude/work/content/13_tabs.txt']: base.update(blocks(f))
zh=blocks('/home/claude/work/content/15_zh.txt')
g=lambda x:[re.match(r'## (\{\w+\})',l).group(1) for l in x.split('\n') if l.startswith('## ')]
for rid,b in zh.items():
    si=base[rid].split('\n#si\n')[1].split('\n#en\n')[0]; z=b.split('\n#zh\n')[1]
    print(rid,len(g(si)),len(g(z)),g(si)==g(z), 'ags', len([l for l in z.split('## {kkv} 构成支分')[1].split('\n## ')[0].split('\n') if l.startswith('# ')]) if '构成支分' in z else 'NA')
