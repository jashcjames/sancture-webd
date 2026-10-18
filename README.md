# Sancture website

Static site for GitHub Pages. No build step needed (build.py only regenerates the HTML).

## Before going live
1. Replace the domain `www.sancture.in` in `CNAME`, `build.py` (D), sitemap.xml and robots.txt, then run `python3 build.py`.
2. Replace placeholder email, phone, WhatsApp number and office address in `build.py`.
3. Create a free form at formspree.io and put its ID in `contact.html` (YOUR_FORM_ID).
4. Replace `assets/logo.png` with a higher resolution logo if you have one.

## Deploy
1. Push this folder to a GitHub repository.
2. Settings > Pages > Deploy from branch (main, root).
3. Add a CNAME DNS record for `www` pointing to `<username>.github.io`, and A records for the apex domain to GitHub Pages IPs (see GitHub docs).
4. Tick Enforce HTTPS.
