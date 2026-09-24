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
    "federal-5558-employee-plan-extension.html",
    "Form 5558 - Employee Benefit Plan Extension Guide | Extension Guide",
    "Form 5558 requests a one-time extension to file Form 5500, Form 5500-SF, Form 5500-EZ, and/or Form 8955-SSA - automatically approved to the 15th day of the 3rd month after the normal due date, if filed by the normal due date. IRC sect 6081. Confirmed against the current IRS form and instructions.",
    "Form 5558 - Employee Benefit Plan Return Extension",
    "Retirement &amp; Welfare Plans &nbsp;&bull;&nbsp; Automatic (2.5 months) &nbsp;&bull;&nbsp; One-time only",
    ["Form 5558", "Automatic to 15th day of 3rd month after due date", "One-time, per plan"],
    "federal-hub.html",
    SLOGAN + '''
<p class="lead">Form 5558 is the extension mechanism for the employee benefit plan return series - Form 5500, Form 5500-SF, Form 5500-EZ, and Form 8955-SSA (the plan's registration statement for deferred vested participants). It is filed by the plan administrator or plan sponsor, one form per plan, and is separate from any extension of the employer's own income tax return.</p>

<div class="green-box"><strong>Get the form:</strong> <a href="https://www.irs.gov/pub/irs-pdf/f5558.pdf" target="_blank" rel="noopener">Download Form 5558 (PDF, irs.gov)</a> &nbsp;&bull;&nbsp; <a href="https://www.irs.gov/forms-pubs/about-form-5558" target="_blank" rel="noopener">About Form 5558 (irs.gov)</a></div>

<table class="dt">
<tr><th>Item</th><th>Detail</th></tr>
<tr><td>Who files</td><td>Plan administrator or plan sponsor (generally the employer for a single-employer plan), one Form 5558 per plan</td></tr>
<tr><td>Returns covered</td><td>Form 5500, Form 5500-SF, Form 5500-EZ, and/or Form 8955-SSA - a single Form 5558 can extend both a plan's Form 5500 series return and its Form 8955-SSA together</td></tr>
<tr><td>Extension length</td><td>Automatic to the 15th day of the 3rd month after the return's normal due date (2.5 months) - for a calendar-year plan, from July 31 to October 15</td></tr>
<tr><td>Condition for automatic approval</td><td>Form 5558 must be filed on or before the return's normal due date, and the requested date must not be later than the 15th day of the 3rd month after that due date</td></tr>
<tr><td>Filing method</td><td>Electronically through EFAST2, or on paper with the IRS Service Center in Ogden, UT (paper filing available again as of January 1, 2025)</td></tr>
<tr><td>Number of extensions</td><td>One-time only per return - Form 5558 does not have a second-extension mechanism</td></tr>
<tr><td>Authority</td><td>IRC &sect;6081 (extension of time for filing returns)</td></tr>
</table>

<div class="note-box"><strong>Exception - no Form 5558 needed:</strong> if the plan year and the employer's tax year are the same, and the employer has already been granted a federal income tax extension to a date later than the plan return's normal due date, the plan return is automatically extended to that same later date - without filing Form 5558 at all. Filing Form 5558 after the normal due date cannot extend this automatic exception further.</div>

<div class="red-box"><strong>What this does not cover:</strong> an extension of Form 5500/5500-SF/5500-EZ/8955-SSA does not extend the PBGC (Pension Benefit Guaranty Corporation) Form 1, Annual Premium Payment - that is a separate filing with its own deadline, unaffected by Form 5558.</div>
''' + related(
        ("federal-hub.html", "Federal Hub", "All federal extension forms"),
        ("federal-8868-nonprofit-extension.html", "Form 8868", "The nonprofit-return counterpart, Form 990 series"),
        ("federal-7004-business-extension.html", "Form 7004", "Business income tax return extension - separate from the plan's own extension"),
    ),
    "Authority: IRC sect 6081. Sources: Form 5558 (Rev. January 2025) and its instructions, irs.gov/pub/irs-pdf/f5558.pdf, downloaded and searched directly this session; irs.gov/forms-pubs/about-form-5558.",
)

print("wrote federal-5558-employee-plan-extension.html")
