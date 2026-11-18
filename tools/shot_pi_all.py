import asyncio,sys
from playwright.async_api import async_playwright
U='file:///home/claude/work/out/pratimoksha.html'
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        for lang in ('si','en','zh'):
            pg=await b.new_page(viewport={'width':390,'height':900}); errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
            await pg.goto(U); await pg.evaluate(f"localStorage.setItem('pm-settings-v3',JSON.stringify({{lang:'{lang}',pali:true}}))")
            for n in range(11,21):
                await pg.goto(U+f'#r-pac{n}'); await pg.reload(); await pg.wait_for_timeout(700)
                res=[]
                for t in ('story','att','kkv','s17'):
                    if not await pg.query_selector(f'.rtab[data-tab="{t}"]'): res.append(t+':-'); continue
                    await pg.click(f'.rtab[data-tab="{t}"]'); await pg.wait_for_timeout(120)
                    r=await pg.evaluate("""()=>{const ss=[...document.querySelectorAll('.tpanel.on .sec')];ss.forEach(s=>s.classList.add('open'));
                      const vis=ss.filter(s=>{const pv=s.querySelector('.secb > .pv');return pv&&pv.offsetHeight>0&&pv.innerText.trim().length>10}).length;
                      const lv=[...document.querySelectorAll('.tpanel.on .lv')].filter(e=>e.offsetHeight>0).length;return ss.length+'/'+vis+(lv?' LV!':'')}""")
                    res.append(t+':'+r)
                    if lang=='si' and n in (14,19) and t in ('story','s17'):
                        el=await pg.query_selector('#main'); await el.screenshot(path=f'/home/claude/work/shots/pa_{n}_{t}.png')
                print(lang,n,' '.join(res),await pg.inner_text('.plfab'))
            print(lang,'errors',errs); await pg.close()
        await b.close()
asyncio.run(main())
