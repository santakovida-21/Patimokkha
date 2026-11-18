import asyncio,sys
from playwright.async_api import async_playwright
U='file:///home/claude/work/out/pratimoksha.html'
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        for lang,w in (('si',390),('en',390),('zh',390),('si',900)):
            pg=await b.new_page(viewport={'width':w,'height':1100})
            errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
            await pg.goto(U)
            await pg.evaluate("l=>{let s={};try{s=JSON.parse(localStorage.getItem('pm-settings-v3')||'{}')}catch(e){};s.lang=l;s.pali=false;localStorage.setItem('pm-settings-v3',JSON.stringify(s))}",lang)
            await pg.goto(U+'#r-pac11'); await pg.reload(); await pg.wait_for_timeout(1200)
            await pg.click('.rtab[data-tab="story"]')
            await pg.click('.tpanel.on .sec:nth-child(2) .sech'); await pg.wait_for_timeout(200)
            before=await pg.evaluate("[...document.querySelectorAll('.tpanel.on .sec')].map(s=>s.classList.contains('open'))")
            await pg.screenshot(path=f'/home/claude/work/shots/pi_{lang}{w}_a.png')
            await pg.click('.plbtn'); await pg.wait_for_timeout(300)
            after=await pg.evaluate("[...document.querySelectorAll('.tpanel.on .sec')].map(s=>s.classList.contains('open'))")
            lab=await pg.inner_text('.plbtn')
            await pg.screenshot(path=f'/home/claude/work/shots/pi_{lang}{w}_b.png')
            await pg.click('.tpanel.on .sec:nth-child(1) .sech'); await pg.wait_for_timeout(200)
            el=await pg.query_selector('#main'); await el.screenshot(path=f'/home/claude/work/shots/pi_{lang}{w}_c.png')
            for t in ('att','kkv','s17'):
                await pg.click(f'.rtab[data-tab="{t}"]'); await pg.wait_for_timeout(200)
                await pg.evaluate("document.querySelectorAll('.tpanel.on .sec').forEach(s=>s.classList.add('open'))")
                el=await pg.query_selector('#main'); await el.screenshot(path=f'/home/claude/work/shots/pi_{lang}{w}_{t}.png')
            await pg.click('.plbtn'); lab2=await pg.inner_text('.plbtn')
            print(lang,w,before==after,before,repr(lab),repr(lab2),errs)
            await pg.close()
        await b.close()
asyncio.run(main())
