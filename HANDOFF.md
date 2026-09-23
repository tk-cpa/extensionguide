# Extension Guide - Session Handoff

Last updated: 2026-09-23, end of T8 build session (adds estate-inheritance-tax-extensions.html: 13 states + DC estate tax, 4 states inheritance tax, gift tax scoped as federal-only). Jurisdictional coverage: all 50 states + DC + Puerto Rico + 8 city/local jurisdictions + state estate/inheritance tax live. Only excise tax edge cases remain unscoped. Two open items are flagged within the estate/inheritance data itself (Kentucky, Nebraska - no general filing-extension mechanism located in primary sources checked) rather than rounded up to verified.

## What this is

Site name: **Extension Guide** (a tk.cpa resource). Domain: **extensionguide.com** (purchased, DNS pointed at GitHub Pages). Repo: **tk-cpa/extensionguide** on GitHub, public. Deployment: **GitHub Pages**, branch `main`, root, static HTML (no build step). This is a brand-new, standalone site - not a rebrand of cpavalidated.com or globaltaxguide.com, though it shares their design system and workflow conventions.

Core locked slogan, must appear on every page: **"An extension to file is not an extension to pay tax."**

Scope: comprehensive public reference on US federal, state, and local tax filing extensions - all entity/tax types (individuals, C corps, S corps, partnerships, estates/trusts, nonprofits, information returns, estate tax, excise). Direct links to actual extension FORM PDFs on official tax-authority sites (not third-party mirrors) so users can print them, plus statute/authority citations for every rule.

## Current build status

**T1 - Federal (live):** index.html, disclaimer.html, faq.html, master-extension-matrix.html, federal-hub.html, and 5 federal form pages (4868, 7004, 8868, 4768, 8809), federal-special-situations.html, how-to-paper-file-extension.html, efile-and-third-party-services.html, extension-penalties-and-interest.html.

**T2/T3/T4 - All 50 states + DC (live):** every `<state>-extension.html` page exists and is cross-linked from states-hub.html, map.html, and the master matrix. Two system-level insights worth remembering: Ohio's ~600 municipalities and Michigan's ~24 taxing cities are each governed by a single statewide statute, which is why the local batch below consolidates them into one page apiece rather than hundreds of per-city pages.

**T5 - 8 city/local jurisdictions (live, this session):**
- `new-york-city-extension.html` - NYC individual tax rides on NY State Form IT-370 (no separate NYC form); business GCT/UBT uses Form NYC-6, automatic 6 months (up to two further 3-month extensions). N.Y.C. Admin. Code Sec. 11-605(1); NYC Rules tit. 19, ch. 11.
- `philadelphia-extension.html` - BIRT/NPT automatic, tied to the federal extension, no separate city form. Wage Tax has no individual extension mechanism (employer-withheld). Philadelphia Dept. of Revenue guidance.
- `ohio-municipal-extension.html` - covers all ~600 Ohio municipalities (RITA-administered, CCA-administered, or self-administered) under one statute, Ohio Rev. Code Sec. 718.05(G)(2).
- `michigan-cities-extension.html` - covers all ~24 Michigan cities with a city income tax, including Detroit, under one statute, MCL 141.664(1),(2). Written request required, up to 6 months, 70% payment threshold.
- `kansas-city-extension.html` - Kansas City, MO earnings tax, Form RD-112 (wage) / RD-111 (profits), automatic with timely filing and payment. KCMO Code of Ordinances ch. 68, art. VI.
- `st-louis-extension.html` - St. Louis, MO earnings tax, Form E-8 (individual) / Form E-234 (business), payment due with request. City of St. Louis Collector of Revenue guidance.
- `portland-multnomah-extension.html` - Portland/Multnomah County, OR combined business tax, Form EXT, 6 months, 90%/100% payment safe harbor. City of Portland/Multnomah County Revenue Division guidance.
- `san-francisco-extension.html` - SF Annual Business Tax Return extension request, not tied to the federal extension, full payment due by the original date. SF Office of the Treasurer and Tax Collector guidance.

**T6 - Puerto Rico (live, this session):**
- `puerto-rico-extension.html` - individuals and business entities both use the same form, Modelo SC 2644 ("Solicitud de Prorroga para Rendir la Planilla de Contribucion sobre Ingresos"), filed through SURI, automatic upon a timely request, typically 6 months, payment not extended. Authority: 13 L.P.R.A. Sec. 1061.03(c), 1061.06(c), 1061.07(c), 1061.09(b)(4), 1061.10(b)(2), 1061.16 (P.R. Internal Revenue Code), re-confirmed annually by a Carta Circular de Rentas Internas (CC RI 26-01 for tax year 2025). Note on the page itself: this covers the Puerto Rico Treasury (Hacienda) extension only, not federal filing questions for PR residents (IRC Sec. 933 and related), which are out of scope.

`extensions-data.json` now has 75 records (Federal + 50 states/DC + 8 local jurisdictions + Puerto Rico, with New York City, Philadelphia, and Puerto Rico each contributing 2 records for split regimes/filer types). `map.html`'s STATES object is fully populated - every FIPS code including "72" (Puerto Rico) now has a real `slug`, so there are no `slug:null` entries left. Its CITIES array carries a `slug` per city and all pins (state and city) render live/clickable; the map's "coming soon" legend swatch and related stale copy were removed since nothing is pending except the excise/estate edge cases noted below. states-hub.html (added a Puerto Rico row to the "Live now" table), master-extension-matrix.html (build-status table), index.html, llms.txt, search-index.json (76 entries), and sitemap.xml were all updated in the same batch.

**Corrected in-session (T5, caught during verification, never shipped wrong):** New Hampshire's Interest & Dividends Tax was repealed effective for tax periods beginning 1-1-2025 (2024 was the last taxable year). `new-hampshire-extension.html` was rewritten to state this; only the Business Profits Tax (Form BT-EXT, N.H. Code Admin. R. Rev 307.09) still has an active extension mechanism there.

**Remaining gap (intentional, not an oversight):** excise tax and estate/inheritance edge cases have not been scoped or built. Every state, DC, Puerto Rico, and the 8 city/local jurisdictions the user asked for by name are live - this is genuinely full US jurisdictional coverage for the core individual/business income-tax extension use case.

**T7 - this session's corrections and additions:**
- **North Dakota citation corrected.** A user-requested re-verification found that N.D. Cent. Code Sec. 57-38-34(6) - previously cited alone for the "automatic" federal-conformity rule - actually only text reads "the tax commissioner may grant a reasonable extension of time for filing a return when, in the judgment of the tax commissioner, good cause exists." The statute never uses the word "automatic"; that description comes from the ND Tax Commissioner's own published administrative practice applying that same discretionary authority (confirmed via tax.nd.gov/filing-extension). `north-dakota-extension.html` was rewritten to state this precisely: the statute is cited for the Commissioner's general extension authority, and the "automatic" conformity-to-federal-extension practice is attributed to the Tax Commissioner's guidance, not the statute's text.
- **"Verified [date]" removed from every page.** Per explicit instruction, the "Verified 9-2X-2026" badge/tagline text and the "Verified against primary source [date]." sentence in each page's source-row were stripped from all 76 pages that had them (69 via a site-wide script, 3 - faq.html, federal-hub.html, federal-special-situations.html - by hand for edge-case phrasing). This is a display choice only; the underlying verification discipline (checking every fact against primary source before publishing) is unchanged.
- **New `resources.html` page**, added to the nav bar on every page (inserted between "Penalties & Interest" and "FAQ") and to `build/gen_states.py`'s `cat_nav()` for all future pages. Lists official IRS resources (Get an Extension, Free File, Direct Pay, EFTPS, Taxpayer Advocate Service) and two IRS-authorized commercial e-file providers, TaxExtension.com and FileLater.com (both confirmed live and IRS-authorized on their own sites this session), clearly labeled as non-endorsed, no affiliate relationship, official-first. Also fixed a pre-existing plain-text typo on `efile-and-third-party-services.html` ("taxextensions.com" with an s, unlinked) to correctly name and link both real providers and point to the new resources page.

**Quality gate**: all 77 HTML files pass lint (no em-dashes, no forbidden strings 109025/AC58472/P00646638/93250/Knyazev/"Prepared by", disclaimer link present, canonical tag present, balanced divs, Map and Resources nav links present, no leftover "Verified" text). extensions-data.json (75 records), search-index.json (77 records) validated as JSON; sitemap.xml (77 entries) validated as XML - all three counts cross-checked against the 77 files on disk with zero mismatches and zero orphan/dangling links. All 125 external URLs site-wide curl-verified this session; the 11 that return 403/302/000 to curl (github.com, mtc.dor.state.ma.us, mypath.pa.gov, otr.cfo.dc.gov, tax.ri.gov, kcmo.gov, mass.gov x2, ny.gov, revenue.nh.gov, taxes.marylandtaxes.gov) were each independently re-confirmed real and on-topic via WebFetch or WebSearch this session - bot-blocked/egress-blocked, not broken. No genuine 404s remain unfixed as of this handoff.

## BLOCKER: git push is not working

Every `git push origin main` attempt fails identically:

```
remote: access denied by the git proxy: tk-cpa/extensionguide is not in this
session's authorized repository set, so the proxy will not inject a credential
for it. To fix, add the repository to the session's sources.
fatal: unable to access 'https://github.com/tk-cpa/extensionguide.git/':
The requested URL returned error: 403
```

This is a session-level/connector-level allowlist issue on Anthropic's proxy, not a GitHub permissions problem. It has persisted across every session so far. The established workaround, used every batch: commit locally as normal (preserves history for whenever push starts working), then zip the site directory and deliver via SendUserFile for the user to upload manually through GitHub's web "Add file -> Upload files" UI in `tk-cpa/extensionguide`. Do not dwell on this blocker in conversation - attempt the push once per commit, note the result in one line if at all, and move straight to the zip/delivery step.

## DNS / HTTPS status

4 GitHub Pages A records at the registrar (GoDaddy) for `@`: 185.199.108.153, .109.153, .110.153, .111.153. `www CNAME -> extensionguide.com` left in place. DNS propagated; HTTPS/SSL provisioning status should be spot-checked periodically in Settings -> Pages -> "Enforce HTTPS" but needs no action absent a problem report.

## Repo structure and conventions (must follow for all future pages)

- Static HTML, no build step, all CSS/JS inline in each page (no external files except Google Fonts, D3/topojson for map.html).
- Design system: coral #F65F5A / ink #111111 / paper #FAFAF7. Oswald (display) + Inter (sans) + Courier New (mono) via Google Fonts.
- Canonical page anatomy: sticky nav (brand wordmark + tk.cpa CTA button) -> dark cat-nav bar (Home / Federal / States / Map / Master Matrix / Penalties & Interest / Resources / FAQ / Disclaimer) -> dark-hero `.ph` block (h1/sub/badges) -> `.article` content -> `.source-row` citation line -> print button -> `.disc` disclaimer line -> dark footer bar ("a tk.cpa resource" + tk.cpa link). Pages no longer show a "Verified [date]" badge or source-row sentence - that was removed site-wide per explicit instruction; don't re-add it to new pages. Caution: the historical one-off batch scripts under `build/` (pages_states3.py through pages_states5.py, pages_local1.py, page_pr.py) still have "Verified [date]" baked into their `sub` and `source_row` string literals from when they were written - they were run once to produce the live HTML and are not meant to be re-run verbatim. If a future session re-runs any of them, strip the "Verified ..." fragments from the regenerated output, or better, edit the affected page directly instead of regenerating it from the old script.
- Shared build library: `build/gen_states.py` (CSS constant, `cat_nav()`, `FOOTER`, `page()` function). Batch scripts (e.g. `build/pages_states5.py`, `build/pages_local1.py`) import from it and call `page()` once per jurisdiction, then are executed with `python3 build/<script>.py`.
- `extensions-data.json` is the single source of truth. Schema: jurisdiction, tax_type, filer, form, form_name, automatic, federal_extension_honored, payment_triggered_only, length, payment_threshold, efile_url, form_pdf_url, about_form_url, paper_address_source_url, authority, source_url, verified_as_of. master-extension-matrix.html renders it client-side via fetch, splitting on `jurisdiction === 'Federal'` vs everything else (state and local jurisdictions share the same non-federal table).
- Every green-box "Get the form" callout links directly to the official PDF plus the tax authority's About/instructions page - never a third-party form mirror.
- Content hard rules (per tk.cpa operating framework): no em dashes; forbidden strings 109025/AC58472/P00646638/93250/Knyazev/"Prepared by" must never appear; capitalize Client/Clients (n/a on this public site); full 4-digit years; zero extra branding beyond "a tk.cpa resource" footer pattern already established.
- SEO/AI files to update on every batch: sitemap.xml, llms.txt (llmstxt.org format), search-index.json, and master-extension-matrix.html's build-status table.
- Before any commit: run the lint gate (forbidden strings, em-dash, disclaimer link presence, canonical tag presence, div-tag balance, Map nav link) and curl-verify every external link returns 200 (curl 403/000 on a known-government/legal host is not automatically a break - confirm via WebFetch/WebSearch before concluding it's fine, and always chase down and fix an actual 404).
- Filenames: `<state-name>-extension.html` lowercase with dashes for states; `<city-name>-extension.html` for local jurisdictions (consolidate a whole state's municipalities into one page when a single statewide statute governs them, as with Ohio and Michigan); `federal-<form>-<description>.html` for federal.

## T8 additions (this session)

- **estate-inheritance-tax-extensions.html** (NEW): one consolidated page covering state estate tax extensions for 13 states + DC (CT, HI, IL, ME, MD, MA, MN, NY, OR, RI, VT, WA, DC) and state inheritance tax extensions for 4 states (KY, NE, NJ, PA). Maryland has both taxes and appears in both tables. Gift tax extensions are scoped as federal-only (Form 4768/IRC sect 6081) - Connecticut is the only state with its own gift tax and its extension rides the same combined CT-706/709 EXT form as its estate tax.
- **extensions-data.json**: grew from 75 to 92 records (17 new: 13 estate-tax states + DC, 4 inheritance-tax-only states).
- **Two open items flagged, not fabricated**: Kentucky (KRS ch. 140) - no general filing-extension provision was located in the statute; only a deferred-payment election for certain future interests exists (KRS 140.210/140.220-140.224), which is not the same thing. Nebraska - inheritance tax is filed with the county court as part of probate, not via a Department of Revenue extension form; there is no formal filing extension, only a county-court penalty-abatement mechanism for good cause. Both are stated as open items on the page itself, not rounded up to "verified."
- **Statute citations pinned to exact sections via primary source this session** (not carried over from memory): Conn. Gen. Stat. sect 12-392; Haw. Rev. Stat. sect 236E-9; 35 ILCS 405/6; 36 M.R.S. sect 4110; Md. Code Tax-Gen. sect 7-305.1; Minn. Stat. sect 289A.19 subd. 4; N.Y. Tax Law sect 976(a)(1); Or. Rev. Stat. sect 118.100; 32 V.S.A. sect 7481; RCW 83.100.050; D.C. Code sect 47-3705(b); Neb. Rev. Stat. sect 77-2010. Massachusetts, Rhode Island, New Jersey, Illinois, and Pennsylvania are cited to the governing chapter/regulation plus the agency form/instructions rather than one pinpoint subsection, because a live primary source naming the exact subsection was not found this session - this is disclosed, not glossed over.
- Cross-linked from index.html, states-hub.html, and master-extension-matrix.html (build-status table, note-box, and a new stateTable row set per jurisdiction that renders automatically from extensions-data.json). Not added to the persistent top cat-nav, consistent with how every other individual content page (state pages, local-jurisdiction pages, federal form pages) is linked from hub pages rather than the top nav.
- sitemap.xml, search-index.json, llms.txt all updated. File count: 78 HTML pages (up from 77).

## Next build queue

1. **Excise tax edge cases** - not yet scoped. This is the only substantive content gap left on the site.
2. **FAQ buildout** - faq.html exists (T1) but has not been revisited since; consider whether it needs new entries now that state, local, Puerto Rico, and estate/inheritance coverage is complete.
3. Maintain a progress register tracking every jurisdiction x tax-type record's status (verified/drafted/live) - not yet built as a standalone file; could live as a project doc or a simple markdown table in the repo.
4. If time allows, a second pass on Massachusetts, Rhode Island, New Jersey, Illinois, and Pennsylvania to pin the exact statutory subsection for each state's extension-granting authority (currently cited to the governing chapter/regulation plus the agency form).

## Delivery workflow until push is fixed

1. Build the batch (new HTML pages + updated extensions-data.json + updated nav/map/sitemap/llms.txt/search-index.json/master-matrix/states-hub/index).
2. Run the lint gate script, JSON/XML validation, and the link-verification curl loop over every external URL site-wide (not just the new batch - a shared file like map.html or states-hub.html can pick up a stale link during editing).
3. `git add -A && git commit -m "..."` locally (keep committing normally even though push is blocked - preserves history for whenever push starts working).
4. Attempt `git push origin main` once; expect the identical 403 above; do not dwell on it.
5. `zip -r /mnt/user-data/outputs/extensionguide-<batch-name>.zip . -x ".git/*" -x "build/__pycache__/*"` from `/home/claude/extensionguide`.
6. SendUserFile the zip.
7. Ask the user to upload via GitHub's web "Add file -> Upload files" UI (uploading the full file set overwrites in place; GitHub Pages rebuilds automatically from `main`).
