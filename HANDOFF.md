# Extension Guide - Session Handoff

Last updated: 2026-09-23, mid T2 build session (15 states live).

## What this is

Site name: **Extension Guide** (a tk.cpa resource). Domain: **extensionguide.com** (purchased, DNS now pointed at GitHub Pages, HTTPS provisioning). Repo: **tk-cpa/extensionguide** on GitHub, public. Deployment: **GitHub Pages**, branch `main`, root, static HTML (no build step). This is a brand-new, standalone site - not a rebrand of cpavalidated.com or globaltaxguide.com, though it shares their design system and workflow conventions.

Core locked slogan, must appear on every page: **"An extension to file is not an extension to pay tax."**

Scope: comprehensive public reference on US federal, state, and local tax filing extensions - all entity/tax types (individuals, C corps, S corps, partnerships, estates/trusts, nonprofits, information returns, estate tax, excise). Direct links to actual extension FORM PDFs on official tax-authority sites (not third-party mirrors) so users can print them, plus statute/authority citations for every rule. Goal stated by the user: "the most robust, most comprehensive guide on extensions ever made."

## Current build status

**T1 - Federal (live, committed, delivered):** index.html, disclaimer.html, faq.html, master-extension-matrix.html, federal-hub.html, and 5 federal form pages (4868, 7004, 8868, 4768, 8809), federal-special-situations.html, how-to-paper-file-extension.html, efile-and-third-party-services.html, extension-penalties-and-interest.html. Every federal form has a green-box with a direct PDF link + About-Form link, sourced from irs.gov this session.

**T2 - 15 states live (built, committed, delivered as zip - NOT yet uploaded to GitHub, see blocker below):** california-extension.html, new-york-extension.html, texas-extension.html, florida-extension.html, illinois-extension.html, pennsylvania-extension.html, new-jersey-extension.html, massachusetts-extension.html, ohio-extension.html, washington-extension.html, oregon-extension.html, georgia-extension.html, north-carolina-extension.html, virginia-extension.html, michigan-extension.html, states-hub.html. Master matrix renders state rows live from extensions-data.json (now 25 records: Federal + 15 states). sitemap.xml, llms.txt, search-index.json all updated with all 15 state pages.

Key facts verified this session for T2, first batch (CA/NY/TX/FL/IL - all authority citations verified against primary source 2026-09-22):
- **California**: both individual and business extensions automatic, no application form. Individual: Cal. Code Regs. tit. 18 §18567, 6 months. Business: R&TC §18604, 7-month aggregate cap for corps/banks (6 months for S-corps/partnerships/LLCs).
- **New York**: NOT automatic in the sense of "no form" - individual Form IT-370 (N.Y. Tax Law §657) and corporate Form CT-5 (N.Y. Tax Law §1085) both required, both must be filed by the original due date, CT-5 requires an estimated payment.
- **Texas**: no individual income tax. Franchise tax only, Form 05-164, NOT automatic, 34 Tex. Admin. Code §3.585. First extension to Aug 17, 2026; second (EFT-mandated filers) to Nov 16, 2026. Payment threshold: 100% of prior year tax or 90% of current year tax.
- **Florida**: no individual income tax. Corporate income tax only, Form F-7004, NOT automatic, Fla. Stat. §220.222 / §220.32. Must pay 100% of tentative tax with the request; extension voids if underpayment exceeds greater of $2,000 or 30% of tax shown when filed.
- **Illinois**: both individual and corporate extensions automatic, no application form. 35 ILCS 5/505; 86 Ill. Admin. Code §100.5020. Individual 6 months (matches longer federal extension if applicable), corporate 7 months (8 for June 30 fiscal year).
- **Open item**: Illinois Form IL-505-B (corporate payment voucher) has no locatable current-year direct PDF on tax.illinois.gov as of this session - the page links to the Department's forms hub instead of a guessed/stale URL. Flagged on the page itself.

Key facts verified this session for T2, second batch (PA/NJ/MA/OH/WA/OR/GA/NC/VA/MI - all authority citations verified against primary source 2026-09-23):
- **Pennsylvania**: semi-automatic - if federal extension filed and no PA tax due, no PA form needed; otherwise Form REV-276, 61 Pa. Code §117.14, 6 months.
- **New Jersey**: NOT automatic, Form NJ-630, 80% payment threshold or extension is void, N.J.A.C. 18:35-6.1, 6 months individual / 5.5 months fiduciary.
- **Massachusetts**: individual/fiduciary conditional-automatic (80% payment threshold or void), Form M-4868/M-8736; partnerships fully automatic (Form 3). M.G.L. c. 62C §19; 830 CMR 62C.19.1.
- **Ohio**: fully automatic, matches federal extension period exactly, no separate state form. Ohio Rev. Code §5747.08; Ohio Admin. Code §5703-7-05.
- **Washington**: no individual or corporate income tax. B&O excise tax return extensions are discretionary/good-cause only (system failure, lost records, medical emergency, natural disaster - not financial hardship); deposit required beyond 30 days. Wash. Admin. Code §458-20-228(13).
- **Oregon**: individual automatic with federal extension, no separate form; corporations use federal Form 7004 directly, extended due date 15 days after the federal one. Or. Rev. Stat. §314.385.
- **Georgia**: automatic if federal extension attached (Form 4868/7004 or IRS confirmation letter); Form IT-303 otherwise. O.C.G.A. §48-7-57, up to 6 months.
- **North Carolina**: automatic with federal extension (certify on the return); Form D-410 otherwise. 90% payment rule affects late-payment penalty only, not extension validity. N.C. Gen. Stat. §105-263.
- **Virginia**: fully automatic, no application required at all (not even a copy of the federal extension). 90% payment rule under Va. Code §58.1-344. Original due date May 1 (later than federal), extended to Nov 1.
- **Michigan**: NOT automatic - Form 4 or a copy of the federal extension, plus an estimated payment, required by the original due date. Mich. Comp. Laws §206.311.
- **Fixed**: a dead nj.gov link (`extension.shtml`, 404) was replaced with the correct live page (`njit27.shtml`, "When to File and Pay") in both `new-jersey-extension.html` and `extensions-data.json`.

**Quality gate**: all HTML files pass lint (no em-dashes, no forbidden strings 109025/AC58472/P00646638/93250/Knyazev, disclaimer link present, canonical tag present, balanced divs). Every external link across all 15 state pages curl-verified (one broken Texas Webfile URL and one broken New Jersey URL were found and fixed before delivery). A few source pages (mass.gov, justia.com, ilga.gov) return 403/000 to automated curl but are confirmed readable via WebFetch - treated as bot-blocked, not broken, per established precedent; genuine 404s are always fixed.

**Local git state**: 3 commits ahead of what's actually live on GitHub -
- `7fad204` - T1 federal build
- `b6a5db9` - T2 first batch (CA/NY/TX/FL/IL)
- `20a3bbb` - T2 second batch (PA/NJ/MA/OH/WA/OR/GA/NC/VA/MI)
All three commits are clean, tested, and ready to push. They have NOT been pushed - see blocker below (still unresolved, identical error, as of this session). The T1 content did make it to GitHub already via manual zip upload through GitHub's web UI (user did this once already, successfully). Nothing since T1 has been manually uploaded by the user as of this handoff - the T2 batches only exist in zips delivered via SendUserFile (`extensionguide-t2.zip`, `extensionguide-t2b.zip`).

## BLOCKER: git push is not working

Every `git push origin main` attempt fails identically, tested repeatedly across this and prior sessions with different PATs:

```
remote: access denied by the git proxy: tk-cpa/extensionguide is not in this
session's authorized repository set, so the proxy will not inject a credential
for it. To fix, add the repository to the session's sources.
fatal: unable to access 'https://github.com/tk-cpa/extensionguide.git/':
The requested URL returned error: 403
```

This is a **session-level / connector-level allowlist** enforced by Anthropic's own proxy (confirmed via `env | grep -i git` showing `GITHUB_TOKEN=proxy-injected` - the proxy substitutes its own credential for repos it recognizes and refuses everything else, ignoring any PAT supplied in the remote URL). It is NOT a GitHub-side permissions problem in the traditional sense (not an App installation issue - confirmed the user has no GitHub Apps installed on their personal account, `tk-cpa` is a personal username, not an org). `cpavalidated` and `globaltaxguide` push successfully because they were already in this allowlist from earlier sessions; `extensionguide` is a new repo created mid-session and was never added.

**What's been tried and ruled out:**
- Regenerating/swapping the PAT in the remote URL - no effect, proxy ignores it for unauthorized repos.
- Checking github.com Settings → Applications → Installed GitHub Apps - shows "No installed GitHub Apps," ruling out a GitHub App repo-access-list fix.
- User confirmed GitHub Integration connector is already connected in Claude's own Settings → Connectors, and has been for a while (that's why the other two repos work).

**What's in progress as of this handoff:**
- User was about to try Disconnect → Reconnect on the GitHub connector in Claude Settings → Connectors, on the theory that reconnecting will trigger GitHub's OAuth authorization screen again, which may include a repository-selection step where `extensionguide` (or "All repositories") can be explicitly granted.
- User was also going to test whether a brand-new conversation/session (separate from this one) can push successfully, to check whether an existing connector-setting change just needs a fresh session to take effect, versus needing an actual reconnect.

**Next step for whoever picks this up:** ask the user directly what happened with the disconnect/reconnect and the fresh-session test. If push now works, push the 2 pending commits (`7fad204`, `b6a5db9`) immediately - do not rebuild that content. If it's still blocked, the workaround is: zip the site directory (`zip -r extensionguide.zip . -x ".git/*"` from `/home/claude/extensionguide`), deliver via SendUserFile, and ask the user to upload via GitHub's web "Add file → Upload files" UI in `tk-cpa/extensionguide` (this has worked reliably both times it's been used).

## DNS / HTTPS status

User added the 4 required GitHub Pages A records at the registrar (GoDaddy) for `@`: 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153. The old "Parked" A record was deleted. The existing `www CNAME → extensionguide.com` record was left in place (correct, since the GitHub Pages custom domain is the apex, not www). NS, SOA, `_domainconnect`, and `_dmarc` TXT records were left untouched (unrelated). As of this handoff: DNS has propagated and the site loads over HTTP; HTTPS/SSL is still provisioning on GitHub's side (automatic once DNS is verified, typically minutes to an hour - no action needed, just wait and check Settings → Pages → "Enforce HTTPS" periodically).

## Repo structure and conventions (must follow for all future pages)

- Static HTML, no build step, all CSS/JS inline in each page (no external files except Google Fonts).
- Design system: coral #F65F5A / ink #111111 / paper #FAFAF7. Oswald (display) + Inter (sans) + Courier New (mono) via Google Fonts.
- Canonical page anatomy: sticky nav (brand wordmark + tk.cpa CTA button) → dark cat-nav bar (Home / Federal / States / Master Matrix / Penalties & Interest / FAQ / Disclaimer) → dark-hero `.ph` block (h1/sub/badges) → `.article` content → `.source-row` citation line → print button → `.disc` disclaimer line → dark footer bar ("a tk.cpa resource" + tk.cpa link).
- `extensions-data.json` is the single source of truth. Schema: jurisdiction, tax_type, filer, form, form_name, automatic, federal_extension_honored, payment_triggered_only, length, payment_threshold, efile_url, form_pdf_url, about_form_url, paper_address_source_url, authority, source_url, verified_as_of. master-extension-matrix.html renders it client-side via fetch.
- Every green-box "Get the form" callout links directly to the official PDF plus the tax authority's About/instructions page - never a third-party form mirror.
- Content hard rules (per tk.cpa operating framework): no em dashes; forbidden strings 109025/AC58472/P00646638/93250/Knyazev must never appear; capitalize Client/Clients (n/a on this public site, no Client-specific content); full 4-digit years; zero extra branding beyond "a tk.cpa resource" footer pattern already established.
- SEO/AI files to update on every batch: sitemap.xml, llms.txt (llmstxt.org format), search-index.json, and master-extension-matrix.html's build-status table and JS render.
- Before any commit: run the lint gate (forbidden strings, em-dash variants, disclaimer link presence, canonical tag presence, div-tag balance) and curl-verify every external link returns 200.
- Filenames: `<state-name>-extension.html` lowercase with dashes for states; `federal-<form>-<description>.html` for federal.

## Next build queue (in priority order, per original plan)

1. **T3**: remaining ~35 states + DC (15 states now live: CA, NY, TX, FL, IL, PA, NJ, MA, OH, WA, OR, GA, NC, VA, MI).
2. **T4**: city/local taxes - NYC, Philadelphia, Ohio RITA/CCA municipalities, Michigan cities, Kansas City, St. Louis, Portland/Multnomah County, San Francisco.
3. **T5**: excise, estate/inheritance edge cases, FAQ buildout.
4. **US states interactive map** - raised by the user mid-session as "what about the US map??" (this had been explicitly deferred until state pages existed). Not yet resolved with a firm decision: option (a) finish remaining states first, then build the map with full coverage; option (b) build the map now with the 15 live states linked and the rest shown as "coming soon" stubs. Reference pattern for the build itself is globaltaxguide.com/map.html: SVG `<object>` embed, region filter buttons with `data-region`, pin-chip links for small jurisdictions, CC BY-SA 3.0 base map credit. Whoever picks this up should get the user's call on timing before building.
5. Maintain a progress register tracking every jurisdiction × tax-type record's status (verified/drafted/live) - not yet built as a standalone file, should be created (could live as a project doc or a simple markdown table in the repo).

## Delivery workflow until push is fixed

1. Build the batch (new HTML pages + updated extensions-data.json + updated nav/sitemap/llms.txt/search-index.json/master-matrix).
2. Run the lint gate script and link-verification curl loop.
3. `git add -A && git commit -m "..."` locally (keep committing normally even though push is blocked - preserves history for whenever push starts working).
4. `zip -r /mnt/user-data/outputs/extensionguide-<batch-name>.zip . -x ".git/*"` from `/home/claude/extensionguide`.
5. SendUserFile the zip.
6. Ask the user to upload via GitHub's web "Add file → Upload files" UI (uploading the full file set overwrites in place; GitHub Pages rebuilds automatically from `main`).
