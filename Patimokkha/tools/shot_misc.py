import asyncio
from playwright.async_api import async_playwright
U='file:///home/claude/work/out/pratimoksha.html'
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        pg=await b.new_page(viewport={'width':1200,'height':900})
        errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
        await pg.goto(U)
        await pg.evaluate("()=>{localStorage.setItem('pm-settings-v3',JSON.stringify({lang:'zh'}))}")
        await pg.goto(U+'#r-pac21'); await pg.reload(); await pg.wait_for_timeout(1500)
        await pg.screenshot(path='/home/claude/work/shots/zh_pac21.png')
        await pg.goto(U+'#home'); await pg.wait_for_timeout(1000)
        await pg.screenshot(path='/home/claude/work/shots/zh_home.png')
        await pg.click('#setBtn') if await pg.query_selector('#setBtn') else None
        await pg.wait_for_timeout(600)
        await pg.screenshot(path='/home/claude/work/shots/zh_set.png')
        print(errs)
        await b.close()
asyncio.run(main())
