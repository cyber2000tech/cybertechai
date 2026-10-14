# Cyber Tech V33 — Source and Browser Audit

## Changes from V32

- Replaced homepage **Mission and Services** prose with Dr. Cecil’s latest supplied Word document (excluding reviewer-to-Ram instructions).
- Added prominent “Ready to harness the power of AI and related cognitive technologies?” typography.
- Included five benefits, three process domains, and the expanded discussion of cognitive tools, AI, XR, IoT, human-centered design, and consulting.
- Placed **four individual Cecil-supplied PNGs** around the Modeling / Simulation / Exchange Venn composition. The displayed PNG derivatives have transparent dark-theme-ready backgrounds; the original files remain included under `assets/cecil-venn/source/` unchanged.
- Added the exact requested information-centric perspective statement beneath the diagram, adjusting “AI based” to “AI-based” as a straightforward hyphenation fix.
- Created **Expertise** page. Moved all six previously displayed service figures in original order with titles, descriptions, and source image files unchanged.
- Renamed the section **Cross-Section of our Capabilities and Expertise** and included Dr. Cecil’s new introductory paragraph, nine capabilities, and transition sentence.
- Changed primary navigation to **Home | Expertise | Domains | Contact**, removed Contact’s adjacent arrow, and updated `sitemap.xml`.
- Reused the existing theme with restrained cyan accents and responsive diagram styling; retained Domains content, branding, hero, and investor notice.

## Copyediting performed on latest Word file

Minimal grammatical, punctuation and hyphenation corrections; did not change the intended technical claims:

- `well-underway` → `well underway`
- `your organizations ability` → `your organization’s ability`
- `Virtual Reality VR. Augmented Reality AR and Mixed Reality MR` → `Virtual Reality (VR), Augmented Reality (AR), and Mixed Reality (MR)`
- `cognitive enhanced` → `cognitively enhanced`
- `not simply creating` → `not simply to create`
- `medical activates` → `medical activities`
- `user friendly` → `user-friendly` (and related hyphenation)
- Consistent hyphenation for `information-centric`, `AI-based`, `IoT-based`, `technology-based`, and `information-rich` in client-supplied copy

## Checks

- Compared new homepage against the source Word document (opening text, each benefit and each process domain).
- Confirmed exact new Expertise heading, all nine capabilities, all six old figure entries, and the Venn with four image components.
- Confirmed homepage hero wording and the entire Domains page content are unchanged from V32.
- Confirmed all paths, image assets, header/footer naming, metadata URLs, canonical links, mobile navigation markup, sitemap, CNAME and investment note.
- Verified original 4 attached PNGs are byte-identical to retained source copies.
- Verified all images with Pillow and HTML local references with parser-based checks.
- Confirmed JS syntax and CSS stylesheet parsing.
- Chromium inline preview: tested Home, Expertise, Domains at widths 320px, 390px, 768px, 1440px; no horizontal overflow, no missing images, no page-script errors. Verified mobile menu opens and each expertise image displays after scrolling to it.

## Limits

- Local URL loading in the browser environment was blocked, so tests used self-contained inline rendering of the actual HTML, CSS, JS and image bytes.
- This verifies layout and scripts in Chromium, **not** physical iPhone/Android Safari or the live published website.
- Dr. Cecil’s technical claims and the exact editorial tone should be reviewed and approved by Dr. Cecil; this is not a scientific fact-check.
- **This ZIP is not deployed.** The published website will remain unchanged until the files are uploaded.
