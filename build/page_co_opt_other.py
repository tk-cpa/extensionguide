import sys
sys.path.insert(0, "/home/claude/extensionguide/build")
from gen_states import page

SLOGAN = '<div class="slogan"><p>An extension to file is not an extension to pay tax.</p></div>'

def related(*items):
    links = "\n    ".join(
        f'<a href="{href}" class="related-link">{label}<span>{desc}</span></a>' for href, label, desc in items
    )
    return f'''<div class="related">
  <div class="related-title">Related</div>
  <div class="related-links">
    {links}
  </div>
</div>'''

page(
    "colorado-other-cities-opt-extension.html",
    "Colorado Other Cities Occupational Privilege Tax Extension Guide | Extension Guide",
    "Aurora, Greenwood Village, Sheridan, and Glendale each impose their own local Occupational Privilege Tax (OPT), structured like Denver's. No extension mechanism was found in any primary source checked for any of the four - confirmed against each city's own return form and, for Greenwood Village, its full taxpayer guide.",
    "Colorado - Other OPT Cities Extension Guide",
    "Aurora, Greenwood Village, Sheridan, Glendale &nbsp;&bull;&nbsp; No extension mechanism found &nbsp;&bull;&nbsp; Verified 9-23-2026",
    ["4 cities checked", "No extension mechanism found in any", "Same structure as Denver OPT"],
    "states-hub.html",
    SLOGAN + '''
<p class="lead">Colorado has five cities that impose a local Occupational Privilege Tax (OPT), sometimes called a "head tax": Denver (covered on its own page), Aurora, Greenwood Village, Glendale, and Sheridan. Each is a flat monthly per-employee amount owed by both employer and employee once an earnings threshold is met, collected on a short periodic remittance return rather than an annual income tax return. This page covers all four of the remaining cities, each checked directly against a primary source this session: Aurora, Greenwood Village, Sheridan, and Glendale.</p>

<div class="red-box"><strong>No extension mechanism was found for any of the four cities checked.</strong> Aurora's own OPT return form (Form COA STM 0101) has a late-filing penalty and interest line but no extension line or reference anywhere in the form or its instructions. Sheridan's quarterly OPT return form is identically structured - a late-filing penalty (10% or $15, whichever is greater) and 1%-per-month interest line, with no extension provision anywhere in the form. Glendale's OPT return form likewise has only a late-filing penalty (10% or $100, whichever is greater) and 1.5%-per-month interest line, with no extension provision. Greenwood Village's full taxpayer guide ("Understanding Taxes in Greenwood Village," over 17,000 characters, covering OPT filing frequency, thresholds, and remittance timing in detail) contains no mention of an extension of time to file. This mirrors the pattern already confirmed for Denver's OPT.</div>

<table class="dt">
<tr><th>City</th><th>Rate</th><th>Filing frequency</th><th>Extension mechanism</th></tr>
<tr><td>Aurora</td><td>$2/month employer + $2/month employee ($4 combined) per qualifying employee earning $250+/month</td><td>Monthly (per return due date shown on the form)</td><td>None found - Form COA STM 0101 has no extension line or reference</td></tr>
<tr><td>Greenwood Village</td><td>$2/month employer + $2/month employee ($4 combined) per qualifying employee earning $250+/month</td><td>Annual (2 or fewer employees), quarterly (up to 10 employees), or monthly (more than 10 employees)</td><td>None found - full taxpayer guide has no extension mention</td></tr>
<tr><td>Sheridan</td><td>$3/month employer + $3/month employee ($6 combined) per qualifying employee earning $500+/month, plus a $3/month minimum for self-employed owners/partners/managers even with no taxable employees</td><td>Quarterly, due the last day of the month following the quarter</td><td>None found - the return form has no extension line or reference</td></tr>
<tr><td>Glendale</td><td>$5/month employer + $5/month employee ($10 combined) per qualifying employee earning $750+/month</td><td>Monthly, quarterly, or annual by assignment (per return due date shown on the form)</td><td>None found - the return form has no extension line or reference</td></tr>
</table>
''' + related(
        ("states-hub.html", "All States", "Back to the states hub"),
        ("denver-opt-extension.html", "Denver OPT", "Colorado's largest OPT city - same structure, same finding"),
        ("colorado-extension.html", "Colorado (State)", "Colorado's own state income tax extension rules"),
    ),
    "Authority: City of Aurora Municipal Code (OPT); City of Sheridan Code of Ordinances, Part II, Ch. 62, Art. VI; City of Greenwood Village Municipal Code (OPT); City of Glendale Municipal Code (OPT). Sources: Aurora OPT Return Form COA STM 0101 (zillionforms.com mirror); City of Sheridan Occupational Privilege Tax Return (quarterly, zillionforms.com mirror); Greenwood Village \"Understanding Taxes in Greenwood Village\" taxpayer guide (zillionforms.com mirror); City of Glendale Occupational Privilege Tax Return (zillionforms.com mirror) - all searched directly for the word \"extension\" this session, no matches found. Sheridan's and Glendale's Municode ordinance pages (library.municode.com) are JavaScript-rendered and could not be retrieved as text this session; those two findings rest on the return form itself, not the ordinance text. Verified against primary source September 23, 2026.",
)

print("wrote colorado-other-cities-opt-extension.html")
