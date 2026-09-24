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
    "international-information-returns-extension.html",
    "International Information Returns Extension Guide - Forms 3520, 3520-A, 5471, 5472, 8621, 8854, 8865, 8938 | Extension Guide",
    "How the extension rules work for Forms 3520, 3520-A, 5471, 5472, 8621, 8854, 8865, and 8938. Most ride on the filer's own income tax return extension with no separate form - Form 3520-A is the exception, requiring its own Form 7004 filed under the foreign trust's own EIN. Confirmed against each form's current IRS instructions.",
    "International Information Returns - Extension Rules",
    "Forms 3520, 3520-A, 5471, 5472, 8621, 8854, 8865, 8938 &nbsp;&bull;&nbsp; Mostly ride on your own return &nbsp;&bull;&nbsp; One key exception",
    ["Form 3520-A needs its own Form 7004", "The rest ride on your own return extension", "No separate form for most"],
    "federal-hub.html",
    SLOGAN + '''
<p class="lead">Forms 3520, 5471, 5472, 8621, 8854, 8865, and 8938 are information returns (or elections) attached to, or timed against, a taxpayer's own federal income tax return - they do not have separate extension forms of their own. Extending the underlying income tax return extends these along with it. Form 3520-A is the one exception on this page: it is filed by the foreign trust itself, under the trust's own EIN, and requires its own separate Form 7004 - a Form 4868 or Form 7004 extending the U.S. owner's personal or business return does not extend Form 3520-A.</p>

<div class="red-box"><strong>Form 3520-A is the trap.</strong> "Note: An extension of time to file an income tax return does NOT extend the time to file Form 3520-A. You MUST file Form 7004 using the foreign trust's EIN to request an extension of time to file Form 3520-A." (Instructions for Form 3520-A). This is filed separately from, and on a different due date than, the U.S. owner's own Form 3520 or Form 1040.</div>

<table class="dt">
<tr><th>Form</th><th>What it reports</th><th>Extension mechanism</th></tr>
<tr><td>Form 3520</td><td>U.S. person's transactions with foreign trusts, and large foreign gifts/bequests</td><td>Rides on the filer's own income tax return extension - no separate form. For a calendar-year individual with an income tax extension, Form 3520 is due no later than October 15 (the 15th day of the 10th month), which may differ from the actual extended due date of the income tax return itself.</td></tr>
<tr><td>Form 3520-A</td><td>Annual information return of a foreign trust with a U.S. owner, filed by the trust (or a U.S. agent)</td><td><strong>Separate extension required.</strong> File Form 7004 using the foreign trust's own EIN by the 15th day of the 3rd month after the trust's tax year end. Does not ride on the U.S. owner's Form 4868 or Form 7004.</td></tr>
<tr><td>Form 5471</td><td>U.S. persons who are officers, directors, or shareholders of certain foreign corporations</td><td>Rides on the filer's own income tax return extension - filed as an attachment, due by the due date (including extensions) of that return. No separate form.</td></tr>
<tr><td>Form 5472</td><td>25%-foreign-owned U.S. corporations and foreign corporations engaged in a U.S. trade or business, reportable-transaction disclosure</td><td>Rides on the reporting corporation's own Form 7004, filed by the regular due date of the corporation's return. A foreign-owned U.S. disregarded entity with no income tax return of its own must file a pro forma Form 1120 with Form 5472 attached, and requests its extension by filing Form 7004 under the DE's own EIN by the regular due date of that pro forma return.</td></tr>
<tr><td>Form 8621</td><td>U.S. shareholders of a Passive Foreign Investment Company (PFIC), including the Qualified Electing Fund (QEF) and mark-to-market elections</td><td>Rides on the filer's own income tax return extension - attached to that return and due by its due date (including extensions). A QEF election under section 1295 must likewise be made by the due date (including extensions) of the shareholder's income tax return for the relevant year.</td></tr>
<tr><td>Form 8854</td><td>Initial and Annual Expatriation Statement (covered expatriates - former citizens and long-term residents)</td><td>Rides on the filer's own income tax return extension. For the initial-year statement, the form is filed by the date the taxpayer's Form 1040-NR (or Form 1040/1040-SR) would have been due, including extensions, had one been required.</td></tr>
<tr><td>Form 8865</td><td>U.S. persons with interests in certain foreign partnerships</td><td>Rides on the filer's own income tax return extension when one is required, filed by the due date (including extensions) of that return. If the filer has no income tax return filing requirement, Form 8865 is filed separately, at the time and place the filer would otherwise have filed an income tax return - i.e., following the same extension timing that return would have had.</td></tr>
<tr><td>Form 8938</td><td>Specified foreign financial assets (FATCA)</td><td>Rides on the filer's own income tax return extension - filed as an attachment, due by the due date (including extensions) of that return. No separate form.</td></tr>
</table>

<div class="note-box">None of these forms have their own independent payment obligation - they are informational. The "extension" that matters is the underlying income tax return's extension (Form 4868 for individuals, Form 7004 for businesses/entities), except for Form 3520-A, which needs its own Form 7004 regardless of what the U.S. owner does with their personal return.</div>
''' + related(
        ("federal-hub.html", "Federal Hub", "All federal extension forms"),
        ("federal-4868-individual-extension.html", "Form 4868", "The individual return extension most of these forms ride on"),
        ("federal-7004-business-extension.html", "Form 7004", "The business/entity extension Form 3520-A and Form 5472 use directly"),
        ("other-extensions.html", "FBAR & Other Filings", "FinCEN 114 and other non-income-tax federal filings"),
    ),
    "Authority: IRC sect 6081. Sources: Instructions for Form 3520 (Rev. December 2025); Instructions for Form 3520-A; Instructions for Form 5471; Instructions for Form 5472 (12/2024); Instructions for Form 8621; Instructions for Form 8854; Instructions for Form 8865; Instructions for Form 8938 - all downloaded directly from irs.gov and searched for the word \"extension\" this session.",
)

print("wrote international-information-returns-extension.html")
