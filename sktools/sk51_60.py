import sys; sys.path.insert(0,'/home/claude/work/sktools')
from skgen import *
B=[]
KP='P1 sd=s an=a anu=0 ved=D'
low=lambda y:y[:1].lower()+y[1:]
def R(n,T,V,st,ex,off,ag,ana_si=(),ana_en=(),K=KP,sm=SM_P1,N=None,P=None,place=None,pann=None):
    zsi='; '.join(x.replace('**','').rstrip('.') for x in ana_si); zen='; '.join(low(x.replace('**','').rstrip('.')) for x in ana_en)
    d=dict(n=n,T=T,V=V,K=K,Z=f'නොසිතා, නොසිහියෙන්, නොදැන; ගිලන්ව; {zsi+"; " if zsi else ""}ආපදාවල දී; උමතු ආදීන් || Unintentionally, unmindfully, not knowing; ill; {zen+"; " if zen else ""}emergencies; the insane etc.',
      story=st,extra=ex,off=([f'**අනාදරයෙන්** {off[0]}'],[f'{off[1]} **out of disrespect**']),ana=ANA(list(ana_si),list(ana_en)),ag=ag,sm=sm)
    if N: d['N']=N
    if P: d['P']=P
    if place: d['place']=place
    if pann: d['pann']=pann
    B.append(d)
BH_N='භග්ග ජනපදය, සුංසුමාරගිරය || Bhagga country, Suṃsumāragira'
BH_PL=('භග්ග ජනපදය · සුංසුමාරගිරය, භේසකළා වනයේ මිගදාය','Bhagga country · Suṃsumāragira, the deer park in Bhesakaḷā grove')
KOKA=('**කොකනද ප්‍රාසාදය** — **"කොකනද" යනු පියුමයි**; ඒ ප්‍රාසාදය **පියුමක හැඩයෙන්** තිබූ බැවින් එසේ නම් කළහ (සමන්තපාසාදිකා).','**Kokanada palace** — **“kokanada” means a lotus**; the palace was **lotus-shaped**, hence its name (Samantapāsādikā).')
R(51,'සුරුසුරුකාරක සික්ඛාපදය || Not Slurping','"සුරු සුරු" යන හඬ නගමින් වැළඳීම || Eating or drinking with a slurping sound',
  ('එක් **බමුණෙක්** සංඝයාට **කිරි පානයක්** පිළියෙළ කළේය. භික්ෂූහු ==**"සුරු සුරු" යන හඬ නගමින්** කිරි බීහ==. **පෙර නළුවෙකු වූ** එක් භික්ෂුවක් ==**"මේ මුළු සංඝයා ම සීතලෙන් ගැහෙන්නාක් මෙනැ"**== යි **සංඝයා අරබයා විහිළුවක්** කළේය. අල්පේච්ඡ භික්ෂූහු දොස් කීහ. භාග්‍යවතුන් වහන්සේ ඔහුට ගරහා, "**මහණෙනි, බුදුන්, දහම, සඟුන් අරබයා විහිළු නොකළ යුතුය; කරන්නාට දුක්කට**" යි වදාරා, සුරුසුරු ශික්ෂාපදය ද පැනවූහ.',
   'A **brahmin** had prepared **a milk drink** for the Saṅgha. The monks ==drank the milk **with a slurping sound**==. A monk **who had been an actor** said ==“**I think the whole Saṅgha has caught a chill**”== — **a joke about the Saṅgha**. Monks of few wishes criticised him. The Blessed One rebuked him, said “**Monks, one should not joke about the Buddha, the Dhamma or the Saṅgha; whoever does so: dukkaṭa**,” and laid down the rule on slurping as well.'),
  [('පද විවරණය','**සුරුසුරුකාරකං** — ==**"සුරු සුරු" යන හඬ කර කර**== වැළඳීම, බීම.','Explanation of terms','**Surusurukārakaṃ** — ==eating or drinking **making the sound “suru suru”**==.'),
   ('තෙරුවන් අරබයා විහිළු (දව)','**දවො** — **පරිහාස වචනය**. ==**කවර ආකාරයකින් වුව ද තෙරුවන් අරබයා** විහිළු නොකළ යුතුය== (සමන්තපාසාදිකා), උදාහරණ:\n|! රත්නය | විහිළු ආකාර\n| **බුද්ධ** | "කුමන බුද්ධ ද? **සිලක බුද්ධ** ද, **පටිබුද්ධ** ද?"\n| **ධම්ම** | "කුමන ධම්ම ද? **ගෝ ධම්ම** ද, **අජ ධම්ම** ද?"\n| **සංඝ** | "කුමන සංඝ ද? **මිග සංඝ** ද, **පසු සංඝ** ද?"\nඑසේ කිරීම **දුක්කට** ය.','Joking about the Triple Gem (dava)','**Davo** — **words of mockery**. ==**One should not joke about the Three Jewels in any way at all**== (Samantapāsādikā), for example:\n|! Jewel | Forms of mockery\n| **Buddha** | “What Buddha? **A silaka-Buddha**? **A paṭibuddha**?”\n| **Dhamma** | “What Dhamma? **A cow-dhamma**? **A goat-dhamma**?”\n| **Saṅgha** | “What Saṅgha? **A herd of deer**? **A herd of cattle**?”\nDoing so is **dukkaṭa**.')],
  ('"සුරු සුරු" හඬ නගමින් වැළඳීම / බීම','Eating or drinking with a slurping sound'),('**සුරු සුරු හඬ නගමින් වැළඳීම**','**Eating with a slurping sound**'),
  N='කොසඹෑ නුවර, ඝෝසිතාරාමය || Kosambī, Ghositārāma',P='බොහෝ භික්ෂූන් || A number of monks',place=('කොසඹෑ නුවර · ඝෝසිතාරාමය','Kosambī · Ghositārāma'),
  pann=('**කොසඹෑ නුවරදී** බොහෝ භික්ෂූන් අරබයා පැනවිණි. **සාධාරණ ප්‍රඥප්තියකි**. **අනාණත්තිකයි**. **දුක්කට පමණි**.','It was laid down at **Kosambī** concerning a number of monks. It is a **common rule**, **anāṇattika**, **dukkaṭa only**.'))
LICK_SI='==වළඳන විට **ඇඟිල්ලක් තරම්වත්** ලෙවකෑම නොවටී==. එහෙත් **ඝන කැඳ, පැණි (ඵාණිත), කිරිබත් (පායාස)** ආදිය **ඇඟිලිවලින් ගෙන ඇඟිලි කටට දමා** වැළඳීම වටී.'
LICK_EN='==While eating, one may not lick **even a finger**==. But **thick porridge, molasses (phāṇita), milk-rice (pāyāsa)** etc. may be taken **with the fingers and the fingers put into the mouth**.'
R(52,'හත්ථනිල්ලේහක සික්ඛාපදය || Not Licking the Hand','අත ලෙවකමින් වැළඳීම || Eating while licking the hand',
  story('**අත ලෙවකමින්** වැළඳූහ','ate **licking their hands**'),
  [('පද විවරණය','**හත්ථනිල්ලෙහකං** — ==**අත ලෙවකා ලෙවකා**== වැළඳීම.\n'+LICK_SI,'Explanation of terms','**Hatthanillehakaṃ** — ==eating **licking the hand again and again**==.\n'+LICK_EN)],
  ('අත ලෙවකමින් වැළඳීම','Eating while licking the hand'),('**අත ලෙවකමින් වැළඳීම**','**Eating while licking the hand**'))
R(53,'පත්තනිල්ලේහක සික්ඛාපදය || Not Licking the Bowl','පාත්‍රය ලෙවකමින් වැළඳීම || Eating while licking the bowl',
  story('**පාත්‍රය ලෙවකමින්** වැළඳූහ','ate **licking their bowls**'),
  [('පද විවරණය','**පත්තනිල්ලෙහකං** — ==**පාත්‍රය ලෙවකා ලෙවකා**== වැළඳීම. ==**එක් ඇඟිල්ලකින් වුව ද** පාත්‍රය ලෙවකා නොකෑ යුතුය==.\n**පරිත්තකෙ සෙසෙ** — පාත්‍රයේ **ඉතිරිය ස්වල්පයක්** වූ විට **එක් තැනකට එකතු කොට** ලෙවකා වැළඳීම **අනාපත්ති** ය.',
    'Explanation of terms','**Pattanillehakaṃ** — ==eating **licking the bowl again and again**==. ==The bowl should not be licked **even with one finger**==.\n**Parittake sese** — when **only a little is left**, **gathering it together** and licking it up is **no offence**.')],
  ('පාත්‍රය ලෙවකමින් වැළඳීම','Eating while licking the bowl'),('**පාත්‍රය ලෙවකමින් වැළඳීම**','**Eating while licking the bowl**'),
  ['**ඉතිරිය ස්වල්පයක්** වූ විට එකතු කොට ලෙවකා වැළඳීම.'],['Gathering together and licking up **a small remainder**.'])
R(54,'ඔට්ඨනිල්ලේහක සික්ඛාපදය || Not Licking the Lips','තොල් ලෙවකමින් වැළඳීම || Eating while licking the lips',
  story('**තොල් ලෙවකමින්** වැළඳූහ','ate **licking their lips**'),
  [('පද විවරණය','**ඔට්ඨනිල්ලෙහකං** — ==**තොල් ලෙවකා ලෙවකා**== වැළඳීම.\n==**එක් තොලක් වුව ද දිවෙන්** ලෙවකා නොකෑ යුතුය==; **තොල් මසින් ම ගෙන ඇතුළට** ගැනීම වටී.',
    'Explanation of terms','**Oṭṭhanillehakaṃ** — ==eating **licking the lips again and again**==.\n==**Not even one lip** should be licked **with the tongue**==; one may **draw it in with the flesh of the lips**.')],
  ('තොල් ලෙවකමින් වැළඳීම','Eating while licking the lips'),('**තොල් ලෙවකමින් වැළඳීම**','**Eating while licking the lips**'))
R(55,'සාමිස සික්ඛාපදය || Not Taking the Water Vessel with a Soiled Hand','ආහාර තැවරුණු අතින් පැන් භාජනය පිළිගැනීම || Taking the drinking-water vessel with a food-soiled hand',
  ('භික්ෂූහු **කොකනද ප්‍රාසාදයේ** ==**ආහාර තැවරුණු අතින් පැන් භාජනය** පිළිගත්හ==. මිනිස්සු "**කාමභෝගී ගිහියන් මෙනි**" යි දොස් කීහ. භාග්‍යවතුන් වහන්සේ ශික්ෂාපදය පැනවූහ.',
   'At **the Kokanada palace** the monks ==took **the drinking-water vessel with food-soiled hands**==. People complained, “**Just like householders enjoying sensual pleasures!**”, and the Blessed One laid down the rule.'),
  [('පද විවරණය',KOKA[0]+'\n**සාමිසෙන හත්ථෙන** — ==**ආමිස (ආහාර) තැවරුණු අතින්**==.\n==මෙය **පිළිකුල් බව නිසා** තහනම් කළේය== (සමන්තපාසාදිකා). එබැවින් —\n|! භාජනය | විනිශ්චය\n| **සාංඝික, පෞද්ගලික, ගිහියන් සතු, තමා සතු** — කවරක් වුව ද | ආමිස අතින් නොගත යුතුය — DK\n| **සක්, කෝප්පය (සරාව), තැටිය (ථාලක)** | ආමිස අතින් නොගත යුතුය — DK\n| අතේ **ආමිස නොතැවරුණු කොටසකින්** ගැනීම | වටී',
    'Explanation of terms',KOKA[1]+'\n**Sāmisena hatthena** — ==**with a hand soiled with food**==.\n==It was forbidden **because it is repulsive**== (Samantapāsādikā). So —\n|! Vessel | Ruling\n| **Saṅgha\'s, personal, a layman\'s, one\'s own** — any at all | not to be taken with a soiled hand — DK\n| **a conch-shell, a cup (sarāva), a plate (thālaka)** | not to be taken with a soiled hand — DK\n| taking it **with a part of the hand not soiled** | allowable'.replace("\\'","’"))],
  ('ආහාර තැවරුණු අතින් පැන් භාජනය පිළිගැනීම','Taking the drinking-water vessel with a food-soiled hand'),('**ආහාර තැවරුණු අතින් පැන් භාජනය පිළිගැනීම**','**Taking the water vessel with a soiled hand**'),
  ['"**සෝදන්නෙමි**" හෝ "**සෝදවන්නෙමි**" යි පිළිගැනීම.'],['Taking it with the thought “**I’ll wash it**” or “**I’ll have it washed**.”'],
  N=BH_N,P='බොහෝ භික්ෂූන් || A number of monks',place=BH_PL,
  pann=('**භග්ග ජනපදයේ සුංසුමාරගිරයේදී** බොහෝ භික්ෂූන් අරබයා පැනවිණි. **සාධාරණ ප්‍රඥප්තියකි**. **අනාණත්තිකයි**. **දුක්කට පමණි**.','It was laid down at **Suṃsumāragira in the Bhagga country** concerning a number of monks. It is a **common rule**, **anāṇattika**, **dukkaṭa only**.'))
R(56,'සසිත්ථක සික්ඛාපදය || Not Throwing out Rice-filled Rinse Water','බත් ඇට සහිත පාත්‍රය සේදූ දිය ගම් අතර ඉවත දැමීම || Throwing out bowl-rinsing water with rice grains among the houses',
  ('භික්ෂූහු **කොකනද ප්‍රාසාදයේ** ==**බත් ඇට සහිත පාත්‍රය සේදූ දිය ගම් අතර** ඉවත දැමූහ==. මිනිස්සු "**කාමභෝගී ගිහියන් මෙනි**" යි දොස් කීහ. භාග්‍යවතුන් වහන්සේ ශික්ෂාපදය පැනවූහ.',
   'At **the Kokanada palace** the monks ==threw out **bowl-rinsing water containing rice grains among the houses**==. People complained, “**Just like householders enjoying sensual pleasures!**”, and the Blessed One laid down the rule.'),
  [('පද විවරණය',KOKA[0]+'\n**සසිත්ථකං පත්තධොවනං** — ==**බත් ඇට (සිත්ථ) සහිත** පාත්‍රය සේදූ දිය==.\n**අන්තරඝරෙ ඡඩ්ඩෙති** — **ගම් අතර (නිවාස අතර)** ඉවත දමයි.',
    'Explanation of terms',KOKA[1]+'\n**Sasitthakaṃ pattadhovanaṃ** — ==bowl-rinsing water **with rice grains (sittha)** in it==.\n**Antaraghare chaḍḍeti** — throws it out **among the houses**.'),
   ('ඉවත දැමිය හැකි ආකාර','|! ක්‍රමය | විස්තරය\n| **උද්ධරිත්වා** | බත් ඇට **දියෙන් ඉවතට ගෙන එක් තැනක ගොඩ කොට** දිය පමණක් ඉවත දැමීම\n| **භින්දිත්වා** | බත් ඇට **පොඩි කොට දිය හා සමාන** කොට ඉවත දැමීම\n| **පටිග්ගහෙ** | **පිළිගන්නා භාජනයක් (පටිග්ගහ)** ඇත්නම් **ඊට** දැමීම\n| **නීහරිත්වා** | **පිටතට ගෙන ගොස්** ඉවත දැමීම\nමෙසේ ඉවත දමන්නාට **අනාපත්ති** ය.','Allowed ways of disposal','|! Method | Description\n| **uddharitvā** | **taking the grains out of the water, heaping them in one place**, and throwing out only the water\n| **bhinditvā** | **crushing the grains so they become like water** and throwing it out\n| **paṭiggahe** | throwing it **into a receptacle (paṭiggaha)**, if one is held out\n| **nīharitvā** | **taking it outside** and throwing it out\nThrowing it out thus is **no offence**.')],
  ('බත් ඇට සහිත පාත්‍රය සේදූ දිය ගම් අතර ඉවත දැමීම','Throwing out rinse water with rice grains among the houses'),('**බත් ඇට සහිත සේදූ දිය ගම් අතර දැමීම**','**Throwing out rinse water with rice grains among the houses**'),
  ['බත් ඇට **ඉවතට ගෙන**, **පොඩි කොට**, **පිළිගන්නා භාජනයකට**, හෝ **පිටතට ගෙන ගොස්** ඉවත දැමීම.'],['Throwing it out after **removing**, or **crushing** the grains, **into a receptacle**, or **taking it outside**.'],
  N=BH_N,P='බොහෝ භික්ෂූන් || A number of monks',place=BH_PL,
  pann=('**භග්ග ජනපදයේ සුංසුමාරගිරයේදී** බොහෝ භික්ෂූන් අරබයා පැනවිණි. **සාධාරණ ප්‍රඥප්තියකි**. **අනාණත්තිකයි**. **දුක්කට පමණි**.','It was laid down at **Suṃsumāragira in the Bhagga country** concerning a number of monks. It is a **common rule**, **anāṇattika**, **dukkaṭa only**.'))
DH_SI=('**ධම්මො** — ==**බුදුන් වදාළ, ශ්‍රාවකයන් වදාළ, ඍෂීන් වදාළ, දෙවියන් වදාළ**, **අර්ථය හා ධර්මය හා බැඳුණු**== දෙය.\n|! දේශනා ක්‍රමය | ඇවැත\n| **පදයෙන්** දේශනා කිරීම | **පදයක් පාසා** DK\n| **අක්ෂරයෙන්** දේශනා කිරීම | **අක්ෂරයක් පාසා** DK')
DH_EN=('**Dhammo** — ==what is **spoken by the Buddha, by disciples, by sages or by deities**, **connected with the meaning and with the Dhamma**==.\n|! Way of teaching | Offence\n| teaching **word by word** | DK **for each word**\n| teaching **syllable by syllable** | DK **for each syllable**')
DH_PANN=('**සැවැත් නුවරදී** ෂඩ්වර්ගීය භික්ෂූන් අරබයා පැනවිණි. **ගිලන් බව අනුව එක් අනුප්‍රඥප්තියකි** — ==ගිලනෙකුට දහම් දෙසීමට භික්ෂූන් කුකුස් කළ විට මිනිස්සු "**ගිලනෙකුට දහම් නොදෙසන්නේ කෙසේ ද?**" යි දොස් කීහ; එවිට "**නොගිලන්**" යන්න එක් කළහ==. **සාධාරණ ප්‍රඥප්තියකි**. **අනාණත්තිකයි**. **දුක්කට පමණි**.',
         'It was laid down at **Sāvatthī** concerning the group-of-six. There is **one amendment on account of illness** — ==when monks hesitated to teach someone ill, people complained, “**How can they not teach Dhamma to one who is ill?**”, and “**not ill**” was added==. It is a **common rule**, **anāṇattika**, **dukkaṭa only**.')
def DH(n,Tsi,Ten,vsi,ven,hold_si,hold_en,ex_si,ex_en,ag_si,ag_en):
    R(n,f'{Tsi} සික්ඛාපදය || Not Teaching One Holding {Ten}',f'{hold_si} අතැති නොගිලනෙකුට දහම් දෙසීම || Teaching Dhamma to one holding {hold_en} who is not ill',
      story(f'**{hold_si} අතැති අයට** දහම් දෙසූහ',f'taught Dhamma to **people holding {hold_en}**',crit=('අල්පේච්ඡ භික්ෂූහු දොස් කීහ.','Monks of few wishes complained,')),
      [('පද විවරණය',ex_si+'\n'+DH_SI,'Explanation of terms',ex_en+'\n'+DH_EN)],
      (f'{hold_si} අතැති නොගිලනෙකුට දහම් දෙසීම',f'Teaching Dhamma to one holding {hold_en} who is not ill'),(ag_si,ag_en),
      K='DD sd=s an=a anu=1',sm=SM_DD,pann=DH_PANN)
DH(57,'ඡත්තපාණි','an Umbrella','','','කුඩයක්','an umbrella',
  '**ඡත්තං** — කුඩ **තුන් වර්ගයකි**:\n|! කුඩය | අර්ථය\n| **සේතච්ඡත්ත** | **රෙද්දෙන් වැසූ සුදු කුඩය**\n| **කිලඤ්ජච්ඡත්ත** | **පැදුරු (වේවැල් පටි) කුඩය**\n| **පණ්ණච්ඡත්ත** | **තල් කොළ ආදී** කොළවලින් කළ කුඩය\n**මණ්ඩලබද්ධ, සලාකබද්ධ** — තුන ම **රවුමින් හා කූරුවලින් බැඳි** බව දැක්වීමට කීවකි. **එහි ම හටගත් දණ්ඩක** සහිත **එක් කොළයක කුඩය** ද කුඩයක් ම ය.\n**ඡත්තපාණි** — ==කුඩය **ඉසිලුව ද, උරහිසේ තැබුව ද, කලවයේ තැබුව ද**, **අතින් නොමුදා** සිටින තාක්== ඔහුට දහම් දෙසීම නොවටී. ==**අනෙකෙකු කුඩය ඉසිලුව ද**, කුඩ රඳවනයක තිබුණ ද, **අතින් ඉවත් වූ විගස** "ඡත්තපාණි" නොවේ== — දෙසීම වටී.',
  '**Chattaṃ** — **three kinds** of umbrella:\n|! Umbrella | Meaning\n| **setacchatta** | **a white umbrella covered with cloth**\n| **kilañjacchatta** | **a wicker (split-cane) umbrella**\n| **paṇṇacchatta** | one made of **palm leaves** or other leaves\n**Maṇḍalabaddha, salākabaddha** — said to show that all three are **bound with rings and ribs**. **A single-leaf umbrella** with **its own stalk** is also an umbrella.\n**Chattapāṇi** — ==as long as he **does not let go of it with his hand** — **holding it up, resting it on the shoulder or on the thigh**== — one may not teach him. ==If **someone else holds it**, or it stands on an umbrella stand, **as soon as it leaves his hand**== he is not “holding an umbrella” — one may teach him.',
  '**කුඩයක් අතැති නොගිලනෙකුට දහම් දෙසීම**','**Teaching one holding an umbrella who is not ill**')
DH(58,'දණ්ඩපාණි','a Staff','','','සැරයටියක්','a staff',
  '**දණ්ඩො** — ==**මධ්‍යම පුරුෂයෙකුගේ රියන් සතරක්** ප්‍රමාණයේ සැරයටිය==. **ඊට දිග** එකක් ද, **ඊට කෙටි** එකක් ද "**දණ්ඩ**" නොවේ.\n**දණ්ඩපාණි** — සැරයටිය **අතින් නොමුදා සිටින තාක්** ඔහුට දහම් දෙසීම නොවටී; **අතින් ඉවත් වූ විගස** දෙසීම වටී.',
  '**Daṇḍo** — ==a staff **four cubits long by a medium-sized man\'s measure**==. **One longer** or **one shorter** is “**not a staff**.”\n**Daṇḍapāṇi** — as long as he **does not let go of it with his hand**, one may not teach him; **as soon as it leaves his hand**, one may.'.replace("\\'","’"),
  '**සැරයටියක් අතැති නොගිලනෙකුට දහම් දෙසීම**','**Teaching one holding a staff who is not ill**')
DH(59,'සත්ථපාණි','a Knife','','','ආයුධයක් (සත්ථයක්)','a knife or blade',
  '**සත්ථං** — ==**එක් පසෙකින් මුවහත් හෝ දෙපසින් මුවහත්** පහර දෙන ආයුධය== (කඩුව, පිහිය ආදිය).\n**සත්ථපාණි** — එය **අතින් නොමුදා සිටින තාක්** ඔහුට දහම් දෙසීම නොවටී. ==**කඩුව ඉණේ බැඳගෙන සිටින්නා** "සත්ථපාණි" නොවේ==.',
  '**Satthaṃ** — ==a striking weapon **with one edge or two edges**== (a sword, knife etc.).\n**Satthapāṇi** — as long as he **does not let go of it with his hand**, one may not teach him. ==**One standing with a sword girded on** is not “holding a knife”==.',
  '**සත්ථයක් අතැති නොගිලනෙකුට දහම් දෙසීම**','**Teaching one holding a blade who is not ill**')
DH(60,'ආවුධපාණි','a Weapon','','','දුන්නක් (ආයුධයක්)','a weapon (bow)',
  '**ආවුධං** — පාළියේ "**චාපය, කෝදණ්ඩය**" (දුන්න) යි කීව ද, ==**සෑම දුනු වර්ගයක් ම ඊතල වර්ග සමඟ** ආයුධ යැයි දත යුතුය== (සමන්තපාසාදිකා). එබැවින් —\n|! අතේ ඇති දෙය | විනිශ්චය\n| **ඊතලය සමඟ දුන්න** | දෙසීම නොවටී\n| **දුන්න පමණක්**, හෝ **ඊතලය පමණක්** | දෙසීම නොවටී\n| **ලණුව බැඳි** හෝ **ලණුව නැති** දුන්න | දෙසීම නොවටී\n| දුන්න **කරේ (සමන්තපාසාදිකා) / උරහිසේ (කඞ්ඛාවිතරණී) එල්ලා** — **අතින් නොගන්නා තාක්** | දෙසීම වටී\nසිටගෙන හෝ හිඳගෙන සිටියත් එසේ ම ය.',
  '**Āvudhaṃ** — though the Pāli says “**a bow, a cross-bow**,” ==**every kind of bow together with every kind of arrow** is to be understood as a weapon== (Samantapāsādikā). So —\n|! In his hand | Ruling\n| **a bow with an arrow** | not allowable to teach\n| **a bow alone**, or **an arrow alone** | not allowable\n| a bow **strung** or **unstrung** | not allowable\n| a bow **hung on the neck (Samantapāsādikā) / shoulder (Kaṅkhāvitaraṇī)** — **as long as he does not take it in hand** | allowable\nThe same whether he is standing or sitting.',
  '**ආයුධයක් අතැති නොගිලනෙකුට දහම් දෙසීම**','**Teaching one holding a weapon who is not ill**')
open('/home/claude/work/content/10g_sk51_60.txt','w').write('\n\n'.join(block(d) for d in B)+'\n')
print(len(B))
