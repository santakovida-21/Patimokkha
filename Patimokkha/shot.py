import asyncio,sys
from playwright.async_api import async_playwright
import os
BASE=os.environ.get('BASE','file:///home/claude/work/out/pratimoksha.html')
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox','--use-angle=swiftshader','--enable-unsafe-swiftshader'])
        shots=sys.argv[1:]
        for spec in shots:
            name,hash_,w,h,*act=spec.split('§')
            pg=await b.new_page(viewport={'width':int(w),'height':int(h)},device_scale_factor=1)
            errs=[]; pg.on('pageerror',lambda e: errs.append(str(e))); pg.on('console',lambda m: errs.append(m.text) if m.type=='error' else None)
            await pg.goto((BASE+'#'+hash_))
            await pg.wait_for_timeout(1500)
            for a in act:
                if a.startswith('js:'): await pg.evaluate(a[3:])
                elif a.startswith('click:'): await pg.click(a[6:])
                await pg.wait_for_timeout(700)
            await pg.screenshot(path=f'/home/claude/work/shots/{name}.png',full_page=False)
            if errs: print(name,'ERR',errs[:5])
            await pg.close()
        await b.close()
asyncio.run(main())
