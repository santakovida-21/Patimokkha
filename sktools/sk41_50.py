import sys; sys.path.insert(0,'/home/claude/work/sktools')
from skgen import *
B=[]
KP='P1 sd=s an=a anu=0 ved=D'
def Zx(si='',en=''):
    return f'නොසිතා, නොසිහියෙන්, නොදැන; ගිලන්ව; {si+"; " if si else ""}ආපදාවල දී; උමතු ආදීන් || Unintentionally, unmindfully, not knowing; ill; {en+"; " if en else ""}emergencies; the insane etc.'
def R(n,T,V,st_si,st_en,ex_si,ex_en,off_si,off_en,ag_si,ag_en,ana_si=(),ana_en=(),K=KP,sm=SM_P1,extra2=()):
    B.append(dict(n=n,T=T,V=V,K=K,Z=Zx('; '.join(x.replace('**','').rstrip('.') for x in ana_si),'; '.join((lambda y:y[:1].lower()+y[1:])(x.replace('**','').rstrip('.')) for x in ana_en)),
      story=story(st_si,st_en),extra=[('පද විවරණය',ex_si,'Explanation of terms',ex_en)]+list(extra2),
      off=([f'**අනාදරයෙන්** {off_si}'],[f'{off_en} **out of disrespect**']),ana=ANA(list(ana_si),list(ana_en)),ag=(ag_si,ag_en),sm=sm))
R(41,'අනාහට සික්ඛාපදය || Not Opening the Mouth Early','බත් පිඩ මුඛය වෙත නොපැමිණියදී ම කට ඇරීම || Opening the mouth before the mouthful is brought to it',
  '**බත් පිඩ මුඛය වෙත නොපැමිණියදී ම** කට ඇරියහ','opened their mouths **before the mouthful was brought up**',
  '**අනාහටෙ** — ==**ගෙන නොආ**; එනම් **මුඛ දොරටුවට නොපැමිණි**== (බත් පිඩ).\n**මුඛද්වාරං විවරති** — **කට අරියි**.','**Anāhaṭe** — ==**not yet brought**, i.e. **not yet reached the mouth**== (the mouthful).\n**Mukhadvāraṃ vivarati** — **opens the mouth**.',
  'බත් පිඩ මුඛයට නොපැමිණියදී කට ඇරීම','Opening the mouth before the mouthful arrives','**බත් පිඩ නොපැමිණියදී කට ඇරීම**','**Opening the mouth before the mouthful arrives**')
R(42,'සබ්බහත්ථ සික්ඛාපදය || Not Putting the Whole Hand in the Mouth','වළඳන අතර මුළු අත ම කටට දැමීම || Putting the whole hand into the mouth while eating',
  'වළඳන අතර **මුළු අත ම කටට** දැමූහ','put **the whole hand into the mouth** while eating',
  '**සබ්බං හත්ථං** — ==**මුළු අත ම** (සකල හස්තය)==.','**Sabbaṃ hatthaṃ** — ==**the whole hand**==.',
  'වළඳන අතර මුළු අත කටට දැමීම','Putting the whole hand into the mouth while eating','**මුළු අත කටට දැමීම**','**Putting the whole hand into the mouth**')
R(43,'සකබළ සික්ඛාපදය || Not Speaking with the Mouth Full','කටේ බත් පිඩ ඇතිව කථා කිරීම || Speaking with food in the mouth',
  '**කටේ බත් පිඩ ඇතිව** කථා කළහ','spoke **with food in their mouths**',
  '**සකබළෙන මුඛෙන** — ==**වචනය අසම්පූර්ණ වන තරමට** කටේ ආහාර ඇතිව කථා කරන්නාට ඇවැත==.\n**ධර්ම දේශනා කරද්දී** **අරළු** හෝ **වැල්මී** ආදියක් කටේ දමාගෙන කථා කරයි නම්, **වචනය අසම්පූර්ණ නොවන තරමක්** කටේ ඇති විට **කථා කිරීම වටී** (සමන්තපාසාදිකා, කඞ්ඛාවිතරණී).',
  '**Sakabaḷena mukhena** — ==the offence is for speaking **with so much food in the mouth that the words are incomplete**==.\nIf, **while teaching Dhamma**, one has **myrobalan** or **liquorice** in the mouth, it is **allowable to speak** as long as **there is not so much that the words become unclear** (Samantapāsādikā, Kaṅkhāvitaraṇī).',
  'වචනය අසම්පූර්ණ වන සේ කටේ ආහාර ඇතිව කථා කිරීම','Speaking with so much food in the mouth that the words are unclear','**කටේ ආහාර ඇතිව කථා කිරීම**','**Speaking with food in the mouth**',K='SB kr=K sd=s an=a anu=0',sm=SM_SB)
R(44,'පිණ්ඩුක්ඛේපක සික්ඛාපදය || Not Tossing Food into the Mouth','බත් පිඩ ඔසවා ඔසවා (උඩ දමා) කටට දැමීම || Eating by tossing lumps of food into the mouth',
  '**බත් පිඩු උඩ දමමින්** වැළඳූහ','ate **tossing lumps of food up into their mouths**',
  '**පිණ්ඩුක්ඛෙපකං** — ==**පිඩ ඔසවා ඔසවා** (උඩට විසි කොට) කටට දමමින්==.\n**ඛජ්ජක, ඵලාඵල** — කැවිලි, පලතුරු සඳහා **අනාපත්ති** ය.','**Piṇḍukkhepakaṃ** — ==**tossing lumps up again and again** into the mouth==.\n**Khajjaka, phalāphala** — for snacks and fruit, **no offence**.',
  'පිඩු උඩ දමමින් වැළඳීම','Eating by tossing lumps into the mouth','**පිඩු උඩ දමමින් වැළඳීම**','**Eating by tossing lumps into the mouth**',
  ['**කැවිලි** (ඛජ්ජක).','**පලතුරු**.'],['**Snacks** (khajjaka).','**Fruit**.'])
R(45,'කබළාවච්ඡේදක සික්ඛාපදය || Not Biting off Mouthfuls','බත් පිඩ කොටස් කොටස් කොට සපා කමින් වැළඳීම || Eating by biting off pieces of a mouthful',
  '**බත් පිඩ කඩමින් (සපා කමින්)** වැළඳූහ','ate **biting pieces off their mouthfuls**',
  '**කබළාවච්ඡෙදකං** — ==**පිඩ කඩා කඩා**== (අඩක් කටට දමා අඩක් අතේ තබා) වැළඳීම.\n**කැවිලි, පලතුරු සමඟ උත්තරිභංගය** ද **අනාපත්ති** ය.','**Kabaḷāvacchedakaṃ** — ==eating by **biting off pieces of the mouthful**== (half in the mouth, half in the hand).\n**Side dishes along with snacks and fruit** are also **no offence**.',
  'පිඩ කඩමින් වැළඳීම','Eating by biting off pieces of a mouthful','**පිඩ කඩමින් වැළඳීම**','**Eating by biting off pieces of a mouthful**',
  ['**කැවිලි, පලතුරු**.','**උත්තරිභංගය**.'],['**Snacks, fruit**.','**Side dishes**.'])
R(46,'අවගණ්ඩකාරක සික්ඛාපදය || Not Stuffing the Cheeks','වඳුරෙකු මෙන් කම්මුල් පුරවා වැළඳීම || Eating with the cheeks stuffed like a monkey',
  '**වඳුරන් මෙන් කම්මුල් පුරවමින්** වැළඳූහ','ate **stuffing their cheeks like monkeys**',
  '**අවගණ්ඩකාරකං** — ==**වඳුරෙකු මෙන් කම්මුල් (ගණ්ඩ) කර කර**==.\n**එකතො වා උභතො වා** — **එක් කම්මුලක් හෝ දෙක ම** පුරවා.\n**ඵලාඵල** — **පලතුරු පමණක්** සඳහා **අනාපත්ති** ය.','**Avagaṇḍakārakaṃ** — ==**making cheek-pouches like a monkey**==.\n**Ekato vā ubhato vā** — stuffing **one cheek or both**.\n**Phalāphala** — **for fruit only**, **no offence**.',
  'එක් කම්මුලක් හෝ දෙක පුරවා වැළඳීම','Eating with one or both cheeks stuffed','**කම්මුල් පුරවා වැළඳීම**','**Eating with the cheeks stuffed**',
  ['**පලතුරු** පමණක්.'],['**Fruit** only.'])
R(47,'හත්ථනිද්ධුනක සික්ඛාපදය || Not Shaking the Hand','අත ගසමින් (සොලවමින්) වැළඳීම || Eating while shaking the hand',
  '**අත ගසමින්** වැළඳූහ','ate **shaking their hands**',
  '**හත්ථනිද්ධුනකං** — ==**අත ගසා ගසා (සොලවා සොලවා)**== වැළඳීම.\n**කචවරං ඡඩ්ඩෙන්තො** — **කුණු (කසළ) ඉවත දමන්නට** අත ගැසීම **අනාපත්ති** ය.','**Hatthaniddhunakaṃ** — ==eating **shaking the hand again and again**==.\n**Kacavaraṃ chaḍḍento** — shaking the hand **to get rid of dirt** is **no offence**.',
  'අත ගසමින් වැළඳීම','Eating while shaking the hand','**අත ගසමින් වැළඳීම**','**Eating while shaking the hand**',
  ['**කසළ ඉවත දමන්නට** අත ගැසීම.'],['Shaking the hand **to get rid of dirt**.'])
R(48,'සිත්ථාවකාරක සික්ඛාපදය || Not Scattering Rice','බත් ඇට විසුරුවමින් වැළඳීම || Eating while scattering grains of rice',
  '**බත් ඇට විසුරුවමින්** වැළඳූහ','ate **scattering grains of rice**',
  '**සිත්ථාවකාරකං** — ==**බත් ඇට (සිත්ථ) විසුරුවා විසුරුවා**== වැළඳීම.\n**කචවරං ඡඩ්ඩෙන්තො** — **කසළ ඉවත දමද්දී** බත් ඇටයක් ද ඉවත යාම **අනාපත්ති** ය.','**Sitthāvakārakaṃ** — ==eating **scattering grains of rice**==.\n**Kacavaraṃ chaḍḍento** — when **removing dirt** a grain goes with it: **no offence**.',
  'බත් ඇට විසුරුවමින් වැළඳීම','Eating while scattering rice','**බත් ඇට විසුරුවමින් වැළඳීම**','**Eating while scattering rice**',
  ['**කසළ ඉවත දමද්දී** බත් ඇටයක් ඉවත යාම.'],['A grain going out **when removing dirt**.'])
R(49,'ජිව්හානිච්ඡාරක සික්ඛාපදය || Not Sticking out the Tongue','දිව දිගු කරමින් වැළඳීම || Eating while sticking out the tongue',
  '**දිව දිගු කරමින් (එළියට දමමින්)** වැළඳූහ','ate **sticking out their tongues**',
  '**ජිව්හානිච්ඡාරකං** — ==**දිව එළියට දමා දමා**== (දිවෙන් ලෙවකමින්) වැළඳීම.','**Jivhānicchārakaṃ** — ==eating **sticking the tongue out again and again**== (licking).',
  'දිව දිගු කරමින් වැළඳීම','Eating while sticking out the tongue','**දිව දිගු කරමින් වැළඳීම**','**Eating while sticking out the tongue**')
R(50,'චපුචපුකාරක සික්ඛාපදය || Not Smacking the Lips','"චපු චපු" යන හඬ නගමින් වැළඳීම || Eating with a smacking sound',
  '**"චපු චපු" යන හඬ නගමින්** වැළඳූහ','ate **making a smacking “capu capu” sound**',
  '**චපුචපුකාරකං** — ==**"චපු චපු" යන හඬ කර කර**== වැළඳීම.\n> ඊළඟ **සුරුසුරු** (සේඛිය 51) ශික්ෂාපදය ද මේ ක්‍රමය ම ය.','**Capucapukārakaṃ** — ==eating **making the sound “capu capu”**==.\n> The next rule, **slurping** (sekhiya 51), follows the same pattern.',
  '"චපු චපු" හඬ නගමින් වැළඳීම','Eating with a smacking sound','**චපු චපු හඬ නගමින් වැළඳීම**','**Eating with a smacking sound**')
open('/home/claude/work/content/10f_sk41_50.txt','w').write('\n\n'.join(block(d) for d in B)+'\n')
print(len(B))
