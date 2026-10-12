# Cyber Tech - GitHub Pages deployment package

**Official domain:** https://cybertechai.us  
**GitHub username from setup screenshot:** `cyber2000tech`  
**Suggested repository:** `cybertechai`  
**Contact:** cyber2000tech@gmail.com

This production-ready package contains four pages: Home (`index.html`), Services, Domains and Mission. It is static HTML/CSS/JavaScript with no build step, no Node/npm and no Cloudflare Worker. The orbital animation and technical SVG art remain on mobile, tablets and desktop. The investment notice is preserved verbatim.

## FIRST: Upload the website to GitHub

1. In GitHub, create repository **cybertechai**, owner **cyber2000tech**, **Public** (required for GitHub Pages on GitHub Free). The screenshot shows the name is available. It is simplest to leave the README, `.gitignore` and license options off for the initial upload; this package has its own README.
2. Download and **extract** the ZIP. Inside, you should see `index.html`, `services.html`, `domains.html`, `mission.html`, `CNAME`, `.nojekyll`, `robots.txt`, `sitemap.xml`, `README.md`, `GITHUB-CLOUDFLARE-SETUP.md`, and an `assets/` folder.
3. On the repository's **Code** tab, choose **Add file -> Upload files**. Drag **the contents of the extracted folder**, including the entire `assets` folder, into the uploader. Do NOT upload the ZIP alone or put everything inside an extra nested folder. Commit directly to `main`.
4. In your repo, open **Settings -> Pages**. Under **Build and deployment**, select **Deploy from a branch**. Choose branch `main`, folder `/(root)`, and press **Save**.
5. In the same **Pages** settings, under **Custom domain**, enter **cybertechai.us** (no `https://`), then save. This package already has a matching root `CNAME` file.

## SECOND: DNS records at Cloudflare

Cloudflare -> cybertechai.us -> DNS -> Records. **Use DNS only (gray cloud)** for initial setup and certificate provisioning. Remove/replace any old/conflicting A/AAAA/CNAME records for `@` or `www` that point to other hosts; DO NOT remove unrelated mail/verification records such as MX/TXT.

| Type | Name | Content | Proxy | TTL |
| --- | --- | --- | --- | --- |
| A | @ | 185.199.108.153 | DNS only | Auto |
| A | @ | 185.199.109.153 | DNS only | Auto |
| A | @ | 185.199.110.153 | DNS only | Auto |
| A | @ | 185.199.111.153 | DNS only | Auto |
| CNAME | www | cyber2000tech.github.io | DNS only | Auto |

Optional IPv6 records, also DNS only:

| Type | Name | Content |
| --- | --- | --- |
| AAAA | @ | 2606:50c0:8000::153 |
| AAAA | @ | 2606:50c0:8001::153 |
| AAAA | @ | 2606:50c0:8002::153 |
| AAAA | @ | 2606:50c0:8003::153 |

Keep the custom domain set to **cybertechai.us** (without www). GitHub Pages normally redirects the `www` variant to the configured apex after DNS is correct. There is no need for a Cloudflare Worker or Page Rule.

## THIRD: Enable HTTPS and test

1. Wait for GitHub Pages deployment and DNS checks. DNS/SSL setup can take up to 24 hours.
2. GitHub repository -> **Settings -> Pages** -> enable **Enforce HTTPS** when available.
3. Verify https://cybertechai.us and https://www.cybertechai.us, then click each navigation item, test mobile menu and contact mailto.
4. Verify https://cybertechai.us/robots.txt, https://cybertechai.us/sitemap.xml, and https://cybertechai.us/assets/social-preview.png.

See **GITHUB-CLOUDFLARE-SETUP.md** for a more detailed visual step list, HTTPS guidance, and troubleshooting.

## Included publishing configuration

- `CNAME` binds the GitHub Pages branch site to cybertechai.us.
- `.nojekyll` bypasses Jekyll processing so files are served as uploaded.
- `robots.txt` and `sitemap.xml` use the confirmed domain.
- Canonical URLs, Open Graph URLs/images, Twitter share-image metadata, and Organization structured data use the confirmed domain.
- `assets/social-preview.png` is a social preview. It may be accessed at the absolute URL after deployment.
- `cyber2000tech@gmail.com` is the current contact email.

## Official references

- GitHub publishing source: https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site
- GitHub custom domain DNS: https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site
- GitHub HTTPS: https://docs.github.com/en/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https
- Cloudflare proxy status: https://developers.cloudflare.com/dns/proxy-status/


## Client PowerPoint visual integration (October 2026)

The six image files in `assets/client/` were extracted from the client-provided presentation **FOR THE WEB PAGE.pptx**. Diagrams containing grouped PowerPoint elements were rendered faithfully to WebP. All assets are self-hosted by the website and are editable/replacable independently of page code.

| PowerPoint slide | Website location | Image asset |
| --- | --- | --- |
| 1, Modeling / Simulation / Exchange Venn | Homepage, "Our information-centric perspective" | `modeling-simulation-exchange.webp` |
| 2, 3D digital twin design framework | Services, "Digital twins, built on understanding" | `digital-twin-framework.webp` |
| 3, Cognitive manufacturing workflow | Domains, "Cognitive manufacturing and simulation" | `cognitive-manufacturing-workflow.webp` |
| 4, Immersive vs physical manufacturing system | Domains, "Virtual and physical systems together" | `immersive-physical-manufacturing.webp` |
| 5, Factory/shop-floor digital twin examples | Homepage application preview & Domains, "Immersive manufacturing environments" | `factory-digital-twins.webp` |
| 6, Virtual/Mixed Reality nurse/surgeon training | Homepage application preview & Domains, "Virtual and mixed reality for clinical training" | `surgical-vr-training.webp` |

Captions are positioned directly under the images; the larger technical captions are on the respective interior pages. Clicking a technical image opens a full-size version for detailed inspection. The homepage remains structured around Services, Domains, Mission and Contact; adding new application pages later does not require redesigning it.

**Publishing:** This ZIP is a revised release. Upload and commit all updated files including the entire `assets/client/` folder to the existing public GitHub repository `cyber2000tech/cybertechai` on branch `main`. The existing `CNAME`, `robots.txt` and `sitemap.xml` remain intact. Do not remove the custom domain setting.

## Homepage client-image presentation fix (October 2026)

The homepage previews now use responsive proportional media frames, with full-image containment, centered positioning, and inset spacing. The Venn diagram is constrained to fit within its presentation frame. This update changes only `index.html` image dimensions and `assets/styles.css` homepage styles; the source client images and detailed sections stay unchanged.


## Brand name update
The public-facing brand is **Cyber Tech**. The existing domain `cybertechai.us`, GitHub repository `cyber2000tech/cybertechai`, and the root `CNAME` file remain unchanged to avoid interrupting hosting or HTTPS.


## Cyber Tech client revision (October 12, 2026)
- Display name: Cyber Tech. The live domain remains cybertechai.us.
- Top navigation now displays Home, Services, Domains, and highlighted Contact. Mission is linked from the homepage card and footer.
- Homepage content follows the client-supplied replacement wording and the original investor notice remains exact.
- Services includes the client-provided wording, benefits, and two original service areas.
- Domains includes the three requested focus areas, learning statement, and all six slides from the available PowerPoint in their original order. Captions match the PowerPoint text.
- The latest-referenced second PowerPoint deck was not available among the attached files for this run. The deck used here was FOR THE WEB PAGE.pptx. Replace the six slide images and captions if the newer deck differs.
- Upload the extracted ZIP contents to the root of github.com/cyber2000tech/cybertechai; do not upload the ZIP as a single file. No DNS changes are needed.
