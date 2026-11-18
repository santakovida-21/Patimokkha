import re,html
# ---------- Sinhala-script Pali -> Roman ----------
IND={'අ':'a','ආ':'ā','ඉ':'i','ඊ':'ī','උ':'u','ඌ':'ū','එ':'e','ඒ':'e','ඔ':'o','ඕ':'o','ඖ':'u'}
CON={'ක':'k','ඛ':'kh','ග':'g','ඝ':'gh','ඞ':'ṅ','ච':'c','ඡ':'ch','ජ':'j','ඣ':'jh','ඤ':'ñ','ට':'ṭ','ඨ':'ṭh','ඩ':'ḍ','ඪ':'ḍh','ණ':'ṇ','ත':'t','ථ':'th','ද':'d','ධ':'dh','න':'n','ප':'p','ඵ':'ph','බ':'b','භ':'bh','ම':'m','ය':'y','ර':'r','ල':'l','ව':'v','ස':'s','හ':'h','ළ':'ḷ','ෂ':'ṣ','ශ':'ś','ෆ':'f'}
DEP={'ා':'ā','ි':'i','ී':'ī','ු':'u','ූ':'ū','ෙ':'e','ේ':'e','ො':'o','ෝ':'o','ෘ':'ṛ'}
def roman(s):
    s=s.replace('‍','').replace('්ඖ','්උ')
    out=[];i=0;n=len(s)
    while i<n:
        c=s[i]
        if c in CON:
            out.append(CON[c]); nx=s[i+1] if i+1<n else ''
            if nx=='්': i+=2; continue
            if nx in DEP: out.append(DEP[nx]); i+=2; continue
            out.append('a'); i+=1; continue
        if c in IND: out.append(IND[c]); i+=1; continue
        if c=='ං': out.append('ṃ'); i+=1; continue
        if c in DEP: out.append(DEP[c]); i+=1; continue
        out.append(c); i+=1
    r=''.join(out)
    return r
def cap(s): return s[:1].upper()+s[1:]
# ---------- mini markup ----------
TAGS={'PR':('r','පාරාජික','Pārājika'),'SD':('o','සංඝාදිසේස','Saṅghādisesa'),'TH':('p','ථුල්ලච්චය','Thullaccaya'),
 'NP':('y','නිස්සග්ගිය පාචිත්තිය','Nissaggiya pācittiya'),'PC':('y','පාචිත්තිය','Pācittiya'),'PD':('b','පාටිදේසනීය','Pāṭidesanīya'),
 'DK':('g','දුක්කට','Dukkaṭa'),'DB':('g','දුබ්භාසිත','Dubbhāsita'),'N':('n','අනාපත්ති','No offence'),'AN':('n','අනාපත්ති','No offence')}
TAGZH={'PR':'波罗夷','SD':'僧残','TH':'偷兰遮','NP':'尼萨耆波逸提','PC':'波逸提','PD':'波罗提提舍尼','DK':'突吉罗','DB':'恶说','N':'不犯','AN':'不犯'}
def tagname(code,lang):
    c,si,en=TAGS[code]
    return si if lang=='si' else (TAGZH[code] if lang=='zh' else en)
def inline(t):
    t=html.escape(t,quote=False)
    t=re.sub(r'\*\*(.+?)\*\*',r'<strong>\1</strong>',t)
    t=re.sub(r'==(.+?)==',r'<mark>\1</mark>',t)
    t=re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?!\w)',r'<i class="term">\1</i>',t)
    t=t.replace('"','“',1) if False else t
    return t
def tagspan(code,lang):
    parts=[p for p in re.split(r'[+/]',code.strip()) if p]
    out=[]
    for p in parts:
        p=p.strip()
        if p in TAGS:
            out.append(f'<span class="tag {TAGS[p][0]}">{tagname(p,lang)}</span>')
        else: out.append(inline(p))
    return ' '.join(out)
def celltags(h,lang):
    # turn stand-alone offence codes inside a table cell into small tags (not rule refs like 'NP 23')
    def rep(m):
        return f'<span class="tag sm {TAGS[m.group(1)][0]}">{tagname(m.group(1),lang)}</span>'
    return re.sub(r'(?<![\w.-])(PR|SD|TH|NP|PC|PD|DK)(?![\w.-])(?!\s*\d)',rep,h)

# ---------- Sinhala-script Pāli → dual (native + Roman) spans for en / zh ----------
_SIRUN=re.compile(r"[\u0D80-\u0DFF\u200D](?:[\u0D80-\u0DFF\u200C\u200D\s,.;:–—’‘'“”?!()\-]*[\u0D80-\u0DFF\u200D])?")
def dual(h):
    """Wrap every run of Sinhala-script Pāli in an html string as native + Roman spans (CSS shows one by script setting)."""
    def rep(m):
        t=m.group(0); r=roman(t)
        return f'<span class="p-si">{t}</span><span class="p-ro">{r}</span>'
    out=[];pos=0
    # skip text inside tags
    for mt in re.finditer(r'<[^>]*>',h):
        out.append(_SIRUN.sub(rep,h[pos:mt.start()])); out.append(mt.group(0)); pos=mt.end()
    out.append(_SIRUN.sub(rep,h[pos:]))
    r=''.join(out)
    # capitalise the first Roman letter at the start of a Pāli block
    r=re.sub(r'(<div class="(?:pali|pnp)"><span class="p-si">[^<]*</span><span class="p-ro">)([a-zāīū])',lambda m:m.group(1)+m.group(2).upper(),r)
    return r

def md(src,lang):
    h=_md(src,lang)
    return h if lang=='si' else dual(h)
def _md(src,lang,_sl_done=None):
    if _sl_done is None: _sl_done=[False]
    """mini markup -> html"""
    lines=src.strip('\n').split('\n'); o=[]; i=0
    while i<len(lines):
        ln=lines[i].rstrip()
        if not ln.strip(): i+=1; continue
        if ln.startswith('|'):
            rows=[]
            while i<len(lines) and lines[i].startswith('|'):
                rows.append(lines[i]); i+=1
            h=['<div class="scroll"><table>']
            for r in rows:
                head=r.startswith('|!')
                cells=[c.strip() for c in r.lstrip('|!').split('|')]
                if cells and cells[-1]=='' : cells=cells[:-1]
                tg='th' if head else 'td'; tr=[]
                for j,c in enumerate(cells):
                    if not head and j==len(cells)-1 and len(cells)>1 and re.fullmatch(r'[A-Z+/ ]+',c) and all(p.strip() in TAGS for p in re.split(r'[+/]',c) if p.strip()):
                        tr.append(f'<td>{tagspan(c,lang)}</td>')
                    elif not head: tr.append(f'<td>{celltags(inline(c),lang)}</td>')
                    else: tr.append(f'<{tg}>{inline(c)}</{tg}>')
                h.append('<tr>'+''.join(tr)+'</tr>')
            h.append('</table></div>'); o.append(''.join(h)); continue
        if re.match(r'#\s',ln) or ln.startswith('- '):
            num=ln.startswith('#'); items=[]
            while i<len(lines) and (re.match(r'#\s',lines[i]) if num else lines[i].startswith('- ')):
                items.append(lines[i][2:].strip()); i+=1
            if num:
                o.append('<div class="factors">'+''.join(f'<div class="fitem"><b>{k+1}</b><div>{inline(t)}</div></div>' for k,t in enumerate(items))+'</div>')
            else:
                o.append('<ul class="ul">'+''.join(f'<li>{inline(t)}</li>' for t in items)+'</ul>')
            continue
        if ln.startswith('> '):
            q=[]
            while i<len(lines) and lines[i].startswith('> '): q.append(inline(lines[i][2:])); i+=1
            o.append('<div class="pali">'+'<br>'.join(q)+'</div>'); continue
        m=re.match(r'!dgm:\s*([a-z0-9-]+)(?:\s+(.*))?$',ln)
        if m:
            cap=inline(m.group(2)) if m.group(2) else ''
            o.append(f'<figure class="dgm" data-dgm="{m.group(1)}"><div class="dgm-stage"></div>{f"<figcaption>{cap}</figcaption>" if cap else ""}</figure>'); i+=1; continue
        if ln.startswith('!pn:'):
            lab=inline(ln[4:].strip()); i+=1; pl=[]; tr=[]
            while i<len(lines) and (lines[i].startswith('> ') or lines[i].startswith('~ ')):
                (pl if lines[i].startswith('> ') else tr).append(inline(lines[i][2:])); i+=1
            o.append(f'<div class="pnb"><span class="lbl">{lab}</span><div class="pnp">{"<br>".join(pl)}</div>'+(f'<div class="pnt">{"<br>".join(tr)}</div>' if tr else '')+'</div>'); continue
        if ln.startswith('%% '):
            rows=[]
            while i<len(lines) and lines[i].startswith('%% '):
                a,_,b=lines[i][3:].partition('|'); rows.append((inline(a.strip()),inline(b.strip()))); i+=1
            o.append('<div class="flow">'+''.join(f'<div class="fl"><b>{a}</b><span>{b}</span></div>' for a,b in rows)+'</div>'); continue
        if ln.strip() in (':::short',':::long'):
            kind=ln.strip()[3:]; i+=1; inner=[]
            while i<len(lines) and lines[i].strip()!=':::': inner.append(lines[i]); i+=1
            i+=1
            if kind=='short' and not _sl_done[0]:
                _sl_done[0]=True
                lab={'si':('කෙටි','දීර්ඝ'),'zh':('简略','详细')}.get(lang,('Short','Long'))
                o.append(f'<div class="sltog" role="group"><button type="button" data-sl="short">{lab[0]}</button><button type="button" data-sl="long">{lab[1]}</button></div>')
            o.append(f'<div class="sl-{kind}">'+_md('\n'.join(inner),lang,[True])+'</div>'); continue
        if ln.startswith('### '):
            o.append(f'<h3 class="vh">{inline(ln[4:].strip())}</h3>'); i+=1; continue
        if ln.startswith('!src:'):
            o.append(f'<p class="srcn">{inline(ln[5:].strip())}</p>'); i+=1; continue
        if ln.startswith('@ '):
            o.append(f'<div class="place">{inline(ln[2:])}</div>'); i+=1; continue
        o.append(f'<p>{inline(ln)}</p>'); i+=1
    return ''.join(o)
