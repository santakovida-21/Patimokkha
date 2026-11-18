import asyncio
from playwright.async_api import async_playwright
U='file:///home/claude/work/out/pratimoksha.html'
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        for lang in ('si','en'):
            pg=await b.new_page(viewport={'width':900,'height':1200})
            errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
            await pg.goto(U)
            await pg.evaluate("l=>{let s={};try{s=JSON.parse(localStorage.getItem('pm-settings-v3')||'{}')}catch(e){};s.lang=l;localStorage.setItem('pm-settings-v3',JSON.stringify(s))}",lang)
            await pg.goto(U+'#r-'+RID+''); await pg.reload(); await pg.wait_for_timeout(1500)
            for tab in ('story','att','kkv','s17'):
                await pg.click(f'.rtab[data-tab="{tab}"]'); await pg.wait_for_timeout(300)
                await pg.evaluate("document.querySelectorAll('.tpanel.on .sec').forEach(s=>s.classList.add('open'))")
                await pg.wait_for_timeout(300)
                el=await pg.query_selector('#main')
                await el.screenshot(path=f'/home/claude/work/shots/'+RID+'_{lang}_{tab}.png')
            print(lang,errs)
            await pg.close()
        await b.close()
asyncio.run(main())
