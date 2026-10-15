# Cyber Tech LLC — V36 robotics section update

## Client change checklist

1. **Expertise → Robotics first:** Moved the existing “Designing Robots for advanced manufacturing and medical surgery” figure from the sixth/final illustration to the first illustration, immediately below “A cross-section of our capabilities follows.”
2. **Spelling:** Replaced “microdevice assembly” with the client-specified “micro devices assembly” in the robotics description.
3. **Revised copy:** Replaced the old short robotics description with the two paragraphs supplied in Cecil's latest email screenshot, maintaining their technical meaning and the emphasis on *cyber-physical cobots*.
4. **Description positioning:** Placed the revised text directly below the robotics title and above the two replacement images.
5. **Replacement images:** Replaced the old robotics illustration on the page with both camera/light-guide apparatus and three-panel gripper photographs from the two provided email screenshots. **Source-quality limitation:** these photographs were cropped from screenshots, not original full-resolution image files. More detailed originals can be substituted later without altering the layout.
6. **Responsive styling:** Added scoped CSS for the two images and restored the normal size of the final (surgical training) illustration, which otherwise would have inherited an older last-figure width rule.

## Scope preserved

- Other five expertise figures retain their original copy and order relative to one another.
- Homepage, Domains, Contact options, email address, investor notice, main site navigation, CNAME and site metadata are unchanged.
- No contact form was added.

## Validation

- Page structure: six expertise figures, one robotics figure, two replacement image references; robotics placed first.
- Content: client-specified “micro devices assembly”; new robotics description appears above images.
- Asset validation: all images and local resources referenced by all HTML pages exist in the package.
- Chromium inline-render tests at **320px, 390px, 768px and 1440px** found no horizontal overflow or page JavaScript errors; both replacement images loaded with their natural dimensions. The mobile navigation opened successfully after its CSS transition.
- The ZIP is checked for CRC errors after packaging.

## Before going live

GitHub publishing is separate from this ZIP. After upload, refresh the Expertise page on desktop and mobile. The pictures will look sharper if Cecil sends their original files instead of screenshots. Real Gmail delivery and physical-device browsing were not part of this update.
