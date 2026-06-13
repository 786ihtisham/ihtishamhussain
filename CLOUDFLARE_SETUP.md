# Cloudflare Pages setup — ihtishamhussain.com

Complete walkthrough from 404 to live portfolio.

**Cost:** $0 (Free plan)

---

## Current status

| Item | Status |
|------|--------|
| Domain on Cloudflare | ✅ Nameservers: `moura.ns.cloudflare.com`, `dina.ns.cloudflare.com` |
| Live site | ❌ **404** — no Pages project attached |
| Site code ready | ✅ `ihtishamhussain-site/` in this workspace |
| GitHub repo | Push with `gh repo create ihtishamhussain` (see README) |

---

## Part 1 — Cloudflare account

### Step 1: Log in

1. Open https://dash.cloudflare.com
2. Use the email tied to your domain registrar or old hosting

### Step 2: Find the domain

If `ihtishamhussain.com` is already in your dashboard (likely — nameservers point to Cloudflare), click it and go to **Part 2**.

If not listed:
1. **Add a site** → enter `ihtishamhussain.com`
2. Choose **Free** plan
3. Confirm nameservers match your registrar

---

## Part 2 — Create Pages project

### Step 3: Connect GitHub

1. Dashboard → **Workers & Pages** → **Create** → **Pages** → **Connect to Git**
2. Authorize **Cloudflare Pages** on GitHub
3. Select repository: **786ihtisham/ihtishamhussain**

### Step 4: Build settings

This is a **static site** — no build step needed.

| Field | Value |
|-------|--------|
| Project name | `ihtishamhussain` |
| Production branch | `main` |
| Framework preset | **None** |
| Build command | *(empty)* |
| Build output directory | `/` |

Click **Save and Deploy**. First deploy takes ~30 seconds.

**Preview URL:** `https://ihtishamhussain.pages.dev`

---

## Part 3 — Custom domain

### Step 5: Attach ihtishamhussain.com

1. Pages project → **Custom domains**
2. **Set up a custom domain** → `ihtishamhussain.com` → **Continue**
3. Repeat for `www.ihtishamhussain.com`

Cloudflare creates DNS records automatically when the zone is in the same account.

### Step 6: Clean up old DNS

Go to **Websites** → `ihtishamhussain.com` → **DNS** → **Records**.

**Delete** any records pointing to dead hosting (old WordPress server IPs, Ezoic, etc.).

**Keep** records Pages creates:
- `ihtishamhussain.com` → CNAME → `ihtishamhussain.pages.dev` (proxied)
- `www` → CNAME → `ihtishamhussain.pages.dev` (proxied)

### Step 7: SSL

**SSL/TLS** → mode **Full**. HTTPS is automatic.

---

## Part 4 — Verify

Wait 1–2 minutes after deploy, then check:

- [ ] https://ihtishamhussain.com/
- [ ] https://ihtishamhussain.com/about/
- [ ] https://ihtishamhussain.com/portfolio/
- [ ] https://ihtishamhussain.com/contact/
- [ ] https://www.ihtishamhussain.com/ loads or redirects
- [ ] Profile photo displays
- [ ] Links to DataSourceCode & MonolithX work

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Still 404 after deploy | Old DNS records still active — clean up Step 6 |
| Domain on another Cloudflare account | Log in with old email or reset nameservers at registrar |
| GitHub repo not listed | GitHub → Settings → Applications → Cloudflare Pages → grant repo access |
| www doesn't work | Add `www.ihtishamhussain.com` as custom domain in Pages |
| `/privacy-policy-2/` 404 | `_redirects` file redirects to `/privacy-policy/` |

---

## Deploy both sites from one account

You can host **both** domains on the same free Cloudflare account:

| Domain | Pages project | Repo |
|--------|---------------|------|
| datasourcecode.com | `datasourcecode` | `786ihtisham/DataSourceCode` |
| ihtishamhussain.com | `ihtishamhussain` | `786ihtisham/ihtishamhussain` |

Unlimited sites on the Free plan.

---

## Quick reference

```
Account:     https://dash.cloudflare.com
GitHub repo: https://github.com/786ihtisham/ihtishamhussain
Branch:      main
Build:       (none — static HTML)
Output:      / (root)
Plan:        Free ($0)
```
