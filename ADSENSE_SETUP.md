# OrbitBrief AdSense Setup

OrbitBrief is prepared for AdSense review using publisher ID:

```text
ca-pub-6571112990031093
```

## Current State

- Static SEO/GEO pages include visual placeholder slots with class `orbitbrief-ad-slot`.
- The AdSense verification / Auto Ads script is included in HTML pages.
- `ads.txt` has been added at the site root.

## Active Verification Script

The following script is included inside `<head>`:

```html
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6571112990031093"
     crossorigin="anonymous"></script>
```

## When AdSense Is Approved

After approval, replace placeholder blocks:

```html
<div class="orbitbrief-ad-slot" aria-label="Future advertising slot">
  Future AdSense placement: responsive in-content unit.
</div>
```

with an AdSense unit:

```html
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-6571112990031093"
     data-ad-slot="YOUR_SLOT_ID"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
<script>
  (adsbygoogle = window.adsbygoogle || []).push({});
</script>
```

## Recommended Ad Placement

For OrbitBrief content pages:

- One in-content ad after the first two sections.
- One lower-page ad before FAQ.
- Avoid placing ads above the fold until traffic and UX are stable.

## SEO and Policy Notes

- Keep pages useful even without ads.
- Do not overload pages with ads.
- Do not ask users to click ads.
- Add privacy/cookie wording if required by your AdSense region/settings.
- Keep content original and avoid thin duplicate pages.

## Next Automation

When AdSense gives you ad slot IDs, the generator can be updated to output live AdSense units automatically across OrbitBrief pages.

