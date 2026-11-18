import asyncio
from playwright.async_api import async_playwright
U='file:///home/claude/work/out/pratimoksha.html'
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        for lang,w in (('si',390),('en',1280)):
            pg=await b.new_page(viewport={'width':w,'height':850}); errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
            await pg.goto(U); await pg.evaluate(f"localStorage.setItem('pm-settings-v3',JSON.stringify({{lang:'{lang}',pali:false}}))")
            await pg.goto(U+'#r-pac11'); await pg.reload(); await pg.wait_for_timeout(1000)
            await pg.click('.tpanel.on .sec:nth-child(1) .sech'); await pg.click('.tpanel.on .sec:nth-child(2) .sech')
            v0=await pg.evaluate("document.querySelector('.plfab').classList.contains('show')")
            await pg.mouse.wheel(0,1500); await pg.wait_for_timeout(400)
            v1=await pg.evaluate("document.querySelector('.plfab').classList.contains('show')")
            await pg.screenshot(path=f'/home/claude/work/shots/fab_{lang}_1.png')
            y=await pg.evaluate('scrollY')
            await pg.click('.plfab'); await pg.wait_for_timeout(300)
            y2=await pg.evaluate('scrollY'); lab=await pg.inner_text('.plfab'); lab2=await pg.inner_text('.thd .plbtn')
            await pg.screenshot(path=f'/home/claude/work/shots/fab_{lang}_2.png')
            await pg.goto(U+'#r-pac21'); await pg.wait_for_timeout(600)
            print(lang,w,v0,v1,y,y2,repr(lab),repr(lab2),await pg.evaluate("!!document.querySelector('.plfab')"),errs)
            await pg.close()
        await b.close()
asyncio.run(main())
