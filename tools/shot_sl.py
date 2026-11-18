import asyncio
from playwright.async_api import async_playwright
import sys
RIDS=sys.argv[1:]
U='file:///home/claude/work/out/pratimoksha.html'
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        for RID in RIDS:
         for w in (900,):
          for lang in ('si','en','zh'):
            pg=await b.new_page(viewport={'width':w,'height':1000})
            errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
            await pg.goto(U)
            await pg.evaluate("l=>localStorage.setItem('pm-settings-v3',JSON.stringify({lang:l}))",lang)
            await pg.goto(U+'#r-'+RID); await pg.reload(); await pg.wait_for_timeout(1200)
            await pg.click('.rtab[data-tab="story"]')
            await pg.click('.tpanel.on .sech'); await pg.wait_for_timeout(300)
            sec=await pg.query_selector('.tpanel.on .sec')
            await sec.screenshot(path=f'/home/claude/work/shots/sl_{RID}_{lang}_long.png')
            await pg.click('.tpanel.on [data-sl="short"]'); await pg.wait_for_timeout(300)
            await sec.screenshot(path=f'/home/claude/work/shots/sl_{RID}_{lang}_short.png')
            await pg.click('.tpanel.on [data-sl="long"]')
            print(w,lang,errs)
            await pg.close()
        await b.close()
asyncio.run(main())
