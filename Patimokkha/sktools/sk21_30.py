import sys; sys.path.insert(0,'/home/claude/work/sktools')
from skgen import *
B=[]
def gs(g): return ('ගම් අතර යාම','going among the houses') if g else ('ගම් අතර හිඳීම','sitting among the houses')
def Zs(sit,apada=True,extra=('','')):
    si='නොසිතා, නොසිහියෙන්, නොදැන; ගිලන්ව; '+extra[0]+('වාසය සඳහා පැමිණ සිටින විට; ' if sit else '')+('ආපදාවල දී; ' if apada else '')+'උමතු ආදීන්'
    en='Unintentionally, unmindfully, not knowing; ill; '+extra[1]+('when staying there; ' if sit else '')+('emergencies; ' if apada else '')+'the insane etc.'
    return si+' || '+en
VNOTE=('**වාසූපගතස්ස** — ==හිඳීම සම්බන්ධ **ඛම්භකත (22), ඔගුණ්ඨිත (24), පල්ලත්ථික (26)** යන ශික්ෂාපදවල **වාසය සඳහා පැමිණ සිටින්නාට අනාපත්ති**== (කඞ්ඛාවිතරණී).',
       '**Vāsūpagatassa** — ==in the sitting rules **arms akimbo (22), head covered (24), clasping the knees (26)**, **no offence for one staying there**== (Kaṅkhāvitaraṇī).')
# 21-22 khambhakata
for n,g in ((21,True),(22,False)):
    sv,ev=gs(g)
    ex_si='**ඛම්භකතො** — ==**ඉණෙහි අත තබා** කළ "කණුව" (ඛම්භය) ඇති== — **දෑත ඉඟටියේ තබා වැලමිට දෙපසට** යොමු කළ ඉරියව්ව.\n**එකතො වා උභතො වා** — **එක් අතකින් හෝ දෑතින් ම** ඛම්භය කොට.'
    ex_en='**Khambhakato** — ==with **a “pillar” made by placing the hand on the hip**== — the posture with hands on the waist and elbows turned out.\n**Ekato vā ubhato vā** — making the akimbo with **one arm or both**.'
    if not g: ex_si+='\n'+VNOTE[0]; ex_en+='\n'+VNOTE[1]
    B.append(dict(n=n,T=f'ඛම්භකත {"ගමන" if g else "නිසීදන"} සික්ඛාපදය || Not {"Going" if g else "Sitting"} with Arms Akimbo',
      V=f'ඉණෙහි අත් තබා {sv} || Arms akimbo while {ev}',K='P1 sd=s an=a anu=0 ved=D',Z=Zs(not g),
      story=story(f'**ඉණෙහි අත් තබාගෙන (ඛම්භකතව)** {"ගම් අතර ගියහ" if g else "ගම් අතර හිඳගත්හ"}',f'{"went" if g else "sat"} among the houses **with arms akimbo**'),
      extra=[('පද විවරණය',ex_si,'Explanation of terms',ex_en)],
      off=([f'**අනාදරයෙන්** එක් අතකින් හෝ දෑතින් ඛම්භය කොට {sv}'],[f'{ev.capitalize()} with one or both arms akimbo **out of disrespect**']),
      ana=ANA([VASU[0]] if not g else [],[VASU[1]] if not g else []),ag=(f'**ඛම්භකතව {sv}**',f'**{ev.capitalize()} with arms akimbo**'),sm=SM_P1))
# 23-24 ogunthita
for n,g in ((23,True),(24,False)):
    sv,ev=gs(g)
    ex_si='**ඔගුණ්ඨිතො** — ==**හිස සහිතව** සිවුරෙන් **පොරවා**== (හිස වසාගෙන).\n> සේඛිය 3 හි "**හිස සහිතව පොරවා නොව**" යි කී සුප්පටිච්ඡන්න ලක්ෂණය ද බලන්න.'
    ex_en='**Oguṇṭhito** — ==**covered with the robe including the head**==.\n> See also the sign of “well covered” in sekhiya 3: “**not with the head covered**.”'
    if not g: ex_si+='\n'+VNOTE[0]; ex_en+='\n'+VNOTE[1]
    B.append(dict(n=n,T=f'ඔගුණ්ඨිත {"ගමන" if g else "නිසීදන"} සික්ඛාපදය || Not {"Going" if g else "Sitting"} with the Head Covered',
      V=f'හිස වසා පොරවාගෙන {sv} || Head covered while {ev}',K='P1 sd=s an=a anu=0 ved=D',Z=Zs(not g),
      story=story(f'**හිස සහිතව පොරවාගෙන** {"ගම් අතර ගියහ" if g else "ගම් අතර හිඳගත්හ"}',f'{"went" if g else "sat"} among the houses **with their heads covered**'),
      extra=[('පද විවරණය',ex_si,'Explanation of terms',ex_en)],
      off=([f'**අනාදරයෙන්** හිස සහිතව පොරවා {sv}'],[f'{ev.capitalize()} with the head covered **out of disrespect**']),
      ana=ANA([VASU[0]] if not g else [],[VASU[1]] if not g else []),ag=(f'**හිස වසා {sv}**',f'**{ev.capitalize()} with the head covered**'),sm=SM_P1))
# 25 ukkutika
B.append(dict(n=25,T='උක්කුටික සික්ඛාපදය || Not Walking on Toes or Heels',V='ඇඟිලි තුඩින් හෝ විලුඹෙන් පමණක් ගම් අතර යාම || Walking among the houses on toes or heels',
  K='P1 sd=s an=a anu=0 ved=D',Z=Zs(False),
  story=story('**උක්කුටිකව (ඇඟිලි තුඩින් හෝ විලුඹෙන්)** ගම් අතර ගියහ','went among the houses **on their toes or heels**'),
  extra=[('පද විවරණය','**උක්කුටිකා** — ==**විලුඹ ඔසවා පා ඇඟිලි තුඩින් පමණක්**, හෝ **පා ඇඟිලි ඔසවා විලුඹෙන් පමණක්** බිම ස්පර්ශ කරමින්== යාම. කරණ විභක්තිය **ඉත්ථම්භූත ලක්ෂණයෙහි** ය.\n> **සේඛිය 25** ගමනට පමණක් අදාළ ය; හිඳීම සම්බන්ධ යුගලය **පල්ලත්ථික (26)** ය.',
          'Explanation of terms','**Ukkuṭikā** — walking ==touching the ground **only with the toes, heels raised**, or **only with the heels, toes raised**==. The instrumental is **of manner**.\n> **Sekhiya 25** concerns going only; its sitting pair is **clasping the knees (26)**.')],
  off=(['**අනාදරයෙන්** ඇඟිලි තුඩින් හෝ විලුඹෙන් පමණක් ගම් අතර යාම'],['Walking among the houses on toes or heels **out of disrespect**']),
  ana=ANA(),ag=('**උක්කුටිකව ගම් අතර යාම**','**Walking among the houses on toes or heels**'),sm=SM_P1))
# 26 pallatthika
B.append(dict(n=26,T='පල්ලත්ථික සික්ඛාපදය || Not Sitting Clasping the Knees',V='දණහිස් බැඳගෙන ගම් අතර හිඳීම || Sitting among the houses clasping the knees',
  K='P1 sd=s an=a anu=0 ved=D',Z=Zs(True),
  story=story('**පල්ලත්ථිකයෙන් (දණහිස් බැඳගෙන)** ගම් අතර හිඳගත්හ','sat among the houses **clasping their knees**'),
  extra=[('පද විවරණය','**පල්ලත්ථිකා** — ==දණහිස් ඔසවා **ඒවා වටා බැඳගෙන** හිඳීම==:\n|! වර්ගය | අර්ථය\n| **හත්ථපල්ලත්ථිකා** | **අත්වලින්** දණහිස් වටා බැඳගෙන\n| **දුස්සපල්ලත්ථිකා** | **රෙද්දකින්** බැඳගෙන — **ආයෝග පටියකින්** බැඳීම ද මෙයට ම අයත් ය (සමන්තපාසාදිකා)\n'+VNOTE[0],
          'Explanation of terms','**Pallatthikā** — ==sitting with knees raised and **bound around**==:\n|! Kind | Meaning\n| **hatthapallatthikā** | holding the knees **with the arms**\n| **dussapallatthikā** | binding them **with a cloth** — binding with **a strap (āyoga)** also counts as this (Samantapāsādikā)\n'+VNOTE[1])],
  off=(['**අනාදරයෙන්** අතින් හෝ රෙද්දෙන් දණහිස් බැඳගෙන ගම් අතර හිඳීම'],['Sitting among the houses clasping the knees with the arms or a cloth **out of disrespect**']),
  ana=ANA([VASU[0]],[VASU[1]]),ag=('**දණහිස් බැඳගෙන ගම් අතර හිඳීම**','**Sitting among the houses clasping the knees**'),sm=SM_P1))
FOODNOTE=('> **භෝජන සම්බන්ධ සේඛිය** මෙතැන් සිට ආරම්භ වේ (සේඛිය 27–56). ඒවා **ගම් අතර පමණක් නොව සෑම තැනම** අදාළ ය.','> **The sekhiyas on food** begin here (sekhiya 27–56). They apply **everywhere, not only among the houses**.')
# 27
B.append(dict(n=27,T='සක්කච්ච පටිග්ගහණ සික්ඛාපදය || Receiving Alms Appreciatively',V='පිණ්ඩපාතය ගෞරවයෙන් තොරව (ඉවත දමනු කැමැත්තෙකු මෙන්) පිළිගැනීම || Receiving almsfood carelessly, as if wanting to throw it away',
  K='P1 sd=s an=a anu=0 ved=D',Z=Zs(False),
  story=story('**ඉවත දමනු කැමැත්තන් මෙන්**, **ගෞරවයෙන් තොරව** පිණ්ඩපාතය පිළිගත්හ','received almsfood **without care, as if wanting to throw it away**'),
  extra=[('පද විවරණය','**සක්කච්චං** — ==**සිහිය එළඹ සිටුවා**== (සතිං උපට්ඨාපෙත්වා) — **ගෞරවයෙන්**.\n**ඡඩ්ඩෙතුකාමො විය** — **ඉවත දමනු කැමැත්තෙකු මෙන්**.\n'+FOODNOTE[0],
          'Explanation of terms','**Sakkaccaṃ** — ==**with mindfulness established**== (satiṃ upaṭṭhāpetvā) — **appreciatively**.\n**Chaḍḍetukāmo viya** — **as if wanting to throw it away**.\n'+FOODNOTE[1])],
  off=(['**අනාදරයෙන්** ඉවත දමනු කැමැත්තෙකු මෙන් පිණ්ඩපාතය පිළිගැනීම'],['Receiving almsfood **out of disrespect**, as if wanting to throw it away']),
  ana=ANA(),ag=('**ගෞරවයෙන් තොරව පිණ්ඩපාතය පිළිගැනීම**','**Receiving almsfood carelessly**'),sm=SM_P1))
# 28
B.append(dict(n=28,T='පත්තසඤ්ඤී පටිග්ගහණ සික්ඛාපදය || Attention on the Bowl when Receiving',V='මෙහෙ අහෙ බලමින් පිණ්ඩපාතය පිළිගැනීම || Receiving almsfood while looking here and there',
  K='P1 sd=s an=a anu=0 ved=D',Z=Zs(False),
  story=story('**මෙහෙ අහෙ බලමින්** පිණ්ඩපාතය පිළිගත්හ; **දායකයන් දමද්දී ද පාත්‍රය පිරී ඉතිරී යද්දී ද නොදැන** සිටියහ','received almsfood **looking here and there**, **not noticing even when food was being given or was overflowing**'),
  extra=[('පද විවරණය','**පත්තසඤ්ඤී** — ==**පාත්‍රයෙහි සංඥාව** ඇති — **තම භාජනයට සිත බැඳ**== (කඞ්ඛාවිතරණී).\n**ආකිරන්තෙපි** — **පිණ්ඩපාතය දෙද්දී පවා** (සමන්තපාසාදිකා).\n**අතික්කන්තෙපි** — **පාත්‍රය ඉක්මවා (ඉතිරී) යද්දී පවා**.',
          'Explanation of terms','**Pattasaññī** — ==with **attention on the bowl** — **the mind fixed on one\'s own vessel**== (Kaṅkhāvitaraṇī).\n**Ākirantepi** — **even while almsfood is being given** (Samantapāsādikā).\n**Atikkantepi** — **even when it overflows the bowl**.')],
  off=(['**අනාදරයෙන්** මෙහෙ අහෙ බලමින් පිණ්ඩපාතය පිළිගැනීම'],['Receiving almsfood looking here and there **out of disrespect**']),
  ana=ANA(),ag=('**පාත්‍රයට සිත නොයොමා පිණ්ඩපාතය පිළිගැනීම**','**Receiving almsfood without attention on the bowl**'),sm=SM_P1))
# 29
B.append(dict(n=29,T='සමසූපක පටිග්ගහණ සික්ඛාපදය || Receiving Curry in Proportion',V='සූපය පමණක් බොහෝ කොට පිළිගැනීම || Receiving too much bean curry',
  K='P1 sd=s an=a anu=0 ved=D',Z='නොසිතා, නොසිහියෙන්, නොදැන; ගිලන්ව; රසරස (අනෙක් ව්‍යඤ්ජන); ඥාතීන්ගෙන් හෝ පවාරණය කළ අයගෙන්; අනෙකෙකු සඳහා; තම ධනයෙන්; ආපදාවල දී; උමතු ආදීන් || Unintentionally, unmindfully, not knowing; ill; other curries; from relatives or those who invited; for another; with one\'s own funds; emergencies; the insane etc.',
  story=story('පිණ්ඩපාතය පිළිගන්නා විට **සූපය ම බොහෝ කොට** පිළිගත්හ','when receiving almsfood, took **a great deal of bean curry**'),
  extra=[('පද විවරණය','**සූපො** — **මුං සූපය** හා **මෑ (මාෂ) සූපය** යන සූප දෙක; ==**කොල්ලු ආදියෙන් කළ සූප ද** මෙයට ඇතුළත් ය== (මහාපච්චරිය).\n**හත්ථහාරියො** — **අතින් ගෙන යා හැකි** (බත සමඟ කලවම් කළ හැකි).\n**සමසූපකො** — ==සූපය **බතෙන් සතරෙන් පංගුවක්** පමණ== වූ පිණ්ඩපාතය. ඊට වැඩියෙන් ගැනීම **දුක්කට** ය.',
          'Explanation of terms','**Sūpo** — the two bean curries: **mung bean** and **black gram**; ==curries of **horse gram** etc. are also included== (Mahāpaccarī).\n**Hatthahāriyo** — **that can be taken up by hand** (mixed with rice).\n**Samasūpako** — almsfood where ==the curry is **about a quarter of the rice**==. Taking more is **dukkaṭa**.'),
         ('රසරස — සීමාවක් නැති ව්‍යඤ්ජන','|! ව්‍යඤ්ජනය | සීමාව\n| **මුං, මෑ, කොල්ලු** ආදී **සූප** | බතෙන් **¼** පමණ\n| **ඕලෝණී, එළවළු (සාක), මාළු හොදි, මස් හොදි** ආදී **රසරස** | **සීමාවක් නැත** — බොහෝ ගැනීම ද අනාපත්ති','Rasarasa — curries without limit','|! Curry | Limit\n| **bean curries** — mung, black gram, horse gram etc. | about **¼** of the rice\n| **rasarasa** — **olonī, vegetable, fish or meat sauces** etc. | **no limit** — taking much is no offence')],
  off=(['**අනාදරයෙන්** බතෙන් ¼ ට වඩා සූපය පිළිගැනීම'],['Receiving more bean curry than a quarter of the rice **out of disrespect**']),
  ana=ANA(['**රසරස** (සූප හැර අනෙක් ව්‍යඤ්ජන) බොහෝ ගැනීම.','**ඥාතීන්ගෙන්** හෝ **පවාරණය කළ අයගෙන්**.','**අනෙකෙකු සඳහා**.','**තම ධනයෙන්** ලැබූ විට.'],['Taking much **rasarasa** (curries other than bean curries).','From **relatives** or **those who have invited**.','**For another**.','When obtained **with one\'s own funds**.']),
  ag=('**සූපය පමණ ඉක්මවා පිළිගැනීම**','**Receiving curry beyond the proportion**'),sm=SM_P1))
# 30
B.append(dict(n=30,T='සමතිත්තික සික්ඛාපදය || Receiving Level with the Rim',V='පාත්‍රයේ මුව දාරය ඉක්මවා ගොඩ ගසා පිණ්ඩපාතය පිළිගැනීම || Receiving almsfood heaped above the rim',
  K='P1 sd=s an=a anu=0 ved=D',Z='නොසිතා, නොසිහියෙන්, නොදැන; ආපදාවල දී; උමතු ආදීන් (ගිලනාට අනාපත්තියක් නැත) || Unintentionally, unmindfully, not knowing; emergencies; the insane etc. (no exemption for illness)',
  story=story('**ගොඩ ගසා (ථූපීකත කොට)** පිණ්ඩපාතය පිළිගත්හ','received almsfood **heaped up**'),
  extra=[('පද විවරණය','**සමතිත්තිකං** — ==**සමව පිරුණු, සමව පිරවූ**== — **අධිෂ්ඨාන කළ හැකි පාත්‍රයක** **මුව ඇතුළත දාර රේඛාව** ඉක්මවා නොගොස් පිරවූ.\n**ථූපීකතං** — **මුව ඇතුළත දාර රේඛාව ඉක්මවා** පාත්‍රයේ දමා **ගොඩ ගසා පිරවූ**.\n**පිණ්ඩපාතං** — ඕනෑම **යාවකාලිකයක්**.\n!dgm: sk-tittika **සමතිත්තික හා ථූපීකත** — පාත්‍රයේ මුව ඇතුළත දාර රේඛාවට සාපේක්ෂව.',
          'Explanation of terms','**Samatittikaṃ** — ==**evenly filled, evenly full**== — filled in **a bowl fit for determination** without going past **the inner rim line**.\n**Thūpīkataṃ** — put in the bowl and **heaped up past the inner rim line**.\n**Piṇḍapātaṃ** — any **food allowed until noon**.\n!dgm: sk-tittika **Level and heaped** — against the inner rim line of the bowl.'),
         ('"ථූපීකත" — ස්ථවිර මත','|! ස්ථවිරයා | මතය\n| **අභය** ස්ථවිර | **භෝජන පසින්** කළ දෙය\n| **තිපිටක චූළනාග** ස්ථවිර | "පිණ්ඩපාතය නම් කැඳ, බත්, කෑම, සුණු පිඬු, **දැහැටි, දසා නූල** ද" යන සූත්‍රය අනුව **දසා නූලක් වුව ද** ගොඩ ගසා නොවටී\n| **චූළසුමන** ස්ථවිර (රෝහණයේ) | "**චූළනාග ශාසනයෙන් පිරිහුණේය**" යි කියා, **යාවකාලිකයෙන්** සීමා වේ යැයි නියම කළේය — මෙය පිළිගත් මතයයි','“Heaped” — the Elders\' views','|! Elder | View\n| Elder **Abhaya** | what is made of **the five foods**\n| Elder **Cūḷanāga**, master of the Tipiṭaka | quoting “almsfood means porridge, rice, snacks, powder-balls, **tooth sticks, fringe threads**,” said **even a fringe thread** may not be heaped\n| Elder **Cūḷasumana** (in Rohaṇa) | said “**Cūḷanāga has strayed from the teaching**,” and ruled that it is limited **by food allowed until noon** — the accepted view'),
         ('ගොඩ ගැසුව ද වටින දේ','|! අවස්ථාව | විනිශ්චය\n| **අධිෂ්ඨාන කළ නොහැකි** භාජනයක | ගොඩ ගැසුව ද වටී\n| **යාමකාලික, සත්තාහකාලික, යාවජීවික** | අධිෂ්ඨාන පාත්‍රයේ වුව ද වටී\n| **පාත්‍ර දෙකක** ගෙන එකක් පුරවා විහාරයට යැවීම | වටී (මහාපච්චරිය)\n| දමද්දී **පහළට බසින** කැවුම්, උක් කැබලි, පලතුරු | ථූපීකත නොවේ\n| **තක්කෝල, වටංසක** ආදිය **උඩින් තබා** දීම | ථූපීකත නොවේ\n| **කොළයක හෝ තැටියක** දමා පාත්‍රය මත තැබීම | ථූපීකත නොවේ','What is allowed even if heaped','|! Situation | Ruling\n| in a vessel **not fit for determination** | allowable even heaped\n| **juice drinks, seven-day tonics, lifetime medicines** | allowable even in the determined bowl\n| receiving in **two bowls**, filling one to send to the monastery | allowable (Mahāpaccarī)\n| cakes, sugarcane pieces, fruit that **sink down** as they are put in | not “heaped”\n| **takkola, vaṭaṃsaka** etc. **placed on top** | not “heaped”\n| put **on a leaf or plate** set on the bowl | not “heaped”'),
         ('ගිලනාට ද අනාපත්තියක් නැත','==මෙහි අනාපත්ති ලැයිස්තුවේ **ගිලානයා සඳහන් නොවේ**; එබැවින් **ගිලනා ද සමතිත්තිකව ම** පිළිගත යුතුය==. සියලු සේඛියවල **ආබාධ හේතුවෙන් අනාපත්ති** වුව ද, **ථූපීකත පිණ්ඩපාතය** (30), **සූප ව්‍යඤ්ජන බතින් වැසීම** (36), **උජ්ඣානසඤ්ඤී** (38) යන **තුනෙහි ගිලානයෙක් නැත**.\n> වරද ඇත්තේ **පිළිගැනීමෙහි** පමණි; **පිළිගත් දෙය මනාව පිළිගත්තක් ම වේ** — වැළඳීම වටී.','No exemption even for the sick','==The no-offence list here **does not mention the sick**; so **even one who is ill must receive it level**==. Though in all sekhiyas there is **no offence on account of illness**, in **three** — **heaped almsfood** (30), **covering curry with rice** (36), **looking critically** (38) — **there is no “ill” exemption**.\n> The fault is only **in receiving**; **what is received is properly received** — it may be eaten.')],
  off=(['**අනාදරයෙන්** මුව ඇතුළත දාර රේඛාව ඉක්මවා ගොඩ ගසා පිණ්ඩපාතය පිළිගැනීම'],['Receiving almsfood heaped past the inner rim line **out of disrespect**']),
  ana=(['**නොසිතා**; **නොසිහියෙන්**; **නොදැන**.','**ආපදාවල** දී.','උමතු ආදීන්ට හා ආදිකම්මිකයාට.'],['**Unintentionally**; **unmindfully**; **not knowing**.','In **emergencies**.','For the insane and so on, and the first offender.']),
  ag=('**ගොඩ ගසා පිණ්ඩපාතය පිළිගැනීම**','**Receiving almsfood heaped up**'),sm=SM_P1))
open('/home/claude/work/content/10d_sk21_30.txt','w').write('\n\n'.join(block(d) for d in B)+'\n')
print(len(B))
