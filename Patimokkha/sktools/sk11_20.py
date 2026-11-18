import sys; sys.path.insert(0,'/home/claude/work/sktools')
from skgen import *
B=[]
LAUGH_SI='**උජ්ජග්ඝිකාය** — **මහා හඬින් සිනාසෙමින්** (ඉත්ථම්භූත ලක්ෂණයෙහි කරණ විභක්තිය).\n**හසනීයස්මිං වත්ථුස්මිං මිහිතමත්තං** — ==**සිනා උපදවන කරුණක** දී **සිනහවක් (මඳ සිනාවක්) පමණක්** පෑම **අනාපත්ති** ය==.'
LAUGH_EN='**Ujjagghikāya** — **laughing loudly** (instrumental of manner).\n**Hasanīyasmiṃ vatthusmiṃ mihitamattaṃ** — ==merely **smiling** at **something funny** is **no offence**==.'
for n,g in ((11,True),(12,False)):
    si_v='ගම් අතර යාම' if g else 'ගම් අතර හිඳීම'; en_v='going among the houses' if g else 'sitting among the houses'
    B.append(dict(n=n,T=('උජ්ජග්ඝික ගමන සික්ඛාපදය || Not Going Laughing Loudly' if g else 'උජ්ජග්ඝික නිසීදන සික්ඛාපදය || Not Sitting Laughing Loudly'),
      V=f'මහ හඬින් සිනාසෙමින් {si_v} || Laughing loudly while {en_v}',K='SB kr=K sd=s an=a anu=0',
      Z='නොසිතා, නොසිහියෙන්, නොදැන; ගිලන්ව; සිනා උපදවන කරුණක සිනහවක් පමණක් පෑම; ආපදාවල දී; උමතු ආදීන් || Unintentionally, unmindfully, not knowing; ill; merely smiling at something funny; emergencies; the insane etc.',
      story=story(f'**මහ හඬින් සිනාසෙමින්** {"ගම් අතර ගියහ" if g else "ගම් අතර හිඳගත්හ"}',f'{"went" if g else "sat"} among the houses **laughing loudly**'),
      extra=[('පද විවරණය',LAUGH_SI,'Explanation of terms',LAUGH_EN)],
      off=([f'**අනාදරයෙන්** මහ හඬින් සිනාසෙමින් {si_v}'],[f'{en_v.capitalize()} laughing loudly **out of disrespect**']),
      ana=ANA(['**සිනා උපදවන කරුණක** දී **සිනහවක් පමණක්** පෑම.'],['Merely **smiling** at **something funny**.']),
      ag=(f'**මහ හඬින් සිනාසෙමින් {si_v}**',f'**{en_v.capitalize()} laughing loudly**'),sm=SM_SB))
QUIET_SI='**අප්පසද්දො** — **උස් හඬ, මහ හඬ නොනගා**.\n|! ආසන පිළිවෙළ (රියන් 12 ක ගෙයක) | ඇසෙන දේ | විනිශ්චය\n| මුලදී **සංඝස්ථවිර**, මැද **දෙවන ස්ථවිර**, අගදී **තෙවන ස්ථවිර** හිඳ, සංඝස්ථවිර දෙවැන්නා සමඟ කථා කරයි | දෙවැන්නාට **හඬ ද ඇසේ, කථාව ද තේරේ**; තෙවැන්නාට **හඬ පමණක්** ඇසේ, **කථාව නොතේරේ** | **අප්පසද්ද** (මඳ හඬ)\n| එසේ ම | **තෙවැන්නාට ද කථාව තේරේ** | **මහාසද්ද** (මහ හඬ)'
QUIET_EN='**Appasaddo** — **without loud noise or clamour**.\n|! Seating (in a house of 12 cubits) | What is heard | Ruling\n| **the senior elder** at the start, **the second** in the middle, **the third** at the end; the senior speaks with the second | the second **hears the sound and follows the talk**; the third **hears only the sound**, **not following the talk** | **quiet**\n| the same | **the third also follows the talk** | **loud**'
for n,g in ((13,True),(14,False)):
    si_v='ගම් අතර යාම' if g else 'ගම් අතර හිඳීම'; en_v='going among the houses' if g else 'sitting among the houses'
    B.append(dict(n=n,T=('අප්පසද්ද ගමන සික්ඛාපදය || Going Quietly' if g else 'අප්පසද්ද නිසීදන සික්ඛාපදය || Sitting Quietly'),
      V=f'උස් හඬින් කෑ ගසමින් {si_v} || Making a loud noise while {en_v}',K='SB kr=K sd=s an=a anu=0',
      Z='නොසිතා, නොසිහියෙන්, නොදැන; ගිලන්ව; ආපදාවල දී; උමතු ආදීන් || Unintentionally, unmindfully, not knowing; ill; emergencies; the insane etc.',
      story=story(f'**උස් හඬින්, මහ හඬින්** කථා කරමින් {"ගම් අතර ගියහ" if g else "ගම් අතර හිඳගත්හ"}',f'{"went" if g else "sat"} among the houses **making a loud noise and clamour**'),
      extra=[('පද විවරණය හා "මඳ හඬ" සීමාව',QUIET_SI,'Explanation of terms and the limit of “quiet”',QUIET_EN)],
      off=([f'**අනාදරයෙන්** උස් හඬ, මහ හඬ නගමින් {si_v}'],[f'{en_v.capitalize()} making a loud noise **out of disrespect**']),
      ana=ANA(),ag=(f'**උස් හඬ නගමින් {si_v}**',f'**{en_v.capitalize()} making a loud noise**'),sm=SM_SB))
PARTS=[(15,16,('Kāyappacālakaṃ','Kāyaṃ paggahetvā'),'සිරුර','body','කායප්පචාලක','Not Swaying the Body while','කායං පග්ගහෙත්වා','සිරුර **නොසොල්වා (නිශ්චල කොට)**, **සෘජු සිරුරෙන්**, **සම ඉරියව්වෙන්**','keeping the body **still**, **upright**, in **an even posture**','සිරුර එල්ලා (නමා) සොලවමින්','swaying, letting the body droop'),
       (17,18,('Bāhuppacālakaṃ','Bāhuṃ paggahetvā'),'අත්','arms','බාහුප්පචාලක','Not Swinging the Arms while','බාහුං පග්ගහෙත්වා','අත් **නොසොල්වා (නිශ්චල කොට)**','keeping the arms **still**','අත් එල්ලා වනමින්','swinging, letting the arms dangle'),
       (19,20,('Sīsappacālakaṃ','Sīsaṃ paggahetvā'),'හිස','head','සීසප්පචාලක','Not Shaking the Head while','සීසං පග්ගහෙත්වා','හිස **නොසොල්වා, සෘජුව** තබා','keeping the head **still and upright**','හිස එල්ලා සොලවමින්','shaking, letting the head droop')]
for ng,ns,pal,si_p,en_p,tp,te,pg,pgsi,pgen,actsi,acten in PARTS:
    for n,g in ((ng,True),(ns,False)):
        si_v='ගම් අතර යාම' if g else 'ගම් අතර හිඳීම'; en_v='going among the houses' if g else 'sitting among the houses'
        ex_si=f'**{tp}ං** — {si_p} **සොලවමින් සොලවමින්** ("{tp}ං" ආදී සෑම පදයක ම මේ ක්‍රමය ය).\n**{pg}** — =={pgsi}== {"යා" if g else "හිඳිය"} යුතුය. පාළියේ "**{si_p} එල්ලා (ඔලම්බෙන්තො)**" යි ද කියයි.'
        ex_en=f'**{pal[0]}** — **{acten.split(",")[0]}** the {en_p} again and again (the same pattern in every such term).\n**{pal[1]}** — one should {"go" if g else "sit"} =={pgen}==. The Pāli also says “**letting the {en_p} droop (olambento)**.”'
        if not g:
            ex_si+='\n**වාසූපගතස්ස** — ==හිඳීම සම්බන්ධ (කාය, බාහු, සීස) ශික්ෂාපද **තුනෙහි** **වාසය සඳහා පැමිණ සිටින්නාට අනාපත්ති**== (කඞ්ඛාවිතරණී).'
            ex_en+='\n**Vāsūpagatassa** — ==in **the three** sitting rules (body, arms, head), **no offence for one staying there**== (Kaṅkhāvitaraṇī).'
        ana=ANA([VASU[0]],[VASU[1]]) if not g else ANA()
        B.append(dict(n=n,T=f'{tp} {"ගමන" if g else "නිසීදන"} සික්ඛාපදය || {te} {"Going" if g else "Sitting"}',
          V=f'{actsi} {si_v} || {acten.split(",")[0].capitalize()} the {en_p} while {en_v}',K='P1 sd=s an=a anu=0 ved=D',
          Z='නොසිතා, නොසිහියෙන්, නොදැන; ගිලන්ව; '+('වාසය සඳහා පැමිණ සිටින විට; ' if not g else '')+'ආපදාවල දී; උමතු ආදීන් || Unintentionally, unmindfully, not knowing; ill; '+('when staying there; ' if not g else '')+'emergencies; the insane etc.',
          story=story(f'**{si_p} සොලවමින්** {"ගම් අතර ගියහ" if g else "ගම් අතර හිඳගත්හ"}',f'{"went" if g else "sat"} among the houses **{acten.split(",")[0]} the {en_p}**'),
          extra=[('පද විවරණය',ex_si,'Explanation of terms',ex_en)],
          off=([f'**අනාදරයෙන්** {actsi} {si_v}'],[f'{en_v.capitalize()} {acten} **out of disrespect**']),
          ana=ana,ag=(f'**{si_p} සොලවමින් {si_v}**',f'**{en_v.capitalize()} {acten.split(",")[0]} the {en_p}**'),sm=SM_P1))
open('/home/claude/work/content/10c_sk11_20.txt','w').write('\n\n'.join(block(d) for d in B)+'\n')
print(len(B))
