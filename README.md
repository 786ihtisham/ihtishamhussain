# ihtishamhussain.com

Static personal portfolio for [ihtishamhussain.com](https://ihtishamhussain.com), deployed on **Cloudflare Pages (Free)**.

Recovered from the [Wayback Machine snapshot (Mar 2024)](https://web.archive.org/web/20240320020819/https://ihtishamhussain.com/) and updated with current CV data (TH OWL, MonolithX, Adept Tech).

| Path | Content |
|------|---------|
| `/` | Homepage — hero, skills, experience |
| `/about/` | About & education |
| `/services/` | Services offered |
| `/portfolio/` | Projects (MonolithX, DataSourceCode, etc.) |
| `/contact/` | Contact & social links |

## Local preview

```bash
cd ihtishamhussain-site
python3 -m http.server 8080
```

Open http://localhost:8080

## Cloudflare Pages (Git)

### 1. Push to GitHub

```bash
cd ihtishamhussain-site
git init
git add .
git commit -m "Recover ihtishamhussain.com portfolio for Cloudflare Pages"
gh repo create ihtishamhussain --public --source=. --remote=origin --push
```

### 2. Pages settings

Dashboard → **Workers & Pages** → **Create** → **Pages** → **Connect to Git** → `786ihtisham/ihtishamhussain`

> Full walkthrough: **[CLOUDFLARE_SETUP.md](./CLOUDFLARE_SETUP.md)**

| Setting | Value |
|---------|--------|
| Production branch | `main` |
| Framework preset | **None** |
| Build command | *(leave empty)* |
| Build output directory | `/` (root) |

### 3. Custom domain

Pages project → **Custom domains** → add `ihtishamhussain.com` and `www.ihtishamhussain.com`.

## DNS status

- Nameservers: `moura.ns.cloudflare.com`, `dina.ns.cloudflare.com` ✅
- Current live status: **404** — domain on Cloudflare but no Pages project attached yet

## Archive reference

- Best snapshot: https://web.archive.org/web/20240320020819/https://ihtishamhussain.com/
- Original: WordPress + Astra + Elementor personal portfolio
