import re,glob
ADM_SI='**අවවාදය හා සමනුභාසනය:**\n|! පියවර | නොකළොත් / අත් නොහළොත්\n| ඔහු එසේ සිටිනු **සම්මුඛව දකින** හෝ **අසන** භික්ෂූන් — අවම වශයෙන් **අඩ යොදුනක්** දක්වා ගොස් වුව ද — අවවාද නොකළොත් | DK\n| **පුද්ගලිකව තුන් වරක්** අවවාද කළ පසු අත් නොහැරීම | DK\n| **සංඝ මධ්‍යයේ තුන් වරක්** අවවාද කළ පසු අත් නොහැරීම | DK\n| ඉන්පසු **සමනුභාසන කර්මය** (ඤත්තිචතුත්ථ) කළ යුතුය | —'
ADM_EN='**Admonition and the formal rebuke:**\n|! Step | If not done / not relinquished\n| monks who **see him face to face** or **hear** of it — even going **half a yojana** — not admonishing him | DK\n| not relinquishing after being admonished **three times privately** | DK\n| not relinquishing after being admonished **three times in the Saṅgha** | DK\n| then **the formal rebuke** (motion and three announcements) is to be carried out | —'
ANI_SI='**ඉමෙ ඛො පන** — "**ආයුෂ්මතුනි, මේ අනියත ධර්ම දෙක උද්දේශයට එයි**" යන නිදානයේ — එනම් **මෙසේ උද්දේශ කරනු ලබන** අනියත දෙක.'
ANI_EN='**Ime kho pana** — in “**these two undetermined matters, venerables, come up for recitation**” — i.e. **the two undetermined rules recited here**.'
ANI2_SI='**මාතුගාමෙන** — එදින උපන් වුව ද **ජීවමාන මනුෂ්‍ය ස්ත්‍රියක** සමඟ.\n**එකො එකාය** — **එක් භික්ෂුවක් එක් ස්ත්‍රියක** සමඟ.\n**රහො** — මෙහි **කනට රහස්** වූ තැන — **සාමාන්‍ය කථාව නොඇසෙන** තැන.\n**නිසජ්ජං කප්පෙය්‍ය** — හිඳී; **සැතපීම ද** හිඳීමට ම ඇතුළත් ය.\n**සද්ධෙය්‍යවචසා උපාසිකා** — **විශ්වාස කළ යුතු වචන ඇති** ආර්‍ය ශ්‍රාවිකාවක් (උපාසිකාවක්).'
ANI2_EN='**Mātugāmena** — with **a living human woman**, even one born that day.\n**Eko ekāya** — **one monk with one woman**.\n**Raho** — here a place **private to the ear** — **where ordinary speech is not overheard**.\n**Nisajjaṃ kappeyya** — sits; **lying down** is also included in sitting.\n**Saddheyyavacasā upāsikā** — a noble female disciple (lay follower) **whose word is to be trusted**.'
SD7_SI='සෙසු පද:\n|! පදය | අර්ථය\n| **උල්ලිත්තා / අවලිත්තා / උල්ලිත්තාවලිත්තා** | වහලයේ **ඇතුළත**, **පිටත**, හෝ **ඇතුළත හා පිටත** හුණු හෝ මැටියෙන් **ලේප කළ** විහාරය\n| **අනාරම්භ** (හිංසා රහිත) | **කුහුඹු, වේයන්, මීයන්, සර්පයන්, ගෝනුස්සන්, පත්තෑයන්, ඇතුන්, අසුන්, සිංහයන්, ව්‍යාඝ්‍රයන්, දිවියන්, වලසුන්, තරච්ඡයන්** යන සතුන් 13 දෙනාගේ වාසස්ථානවලින් ද, **පෙර/පසු ධාන්‍ය කෙත්, සතුන් මරන තැන්, වධස්ථාන, සොහොන්, උයන්, රජ බිම්, ඇත් හල්, අස් හල්, සිරගෙවල්, සුරා හල්, මස් කඩ, වීථි, හතරමං හන්දි, සභා ශාලා, සංසරණ මාර්ග** යන උපද්‍රව 16 න් ද තොර\n| **සපරික්කමන** (වටේ ඉඩ ඇති) | ගවයන් දෙදෙනෙකු හෝ සතර දෙනෙකු යෙදූ **කරත්තයක එක් රෝදයක් පියස්සේ වැහි වතුර වැටෙන තැනට ඇතුළතින් ද අනෙක පිටතින් ද** තබා වටේ යැවිය හැකි වීම\n| **භූමිය පෙන්වීම** | ස්ථානය පිරිසිදු කොට **සංඝයාගෙන් තුන් වරක් ඉල්ලා**, සංඝයා හෝ සම්මත භික්ෂූන් කැඳවාගෙන ගොස්, **ඤත්තිදුතිය කර්මයෙන්** භූමිය පෙන්වා ගැනීම\nකුටිකාර (සංඝාදිසේස 6) ශික්ෂාපදයෙන් **වෙනස හිමියෙකු සිටීම පමණි**.'
SD7_EN='The other terms:\n|! Term | Meaning\n| **ullittā / avalittā / ullittāvalittā** | a dwelling **plastered** with lime or clay **inside** the roof, **outside**, or **both inside and out**\n| **anārambha** (free of disturbances) | free of the abodes of the **thirteen creatures** — ants, termites, rats, snakes, scorpions, centipedes, elephants, horses, lions, tigers, leopards, bears, hyenas — and of the **sixteen disturbances**: near early-crop and late-crop fields, a slaughter-place, a place of execution, a cemetery, a park, royal property, an elephant stable, a horse stable, a prison, a tavern, a butcher\'s, a street, a crossroads, a meeting hall, a thoroughfare\n| **saparikkamana** (with space around) | such that **a cart yoked to two or four oxen** can be driven around it **with one wheel inside the eaves\' drip-line and one outside**\n| **marking the site** | clearing the place, **asking the Saṅgha three times**, bringing the Saṅgha or appointed monks, and having the site marked out **by a motion-and-one-announcement act**\nThe only difference from the hut rule (saṅghādisesa 6) is **having an owner**.'.replace("\\'","’")
NP12_SI='**එළකලොමානං සන්ථතං** — සම බිමක ලොම් **එකක් මත එකක් අතුරා**, කැඳ ආදිය ඉස **තළා** සකසන **පෙරළිම් සන්ථතයක්** (වියන ලද රෙද්දක් නොවේ).\n**කාරාපෙය්‍ය නිස්සග්ගියං** — කරන, කරවන **ප්‍රයෝගවල දුක්කට**; **ලැබීමෙන්** නිස්සග්ගිය වේ.\n|! ආකාරය | ඇවැත\n| තමා පිණිස — තමා හෝ අනුන් **ආරම්භ කොට** තමා හෝ අනුන් **නිම කළ** එකක් ලැබීම | NP\n| **අනෙකෙකු පිණිස** කිරීම / කරවීම | DK\n| **අනෙකෙකු කළ** එකක් ලැබ පරිහරණය | DK\n**අනාපත්ති** — **වියනක්, බිම් ඇතිරිල්ලක්, තිර පවුරක්, මෙට්ටයක් හෝ කොට්ටයක්** කිරීම; උමතු ආදීන්.'
NP12_EN='**Eḷakalomānaṃ santhataṃ** — a **felt** rug made by **spreading the wool layer upon layer** on level ground, sprinkling it with rice-water and the like and **beating** it (not woven cloth).\n**Kārāpeyya nissaggiyaṃ** — **dukkaṭa in the efforts** of making or having it made; **nissaggiya on receiving it**.\n|! Case | Offence\n| for oneself — **begun** by oneself or others and **finished** by oneself or others, receiving it | NP\n| making / having made **for another** | DK\n| using one **made by another** | DK\n**No offence** — making **a canopy, floor covering, screen, mattress or pillow**; the insane etc.'
NP19_SI='එය **සංඝ මධ්‍යයේ** නිස්සජ්ජනය කළ යුතුය. ගිහියෙක් පැමිණියොත් "**මෙය දැනගන්න**" යි කිව යුතුය; "මෙයින් කුමක් ගෙනෙන්න ද?" යි ඇසුවොත් **ගිතෙල් ආදී කැප දෙය පමණක්** කිව යුතුය. ඔහු ගෙනාවොත් **හුවමාරු කළ භික්ෂුව හැර** සියල්ලන් පරිභෝග කළ යුතුය; ඔහු ඉවත නොදමයි නම් **අංග පහකින් යුත් රූපිය ඡට්ටකයෙකු** සම්මත කොට **සලකුණක් නොතබා** ඉවත දැමවිය යුතුය.'
NP19_EN='It is to be forfeited **in the midst of the Saṅgha**. If a layman comes, he should be told, “**Know this**”; if he asks what to bring with it, only **allowable things such as ghee** should be named. If he brings something, all may use it **except the monk who made the exchange**; if he will not throw it away, **a money-disposer with five qualities** is appointed, who throws it away **without noting the place**.'
PAC62_SI='**ප්‍රාණීන් සිටින** බව දැන, හෝ "**පරිභෝගයෙන් මැරෙනු ඇත**" යි දැන, **ප්‍රාණීන් සහිත ජලය** තමා **බීම, නෑම** ආදියෙන් පරිභෝග කිරීම — **ප්‍රයෝගයක් පාසා** පාචිත්තිය ය; ප්‍රාණීන් නැතැයි සිතා, නොදැන, හෝ නොමැරෙන බව දැන පරිභෝග කිරීම අනාපත්ති ය. වෙනත් සමාන ශික්ෂාපද සමඟ:'
PAC62_EN='Using **water with living beings** in it — **drinking, bathing** etc. — **knowing there are beings** in it, or knowing “**they will die from the use**,” is pācittiya **for each effort**; using it perceiving no beings, not knowing, or knowing they will not die, is no offence. Compared with related rules:'
PAC67_SI='**සංවිධාය** — කතිකා කොට — **යන කාලය ගැන සංකේතයක්** ඇති කොට ("අද යමු", "හෙට යමු").\n**එකද්ධානමග්ගං** — එක ම දීර්ඝ මාර්ගයක් — හෝ **එකට** දීර්ඝ මාර්ගයක.\n**අන්තමසො ගාමන්තරම්පි** — අවම වශයෙන් **එක් ගමක සිට අනෙක් ගමට** වුව ද.'
PAC67_EN='**Saṃvidhāya** — by arrangement — **fixing a time to go** (“let\'s go today,” “let\'s go tomorrow”).\n**Ekaddhānamaggaṃ** — the same long road — or a long road **together**.\n**Antamaso gāmantarampi** — **even from one village to the next**.'.replace("\\'","’")
PAC70_SI='**සම්භුඤ්ජෙය්‍ය** — **ආමිස සම්භෝගය** (ආහාර දීම / ගැනීම) හෝ **ධර්ම සම්භෝගය** (උද්දේශ දීම / ගැනීම) කරයි.\n**සහ වා සෙය්‍යං කප්පෙය්‍ය** — **වෙනස් උපචාර ඇති** තැනක වුව ද **එක ම වහලක් යට** සැතපෙයි.'
PAC70_EN='**Sambhuñjeyya** — shares **material things** (giving / receiving food) or **Dhamma** (giving / receiving recitation).\n**Saha vā seyyaṃ kappeyya** — lies down **under the same roof**, even where the precincts are separate.'
PAC70T_SI='|! ක්‍රියාව | ඇවැත් පරිච්ඡේදය\n| **ආමිස සම්භෝගය** — **එක් ප්‍රයෝගයකින්** බොහෝ දේ දීම / ගැනීම | **එක්** PC\n| ආමිස සම්භෝගය — **නවත්වා නවත්වා** | **ප්‍රයෝගයක් පාසා** PC\n| **ධර්ම සම්භෝගය** — පද ආදියෙන් උගන්වීම / උගැන්වීම | **පදයක් පාසා** PC\n| **සහසෙය්‍යාව** | එකෙක් සැතපුණු කල්හි අනෙකාගේ **සැතපීමේ ප්‍රයෝගය** අනුව\n| **උපලාපනය**, **උපස්ථාන ගැනීම** | PC'
PAC70T_EN='|! Act | Measure of offences\n| **material sharing** — giving / receiving much **in one effort** | **one** PC\n| material sharing — **stopping and starting** | PC **for each effort**\n| **Dhamma sharing** — teaching / having taught by lines etc. | PC **for each line**\n| **sharing a sleeping place** | by **each effort of lying down** when the other is lying down\n| **enticing**, **having him serve** | PC'
PAC82_SI='**ජානං** — **තමා ම දැන**, හෝ **අනුන් කියා**, හෝ **දායකයා ම කියා**.\n**සඞ්ඝිකං** — සංඝයාට **පරිණත** වූ බැවින් **අතට නොපැමිණිය ද** එක් පරියායකින් සංඝයා සතු වූ.\n**ලාභං** — **සිවුරු, පිණ්ඩපාත, සෙනසුන්, ගිලන්පස බෙහෙත් පිරිකර**; අවම වශයෙන් **සුණු පිඩක්, දැහැටියක්, දසිකාවේ නූලක්** වුව ද.\n**පරිණතං** — "**දෙන්නෙමු, කරන්නෙමු**" යි **වචනය බිඳ** හෝ **අත් සන්නයකින්** — සංඝයාට **නැඹුරු වී** සිටින.'
PAC82_EN='**Jānaṃ** — **knowing it himself**, or **told by others**, or **told by the donor**.\n**Saṅghikaṃ** — belonging to the Saṅgha in a sense, being **intended** for it **even if not yet handed over**.\n**Lābhaṃ** — **robes, almsfood, lodgings, medicines**; even **a lump of bath powder, a tooth stick, a fringe thread**.\n**Pariṇataṃ** — **inclined** towards the Saṅgha by **words spoken** (“we will give, we will make”) or **by a gesture**.'
PAC88_SI='**මඤ්චො / පීඨං** — වර්ග **සතරකි**: **මසාරක** (පාද ගැට්ටෙහි සිදුරුවලට ඇතුළු කළ), **බුන්දිකාබද්ධ** (ගැට්ට පාද කෙළවරට සවි කොට බැඳි), **කුළීරපාදක** (කකුළු පා මෙන් වක් පාද ඇති), **ආහච්චපාදක** (ගලවා සවි කළ හැකි පාද ඇති).'
PAC88_EN='**Mañco / pīṭhaṃ** — of **four kinds**: **masāraka** (legs inserted into holes in the frame), **bundikābaddha** (frame bound onto the tops of the legs), **kuḷīrapādaka** (legs curved like a crab\'s), **āhaccapādaka** (detachable legs).'.replace("\\'","’")
PD3_SI='**ඛාදනීයං / භොජනීයං** — **ඔදන, කුම්මාස, සත්තු, මාළු, මස්** යන **භෝජන පස** සහ **යාමකාලික, සත්තාහකාලික, යාවජීවික හැර** සෙසු **කෑ යුතු දේ** (යාවකාලික).'
PD3_EN='**Khādanīyaṃ / bhojanīyaṃ** — **the five foods: rice, porridge, flour, fish, meat**, and anything **to be chewed** other than **juice drinks, seven-day tonics and lifetime medicines** (i.e. food allowed until noon).'
R=[
 ('සෙසු විනිශ්චය **අටවන ශික්ෂාපදයේ කී පරිදි ම ය**:','ඇවැත් විනිශ්චය:'),
 ('The rest of the analysis is **as in the eighth rule**:','Analysis of offences:'),
 ('සෙසු පද හා විනිශ්චය **දසවන ශික්ෂාපදයේ කී පරිදි ම ය** — දැක හෝ අසා අවවාද කිරීම, පුද්ගලිකව හා සංඝ මධ්‍යයේ තුන් වරක් කීම, ඉන්පසු සමනුභාසනය.',ADM_SI),
 ('The rest of the terms and the analysis are **as in the tenth rule** — admonition by those who see or hear, three times privately and in the Saṅgha, then the formal rebuke.',ADM_EN),
 ('සෙසු විනිශ්චය **දසවන ශික්ෂාපදයේ කී පරිදි ම ය**.',ADM_SI),
 ('The rest of the analysis is **as in the tenth rule**.',ADM_EN),
 ('**ඉමෙ ඛො පන** — පෙර කී නයින් ම ය.',ANI_SI),('**Ime kho pana** — as explained before.',ANI_EN),
 ('සෙසු පද **පළමු අනියතයේ කී පරිදි ම ය**.',ANI2_SI),('The other terms are **as in the first undetermined rule**.',ANI2_EN),
 ('# පළමු කඨින ශික්ෂාපදයේ කී පරිදි **දුන්,','# **දුන්,'),(', as in the first kathina rule.','.'),
 ('ඉතිරි සියල්ල **පළමු කඨිනයේ කී පරිදි ම ය**; වෙනස: එහි **දින දහය**, මෙහි **මාසය** ඉක්මවීම ය.','==**මාසය** ඉක්මවූ කල්හි== නිස්සග්ගිය වේ:'),
 ('Everything else is **as in the first kathina rule**; the difference is that there **ten days**, here **a month**, is exceeded.','It becomes nissaggiya ==when **the month** is exceeded==:'),
 ('**එළකලොමානං සන්ථතං** — පෙර කී පරිදි අතුරා, තළා සකසන **පෙරළිම් සන්ථතයක්**.\nසෙසු පද හා විනිශ්චය **පළමු ශික්ෂාපදය (කෝසිය) හා සමාන ය**.',NP12_SI),
 ('**Eḷakalomānaṃ santhataṃ** — a **felt** rug, spread and beaten as described before.\nThe other terms and the analysis are **as in the first (silk) rule**.',NP12_EN),
 ('සියලු විනිශ්චය **පුරාණ චීවරය සෝදවීමේ (නිස්සග්ගිය 4) කී පරිදි ම ය** — ','විනිශ්චයට අයත් කරුණු — '),
 ('The whole analysis is **as in the rule on having an old robe washed (Nissaggiya 4)** — ','The analysis covers — '),
 ('එය පෙර නයින් ම **සංඝ මධ්‍යයේ** නිස්සජ්ජනය කළ යුතු අතර නිස්සජ්ජනය කළ වස්තුව සම්බන්ධයෙන් ද එහි කී පරිදි ම පිළිපැදිය යුතුය.',NP19_SI),
 ('It is to be forfeited **in the midst of the Saṅgha** as before, and the forfeited object dealt with as described there.',NP19_EN),
 ('කී ලක්ෂණයෙන් **සංඝයාට, ගණයකට හෝ පුද්ගලයෙකුට**','නිස්සග්ගිය වචනයෙන් **සංඝයාට, ගණයකට හෝ පුද්ගලයෙකුට**'),
 ('**to a Saṅgha, a group or an individual** as described.','**to a Saṅgha, a group or an individual** with the forfeiture formula.'),
 (' සෙසු විස්තර **චීවර වර්ගයේ පළමු ශික්ෂාපදයේ** කී පරිදි ය.',''),(' The rest is as in **the first rule of the robe chapter**.',''),(' The rest is as in **the first robe rule**.',''),
 (' සෙසු විස්තර **චීවර වර්ගයේ දෙවන ශික්ෂාපදයේ** කී පරිදි ය.',''),(' The rest is as in **the second robe rule**.',''),
 ('(පෙර ශික්ෂාපදය මෙන්)',''),('(as in the previous rule)',''),
 ('සෙසු සියලු විනිශ්චය **චීවරප්පටිග්ගහණ ශික්ෂාපදයේ (නිස්සග්ගිය 5)** කී පරිදි ය; වෙනස —','**නිස්සග්ගිය 5** (සිවුරු පිළිගැනීම) සමඟ සැසඳීම —'),
 ('All other rulings are as in **the rule on accepting a robe (nissaggiya 5)**; the difference —','Compared with **nissaggiya 5** (accepting a robe) —'),
 ('සෙසු සියල්ල **සංවිධාන ශික්ෂාපදයේ (පා. 27)** කී පරිදි ය; එහි ','කතිකාවේ දී **පළමු පියට දුක්කට** ය. මෙහි '),
 ('All the rest is as in **the arrangement rule (Pāc. 27)**; here ','Making the arrangement is **dukkaṭa at the first step**. Here '),
 ('මෙහි **සියලු පාළි අර්ථය හා විනිශ්චය දෙවන අනියතයේ කී පරිදි ම ය**. මේ ශික්ෂාපදය','මේ ශික්ෂාපදය'),
 ('**All the meaning and rulings are as in the second Aniyata**. This rule','This rule'),
 ('— ගණභෝජනයේ කී පරිදි **භෝජන පහෙන් ආරාධනා ලැබූ**','— **භෝජන පහෙන් එකකින් ආරාධනා ලැබූ**'),(' (as in the group-meal rule)',''),
 ('සෙසු විස්තර **පළමු අනියතයේ** කී පරිදි ය. මේ ශික්ෂාපදය','මේ ශික්ෂාපදය'),('The rest is as in **the first Aniyata**. This rule','This rule'),
 ('| **භික්ෂුණියක්** සමඟ | 45 මෙනි','| **භික්ෂුණියක්** සමඟ | අන්ධ නොවූ, **බිහිරි නොවූ** විඤ්ඤු **ස්ත්‍රියක හෝ පුරුෂයෙක්**'),
 ('| with **a nun** | as in 45','| with **a nun** | a discerning **woman or man**, not blind and **not deaf**'),
 ('**මාතුගාමො, නිසජ්ජං කප්පෙය්‍ය** — පෙර ශික්ෂාපදයේ කී පරිදි ය.','**මාතුගාමො** — **ජීවමාන මනුෂ්‍ය ස්ත්‍රියක**, එදින උපන් වුව ද. **නිසජ්ජං කප්පෙය්‍ය** — හිඳී; **සැතපීම ද** ඇතුළත් ය.'),
 ('**Mātugāmo, nisajjaṃ kappeyya** — as in the previous rule.','**Mātugāmo** — **a living human woman**, even one born that day. **Nisajjaṃ kappeyya** — sits; **lying down** is included.'),
 ('සෙසු විස්තර **දෙවන අනියතයේ** කී පරිදි ය. මෙය','මෙය'),('The rest is as in **the second Aniyata**. This rule','This rule'),
 ('— when he has gone to the army for **such a reason** as in the previous rule (a relative being ill etc.).','— when he has gone to the army for **such a reason** (a relative being ill etc.).'),
 ('සෙසු විස්තර **උය්‍යුත්තසේනා ශික්ෂාපදයේ (පා. 48)** කී පරිදි ය; එහෙත් ==','=='),('The rest is as in **the army rule (Pāc. 48)**, but ==','=='),
 ('සෙසු සියලු විනිශ්චය — ප්‍රයෝග','ප්‍රයෝග'),(' — **තෙවන පාරාජිකයේ (මනුස්සවිග්ගහ)** කී පරිදි ම ය.',' — **මනුෂ්‍ය ඝාතනයේ දී මෙන් ම** සලකා බැලිය යුතුය.'),
 ('All other rulings — the means','The means'),(' — are as in **the third pārājika (killing a human)**.',' — are to be considered **just as for killing a human**.'),
 ('සෙසු විනිශ්චය **සිඤ්චන ශික්ෂාපදයේ (පාචිත්තිය 20)** කී පරිදි ය.',PAC62_SI),('The other rulings are as in **the sprinkling rule (Pācittiya 20)**.',PAC62_EN),
 ('**කතිකාවේ හා ගමනේ ඇවැත් විනිශ්චය** ==**ඕවාද වර්ගයේ (භික්ෂුණිය සමඟ සංවිධාන — පාචිත්තිය 27)**== කී පරිදි ය:','**කතිකාවේ හා ගමනේ ඇවැත් විනිශ්චය**:'),
 ('**the rulings on offences for arranging and travelling** are ==as in **the Exhortation chapter (arranging with a nun — Pācittiya 27)**==:','**the rulings on offences for arranging and travelling** are:'),
 ('**සංවිධාය, එකද්ධානමග්ගං, අන්තමසො ගාමන්තරම්පි** — **භික්ෂුණිය සමඟ සංවිධාන ශික්ෂාපදයේ (පා. 27)** කී පරිදි ය.',PAC67_SI),
 ('**Saṃvidhāya, ekaddhānamaggaṃ, antamaso gāmantarampi** — as in **the rule on arranging with a nun (Pāc. 27)**.',PAC67_EN),
 ('සෙසු සියලු විනිශ්චය **පාචිත්තිය 27** හි කී පරිදි ම ය; වෙනස —','**පාචිත්තිය 27** (භික්ෂුණිය සමඟ) සමඟ සැසඳීම —'),('All the rulings are as in **Pācittiya 27**; the differences —','Compared with **Pācittiya 27** (with a nun) —'),
 ('(සංඝාදිසේස සමනුභාසන ශික්ෂාපදවල මෙන් ම ය; එහෙත් ඇවැත **පාචිත්තිය** ය.)','(සමනුභාසන කර්මයේ අවසානයේ ඇවැත **පාචිත්තිය** ය.)'),('(As in the saṅghādisesa formal-admonition rules, but the offence is **pācittiya**.)','(At the end of the formal rebuke the offence is **pācittiya**.)'),
 ('| **පදසෝධම්මයේ** කී පරිදි (පදයක් පාසා)','| **පදයක් පාසා** PC'),('| as in **the line-by-line rule** (each line)','| PC **for each line**'),
 ('**සම්භුඤ්ජෙය්‍ය, සහ වා සෙය්‍යං කප්පෙය්‍ය** — **අනන්තර ශික්ෂාපදයේ** කී පරිදි ය.',PAC70_SI),('**Sambhuñjeyya, saha vā seyyaṃ kappeyya** — as in **the preceding rule**.',PAC70_EN),
 ('ආමිස / ධර්ම සම්භෝගය හා සහසෙය්‍යාවේ ඇවැත් පරිච්ඡේදය **උක්ඛිත්තසම්භෝග ශික්ෂාපදයේ (පා. 69)** කී පරිදි ය. **උපලාපනය** හා **උපස්ථාන ගැනීම** ද පාචිත්තියට හේතු වේ.',PAC70T_SI),
 ('The measure of offences for material / Dhamma sharing and sharing a sleeping place is as in **the rule on associating with a suspended monk (Pāc. 69)**. **Enticing** and **having him serve** are also grounds for pācittiya.',PAC70T_EN),
 ('අට්ඨකථා දෙකෙහි ම (කඞ්ඛාවිතරණී, සමන්තපාසාදිකා) "**සෙසු සියල්ල සමුට්ඨාන ආදිය සමඟ අරිට්ඨ ශික්ෂාපදයේ කී පරිදි ය**" යි කියා ඇත.',''),
 ('Both commentaries (Kaṅkhāvitaraṇī and Samantapāsādikā) say: “**The rest, together with the origin etc., is as in the Ariṭṭha rule**.”',''),
 ('සෙසු සියල්ල **පෙර ශික්ෂාපදයේ (පහාර)** කී පරිදි ය.',''),('All the rest is as in **the previous rule (striking)**.',''),
 ('**ජානං, සඞ්ඝිකං, ලාභං, පරිණතං** — **තිංසක කාණ්ඩයේ පරිණාමන ශික්ෂාපදයේ (නිස්සග්ගිය 30)** කී පරිදි ය.',PAC82_SI),
 ('**Jānaṃ, saṅghikaṃ, lābhaṃ, pariṇataṃ** — as in **the diverting rule of the Thirty (nissaggiya 30)**.',PAC82_EN),
 ('==සියල්ල **තිංසක කාණ්ඩයේ පරිණාමන ශික්ෂාපදයේ** කී පරිදි ම ය; **මේ පමණක් වෙනස**==:','**නිස්සග්ගිය 30** (තමාට හැරවීම) සමඟ සැසඳීම:'),
 ('==All is as in **the diverting rule of the Thirty**; **only this differs**==:','Compared with **nissaggiya 30** (diverting to oneself):'),
 ('සෙසු සියල්ල **සූචිඝර ශික්ෂාපදය මෙනි** — ',''),('The rest is **as the needle-case rule** — ','It is '),
 ('සෙසු සියල්ල **නිසීදන ශික්ෂාපදය මෙනි** — ',''),('The rest is **as the sitting-cloth rule** — ','It is '),
 ('කඞ්ඛාවිතරණිය අනුව **සෙසු සියල්ල නිසීදන ශික්ෂාපදය මෙනි** — ','කඞ්ඛාවිතරණිය අනුව — '),('Per the Kaṅkhāvitaraṇī, **the rest is as the sitting-cloth rule** — ','Per the Kaṅkhāvitaraṇī, it is '),
 ('**මඤ්චො / පීඨං** — **මසාරක, බුන්දිකාබද්ධ, කුළීරපාදක, ආහච්චපාදක** යන සතර වර්ගය (මඤ්චපීඨ ශික්ෂාපදයේ මෙනි).',PAC88_SI),
 ('**Mañco / pīṭhaṃ** — the four kinds: **masāraka, bundikābaddha, kuḷīrapādaka, āhaccapādaka** (as in the bed rule).',PAC88_EN),
 ('**ඛාදනීයං / භොජනීයං** — පළමු පාටිදේසනීයයේ කී පරිදි ය.',PD3_SI),('**Khādanīyaṃ / bhojanīyaṃ** — as in the first pāṭidesanīya.',PD3_EN),
 (' දුර සෙනසුන (චීවරවිප්පවාස ශික්ෂාපදයේ කී පරිදි).',' දුර සෙනසුන.'),(' from a village (as in the rule on being away from robes).',' from a village.'),
 ('# කී පරිදි **ආරණ්‍ය සෙනසුනක්** (සැක සහිත, භය සහිත) වීම.','# **සැක සහිත, භය සහිත ආරණ්‍ය සෙනසුනක්** වීම.'),('# **A wilderness lodging** as described (suspect, dangerous).','# **A suspect, dangerous wilderness lodging**.'),
 ('| ස්ත්‍රියක් යැයි දැන, අවම වශයෙන් **අත් සංඥාවෙන්** වුව ද කී පරිදි කථා කිරීම','| ස්ත්‍රියක් යැයි දැන, අවම වශයෙන් **අත් සංඥාවෙන්** වුව ද එබඳු දුට්ඨුල්ල වචන කීම'),
 ('addressing her as described — even by **hand gesture**','addressing her with such lewd words — even by **hand gesture**'),
 ('Origin and the rest are **as stated for taking what is not given** — the origin','The origin'),
 ('Z: රතන ශික්ෂාපදයේ නයින් (ආරාමය / ආවසථය තුළ වැටුණු දෙය හිමියාට තබා දීමට) ගැනීම','Z: ආරාමය / ආවසථය තුළ වැටුණු දෙය හිමියාට තබා දීමට ගැනීම'),
 ('# **As in the treasure rule (Pācittiya 84)** — picking up','# Picking up'),
]
used=set()
for f in glob.glob('/home/claude/work/content/0*.txt'):
    s=open(f).read();o=s
    for i,(a,b) in enumerate(R):
        if a in s: s=s.replace(a,b); used.add(i)
    if s!=o: open(f,'w').write(s)
for i,(a,b) in enumerate(R):
    if i not in used: print('UNUSED',a[:90])
