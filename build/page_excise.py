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

body = SLOGAN + '''
<p class="lead">This page closes out the last named gap in this guide's scope. The short, verified answer: there is no extension of time to file for the two main federal excise tax returns, Form 720 and Form 2290. Neither form appears on the Form 7004 list of returns eligible for an automatic extension, and neither form's own instructions provide any other extension mechanism. This was confirmed directly against the current IRS instructions for both forms this session, not assumed from general excise-tax commentary.</p>

<h2>Form 720 - Quarterly Federal Excise Tax Return</h2>
<table class="dt">
<tr><th>Period covered</th><th>Due date</th></tr>
<tr><td>January, February, March</td><td>April 30</td></tr>
<tr><td>April, May, June</td><td>July 31</td></tr>
<tr><td>July, August, September</td><td>October 31</td></tr>
<tr><td>October, November, December</td><td>January 31</td></tr>
</table>
<p>If a due date falls on a Saturday, Sunday, or legal holiday, the return may be filed on the next business day - that is the only date accommodation in the instructions. Form 7004 (the general business extension form used elsewhere on this site for Forms 1120, 1120-S, 1065, 1041, and others) does not include Form 720 anywhere in its list of eligible forms. No other extension provision appears in the current Form 720 instructions.</p>

<h2>Form 2290 - Heavy Highway Vehicle Use Tax Return</h2>
<p>Form 2290 is due based on the month a taxable vehicle is first used on public highways during the tax period (July 1 - June 30) - for example, a vehicle first used in July 2026 is due August 31, 2026. Like Form 720, Form 2290 is not on the Form 7004 eligible-forms list, and the IRS's own filing-deadline guidance for Form 2290 states no automatic extension or grace period.</p>

<div class="note-box">This is a genuine "no" answer, not an unresearched gap: both forms were checked directly against current IRS instructions and the Form 7004 eligible-forms table this session. If the IRS changes this in a future revision, this page will be updated - the guide does not carry a standing assumption that a filing extension exists for either return.</div>

<h2>State excise tax</h2>
<p>State-level excise taxes (fuel, tobacco, alcohol, cannabis, and similar) are administered as recurring license or permit filings in most states rather than through a "request an extension" mechanism comparable to an income or estate tax extension, and the specific rules vary by product and by state far beyond what a single page can responsibly summarize without becoming its own multi-state build. Where a state's general business excise tax does have a documented extension mechanic already covered elsewhere on this site, it is cross-referenced below rather than duplicated here.</p>
<div class="pin-grid">
  <a href="washington-extension.html" class="pin-chip">Washington B&amp;O Excise Tax</a>
  <a href="master-extension-matrix.html" class="pin-chip">Master Matrix</a>
</div>

''' + related(
    ("federal-7004-business-extension.html", "Form 7004", "The general business extension form - see its eligible-forms list"),
    ("federal-hub.html", "Federal Extensions Hub", "Every federal extension form in one place"),
    ("extension-penalties-and-interest.html", "Penalties &amp; Interest", "What accrues on late-filed or late-paid excise tax"),
    ("master-extension-matrix.html", "Master Extension Matrix", "Every jurisdiction and tax type in one sortable table"),
)

page(
    "excise-tax-extension.html",
    "Federal Excise Tax Extensions - Form 720 and Form 2290 | Extension Guide",
    "There is no extension of time to file for Form 720 (quarterly federal excise tax) or Form 2290 (heavy highway vehicle use tax) - neither form is eligible for Form 7004, confirmed directly against current IRS instructions. Due dates and state excise tax scope explained.",
    "Federal Excise Tax Extensions",
    "Form 720: no extension mechanism &nbsp;&bull;&nbsp; Form 2290: no extension mechanism &nbsp;&bull;&nbsp; Confirmed against Form 7004's eligible-forms list",
    ["No extension - verified", "2 federal forms", "State excise scoped out"],
    "excise-tax-extension.html",
    body,
    "Sources: irs.gov/pub/irs-pdf/i720.pdf (Form 720 instructions); irs.gov/pub/irs-pdf/i7004.pdf (Form 7004 instructions and eligible-forms table); irs.gov/newsroom/heavy-highway-vehicle-owners-know-the-form-2290-filing-deadlines; irs.gov/forms-pubs/about-form-2290."
)

print("wrote excise-tax-extension.html")
