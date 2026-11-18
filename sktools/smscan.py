import re,glob,sys
REF=re.compile(r'හා සමාන|කී පරිදි|මෙනි|මෙන් ම|\bas (for|in|the)\b|\bAs \*\*|\bsame as\b|\bAs the\b|\bas \*\*',re.I)
for f in sorted(glob.glob('/home/claude/work/content/[01][0-9]*.txt')):
    if f.endswith('10_sk.txt') or '05_pac01_20' in f: continue
    txt=open(f).read()
    for blk in re.split(r'^(?=@[a-z]+\d+\s*$)',txt,flags=re.M):
        m=re.match(r'@(\S+)',blk)
        if not m: continue
        rid=m.group(1)
        for sec in re.split(r'^## ',blk,flags=re.M)[1:]:
            title,_,body=sec.partition('\n')
            if ('සමුට්ඨාන' in title or 'Origin' in title) and REF.search(body):
                print(f.split('/')[-1],rid,'|',title[:30],'|',body.strip().replace('\n',' ⏎ ')[:230])
