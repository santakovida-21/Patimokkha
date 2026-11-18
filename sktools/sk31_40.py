import sys; sys.path.insert(0,'/home/claude/work/sktools')
from skgen import *
B=[]
Z0='නොසිතා, නොසිහියෙන්, නොදැන; ගිලන්ව; ආපදාවල දී; උමතු ආදීන් || Unintentionally, unmindfully, not knowing; ill; emergencies; the insane etc.'
def R(n,T,V,K,Z,st,extra,off,ana,ag,sm=SM_P1): B.append(dict(n=n,T=T,V=V,K=K,Z=Z,story=st,extra=extra,off=off,ana=ana,ag=ag,sm=sm))
KP='P1 sd=s an=a anu=0 ved=D'
EATNOTE=('> පිළිගැනීම සම්බන්ධ **සේඛිය 27–30** හා **වැළඳීම** සම්බන්ධ **සේඛිය 31–34** යුගල ලෙස පවතී.','> The **receiving** rules (**sekhiya 27–30**) pair with the **eating** rules (**sekhiya 31–34**).')
R(31,'සක්කච්ච භුඤ්ජන සික්ඛාපදය || Eating Appreciatively','පිණ්ඩපාතය ගෞරවයෙන් තොරව (නොවළඳනු කැමැත්තෙකු මෙන්) වැළඳීම || Eating almsfood carelessly, as if unwilling to eat',KP,Z0,
  story('**නොවළඳනු කැමැත්තන් මෙන්**, **ගෞරවයෙන් තොරව** පිණ්ඩපාතය වැළඳූහ','ate almsfood **without care, as if unwilling to eat**'),
  [('පද විවරණය','**සක්කච්චං** — ==**සිහිය එළඹ සිටුවා**== — **ගෞරවයෙන්**.\n**අභුඤ්ජිතුකාමා විය** — **වළඳනු නොකැමැත්තන් මෙන්**.\n'+EATNOTE[0],
    'Explanation of terms','**Sakkaccaṃ** — ==**with mindfulness established**== — **appreciatively**.\n**Abhuñjitukāmā viya** — **as if unwilling to eat**.\n'+EATNOTE[1])],
  (['**අනාදරයෙන්** ගෞරවයෙන් තොරව පිණ්ඩපාතය වැළඳීම'],['Eating almsfood carelessly **out of disrespect**']),ANA(),
  ('**ගෞරවයෙන් තොරව වැළඳීම**','**Eating carelessly**'))
R(32,'පත්තසඤ්ඤී භුඤ්ජන සික්ඛාපදය || Attention on the Bowl when Eating','මෙහෙ අහෙ බලමින් පිණ්ඩපාතය වැළඳීම || Eating almsfood while looking here and there',KP,Z0,
  story('**මෙහෙ අහෙ බලමින්** පිණ්ඩපාතය වැළඳූහ; **තවත් දමද්දී ද ඉතිරී යද්දී ද නොදැන** සිටියහ','ate almsfood **looking here and there**, **not noticing when more was given or when it overflowed**'),
  [('පද විවරණය','**පත්තසඤ්ඤී** — ==**පාත්‍රයෙහි සංඥාව** ඇති — **තම භාජනයට සිත බැඳ**== (කඞ්ඛාවිතරණී).\n**ආකිරන්තෙපි** — **තවත් ආහාර දමද්දී පවා**.\n**අතික්කන්තෙපි** — **පාත්‍රය ඉක්මවා (ඉතිරී) යද්දී පවා**.','Explanation of terms','**Pattasaññī** — ==with **attention on the bowl** — **the mind fixed on one’s own vessel**== (Kaṅkhāvitaraṇī).\n**Ākirantepi** — **even while more food is being put in**.\n**Atikkantepi** — **even when it overflows the bowl**.')],
  (['**අනාදරයෙන්** මෙහෙ අහෙ බලමින් පිණ්ඩපාතය වැළඳීම'],['Eating almsfood looking here and there **out of disrespect**']),ANA(),
  ('**පාත්‍රයට සිත නොයොමා වැළඳීම**','**Eating without attention on the bowl**'))
R(33,'සපදාන සික්ඛාපදය || Eating in Order','පාත්‍රයේ මෙතැනින් එතැනින් හාරමින් වැළඳීම || Eating by picking here and there in the bowl',KP,
  'නොසිතා, නොසිහියෙන්, නොදැන; ගිලන්ව; අනුන්ට දෙමින් හෝ අනුන්ගේ භාජනයට දමමින් හාරීම; උත්තරිභංගය (ව්‍යඤ්ජන) පිළිවෙළ නොතකා ගැනීම; ආපදාවල දී; උමතු ආදීන් || Unintentionally, unmindfully, not knowing; ill; picking while giving to others or putting into another\'s vessel; taking side dishes out of order; emergencies; the insane etc.',
  story('**මෙතැනින් එතැනින් හාරමින් (ඔමසමින්)** පිණ්ඩපාතය වැළඳූහ','ate almsfood **picking at it here and there**'),
  [('පද විවරණය','**සපදානං** — ==**මෙතැන එතැන සීමා නොකොට, අනුපිළිවෙළින්**== (පාත්‍රයේ එක් පසෙක සිට පිළිවෙළින්).\n**ඔමසිත්වා** — **මෙතැනින් එතැනින් හාරා, අතගා**.\n**උත්තරිභඞ්ගං** — බත සමඟ ගන්නා **ව්‍යඤ්ජන ආදිය**; ඒවා **පිළිවෙළ නොතකා** ගැනීම ද **අනාපත්ති** ය (කඞ්ඛාවිතරණී).',
    'Explanation of terms','**Sapadānaṃ** — ==**in order, without picking a spot here and there**== (working through the bowl from one side).\n**Omasitvā** — **digging and poking here and there**.\n**Uttaribhaṅgaṃ** — **side dishes** taken with the rice; taking these **out of order** is also **no offence** (Kaṅkhāvitaraṇī).')],
  (['**අනාදරයෙන්** මෙතැනින් එතැනින් හාරමින් පිණ්ඩපාතය වැළඳීම'],['Eating almsfood picking here and there **out of disrespect**']),
  ANA(['**අනුන්ට දෙමින්** හෝ **අනුන්ගේ භාජනයට දමමින්** හාරීම.','**උත්තරිභංගය** පිළිවෙළ නොතකා ගැනීම.'],['Picking **while giving to others** or **putting it into another\'s vessel**.','Taking **side dishes** out of order.']),
  ('**පිළිවෙළ නොතකා හාරමින් වැළඳීම**','**Eating by picking out of order**'))
R(34,'සමසූපක භුඤ්ජන සික්ඛාපදය || Eating Curry in Proportion','සූපය පමණක් බොහෝ කොට වැළඳීම || Eating too much bean curry',KP,
  'නොසිතා, නොසිහියෙන්, නොදැන; ගිලන්ව; රසරස (අනෙක් ව්‍යඤ්ජන); ඥාතීන්ගෙන් හෝ පවාරණය කළ අයගෙන්; තම ධනයෙන්; ආපදාවල දී; උමතු ආදීන් || Unintentionally, unmindfully, not knowing; ill; other curries; from relatives or those who invited; with one\'s own funds; emergencies; the insane etc.',
  story('පිණ්ඩපාතය වළඳන විට **සූපය ම බොහෝ කොට** වැළඳූහ','when eating almsfood, ate **a great deal of bean curry**'),
  [('පද විවරණය','**සූපො** — **මුං සූපය** හා **මෑ (මාෂ) සූපය** යන සූප දෙක; ==**කොල්ලු ආදියෙන් කළ සූප ද** මෙයට ඇතුළත් ය== (මහාපච්චරිය).\n**හත්ථහාරියො** — **අතින් ගෙන යා හැකි** (බත සමඟ කලවම් කළ හැකි).\n**සමසූපකො** — ==සූපය **බතෙන් සතරෙන් පංගුවක්** පමණ== වූ පිණ්ඩපාතය. ඊට වැඩියෙන් වැළඳීම **දුක්කට** ය.\n|! ව්‍යඤ්ජනය | සීමාව\n| **මුං, මෑ, කොල්ලු** ආදී **සූප** | බතෙන් **¼** පමණ\n| **ඕලෝණී, එළවළු (සාක), මාළු හොදි, මස් හොදි** ආදී **රසරස** | **සීමාවක් නැත** — බොහෝ වැළඳීම ද අනාපත්ති\n> පාළියේ මෙහි අනාපත්ති ලැයිස්තුවේ **"අනෙකෙකු සඳහා" නැත** (සේඛිය 29 හි ඇත).',
    'Explanation of terms','**Sūpo** — the two bean curries: **mung bean** and **black gram**; ==curries of **horse gram** etc. are also included== (Mahāpaccarī).\n**Hatthahāriyo** — **that can be taken up by hand** (mixed with rice).\n**Samasūpako** — almsfood where ==the curry is **about a quarter of the rice**==. Eating more is **dukkaṭa**.\n|! Curry | Limit\n| **bean curries** — mung, black gram, horse gram etc. | about **¼** of the rice\n| **rasarasa** — **olonī, vegetable, fish or meat sauces** etc. | **no limit** — eating much is no offence\n> In the Pāli the no-offence list here **lacks “for another”** (which sekhiya 29 has).')],
  (['**අනාදරයෙන්** බතෙන් ¼ ට වඩා සූපය වැළඳීම'],['Eating more bean curry than a quarter of the rice **out of disrespect**']),
  ANA(['**රසරස** බොහෝ වැළඳීම.','**ඥාතීන්ගෙන්** හෝ **පවාරණය කළ අයගෙන්**.','**තම ධනයෙන්** ලැබූ විට.'],['Eating much **rasarasa**.','From **relatives** or **those who have invited**.','When obtained **with one\'s own funds**.']),
  ('**සූපය පමණ ඉක්මවා වැළඳීම**','**Eating curry beyond the proportion**'))
R(35,'ථූපකත සික්ඛාපදය || Not Eating from the Top','පිණ්ඩපාතය මුදුනින් / මැදින් මඩිමින් වැළඳීම || Eating almsfood by pressing it down from the top',KP,
  'නොසිතා, නොසිහියෙන්, නොදැන; ගිලන්ව; ඉතිරිය ස්වල්පයක් වූ විට එක් තැනකට එකතු කොට මඩා වැළඳීම; ආපදාවල දී; උමතු ආදීන් || Unintentionally, unmindfully, not knowing; ill; gathering and pressing together a small remainder; emergencies; the insane etc.',
  story('**මුදුනින් මඩිමින් (ථූපකතො ඔමද්දිත්වා)** පිණ්ඩපාතය වැළඳූහ','ate almsfood **pressing it down from the top**'),
  [('පද විවරණය','**ථූපකතො** — ==**මුදුනින්**; එනම් **මැද සිට**==.\n**ඔමද්දිත්වා** — **මඩා, තද කොට**.\n**පරිත්තකෙ සෙසෙ** — ==පාත්‍රයේ **ඉතිරිය ස්වල්පයක්** වූ විට **එක් තැනකට එකතු කොට මඩා** වැළඳීම **අනාපත්ති** ය==.',
    'Explanation of terms','**Thūpakato** — ==**from the top**, i.e. **from the middle**==.\n**Omadditvā** — **pressing, squashing it down**.\n**Parittake sese** — ==when **only a little is left**, **gathering it together and pressing it** to eat is **no offence**==.')],
  (['**අනාදරයෙන්** මුදුනින් මඩිමින් පිණ්ඩපාතය වැළඳීම'],['Eating almsfood pressing it down from the top **out of disrespect**']),
  ANA(['**ඉතිරිය ස්වල්පයක්** වූ විට එකතු කොට මඩා වැළඳීම.'],['Gathering and pressing together **a small remainder**.']),
  ('**මුදුනින් මඩිමින් වැළඳීම**','**Eating by pressing down from the top**'))
R(36,'ඔදනප්පටිච්ඡාදන සික්ඛාපදය || Not Hiding Curry with Rice','තවත් ලැබීමේ කැමැත්තෙන් සූපය / ව්‍යඤ්ජනය බතින් වැසීම || Covering curry with rice, wanting more',KP,
  'නොසිතා, නොසිහියෙන්, නොදැන; දායකයන් ම වසා දීම; තවත් ලැබීමේ කැමැත්තක් නැතිව වැසීම; ආපදාවල දී; උමතු ආදීන් (ගිලනාට අනාපත්තියක් නැත) || Unintentionally, unmindfully, not knowing; the donors give it covered; covering without wanting more; emergencies; the insane etc. (no exemption for illness)',
  story('**තවත් ලැබීමේ කැමැත්තෙන්** සූපය ද ව්‍යඤ්ජනය ද **බතින් වසා** සැඟවූහ','**covered** their curries and side dishes **with rice**, **wanting more**'),
  [('පද විවරණය','**භිය්‍යොකම්‍යතං උපාදාය** — ==**තවත් ලැබීමේ කැමැත්ත** නිසා== — "**ව්‍යඤ්ජනය නැති යැයි සිතා තවත් දෙනු ඇත**" යි.\n**සාමිකා පටිච්ඡාදෙත්වා දෙන්ති** — ==**මාඝාත සමයාදියෙහි** (සතුන් මැරීම තහනම් කාලවල)== දායකයන් ම ව්‍යඤ්ජනය **සඟවා** දීම — අනාපත්ති.',
    'Explanation of terms','**Bhiyyokamyataṃ upādāya** — ==**out of wanting more**== — thinking, “**They’ll think I have no curry and give more**.”\n**Sāmikā paṭicchādetvā denti** — when ==**at times of a ban on slaughter** (māghāta) and the like== the donors themselves give the curry **hidden** — no offence.'),
   ('ගිලනාට ද අනාපත්තියක් නැත','==මෙහි අනාපත්ති ලැයිස්තුවේ **ගිලානයා සඳහන් නොවන බැවින් ගිලනාට ද ඇවැත් ම ය**== (කඞ්ඛාවිතරණී). ගිලන් අනාපත්තිය නැති සේඛිය තුනෙන් එකකි (**30, 36, 38**).','No exemption even for the sick','==Since **the sick are not mentioned** in the no-offence list, **even one who is ill commits the offence**== (Kaṅkhāvitaraṇī). It is one of the three sekhiyas without the illness exemption (**30, 36, 38**).')],
  (['**අනාදරයෙන්**, තවත් ලැබීමේ කැමැත්තෙන් සූපය / ව්‍යඤ්ජනය බතින් වැසීම'],['Covering curry or side dishes with rice, wanting more, **out of disrespect**']),
  (['**නොසිතා**; **නොසිහියෙන්**; **නොදැන**.','**දායකයන් ම වසා** දෙන විට.','**තවත් ලැබීමේ කැමැත්තක් නැතිව** වැසීම.','**ආපදාවල** දී.','උමතු ආදීන්ට හා ආදිකම්මිකයාට.'],['**Unintentionally**; **unmindfully**; **not knowing**.','When **the donors give it covered**.','Covering it **without wanting more**.','In **emergencies**.','For the insane and so on, and the first offender.']),
  ('**තවත් ලැබීමේ කැමැත්තෙන් බතින් වැසීම**','**Covering with rice wanting more**'))
R(37,'සූපෝදනවිඤ්ඤත්ති සික්ඛාපදය || Not Asking for Curry or Rice','නොගිලන්ව තමා සඳහා සූප / බත් ඉල්ලා වැළඳීම || Asking for curry or rice for oneself when not ill',
  'TS vj=L cit=A ved=D sd=s an=a anu=1',
  'නොසිතා, නොසිහියෙන්, නොදැන; ගිලන්ව; ඥාතීන්ගෙන් හෝ පවාරණය කළ අයගෙන්; අනෙකෙකු සඳහා; තම ධනයෙන්; ආපදාවල දී; උමතු ආදීන් || Unintentionally, unmindfully, not knowing; ill; from relatives or those who invited; for another; with one\'s own funds; emergencies; the insane etc.',
  ('**ෂඩ්වර්ගීය භික්ෂූහු** ==**තමන් සඳහා සූප ද බත් ද ඉල්ලා** වැළඳූහ==. මිනිස්සු ==**"කාට නම් සම්පන්න දේ අමනාප ද? කාට නම් මිහිරි දේ අරුචි ද?"**== යි දොස් කීහ. භාග්‍යවතුන් වහන්සේ ශික්ෂාපදය පැනවූහ.\n**අනුප්‍රඥප්තිය:** **ගිලන් භික්ෂූහු** "**පෙර අපි සූප බත් ඉල්ලා වැළඳුවෙමු; දැන් කුකුසින් නොඉල්ලන නිසා අපහසු ය**" යි කීහ. භාග්‍යවතුන් වහන්සේ "**නොගිලන්**" යන්න එක් කළහ.',
   '**The group-of-six** ==**asked for curry and rice for themselves** and ate them==. People complained: ==“**Who doesn’t like what is fine? Who doesn’t enjoy what is tasty?**”== The Blessed One laid down the rule.\n**The amendment:** **sick monks** said, “**We used to ask for curry and rice and were comfortable; now, out of scruple, we don’t ask and are uncomfortable.**” The Blessed One added “**not ill**.”'),
  [('පද විවරණය හා සමාන ශික්ෂාපද','**විඤ්ඤාපෙත්වා** — **ඉල්ලා**.\n**අගිලානො** — නොගිලන් තැනැත්තා.\n|! ඉල්ලන දෙය | ශික්ෂාපදය | ඇවැත\n| ගිතෙල් ආදී **ප්‍රණීත භෝජන නවය** (නොගිලන්ව) | පාචිත්තිය 39 | PC\n| **සූප හෝ බත්** (නොගිලන්ව) | **සේඛිය 37** | DK\n> සමන්තපාසාදිකාව අනුව **සූපෝදන විඤ්ඤත්තියේ** භික්ෂු භික්ෂුණී **දෙපිරිසට ම සේඛිය දුක්කට** ය.',
    'Explanation of terms and related rules','**Viññāpetvā** — **having asked**.\n**Agilāno** — one not ill.\n|! What is asked for | Rule | Offence\n| the **nine fine foods** such as ghee (not ill) | pācittiya 39 | PC\n| **curry or rice** (not ill) | **sekhiya 37** | DK\n> Per the Samantapāsādikā, **asking for curry and rice** is **a sekhiya dukkaṭa for both monks and nuns**.')],
  (['**අනාදරයෙන්**, නොගිලන්ව තමා සඳහා සූප / බත් ඉල්ලා වැළඳීම'],['Asking for curry or rice for oneself when not ill and eating it, **out of disrespect**']),
  ANA(['**ඥාතීන්ගෙන්** හෝ **පවාරණය කළ අයගෙන්**.','**අනෙකෙකු සඳහා**.','**තම ධනයෙන්** ලැබීම.'],['From **relatives** or **those who have invited**.','**For another**.','Obtained **with one\'s own funds**.']),
  ('**නොගිලන්ව තමා සඳහා සූප / බත් ඉල්ලා වැළඳීම**','**Asking for curry or rice for oneself when not ill**'),sm=SM_TS)
R(38,'උජ්ඣානසඤ්ඤී සික්ඛාපදය || Not Looking at Others\' Bowls Critically','දොස් සොයන අදහසින් අනුන්ගේ පාත්‍රය බැලීම || Looking at others\' bowls with intent to find fault',KP,
  'නොසිතා, නොසිහියෙන්, නොදැන; "දෙන්නෙමි" හෝ "දෙවන්නෙමි" යි බැලීම; දොස් සොයන අදහසක් නැතිව; ආපදාවල දී; උමතු ආදීන් (ගිලනාට අනාපත්තියක් නැත) || Unintentionally, unmindfully, not knowing; looking with the thought “I’ll give” or “I’ll have it given”; without intent to find fault; emergencies; the insane etc. (no exemption for illness)',
  story('**දොස් සොයන අදහසින්** අනුන්ගේ පාත්‍රය බැලූහ','looked at others\' bowls **with intent to find fault**'),
  [('පද විවරණය','**උජ්ඣානසඤ්ඤී** — ==**දොස් සෙවීමේ (උජ්ඣාන) සංඥාව** ඇති==.\n**"දස්සාමී"ති වා "දාපෙස්සාමී"ති වා** — **"මම දෙන්නෙමි"** හෝ **"දෙවන්නෙමි"** යි අනුන්ගේ පාත්‍රය බැලීම **අනාපත්ති** ය.\n==මෙහි ද **ගිලනා නොමිදේ**== — ගිලන් අනාපත්තිය නැති සේඛිය තුනෙන් එකකි (**30, 36, 38**).',
    'Explanation of terms','**Ujjhānasaññī** — ==with **the perception of finding fault**==.\n**“Dassāmī”ti vā “dāpessāmī”ti vā** — looking at another\'s bowl thinking **“I’ll give”** or **“I’ll have it given”** is **no offence**.\n==Here too **the sick are not released**== — one of the three sekhiyas without the illness exemption (**30, 36, 38**).')],
  (['**අනාදරයෙන්**, දොස් සොයන අදහසින් අනුන්ගේ පාත්‍රය බැලීම'],['Looking at another\'s bowl with intent to find fault **out of disrespect**']),
  (['**නොසිතා**; **නොසිහියෙන්**; **නොදැන**.','"**දෙන්නෙමි**" හෝ "**දෙවන්නෙමි**" යි බැලීම.','**දොස් සොයන අදහසක් නැති** අයට.','**ආපදාවල** දී.','උමතු ආදීන්ට හා ආදිකම්මිකයාට.'],['**Unintentionally**; **unmindfully**; **not knowing**.','Looking with the thought “**I’ll give**” or “**I’ll have it given**.”','For one **without intent to find fault**.','In **emergencies**.','For the insane and so on, and the first offender.']),
  ('**දොස් සොයන අදහසින් අනුන්ගේ පාත්‍රය බැලීම**','**Looking at another\'s bowl to find fault**'))
R(39,'කබළ සික්ඛාපදය || Not Too Large a Mouthful','ඉතා විශාල බත් පිඩක් කිරීම || Making too large a mouthful',KP,
  'නොසිතා, නොසිහියෙන්, නොදැන; ගිලන්ව; කැවිලි (මුල් ආදී කෑ යුතු දේ); පලතුරු; උත්තරිභංගය; ආපදාවල දී; උමතු ආදීන් || Unintentionally, unmindfully, not knowing; ill; snacks (roots etc.); fruit; side dishes; emergencies; the insane etc.',
  story('**ඉතා විශාල බත් පිඩු (කබළ)** කළහ','made **very large mouthfuls**'),
  [('පද විවරණය','**නාතිමහන්තං කබළං** — ==**මොනර බිත්තරය** ඉතා විශාල ය, **කුකුළු බිත්තරය** ඉතා කුඩා ය; **ඒ දෙක අතර ප්‍රමාණය**==.\n|! ප්‍රමාණය | විනිශ්චය\n| මොනර බිත්තරයක් තරම් | ඉතා විශාල — DK\n| මොනර හා කුකුළු බිත්තර අතර | සුදුසු\n| **මුල් ආදී කැවිලි (ඛජ්ජක), පලතුරු, උත්තරිභංගය** | සීමාවක් නැත — අනාපත්ති',
    'Explanation of terms','**Nātimahantaṃ kabaḷaṃ** — ==**a peacock’s egg** is too large, **a hen’s egg** too small; **a size between the two**==.\n|! Size | Ruling\n| as big as a peacock’s egg | too large — DK\n| between a peacock’s and a hen’s egg | proper\n| **snacks such as roots (khajjaka), fruit, side dishes** | no limit — no offence')],
  (['**අනාදරයෙන්** ඉතා විශාල බත් පිඩක් කිරීම'],['Making too large a mouthful **out of disrespect**']),
  ANA(['**කැවිලි** (මුල් ආදී කෑ යුතු දේ), **පලතුරු**, **උත්තරිභංගය**.'],['**Snacks** (roots and other chewables), **fruit**, **side dishes**.']),
  ('**ඉතා විශාල බත් පිඩක් කිරීම**','**Making too large a mouthful**'))
R(40,'ආලෝප සික්ඛාපදය || Round Mouthfuls','දිග් වූ බත් පිඩු කිරීම || Making long mouthfuls',KP,
  'නොසිතා, නොසිහියෙන්, නොදැන; ගිලන්ව; කැවිලි, පලතුරු සමඟ උත්තරිභංගය; ආපදාවල දී; උමතු ආදීන් || Unintentionally, unmindfully, not knowing; ill; side dishes with snacks and fruit; emergencies; the insane etc.',
  story('**දිග් වූ බත් පිඩු (ආලෝප)** කළහ','made **long mouthfuls**'),
  [('පද විවරණය','**පරිමණ්ඩලං ආලොපං** — ==**දිග් නොවූ (වටකුරු)** බත් පිඩ==.\n**ඛජ්ජක, ඵලාඵල සමඟ උත්තරිභංගය** — මෙහි ද **අනාපත්ති** ය (කඞ්ඛාවිතරණී).',
    'Explanation of terms','**Parimaṇḍalaṃ ālopaṃ** — ==a mouthful **not long (round)**==.\n**Side dishes with snacks and fruit** — here too **no offence** (Kaṅkhāvitaraṇī).')],
  (['**අනාදරයෙන්** දිග් වූ බත් පිඩු කිරීම'],['Making long mouthfuls **out of disrespect**']),
  ANA(['**කැවිලි, පලතුරු** සමඟ **උත්තරිභංගය**.'],['**Side dishes** with **snacks and fruit**.']),
  ('**දිග් වූ බත් පිඩු කිරීම**','**Making long mouthfuls**'))
open('/home/claude/work/content/10e_sk31_40.txt','w').write('\n\n'.join(block(d) for d in B)+'\n')
print(len(B))
