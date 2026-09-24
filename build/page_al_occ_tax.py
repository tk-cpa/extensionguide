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
    "alabama-municipal-occupational-tax-extension.html",
    "Alabama Municipal Occupational Tax Extension Guide - Birmingham & Other Cities | Extension Guide",
    "Alabama has no statewide statute governing municipal occupational (employee wage) tax extensions - each city's own ordinance controls. Birmingham's ordinance, independently verified this session, allows the Director of Finance to grant a discretionary extension of up to 30 days, with interest and penalty still accruing. Roughly 15-20 other Alabama municipalities impose a similar tax and are not independently confirmed here.",
    "Alabama Municipal Occupational Tax - Extension Rules",
    "Birmingham confirmed &nbsp;&bull;&nbsp; Other AL cities not independently verified &nbsp;&bull;&nbsp; Verified 9-23-2026",
    ["No statewide statute - city-by-city", "Birmingham: 30-day discretionary extension only", "Interest/penalty accrue regardless"],
    "states-hub.html",
    SLOGAN + '''
<p class="lead">Alabama does not have a single statewide occupational tax - roughly 15 to 20 Alabama municipalities (Birmingham, Bessemer, Gadsden, and others) independently impose their own occupational or license fee tax on wages earned within the city, each under its own local ordinance rather than a state statute. There is no statewide rule governing extensions for these local returns; each city's ordinance (or its private collection agent's administrative practice) controls its own extension policy.</p>

<div class="red-box"><strong>Disclosed as a partial survey.</strong> Only the City of Birmingham's occupational tax ordinance has been independently checked this session. Do not assume any other Alabama municipality's occupational tax follows the same rule - each city's ordinance must be checked on its own before relying on an extension position for that jurisdiction. This follows the same disclosed-sample approach used on this site for Kentucky's roughly 200 local occupational license tax jurisdictions.</div>

<table class="dt">
<tr><th>Jurisdiction</th><th>Extension mechanism</th><th>Status</th></tr>
<tr><td>Birmingham</td><td>The Director of Finance may, at his discretion, for reasonable cause, extend the time for filing the occupational tax withholding return - but the extension cannot exceed 30 days from the original due date, and penalty and interest continue to accrue during the extension period.</td><td>Confirmed - Occupational Tax Code, Ordinance No. 97-184, Section 6</td></tr>
<tr><td>Bessemer, Gadsden, and other Alabama municipalities imposing an occupational/license tax</td><td>Not checked this session</td><td>Not independently confirmed - each city's own ordinance must be verified separately before relying on any extension position</td></tr>
</table>

<div class="note-box">Birmingham's extension is narrower than most federal or state mechanisms on this site: it is discretionary rather than automatic, requires "reasonable cause" shown to the Director of Finance, is capped at 30 days regardless of what any federal or state extension provides, and does not stop interest or the late-filing penalty from running during the extended period.</div>
''' + related(
        ("states-hub.html", "All States", "Back to the states hub"),
        ("alabama-extension.html", "Alabama (State)", "Alabama's own state income tax extension rules"),
        ("kentucky-local-occupational-tax-extension.html", "Kentucky Local Occupational Tax", "Same disclosed-sample approach for a similarly fragmented local tax landscape"),
        ("denver-opt-extension.html", "Denver Occupational Privilege Tax", "A different city-level occupational tax with no extension mechanism at all"),
    ),
    "Authority: City of Birmingham, Alabama, Occupational Tax Code, Ordinance No. 97-184 (adopted December 23, 1997, as amended), Article I, Section 6 (Extension of Time for Making Return) and Section 13.1-13.2 (penalties, computed with regard to any extension granted). Source: full ordinance text, downloaded and extracted this session. Other Alabama municipalities not independently checked - see disclosure above.",
)

print("wrote alabama-municipal-occupational-tax-extension.html")
