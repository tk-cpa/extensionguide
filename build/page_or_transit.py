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
    "oregon-transit-self-employment-tax-extension.html",
    "Oregon Transit Self-Employment Tax Extension Guide - TriMet & Lane Transit District | Extension Guide",
    "TriMet and Lane Transit District (LTD) self-employment tax, reported on Form OR-TM, automatically follows a federal or Oregon individual income tax extension - no separate transit-tax extension form exists. Payment is still due by the original due date. Verified against the 2025 Form OR-TM Instructions.",
    "Oregon Transit Self-Employment Tax - TriMet & LTD - Extension Rules",
    "Form OR-TM &nbsp;&bull;&nbsp; No separate extension form &nbsp;&bull;&nbsp; Verified 9-23-2026",
    ["Rides on your federal/Oregon extension", "No separate form", "Payment still due on time"],
    "states-hub.html",
    SLOGAN + '''
<p class="lead">Oregon imposes a self-employment tax on net earnings from self-employment carried on within the TriMet (Portland metro) or Lane Transit District (Eugene/Springfield area) boundaries, reported on Form OR-TM. There is no separate transit self-employment tax extension form. A federal extension, or an extension to file the taxpayer's own Oregon individual income tax return, automatically extends the time to file Form OR-TM as well - the taxpayer simply checks the "An extension has been filed" box on Form OR-TM.</p>

<div class="red-box"><strong>Filing extension is not a payment extension.</strong> "An extension doesn't mean more time to pay... Oregon doesn't allow an extension of time to pay even if the IRS allows an extension." (2025 Form OR-TM Instructions). Payment must still be made by the original due date, using Form OR-TM-V, to avoid a 5% late-payment penalty; a 20% late-filing penalty applies if the return is filed more than 3 months after the due date including extensions.</div>

<table class="dt">
<tr><th>Item</th><th>Detail</th></tr>
<tr><td>Who files</td><td>Individuals and partnerships with net self-employment earnings from services performed within the TriMet or Lane Transit District boundaries, reported on Form OR-TM</td></tr>
<tr><td>Separate return</td><td>One combined Form OR-TM covers both TriMet and Lane Transit District self-employment tax - there is no separate form for each district</td></tr>
<tr><td>Extension mechanism</td><td>No separate application. A federal extension or an Oregon individual income tax return extension automatically extends the Form OR-TM due date - check the "An extension has been filed" box on the return. Do not attach a copy of the federal extension; keep it with your records</td></tr>
<tr><td>Payment</td><td>Not extended. Pay by the original due date using Form OR-TM-V, which itself is a payment voucher only, not an extension request ("Please note: This voucher isn't a request for an extension to file")</td></tr>
<tr><td>Authority</td><td>ORS 267.385 (TriMet), ORS 267.870 (Lane Transit District); 2025 Form OR-TM Instructions</td></tr>
</table>
''' + related(
        ("states-hub.html", "All States", "Back to the states hub"),
        ("oregon-extension.html", "Oregon (State)", "Oregon's own individual income tax extension rules"),
        ("portland-multnomah-extension.html", "Portland / Multnomah County", "A separate Oregon local tax with its own extension form"),
        ("federal-4868-individual-extension.html", "Federal Form 4868", "The federal extension that also extends this filing"),
    ),
    "Authority: ORS 267.385; ORS 267.870. Source: 2025 Form OR-TM Instructions (150-555-001-1, Rev. 10-15-25) and Form OR-TM-V Instructions (150-555-172-1), both downloaded directly from oregon.gov and searched for the word \"extension\" this session.",
)

print("wrote oregon-transit-self-employment-tax-extension.html")
