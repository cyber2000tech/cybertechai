from playwright.sync_api import sync_playwright
from pathlib import Path
from urllib.parse import quote
root=Path('/mnt/data/cyber-v36-client-robot-update')
url=(root/'expertise.html').as_uri()
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--disable-gpu','--no-sandbox','--disable-dev-shm-usage','--allow-file-access-from-files'])
 for width in [320,390,768,1440]:
  page=browser.new_page(viewport={'width':width,'height':880},device_scale_factor=1)
  errors=[]
  page.on('pageerror',lambda e: errors.append(str(e)))
  page.goto(url,wait_until='domcontentloaded',timeout=12000)
  page.locator('figure.service-visual--robotics').scroll_into_view_if_needed()
  page.wait_for_timeout(300)
  over=page.evaluate('document.documentElement.scrollWidth > window.innerWidth')
  imgs=page.locator('figure.service-visual--robotics img').evaluate_all('(items)=>items.map(e=>({src:e.getAttribute("src"),done:e.complete,ok:e.naturalWidth>0,width:e.naturalWidth}))')
  pos=page.evaluate('''()=>{let a=document.querySelector('figure.service-visual--robotics .robotics-intro'), b=document.querySelector('figure.service-visual--robotics .robotics-photo--main'), c=document.querySelector('figure.service-visual--robotics .robotics-photo--details'); return {descriptionY:a.getBoundingClientRect().top, photo1Y:b.getBoundingClientRect().top, photo2Y:c.getBoundingClientRect().top}}''')
  print(width,'overflow',over,'images',imgs,'order',pos,'errors',errors)
  if width in [390,1440]:
   page.locator('figure.service-visual--robotics').screenshot(path=str(root/f'v36-expertise-robotics-{width}.png'),animations='disabled',timeout=12000)
   page.screenshot(path=str(root/f'v36-expertise-viewport-{width}.png'),animations='disabled',timeout=12000)
  if width==390:
   btn=page.locator('button.menu-toggle');btn.click();print('390 menu opened:',btn.get_attribute('aria-expanded'), 'visible:',page.locator('.nav-links').is_visible())
  page.close()
 browser.close()
