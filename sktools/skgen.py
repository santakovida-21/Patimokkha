import json,sys
# spec: list of dicts; writes content blocks in the standard format
def block(d):
    si_st,en_st=d['story']
    secs_si=[]; secs_en=[]
    L=['@sk%d'%d['n'],'T: '+d['T'],'R: - || -','N: '+d.get('N','සැවැත් නුවර, ජේතවනය || Sāvatthī, Jetavana'),
       'P: '+d.get('P','ෂඩ්වර්ගීය භික්ෂූන් || The group-of-six monks'),'V: '+d['V'],'K: '+d['K'],'Z: '+d['Z'],'G: 3','#si']
    pl_si,pl_en=d.get('place',('සැවැත් නුවර · ජේතවනාරාමය','Sāvatthī · Jetavana monastery'))
    L+=['## කථා වස්තුව','@ '+pl_si,si_st]
    let_si='අආඇඈඉඊඋඌ'; let_si=['අ','ආ','ඇ','ඈ','ඉ','ඊ','උ','ඌ','එ','ඒ']; let_en='ABCDEFGHIJ'
    k=0
    for h_si,b_si,h_en,b_en in d['extra']:
        secs_si.append((f'({let_si[k]}) '+h_si,b_si)); secs_en.append((f'({let_en[k]}) '+h_en,b_en)); k+=1
    pn_si,pn_en=d.get('pann',('**සැවැත් නුවරදී** ෂඩ්වර්ගීය භික්ෂූන් අරබයා පැනවිණි. **සාධාරණ ප්‍රඥප්තියකි**. **අනාණත්තිකයි**. **දුක්කට පමණි**.','It was laid down at **Sāvatthī** concerning the group-of-six. It is a **common rule**, **anāṇattika**, **dukkaṭa only**.'))
    secs_si.append((f'({let_si[k]}) ප්‍රඥප්තිය හා ආණත්තිය',pn_si)); secs_en.append((f'({let_en[k]}) The laying down of the rule and the command',pn_en)); k+=1
    secs_si.append((f'({let_si[k]}) ආපත්ති භේදය','|! ආකාරය | ඇවැත\n'+'\n'.join(f'| {a} | DK' for a in d['off'][0]))); secs_en.append((f'({let_en[k]}) Division of offences','|! Case | Offence\n'+'\n'.join(f'| {a} | DK' for a in d['off'][1]))); k+=1
    secs_si.append((f'({let_si[k]}) අනාපත්ති','\n'.join('# '+x for x in d['ana'][0]))); secs_en.append((f'({let_en[k]}) No offence','\n'.join('# '+x for x in d['ana'][1]))); k+=1
    secs_si.append((f'({let_si[k]}) අංග (= තීණි — තුනකි)',f'# **අනාදරය**.\n# **අනාපත්ති හේතුවක් නැති** බව.\n# {d["ag"][0]}.')); secs_en.append((f'({let_en[k]}) Factors (= tīṇi — three)',f'# **Disrespect**.\n# **No reason for exemption**.\n# {d["ag"][1]}.')); k+=1
    secs_si.append((f'({let_si[k]}) සමුට්ඨානාදිය',d['sm'][0])); secs_en.append((f'({let_en[k]}) Origin and the rest (samuṭṭhāna)',d['sm'][1]))
    for h,b in secs_si: L+=['## '+h,b]
    L+=['#en','## The Story','@ '+pl_en,en_st]
    for h,b in secs_en: L+=['## '+h,b]
    return '\n'.join(L)
SM_P1=('**පඨමපාරාජික සමුට්ඨානයි, කිරියයි, සඤ්ඤාවිමොක්ඛයි, සචිත්තකයි, ලෝකවජ්ජයි, කායකම්මයි, අකුසලචිත්තයි, දුක්ඛවේදනයි**.','**First-pārājika origin, by doing, release by perception, with intention, blameworthy by nature, bodily action, unwholesome mind, painful feeling**.')
SM_SB=('**සමනුභාසන සමුට්ඨානයි** (කාය-වාචා-චිත්ත), **කිරියයි, සඤ්ඤාවිමොක්ඛයි, සචිත්තකයි, ලෝකවජ්ජයි, කාය-වචීකම්මයි, අකුසලචිත්තයි, දුක්ඛවේදනයි** (කඞ්ඛාවිතරණී සාරාංශය).','**Samanubhāsana origin** (body–speech–mind), **by doing, release by perception, with intention, blameworthy by nature, bodily and verbal action, unwholesome mind, painful feeling** (Kaṅkhāvitaraṇī summary).')
SM_DD=('**ධම්මදේසනා සමුට්ඨානයි** (වාචා-චිත්ත), **කිරියාකිරියයි, සඤ්ඤාවිමොක්ඛයි, සචිත්තකයි, ලෝකවජ්ජයි, වචීකම්මයි, අකුසලචිත්තයි, දුක්ඛවේදනයි** (කඞ්ඛාවිතරණී සාරාංශය).','**Dhamma-teaching origin** (speech–mind), **by doing and not doing, release by perception, with intention, blameworthy by nature, verbal action, unwholesome mind, painful feeling** (Kaṅkhāvitaraṇī summary).')
SM_TS=('**ථෙය්‍යසත්ථ සමුට්ඨානයි** (කාය-චිත්ත, කාය-වාචා-චිත්ත), **කිරියයි, සඤ්ඤාවිමොක්ඛයි, සචිත්තකයි, ලෝකවජ්ජයි, කාය-වචීකම්මයි, අකුසලචිත්තයි, දුක්ඛවේදනයි** (කඞ්ඛාවිතරණී සාරාංශය).','**Thieves\'-caravan origin** (body–mind; body–speech–mind), **by doing, release by perception, with intention, blameworthy by nature, bodily and verbal action, unwholesome mind, painful feeling** (Kaṅkhāvitaraṇī summary).')
ANA=lambda extra_si=(),extra_en=(),apada=True:(['**නොසිතා**; **නොසිහියෙන්**; **නොදැන**.','**ගිලන්ව**.']+list(extra_si)+(['**ආපදාවල** දී.'] if apada else [])+['උමතු ආදීන්ට හා ආදිකම්මිකයාට.'],
  ['**Unintentionally**; **unmindfully**; **not knowing**.','When **ill**.']+list(extra_en)+(['In **emergencies**.'] if apada else [])+['For the insane and so on, and the first offender.'])
VASU=('==**වාසය සඳහා පැමිණ සිටින** විට (වාසූපගත)==.','==When **staying there** (vāsūpagata)==.')
def story(si_act,en_act,law_si='',law_en='',crit=('මිනිස්සු දොස් කීහ.','People complained,')):
    return (f'**ෂඩ්වර්ගීය භික්ෂූහු** =={si_act}==. {crit[0]} භාග්‍යවතුන් වහන්සේ ශික්ෂාපදය පැනවූහ.',
            f'**The group-of-six** =={en_act}==. {crit[1]} and the Blessed One laid down the rule.')
