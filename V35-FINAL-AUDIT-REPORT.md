# Cyber Tech LLC — Final website audit (V35)

**Scope:** Downloadable static website package, built from `Cyber-Tech-Website-v34-Contact-Fix.zip`; Dr. Cecil's latest *EDITS TO MISSION AND SERVICES.docx*; the four supplied PNGs; and the previously supplied Domains wording changes. **This report audits the package, not the currently published live website.**

## Outcome

- **286/286 automated source, content-presence, internal-link, asset, and browser checks passed.** This is a count of checks, not a guarantee that every sentence is semantically perfect.
- **12 browser configurations passed** across Home, Expertise, and Domains: widths of 320, 390, 768 and 1440 pixels. All 7 home images, 6 expertise images, and 4 domains images rendered in the test. No JavaScript exceptions or horizontal page overflow were detected. The mobile menu opened and closed correctly on tested phone/tablet widths.
- **V34 issue found and fixed in V35:** The primary **Open Gmail** button showed dark text over a transparent/dark background. V35 now gives it an explicit cyan background `#50DAFA` and dark lettering `#051E30` with a visible hover/focus state. Desktop and mobile screenshots and computed styles confirm the fix.
- **No content, images, navigation, or contact-email destinations changed from V34.** Only `assets/cecil-v34-contact.css` was amended; this report was added to the package.

## Detailed content comparison

### Homepage / Mission and Services

- Confirmed the required **Cyber Tech** heading and **Cognitive Solutions for the interconnected cyber-human-physical metaverse** introduction.
- Confirmed the three original homepage images for robotics/VR, medical simulation, and space systems.
- Reviewed the Mission and Services material against Dr. Cecil's latest Word document, including the opening AI invitation, information-centric/AI introduction, Cognitive Advantage explanation, XR/VR/AR/MR and IoT description, human-centered and HCI material, **five** service benefits, **three** process domains, and closing overview.
- Confirmed the **four separate supplied diagram images** and the information-centric perspective sentence are present.
- The Word document contains copyediting errors that were previously corrected in the website rather than reproduced literally, including **“activates” → “activities”** and **“health care” → “healthcare.”** Hyphenation, punctuation, capitalization and selected grammatical corrections also differ from the raw Word text; these are not missing sections.

### Expertise page

- Confirmed the requested heading **Cross-Section of our Capabilities and Expertise** and new four-item navigation **Home | Expertise | Domains | Contact**.
- Verified each of Dr. Cecil's introductory statements and **all nine** capability bullets are present, including the enterprise-modeling methods (eEML, UML, IDEF).
- Confirmed the **six original service/expertise illustration files** and accompanying content remain in the Expertise page.

### Domains page

- Verified the four domains, including Cyber Learning, and the latest approved replacement passages covering XR environments, virtual manufacturing, digital twins, multidisciplinary expertise, engineering simulation and smart manufacturing.
- The two previously approved typo fixes—**“such as a robotic cell”** and **“to understand”**—are preserved.

### Contact, footer, search files, and navigation

- Contact has **three email options only**: direct Gmail compose link, default email-application link, and a copy-address button. **No contact form** is present, per Dr. Cecil's instruction.
- The Gmail compose and email-app links target `cyber2000tech@gmail.com`. Copy-address feedback was tested in a Chromium browser preview and returned **“Email address copied.”**
- The website does **not send an email itself**; a visitor must send the draft using their own email service. **Actual Gmail delivery was not tested.**
- Internal navigation targets and anchors, `CNAME`, sitemap and robots.txt were checked. The three active content pages are Home, Expertise and Domains; Contact is on the homepage. Legacy mission, services and contact URLs redirect to their homepage sections.
- Verified **Cyber Tech LLC** in visible header/footer branding and preservation of the investor-inquiry note.

## Test methodology and limits

- Source files were parsed and audited programmatically; original image files were opened and checked for corruption.
- Chromium rendered self-contained copies of the pages containing the real CSS and JavaScript, with **scaled-down image copies** to keep automated preview loading reliable. The actual image files included in the release were **not replaced or reduced**.
- Google Fonts loading was omitted in the self-contained preview to avoid external network requests; font metrics could therefore differ modestly from the published website.
- The local browser was not permitted to open localhost URLs, so this used a self-contained preview. This is **not a test on actual iPhones, Android devices, or desktop Safari**, and does not establish email delivery or the content currently published at `cybertechai.us`.

**Disposition:** V35 ZIP is structurally audited and ready for deployment. After publishing, check the Contact section in Safari and send one real Gmail test message.
