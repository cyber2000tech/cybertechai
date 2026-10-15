# Cyber Tech V42 — change list and audit

## Implemented from Dr. Cecil's previously deferred requests

1. Added the new homepage research-positioning headline: **Designing Cognitive Engineering solutions based on pioneering research.**
2. Added the supporting statement: **Our tools and services are based on an extensive research foundation involving some of the world's leading researchers.**
3. Restored the original Cyber/Human/Physical orbital SVG geometry and animations from an earlier Cyber Tech homepage design. The center words now say **CYBER / HUMAN / PHYSICAL / WORLDS**, as requested.
4. Positioned the new section toward the bottom of the homepage, **between Mission and Services and Contact**. The existing three hero PNGs, Venn diagram, and other sections are untouched.
5. Preserved the V41 Contact behavior: show `cyber2000tech@gmail.com` as plain text with one **Copy Email Address** button, with no email-opening link or form.

## Proofreading of the two new lines

- `Desigining` → `Designing`.
- `Our tools and services a based ...` → `Our tools and services are based ...`.
- Added `an` in `an extensive research foundation` for readability; no substantive wording was added.
- New small label `COGNITIVE ENGINEERING` is a presentation label reusing Cecil's own terminology, not a technical claim.

## Regression checks

- Original V41 HTML preserved **byte-for-byte** except the inserted homepage research section and stylesheet link.
- The only modified original website file is `index.html`; the only new website file is `assets/cecil-v42-research-orbit.css`.
- All other V41 pages, scripts, assets, PNG images, and original words retained byte-for-byte.
- All referenced local files exist; all 24 image assets verified as decodable.
- Restored sphere tested in Chromium at 320, 390, 768, 1024, and 1440 px at normal motion and reduced motion (10 tests total). No horizontal overflow. Motion stops when the user requests reduced motion.
- No backend or contact form added; email delivery not relevant to the current plain-text contact setup.
- Repository `CNAME` remains `cybertechai.us`.

## Limitations

- Tests used a locally rendered page with identical CSS/SVG; the published website was not modified.
- Final review on real iPhone/Safari and Android/Chrome remains recommended after upload.
