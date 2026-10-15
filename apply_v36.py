from bs4 import BeautifulSoup
from pathlib import Path
p=Path('/mnt/data/cyber-v36-client-robot-update')
path=p/'expertise.html'
soup=BeautifulSoup(path.read_text(), 'html.parser')
figs=soup.select('.cecil-slide-list > figure.service-visual')
assert len(figs)==6, len(figs)
robot=next(f for f in figs if 'Designing Robots for advanced manufacturing and medical surgery' in f.get_text(' ',strip=True))
assert robot == figs[-1]
container=robot.parent
robot.extract()
container.insert(0,robot)
# Remove original illustration and original short paragraph.
for el in list(robot.select('.service-visual-image,.service-visual-description')):
 el.decompose()
robot['class'] = list(robot['class']) + ['service-visual--robotics']
heading=robot.select_one('h3')
assert heading is not None
# Preserve client-supplied wording, replacing only the expressly specified typo.
paragraphs=[
"We have substantial experience in the design of smart robotic devices for medical surgery (orthopedics) and advanced manufacturing (micro devices assembly). Our gripping approaches involve designing automated grippers with special design features aimed at reducing the impact of van der Waals forces which come into play during manipulation of micron sized objects. For our customers, we can design and build stand-alone robotic devices or entire robotic work cells capable of rapidly assembling micro or macro devices with the help of sensors and other equipment.",
"Engineering and medical organizations need to be aware that we are in the middle of an AI oriented cognitive revolution, which is transforming engineering, medicine and other fields. At Cyber Tech, we are leading this next information centric revolution developing cognitive and cyber-enhanced robotic devices whose performance can be enhanced based on perception, sensing, reasoning and learning. We are pioneering a new class of intelligent robots ('cyber-physical cobots') which function as part of cognitive frameworks which comprise of AI modules, IoT sensors and digital twin-based interfaces. In orthopedic surgery, we can design and build robotic devices and automated setups to aid surgeons accomplish orthopedic and eye surgery. We have worked with surgeons and nurses before to design human-centric, user friendly surgical setups using Digital Twins."
]
intro=soup.new_tag('div', attrs={'class':'robotics-intro service-visual-description'})
for text in paragraphs:
 tag=soup.new_tag('p')
 if "'cyber-physical cobots'" in text:
  prefix,suffix=text.split("'cyber-physical cobots'")
  tag.append(prefix+"'")
  em=soup.new_tag('em')
  em.string='cyber-physical cobots'
  tag.append(em)
  tag.append("'"+suffix)
 else:tag.string=text
 intro.append(tag)
heading.insert_after(intro)
for index,(src,alt,size) in enumerate([
 ('assets/service-visuals/robot-camera-diagram.png','Robotic microassembly setup with vertical and horizontal cameras and annotated light guides',(1058,576)),
 ('assets/service-visuals/robot-gripper-views.png','Three close-up photographs showing microassembly robotic grippers',(748,186)),
]):
 holder=soup.new_tag('div', attrs={'class':'service-visual-image robotics-photo '+('robotics-photo--main' if index==0 else 'robotics-photo--details')})
 image=soup.new_tag('img',attrs={'src':src,'alt':alt,'width':size[0],'height':size[1],'loading':'lazy','decoding':'async'})
 holder.append(image)
 robot.append(holder)
# New styles isolated to the newly revised Expertise figure.
newcss='''/* V36: Cecil's robotics section moved first, with description before replacement images. */
.expertise-section .service-visual--robotics { margin-bottom: 26px; }
.expertise-section .service-visual--robotics .service-visual-title { max-width: 920px; }
.expertise-section .service-visual--robotics .robotics-intro { width: 100%; max-width: 940px; margin: 0 0 24px; }
.expertise-section .service-visual--robotics .robotics-intro p { margin: 0 0 16px; }
.expertise-section .service-visual--robotics .robotics-intro p:last-child {margin-bottom:0;}
.expertise-section .service-visual--robotics .robotics-intro em { font-weight: 600; color: #79dffd; }
.expertise-section .service-visual--robotics .robotics-photo { background: transparent; border: 0; padding: 0; align-self: center; border-radius: 0; max-width: 100%; }
.expertise-section .service-visual--robotics .robotics-photo--main { width: min(100%, 750px); margin-top: 2px; }
.expertise-section .service-visual--robotics .robotics-photo--details { width: min(100%, 530px); margin-top: 16px; }
.expertise-section .service-visual--robotics .robotics-photo img { width: 100%; max-width: 100%; height: auto; display: block; }
@media(max-width:640px) { .expertise-section .service-visual--robotics .robotics-intro {margin-bottom:19px;} .expertise-section .service-visual--robotics .robotics-intro p {margin-bottom:14px;} .expertise-section .service-visual--robotics .robotics-photo--details{margin-top:12px;} }
'''
(p/'assets/cecil-v36-robotics.css').write_text(newcss)
head=soup.head
style=soup.new_tag('link', attrs={'href':'assets/cecil-v36-robotics.css','rel':'stylesheet'})
head.append(style)
path.write_text(str(soup))
assert 'microdevice assembly' not in path.read_text()
assert len(soup.select('.cecil-slide-list > figure.service-visual'))==6
assert soup.select('.cecil-slide-list > figure.service-visual')[0].get('class')[-1]=='service-visual--robotics'
print('Updated',path)
print('title:',soup.select('.cecil-slide-list > figure.service-visual')[0].select_one('h3').get_text())
print('image count:',len(soup.select('figure.service-visual--robotics img')))
