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
    "state-pte-elective-tax-extension.html",
    "State PTE Elective Tax (PTET) Extension Guide - California, New York, New Jersey, Connecticut, Illinois | Extension Guide",
    "How pass-through entity elective tax (PTET/BAIT) extensions work in the five highest-volume PTET states - California, New York, New Jersey, Connecticut, and Illinois. Some states require a separate PTET-specific extension application; others fold the PTET onto the entity's regular return extension. Confirmed against each state's current forms and instructions. Disclosed as a partial survey - over 30 states have enacted a PTET regime and are not all covered here.",
    "State PTE Elective Tax (PTET) - Extension Rules",
    "California, New York, New Jersey, Connecticut, Illinois &nbsp;&bull;&nbsp; Partial survey of major PTET states &nbsp;&bull;&nbsp; Verified 9-23-2026",
    ["Some states need their own PTET extension", "Others ride on the entity's regular return", "Filing extension is never a payment extension"],
    "states-hub.html",
    SLOGAN + '''
<p class="lead">Over 30 states have enacted an elective pass-through entity tax (PTET), typically as a workaround to the federal $10,000 SALT cap. Each state built its own extension mechanism, and they do not follow one pattern: some states require a separate, PTET-specific extension application distinct from the entity's regular income tax return extension; others simply let the PTET ride on the entity's existing 1065/1120-S-equivalent return extension. This page covers the five highest-volume PTET states - California, New York, New Jersey, Connecticut, and Illinois - each verified against a current primary source this session.</p>

<div class="red-box"><strong>This is a partial survey, not full coverage.</strong> More than 30 states have enacted a PTET regime (for example: Alabama, Arizona, Arkansas, Colorado, Georgia, Idaho, Kansas, Louisiana, Maryland, Massachusetts, Michigan, Minnesota, Mississippi, New Mexico, North Carolina, Ohio, Oklahoma, Oregon, Rhode Island, South Carolina, Utah, Virginia, Wisconsin, and others). Only the five states below have been independently verified this session. Do not assume any other state's PTET follows the same pattern as one of these five without checking that state's own rule.</div>

<table class="dt">
<tr><th>State</th><th>PTET mechanism</th><th>Extension mechanism</th></tr>
<tr><td>California</td><td>Elective tax on qualified net income (QNI) at 9.3%, paid via Form FTB 3893, attached to Form 100S/565/568. Applies to taxable years beginning before January 1, 2026 only - the election sunsets after the 2025 taxable year under current law.</td><td><strong>No extension available for the election or the payment.</strong> Payment 1 (the June 15 prepayment) and Payment 2 (the balance, due with the return) must both be made "without regard to any extension of time for filing the return." The entity's own Form 100S/565/568 can still get its regular filing extension, but the PTE elective tax payment deadline does not move with it.</td></tr>
<tr><td>New York</td><td>PTET annual return, generally due March 15 after the close of the PTET taxable year, filed through the entity's Business Online Services account.</td><td>The electing entity may request a six-month extension to file the annual PTET return, online through Business Online Services only (no paper form). This is an extension of time to file only - "an extension to file is not an extension to pay." All PTET must be paid by the original due date regardless of the filing extension.</td></tr>
<tr><td>New Jersey</td><td>Pass-Through Business Alternative Income Tax (BAIT), reported on Form PTE-100.</td><td><strong>Separate extension application required</strong> - Form PTE-200-T, filed online by the original due date, grants a six-month extension to file Form PTE-100 only. At least 80% of the BAIT liability must be paid by the original due date (through estimates or the extension payment) or the extension is retroactively denied, with penalty and interest running from the original due date.</td></tr>
<tr><td>Connecticut</td><td>Connecticut Pass-Through Entity Tax, reported on Form CT-PET (a return separate from the entity's composite return, Form CT-1065/CT-1120SI).</td><td><strong>Separate extension application required</strong> - Form CT-PET EXT, its own dedicated form, filed and paid electronically by the original due date (March 15 for calendar-year filers), grants a six-month extension to file Form CT-PET only, not to pay. A federal Form 7004 extension does not automatically extend the Connecticut filing date; Form CT-PET EXT must still be filed (though no separate reason is required if a federal extension was already requested).</td></tr>
<tr><td>Illinois</td><td>PTE tax, elected and reported directly on the entity's own return - Schedule B of Form IL-1065 or Form IL-1120-ST. There is no separate Illinois PTE tax return.</td><td>No separate extension mechanism - the PTE tax simply rides on the entity's own Form IL-1065/IL-1120-ST, which receives Illinois' automatic seven-month filing extension (granted automatically, no form required to obtain it). Payment of the PTE tax is still due by the original due date of the return regardless of the automatic filing extension.</td></tr>
</table>

<div class="note-box">The pattern to watch for: California and Illinois both build the PTET payment obligation into the entity's regular return timeline (California more strictly - no filing extension helps at all; Illinois more leniently - the automatic 7-month filing extension applies, but payment is still due on the original date). New York, New Jersey, and Connecticut instead give the PTET its own, separate extension-to-file application, layered on top of (not replacing) whatever extension the entity's regular income tax return has. In every state on this page, filing extension and payment extension are two different things, and none of the five extends the payment deadline.</div>
''' + related(
        ("states-hub.html", "All States", "Back to the states hub"),
        ("california-extension.html", "California (State)", "California's own income tax return extension rules"),
        ("new-york-extension.html", "New York (State)", "New York's own income tax return extension rules"),
        ("new-jersey-extension.html", "New Jersey (State)", "New Jersey's own income tax return extension rules"),
        ("connecticut-extension.html", "Connecticut (State)", "Connecticut's own income tax return extension rules"),
        ("illinois-extension.html", "Illinois (State)", "Illinois's own income tax return extension rules"),
    ),
    "Sources: 2025 Instructions for Form FTB 3893 (California, ftb.ca.gov); New York State Department of Taxation and Finance, Pass-Through Entity Tax (PTET) page, tax.ny.gov/bus/ptet; 2026 Instructions for Form PTE-200-T (New Jersey, nj.gov/treasury/taxation); Form CT-PET EXT and instructions, Rev. 12/25 (Connecticut, portal.ct.gov/DRS); Form CT-1065/CT-1120SI Instructions, Rev. 12/25 (Connecticut); 2025 Instructions for Form IL-1120-ST (Illinois, tax.illinois.gov). All downloaded directly from the state agency site and searched for the word \"extension\" this session.",
)

print("wrote state-pte-elective-tax-extension.html")
