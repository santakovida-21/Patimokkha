import sys,re,glob
rid=sys.argv[1]; pat=sys.argv[2] if len(sys.argv)>2 else None
for f in sorted(glob.glob('/home/claude/work/content/0*.txt'))+['/home/claude/work/content/11b_as.txt']:
    t=open(f).read()
    for blk in re.split(r'^(?=@[a-z]+\d+\s*$)',t,flags=re.M):
        if blk.startswith('@'+rid+'\n'):
            for sec in re.split(r'^(?=## )',blk,flags=re.M):
                if pat is None or re.search(pat,sec): print(sec.rstrip()[:3000]); print('~~')
