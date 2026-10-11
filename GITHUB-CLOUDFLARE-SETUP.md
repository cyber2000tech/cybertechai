# CybertechAI.us: GitHub and Cloudflare setup guide

## A. On the GitHub repository creation screen you sent

- **Owner**: `cyber2000tech`
- **Repository name**: `cybertechai` (keep it as shown)
- **Description** (optional): `XR, AI and digital twin engineering for cyber-human-physical systems.`
- **Choose visibility**: `Public` (GitHub Free Pages uses public repos)
- **Add README**: Off (this ZIP includes one)
- **Add .gitignore**: No .gitignore
- **Add license**: No license (select later only if you intend to license the code)
- Click **Create repository**.

## B. Upload extracted site contents, not the ZIP

Go to `https://github.com/cyber2000tech/cybertechai`, click **Add file -> Upload files**, drag in ALL files inside the extracted ZIP, including the `assets` folder, then choose **Commit changes**.

Important: `index.html` and `CNAME` must be in the **repository root**, not within a `cybertechai/` subfolder. The repository will contain four main HTML pages and `assets/`.

## C. Turn on GitHub Pages

Repository -> **Settings** -> **Pages** -> **Build and deployment**:

1. Source: `Deploy from a branch`
2. Branch: `main`
3. Folder: `/(root)`
4. Save.
5. Pages -> Custom domain: `cybertechai.us` -> Save.

The ZIP already contains `CNAME` with `cybertechai.us`. GitHub Pages may commit/update that same file when you save the custom domain.

## D. Cloudflare DNS -> Records

In Cloudflare, select `cybertechai.us`, open **DNS -> Records**, and create:

| Type | Name | Target / IPv4 address | Proxy status |
| --- | --- | --- | --- |
| A | @ | 185.199.108.153 | DNS only (gray) |
| A | @ | 185.199.109.153 | DNS only (gray) |
| A | @ | 185.199.110.153 | DNS only (gray) |
| A | @ | 185.199.111.153 | DNS only (gray) |
| CNAME | www | cyber2000tech.github.io | DNS only (gray) |

Set TTL to Auto. Optional IPv6 records for `@` (all DNS only): `2606:50c0:8000::153`, `2606:50c0:8001::153`, `2606:50c0:8002::153`, `2606:50c0:8003::153`.

**Check old records**: if `@` or `www` already has A, AAAA or CNAME records to parked domains/other hosts, replace those **website records**. Do not alter NS/SOA, MX, SPF, DKIM, DMARC, or verification TXT records unless you know why. Do not create wildcard `*` records.

The Cloudflare panel's `No Workers connected` is **normal**. You are deploying to GitHub Pages, not Cloudflare Workers.

## E. GitHub Pages HTTPS and verification

- Return to GitHub -> Settings -> Pages. When DNS validation completes and the certificate is ready, check **Enforce HTTPS**.
- It can take **up to 24 hours** for DNS/HTTPS to become ready. Do not rush to add extra conflicting DNS records.
- Visit https://cybertechai.us and https://www.cybertechai.us, and ensure the www hostname redirects appropriately.
- Click Services, Domains, Mission, and Contact; test on a phone as well as desktop.
- Open https://cybertechai.us/sitemap.xml and https://cybertechai.us/robots.txt.

## F. If Pages says DNS check unsuccessful

1. Double-check `CNAME` content is exactly `cybertechai.us`, and Pages custom domain is `cybertechai.us`.
2. Confirm Cloudflare has only the desired A / optional AAAA records for `@`, and CNAME for `www`.
3. Confirm records are **DNS only** (gray) during initial HTTPS setup, not Cloudflare Proxied (orange).
4. Check GitHub **Actions** for deployment errors and GitHub **Settings -> Pages** for deployment status.
5. Allow DNS propagation and certificate provisioning time. Don't switch SSL modes to `Flexible` to workaround errors.

Official docs:
- https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site
- https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site
- https://docs.github.com/en/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https
