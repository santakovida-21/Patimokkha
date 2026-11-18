# Writes content/17_pi.txt from all Pāli-view generators (verbatim source cuts).
import sys
sys.path.insert(0,'/home/claude/work/tools')
import pi_pac11, pi_rules
o=pi_pac11.lines()
for f in pi_rules.RULES: o+=f()
open('/home/claude/work/content/17_pi.txt','w',encoding='utf-8').write('\n'.join(o)+'\n')
print('ok', sum(1 for l in o if l.startswith('@')),'rules')
