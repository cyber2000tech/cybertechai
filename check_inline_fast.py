from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from pathlib import Path
import base64,mimetypes
root=Path('/mnt/data/cyber-v36-client-robot-update')
soup=BeautifulSoup((root/'expertise.html').read_text(),'html.parser')
for l in list(soup.select('link[rel="stylesheet"]')):
 href=l.get('href')
 if not href or href.startswith('http'):continue
 css=(root/href).read_text()
 import re
 css=re.sub(r'@import\s+url\([^)]*\);','',css)
 style=soup.new_tag('style');style.string=css;l.replace_with(style)
for f in soup.select('figure.service-visual:not(.service-visual--robotics)'): f.decompose()
for img in soup.select('img[src]'):
 src=img['src']
 if src.startswith('http'):continue
 f=root/src
 if f.is_file():
  mime=mimetypes.guess_type(f)[0] or 'image/png'
  img['src']=f'data:{mime};base64,'+base64.b64encode(f.read_bytes()).decode()
for s in list(soup.select('script[src]')):
 href=s.get('src')
 if href.startswith('http'):continue
 js=(root/href).read_text()
 new=soup.new_tag('script');new.string=js;s.replace_with(new)
for el in soup.select('link[href^="https://fonts"]'):el.decompose()
html=str(soup)
print('inline size',len(html),'byte')
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-dev-shm-usage'])
 for width in [320,390,768,1440]:
  page=browser.new_page(viewport={'width':width,'height':880},device_scale_factor=1)
  errors=[]
  page.on('pageerror', lambda e: errors.append(str(e)))
  page.set_content(html,wait_until='domcontentloaded',timeout=18000)
  page.locator('figure.service-visual--robotics').scroll_into_view_if_needed()
  page.wait_for_timeout(100)
  metrics=page.evaluate('''()=>{let a=document.querySelector('figure.service-visual--robotics .robotics-intro'), b=document.querySelector('figure.service-visual--robotics .robotics-photo--main'), c=document.querySelector('figure.service-visual--robotics .robotics-photo--details');return {overflow: document.documentElement.scrollWidth>window.innerWidth, docw:document.documentElement.scrollWidth, viewport:window.innerWidth, images:[...document.querySelectorAll('figure.service-visual--robotics img')].map(e=>({ok:e.complete&&e.naturalWidth>0,naturalWidth:e.naturalWidth})), positionOrder:a.getBoundingClientRect().top<b.getBoundingClientRect().top&&b.getBoundingClientRect().top<c.getBoundingClientRect().top, figures:document.querySelectorAll('figure.service-visual').length, robotFirst:document.querySelector('figure.service-visual')?.classList.contains('service-visual--robotics')}}''')
  print('WIDTH',width,'metrics',metrics,'JSERRORS',errors)
  assert not errors and not metrics['overflow'] and metrics['robotFirst'] and metrics['positionOrder'] and metrics['figures']==1 and all(i['ok'] for i in metrics['images'])
  if False:
   page.locator('figure.service-visual--robotics').screenshot(path=str(root/f'v36-expertise-robotics-{width}.png'),animations='disabled',timeout=18000)
  if width==390:
   btn=page.locator('button.menu-toggle')
   btn.click()
   print('mobile menu',btn.get_attribute('aria-expanded'), 'visible',page.locator('#primary-navigation').is_visible())
  page.close()
 browser.close()
