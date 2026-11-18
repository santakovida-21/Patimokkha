"""Build the site in two forms:
   site/  — multi-file artifact: index.html, css/app.css, js/app.js, data/index.js, data/<cat>.js
   out/pratimoksha.html — single self-contained file for offline download"""
import json,os,shutil
W='/home/claude/work/'
S=W+'site/'
shutil.rmtree(S,ignore_errors=True)
for d in ('css','js','data'): os.makedirs(S+d)
d=json.load(open(W+'data.json',encoding='utf-8'))
J=lambda o: json.dumps(o,ensure_ascii=False,separators=(',',':')).replace('</','<\\/')
idx=[]; per={}
for r in d['rules']:
    r2={k:v for k,v in r.items() if k!='secs'}
    r2['has']=bool(r.get('secs'))
    idx.append(r2)
    if r.get('secs'): per.setdefault(r['cat'],{})[r['id']]=r['secs']
index_js='window.PM_INDEX='+J({'cats':d['cats'],'rules':idx,'figs':d.get('figs',[])})+';\n'
cat_js={c['id']:'(window.PM_Q=window.PM_Q||[]).push(['+J(c['id'])+','+J(per.get(c['id'],{}))+']);\n' for c in d['cats']}
css=open(W+'src/app.css',encoding='utf-8').read()
app=open(W+'src/app.js',encoding='utf-8').read().replace('/*REFS*/',open(W+'refs.js',encoding='utf-8').read())
html=open(W+'src/index.html',encoding='utf-8').read()
open(S+'index.html','w',encoding='utf-8').write(html)
open(S+'css/app.css','w',encoding='utf-8').write(css)
open(S+'js/app.js','w',encoding='utf-8').write(app)
open(S+'data/index.js','w',encoding='utf-8').write(index_js)
for k,v in cat_js.items(): open(S+'data/'+k+'.js','w',encoding='utf-8').write(v)
three=open(W+'src/three.min.js',encoding='utf-8').read(); dg=open(W+'src/diagrams.js',encoding='utf-8').read()
open(S+'js/three.min.js','w',encoding='utf-8').write(three); open(S+'js/diagrams.js','w',encoding='utf-8').write(dg)
assert '</script' not in three and '</script' not in dg
# standalone
one=html.replace('<link rel="stylesheet" href="css/app.css">','<style>\n'+css+'</style>')
one=one.replace('<script src="data/index.js"></script>\n<script src="js/app.js"></script>',
  '<script>'+index_js+''.join(cat_js.values())+'</script>\n<script type="text/plain" id="src-three.min">'+three+'</script>\n<script type="text/plain" id="src-diagrams">'+dg+'</script>\n<script>\n'+app+'</script>')
assert '<script src=' not in one
open(W+'out/pratimoksha.html','w',encoding='utf-8').write(one)
for f in sorted(os.listdir(S+'data')): print(f, os.path.getsize(S+'data/'+f))
print('standalone',len(one.encode()))
