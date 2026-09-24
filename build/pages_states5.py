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

# ---------------- ALASKA ----------------
page(
    "alaska-extension.html",
    "Alaska Tax Extension Guide | Extension Guide",
    "Alaska has no individual income tax. Corporation net income tax returns are due 30 days after the federal return is due, so a federal extension automatically pushes the Alaska due date. AS 43.20.030.",
    "Alaska - State Tax Extension",
    "Corporations only &nbsp;&bull;&nbsp; Automatic (tied to federal) &nbsp;&bull;&nbsp; Verified 9-23-2026",
    ["No individual income tax", "Corp: 30 days after federal due date", "Automatic"],
    "states-hub.html",
    SLOGAN + '''
<p class="lead">Alaska imposes no individual income tax, so there is no individual extension to request. For corporations, the Alaska Net Income Tax Act ties the state due date directly to the federal due date: a corporation must file its Alaska return within 30 days after the federal return is required to be filed. Because that federal due date already reflects any federal extension (Form 7004), a corporation that extends federally automatically gets a later Alaska due date - no separate Alaska extension form exists.</p>

<div class="green-box"><strong>Forms and guidance:</strong> <a href="https://tax.alaska.gov/programs/programs/forms/index.aspx" target="_blank" rel="noopener">Alaska DOR - Corporate Income Tax Forms</a></div>

<table class="dt">
<tr><th>Item</th><th>Detail</th></tr>
<tr><td>Individual income tax</td><td>None - Alaska does not tax individual wage or salary income</td></tr>
<tr><td>Corporate filing deadline</td><td>30 days after the federal return is required to be filed (AS 43.20.030(a)), including any federal extension</td></tr>
<tr><td>Payment</td><td>Total tax is due and payable at the same time as the federal tax (AS 43.20.030(c)) - a filing extension is not a payment extension</td></tr>
<tr><td>Form required</td><td>None to obtain the extension itself; it follows automatically from the federal deadline</td></tr>
<tr><td>Authority</td><td>AS 43.20.030(a), (c)</td></tr>
</table>

<div class="note-box">Alaska is one of the states with no individual income tax, alongside Florida, Nevada, South Dakota, Tennessee, Texas, Washington, and Wyoming.</div>
''' + related(
        ("states-hub.html", "All States", "Back to the states hub"),
        ("washington-extension.html", "Washington", "Also no individual income tax"),
        ("wyoming-extension.html", "Wyoming", "Also no individual or corporate income tax"),
    ),
    "Authority: AS 43.20.030(a), (c). Sources: touchngo.com/lglcntr/akstats/Statutes/Title43/Chapter20.htm; tax.alaska.gov/programs/programs/forms/index.aspx. Verified against primary source September 23, 2026.",
)

# ---------------- DC ----------------
page(
    "district-of-columbia-extension.html",
    "District of Columbia Tax Extension Guide | Extension Guide",
    "DC individual income tax extension - not automatic, Form FR-127 required, up to 6 months (12 for filers abroad). Full payment due with the extension request.",
    "District of Columbia - Tax Extension",
    "Individuals &amp; Business &nbsp;&bull;&nbsp; Not automatic &nbsp;&bull;&nbsp; Verified 9-23-2026",
    ["Form FR-127 required", "6 months", "Full payment due with request"],
    "states-hub.html",
    SLOGAN + '''
<p class="lead">The District of Columbia does not give individual filers a free pass off the federal extension. Form FR-127 must be filed on or before the original due date, and full payment of any expected tax liability is due with the request. A second 6-month extension is available for filers living or traveling outside the United States. Corporate and unincorporated business filers use Form FR-128.</p>

<div class="green-box"><strong>Forms and guidance:</strong> <a href="https://otr.cfo.dc.gov/page/extension-time-file" target="_blank" rel="noopener">DC Office of Tax and Revenue - Extension of Time to File</a></div>

<table class="dt">
<tr><th>Item</th><th>Detail</th></tr>
<tr><td>Form required</td><td>FR-127 (individual); FR-128 (unincorporated business/franchise)</td></tr>
<tr><td>Automatic</td><td>No - must be filed by the original due date</td></tr>
<tr><td>Extension length</td><td>Up to 6 months; a further 6 months is available for taxpayers living or traveling outside the U.S. (filed by the extended October 15 date)</td></tr>
<tr><td>Payment</td><td>Full payment of any expected tax liability, less credits, is due with the extension request - this is not a payment extension</td></tr>
<tr><td>Special relief</td><td>Combat-zone deployment relief is available for U.S. Armed Forces members and their spouses/domestic partners</td></tr>
</table>

<div class="note-box">Because Form FR-127 must be filed and paid by the original due date, filing a federal extension alone does not extend the DC deadline - do not rely on the federal Form 4868 alone for DC purposes.</div>
''' + related(
        ("states-hub.html", "All States", "Back to the states hub"),
        ("maryland-extension.html", "Maryland", "Also requires a separate extension form"),
        ("virginia-extension.html", "Virginia", "Neighboring jurisdiction, automatic instead"),
    ),
    "Authority: DC Office of Tax and Revenue, Extension of Time to File (Form FR-127 instructions). Sources: otr.cfo.dc.gov/page/extension-time-file. Verified against primary source September 23, 2026.",
)

# ---------------- MARYLAND ----------------
page(
    "maryland-extension.html",
    "Maryland Tax Extension Guide | Extension Guide",
    "Maryland individual income tax extension - Form 502E required unless no tax is owed and a federal extension was filed. COMAR 03.04.02.14.",
    "Maryland - State Tax Extension",
    "Individuals &amp; Business &nbsp;&bull;&nbsp; Conditionally automatic &nbsp;&bull;&nbsp; Verified 9-23-2026",
    ["Form 502E (if tax owed)", "6 months", "Full payment due with application"],
    "states-hub.html",
    SLOGAN + '''
<p class="lead">Maryland requires individuals who cannot file by the due date to submit Form 502E, with full payment of the expected tax due, by the original filing deadline. The one exception: a filer who expects to owe no additional Maryland tax and has already filed federal Form 4868 does not need to file Form 502E separately.</p>

<div class="green-box"><strong>Forms and guidance:</strong> <a href="https://taxes.marylandtaxes.gov/Individual_Taxes/Individual_Tax_Types/Income_Tax/Filing_Information/Filing_Deadlines/Extensions_and_Amendments/" target="_blank" rel="noopener">Comptroller of Maryland - Extensions and Amendments</a></div>

<table class="dt">
<tr><th>Item</th><th>Detail</th></tr>
<tr><td>Form required</td><td>Form 502E, unless no tax is owed and federal Form 4868 was filed</td></tr>
<tr><td>Automatic</td><td>Not automatic when tax is owed - Form 502E must be filed by the original due date</td></tr>
<tr><td>Payment</td><td>Full payment of the expected tax due is required with Form 502E</td></tr>
<tr><td>Extension length</td><td>Additional time to file beyond the original April due date (Comptroller guidance follows the federal 6-month pattern)</td></tr>
<tr><td>Authority</td><td>COMAR 03.04.02.14</td></tr>
</table>

<div class="note-box">If you expect to owe Maryland tax, filing only the federal extension is not enough - Form 502E and payment are still required by the original due date.</div>
''' + related(
        ("states-hub.html", "All States", "Back to the states hub"),
        ("district-of-columbia-extension.html", "District of Columbia", "Also requires a separate form"),
        ("virginia-extension.html", "Virginia", "Neighboring jurisdiction, automatic instead"),
    ),
    "Authority: COMAR 03.04.02.14. Sources: regs.maryland.gov/us/md/exec/comar/03.04.02.14; taxes.marylandtaxes.gov. Verified against primary source September 23, 2026.",
)

# ---------------- MINNESOTA ----------------
page(
    "minnesota-extension.html",
    "Minnesota Tax Extension Guide | Extension Guide",
    "Minnesota individual income tax - automatic filing extension to October 15, no form; a late-payment penalty is presumed reasonable if 90% is paid by the due date and the return is filed within 6 months. Minn. Stat. sect 289A.60, subd. 1(c).",
    "Minnesota - State Tax Extension",
    "Individuals &nbsp;&bull;&nbsp; Automatic &nbsp;&bull;&nbsp; Verified 9-23-2026",
    ["No form", "To October 15", "90% payment presumption"],
    "states-hub.html",
    SLOGAN + '''
<p class="lead">Minnesota does not require individuals to request anything to get extra time: the return is automatically due October 15 without a late-filing penalty. The mechanism sits in the penalty statute rather than a dedicated extension provision - a late-payment penalty is presumed to have reasonable cause when at least 90% of the tax shown owing is paid by the regular due date, the return is filed within six months, and the balance is paid with the return.</p>

<div class="green-box"><strong>Guidance:</strong> <a href="https://www.revenue.state.mn.us/filing-extensions" target="_blank" rel="noopener">Minnesota Department of Revenue - Filing After the Due Date</a></div>

<table class="dt">
<tr><th>Item</th><th>Detail</th></tr>
<tr><td>Form required</td><td>None - do not request an extension to file</td></tr>
<tr><td>Extension length</td><td>Automatically to October 15 for calendar-year filers</td></tr>
<tr><td>Payment condition</td><td>Pay at least 90% of the tax owed by the regular due date, file within six months, and pay the remaining balance with the return, to be presumed to have reasonable cause for late payment</td></tr>
<tr><td>Authority</td><td>Minn. Stat. &sect;289A.60, subd. 1(c)</td></tr>
</table>

<div class="note-box">This is a penalty-relief presumption, not a formal filing-extension statute - interest still accrues on any unpaid balance from the original due date.</div>
''' + related(
        ("states-hub.html", "All States", "Back to the states hub"),
        ("wisconsin-extension.html", "Wisconsin", "Neighboring state, similar automatic mechanics"),
        ("master-extension-matrix.html", "Master Matrix", "Every jurisdiction, one table"),
    ),
    "Authority: Minn. Stat. sect 289A.60, subd. 1(c). Sources: revisor.mn.gov/statutes/cite/289A.60; revenue.state.mn.us/filing-extensions. Verified against primary source September 23, 2026.",
)

# ---------------- MISSISSIPPI ----------------
page(
    "mississippi-extension.html",
    "Mississippi Tax Extension Guide | Extension Guide",
    "Mississippi individual income tax extension - the Commissioner recognizes IRS extensions, 6 months, attach a copy of federal Form 4868. Miss. Code Ann. sect 27-7-50.",
    "Mississippi - State Tax Extension",
    "Individuals &amp; Business &nbsp;&bull;&nbsp; Automatic with federal &nbsp;&bull;&nbsp; Verified 9-23-2026",
    ["Attach federal Form 4868", "6 months", "Payment due by original date"],
    "states-hub.html",
    SLOGAN + '''
<p class="lead">Mississippi's extension statute gives the Commissioner discretion to grant extensions for good cause, and separately allows the Commissioner to automatically recognize IRS extensions. In practice, the Department of Revenue honors a federal extension: a taxpayer with a federal extension gets until October 15 to file the Mississippi return, provided a copy of federal Form 4868 is attached when the Mississippi return is filed. This is a filing extension only - any tax due must still be paid by the original April due date to avoid penalty and interest.</p>

<div class="green-box"><strong>Forms and guidance:</strong> <a href="https://www.dor.ms.gov/individual/individual-income-tax-frequently-asked-questions" target="_blank" rel="noopener">Mississippi DOR - Individual Income Tax FAQ</a> &nbsp;&bull;&nbsp; <a href="https://www.dor.ms.gov/sites/default/files/tax-forms/individual/80106248.pdf" target="_blank" rel="noopener">Form 80-106 (payment voucher, PDF)</a></div>

<table class="dt">
<tr><th>Item</th><th>Detail</th></tr>
<tr><td>Form required</td><td>None separately for the extension - attach a copy of federal Form 4868 to the Mississippi return; Form 80-106 is a payment voucher used only if tax is due</td></tr>
<tr><td>Extension length</td><td>6 months, matching the federal extended due date (October 15 for calendar-year filers)</td></tr>
<tr><td>Payment</td><td>Any tax due must be paid by the original April due date to avoid penalty and interest - the extension is for filing only</td></tr>
<tr><td>Authority</td><td>Miss. Code Ann. &sect;27-7-50</td></tr>
</table>
''' + related(
        ("states-hub.html", "All States", "Back to the states hub"),
        ("louisiana-extension.html", "Louisiana", "Neighboring state, also automatic"),
        ("master-extension-matrix.html", "Master Matrix", "Every jurisdiction, one table"),
    ),
    "Authority: Miss. Code Ann. sect 27-7-50. Sources: law.justia.com/codes/mississippi/title-27/chapter-7/article-1/section-27-7-50; dor.ms.gov/individual/individual-income-tax-frequently-asked-questions. Verified against primary source September 23, 2026.",
)

# ---------------- MISSOURI ----------------
page(
    "missouri-extension.html",
    "Missouri Tax Extension Guide | Extension Guide",
    "Missouri individual income tax extension - automatic with a federal extension attached to the return, up to 6 months. RSMo sect 143.551.",
    "Missouri - State Tax Extension",
    "Individuals &amp; Business &nbsp;&bull;&nbsp; Automatic with federal &nbsp;&bull;&nbsp; Verified 9-23-2026",
    ["Attach federal extension", "6 months max", "Form MO-60 if no federal extension"],
    "states-hub.html",
    SLOGAN + '''
<p class="lead">Missouri automatically extends the filing deadline for any taxpayer who was granted a federal extension - filing a copy of the federal extension with the Missouri return (or by the return's due date) automatically extends the Missouri due date to match, up to a maximum of six months (except for taxpayers outside the United States). A taxpayer without a federal extension who still needs more time files Form MO-60.</p>

<div class="green-box"><strong>Forms and guidance:</strong> <a href="https://dor.mo.gov/forms/MO-60_2025.pdf" target="_blank" rel="noopener">Form MO-60 (PDF, dor.mo.gov)</a></div>

<table class="dt">
<tr><th>Item</th><th>Detail</th></tr>
<tr><td>Form required</td><td>None if a federal extension was granted and filed with the Missouri return; Form MO-60 otherwise</td></tr>
<tr><td>Automatic</td><td>Yes, when tied to a federal extension</td></tr>
<tr><td>Extension length</td><td>Matches the federal extension, capped at 6 months (no cap for taxpayers outside the U.S.)</td></tr>
<tr><td>Payment</td><td>A federal payment extension similarly extends the Missouri payment deadline when filed with the director of revenue; otherwise tax is due by the original date</td></tr>
<tr><td>Authority</td><td>RSMo &sect;143.551</td></tr>
</table>
''' + related(
        ("states-hub.html", "All States", "Back to the states hub"),
        ("kansas-extension.html", "Kansas", "Neighboring state, similar federal tie-in"),
        ("master-extension-matrix.html", "Master Matrix", "Every jurisdiction, one table"),
    ),
    "Authority: RSMo sect 143.551. Sources: revisor.mo.gov/main/OneSection.aspx?bid=7258&section=143.551; dor.mo.gov/forms/MO-60_2025.pdf. Verified against primary source September 23, 2026.",
)

# ---------------- MONTANA ----------------
page(
    "montana-extension.html",
    "Montana Tax Extension Guide | Extension Guide",
    "Montana individual income tax - automatic 6-month extension to file, no application required. Mont. Code Ann. sect 15-30-2604(3)(a).",
    "Montana - State Tax Extension",
    "Individuals &nbsp;&bull;&nbsp; Automatic &nbsp;&bull;&nbsp; Verified 9-23-2026",
    ["No application", "6 months", "Payment still due on original date"],
    "states-hub.html",
    SLOGAN + '''
<p class="lead">Montana grants every individual taxpayer an automatic extension of up to six months to file, with no application required. The extension only moves the filing deadline - taxes, penalties, and interest are still computed from the original due date, so any balance due should be paid by the regular deadline to limit interest and avoid the late-payment penalty. The Department may grant additional time beyond six months for good cause.</p>

<div class="green-box"><strong>Guidance:</strong> <a href="https://mca.legmt.gov/bills/mca/title_0150/chapter_0300/part_0260/section_0040/0150-0300-0260-0040.html" target="_blank" rel="noopener">Mont. Code Ann. &sect;15-30-2604 (official code)</a></div>

<table class="dt">
<tr><th>Item</th><th>Detail</th></tr>
<tr><td>Form required</td><td>None</td></tr>
<tr><td>Extension length</td><td>Up to 6 months following the date prescribed for filing; the Department may allow further time for good cause</td></tr>
<tr><td>Payment</td><td>Not extended - taxes, penalties, and interest continue to run from the original due date</td></tr>
<tr><td>Authority</td><td>Mont. Code Ann. &sect;15-30-2604(3)(a)</td></tr>
</table>
''' + related(
        ("states-hub.html", "All States", "Back to the states hub"),
        ("idaho-extension.html", "Idaho", "Neighboring state, payment-conditioned instead"),
        ("master-extension-matrix.html", "Master Matrix", "Every jurisdiction, one table"),
    ),
    "Authority: Mont. Code Ann. sect 15-30-2604(3)(a). Sources: mca.legmt.gov/bills/mca/title_0150/chapter_0300/part_0260/section_0040/0150-0300-0260-0040.html. Verified against primary source September 23, 2026.",
)

# ---------------- NEBRASKA ----------------
page(
    "nebraska-extension.html",
    "Nebraska Tax Extension Guide | Extension Guide",
    "Nebraska individual income tax extension - a federal extension operates automatically as a Nebraska extension, up to 7 months. Neb. Rev. Stat. sect 77-2770.",
    "Nebraska - State Tax Extension",
    "Individuals &amp; Business &nbsp;&bull;&nbsp; Automatic with federal &nbsp;&bull;&nbsp; Verified 9-23-2026",
    ["Federal extension applies automatically", "Up to 7 months", "Form 4868N if no federal extension"],
    "states-hub.html",
    SLOGAN + '''
<p class="lead">Under Nebraska law, an extension of time granted by the IRS for filing a federal return operates automatically as a Nebraska extension for the same period - no separate state application is required. A taxpayer who needs Nebraska time without a federal extension in place files Form 4868N. The Tax Commissioner's extensions generally cannot exceed a total of seven months (longer for taxpayers abroad).</p>

<div class="green-box"><strong>Forms and guidance:</strong> <a href="https://revenue.nebraska.gov/sites/default/files/doc/tax-forms/2024/f_4868N.pdf" target="_blank" rel="noopener">Form 4868N (PDF, revenue.nebraska.gov)</a></div>

<table class="dt">
<tr><th>Item</th><th>Detail</th></tr>
<tr><td>Form required</td><td>None if relying on a federal extension; Form 4868N otherwise</td></tr>
<tr><td>Automatic</td><td>Yes - an IRS extension operates as a Nebraska extension</td></tr>
<tr><td>Extension length</td><td>Up to 7 months total (except for taxpayers abroad)</td></tr>
<tr><td>Payment</td><td>For individuals, an extension of time for filing also extends the payment deadline; corporate filers must still pay estimated tax by the original due date</td></tr>
<tr><td>Authority</td><td>Neb. Rev. Stat. &sect;77-2770</td></tr>
</table>
''' + related(
        ("states-hub.html", "All States", "Back to the states hub"),
        ("kansas-extension.html", "Kansas", "Neighboring state, similar federal tie-in"),
        ("master-extension-matrix.html", "Master Matrix", "Every jurisdiction, one table"),
    ),
    "Authority: Neb. Rev. Stat. sect 77-2770. Sources: nebraskalegislature.gov/laws/statutes.php?statute=77-2770. Verified against primary source September 23, 2026.",
)

# ---------------- NEVADA ----------------
page(
    "nevada-extension.html",
    "Nevada Tax Extension Guide | Extension Guide",
    "Nevada has no individual or corporate income tax. Nev. Const. art. 10, sect 1. The Commerce Tax applies only above a $4 million gross revenue threshold.",
    "Nevada - State Tax Extension",
    "No income tax &nbsp;&bull;&nbsp; N/A &nbsp;&bull;&nbsp; Verified 9-23-2026",
    ["No individual income tax", "No corporate income tax", "Commerce Tax is separate"],
    "states-hub.html",
    SLOGAN + '''
<p class="lead">Nevada imposes neither an individual income tax nor a general corporate income tax, so there is no income tax extension to request. The Nevada Constitution restricts the legislature's ability to impose certain income-based taxes. Businesses with more than $4 million in Nevada gross revenue in a fiscal year may owe the separate Commerce Tax, which is not an income tax.</p>

<div class="green-box"><strong>Guidance:</strong> <a href="https://tax.nv.gov/about-nevada-department-of-taxation/income-tax-in-nevada/" target="_blank" rel="noopener">Nevada Department of Taxation - Income Tax in Nevada</a></div>

<table class="dt">
<tr><th>Item</th><th>Detail</th></tr>
<tr><td>Individual income tax</td><td>None</td></tr>
<tr><td>Corporate income tax</td><td>None (a separate Commerce Tax applies only above a $4 million gross revenue threshold)</td></tr>
<tr><td>Authority</td><td>Nev. Const. art. 10, &sect;1</td></tr>
</table>

<div class="note-box">Nevada is one of the states with no individual income tax, alongside Alaska, Florida, South Dakota, Tennessee, Texas, Washington, and Wyoming.</div>
''' + related(
        ("states-hub.html", "All States", "Back to the states hub"),
        ("wyoming-extension.html", "Wyoming", "Also no individual or corporate income tax"),
        ("texas-extension.html", "Texas", "Also no individual income tax"),
    ),
    "Authority: Nev. Const. art. 10, sect 1. Sources: tax.nv.gov/about-nevada-department-of-taxation/income-tax-in-nevada; codes.findlaw.com/nv/nevada-constitution/nv-const-art-10-sect-1. Verified against primary source September 23, 2026.",
)

# ---------------- NEW HAMPSHIRE ----------------
page(
    "new-hampshire-extension.html",
    "New Hampshire Tax Extension Guide | Extension Guide",
    "New Hampshire has no broad individual income tax. The Interest and Dividends Tax extension (Form DP-59-A) is automatic for 7 months if 100% of the tax is paid by the due date. N.H. Code Admin. R. Rev 906.04.",
    "New Hampshire - State Tax Extension",
    "Interest &amp; Dividends Tax &nbsp;&bull;&nbsp; Automatic &nbsp;&bull;&nbsp; Verified 9-23-2026",
    ["No general income tax", "Form DP-59-A", "7 months if 100% paid"],
    "states-hub.html",
    SLOGAN + '''
<p class="lead">New Hampshire does not tax wages or salaries. It does tax interest and dividend income above a statutory exemption threshold under the Interest and Dividends Tax (being phased out under prior legislation). A taxpayer who has not paid 100% of the tax liability by the original due date files Form DP-59-A, which functions as both a payment form and an application for a 7-month extension. The Business Profits Tax has a parallel automatic 7-month extension (Form BT-EXT) with the same 100% payment condition.</p>

<div class="green-box"><strong>Forms and guidance:</strong> <a href="https://www.revenue.nh.gov/taxes-glance/interest-dividends-tax" target="_blank" rel="noopener">NH Department of Revenue Administration - Interest &amp; Dividends Tax</a></div>

<table class="dt">
<tr><th>Item</th><th>Detail</th></tr>
<tr><td>General individual income tax</td><td>None</td></tr>
<tr><td>Interest &amp; Dividends Tax extension</td><td>Form DP-59-A, required only if 100% of the tax has not already been paid by the due date</td></tr>
<tr><td>Extension length</td><td>7 months</td></tr>
<tr><td>Payment condition</td><td>100% of the tax liability must be paid with the extension request - a request for less than 100% is rejected</td></tr>
<tr><td>Business Profits Tax</td><td>Parallel automatic 7-month extension, Form BT-EXT, same 100% payment condition (N.H. Code Admin. R. Rev 307.09)</td></tr>
<tr><td>Authority</td><td>N.H. Code Admin. R. Rev 906.04</td></tr>
</table>
''' + related(
        ("states-hub.html", "All States", "Back to the states hub"),
        ("texas-extension.html", "Texas", "Also no general individual income tax"),
        ("master-extension-matrix.html", "Master Matrix", "Every jurisdiction, one table"),
    ),
    "Authority: N.H. Code Admin. R. Rev 906.04; Rev 307.09. Sources: regulations.justia.com/states/new-hampshire/rev/chapter-rev-900/part-rev-906/section-rev-906-04; regulations.justia.com/states/new-hampshire/rev/chapter-rev-300/part-rev-307/section-rev-307-09. Verified against primary source September 23, 2026.",
)

# ---------------- NEW MEXICO ----------------
page(
    "new-mexico-extension.html",
    "New Mexico Tax Extension Guide | Extension Guide",
    "New Mexico personal income tax extension - a federal extension is automatically an approved New Mexico extension, capped at 6 months from the original due date. N.M. Admin. Code sect 3.1.4.12.",
    "New Mexico - State Tax Extension",
    "Individuals &nbsp;&bull;&nbsp; Automatic with federal &nbsp;&bull;&nbsp; Verified 9-23-2026",
    ["Federal extension is sufficient", "Capped at 6 months", "Attach federal form"],
    "states-hub.html",
    SLOGAN + '''
<p class="lead">New Mexico treats an automatic federal extension as an approved extension for state purposes as well - no separate New Mexico application is needed. If the federal extension runs longer than six months from the original due date, the New Mexico extension is nonetheless capped at six months. A copy of the federal extension form, if any was required, must be attached to the New Mexico return.</p>

<div class="green-box"><strong>Guidance:</strong> <a href="https://www.tax.newmexico.gov/individuals/file-your-taxes-overview/extension-of-time-to-file/" target="_blank" rel="noopener">NM Taxation and Revenue Department - Extension of Time to File</a></div>

<table class="dt">
<tr><th>Item</th><th>Detail</th></tr>
<tr><td>Form required</td><td>None separately if relying on the federal extension; attach a copy of the federal form if one was required</td></tr>
<tr><td>Automatic</td><td>Yes, tied to the federal extension</td></tr>
<tr><td>Extension length</td><td>Matches the federal extension, capped at 6 months from the original due date</td></tr>
<tr><td>Authority</td><td>N.M. Admin. Code &sect;3.1.4.12</td></tr>
</table>
''' + related(
        ("states-hub.html", "All States", "Back to the states hub"),
        ("colorado-extension.html", "Colorado", "Neighboring state, also automatic"),
        ("master-extension-matrix.html", "Master Matrix", "Every jurisdiction, one table"),
    ),
    "Authority: N.M. Admin. Code sect 3.1.4.12. Sources: law.cornell.edu/regulations/new-mexico/N-M-Admin-Code-SS-3.1.4.12; tax.newmexico.gov/individuals/file-your-taxes-overview/extension-of-time-to-file. Verified against primary source September 23, 2026.",
)

# ---------------- NORTH DAKOTA ----------------
page(
    "north-dakota-extension.html",
    "North Dakota Tax Extension Guide | Extension Guide",
    "North Dakota income tax extension - the state recognizes the automatic federal extension; Form 101 is needed only for extra time beyond the federal period. N.D. Cent. Code sect 57-38-34(6).",
    "North Dakota - State Tax Extension",
    "Individuals &amp; Business &nbsp;&bull;&nbsp; Automatic with federal &nbsp;&bull;&nbsp; Verified 9-23-2026",
    ["Federal extension recognized", "Form 101 beyond federal period", "Good cause required beyond federal"],
    "states-hub.html",
    SLOGAN + '''
<p class="lead">North Dakota recognizes extensions granted for federal returns: the state filing deadline moves to the same date as the automatic federal extension without a separate state application. A taxpayer who needs more time than the federal extension provides, or who has no federal extension, applies using Form 101 and must show good cause; an extension beyond the federal period is discretionary, not automatic.</p>

<div class="green-box"><strong>Forms and guidance:</strong> <a href="https://www.tax.nd.gov/filing-extension" target="_blank" rel="noopener">North Dakota Office of State Tax Commissioner - Filing an Extension</a></div>

<table class="dt">
<tr><th>Item</th><th>Detail</th></tr>
<tr><td>Form required</td><td>None if relying on the federal extension; Form 101 for additional time or if no federal extension exists</td></tr>
<tr><td>Automatic</td><td>Yes, for the same period as the federal extension</td></tr>
<tr><td>Extension length</td><td>Matches the federal extension; further time requires good cause under the Tax Commissioner's discretionary authority</td></tr>
<tr><td>Authority</td><td>N.D. Cent. Code &sect;57-38-34(6)</td></tr>
</table>
''' + related(
        ("states-hub.html", "All States", "Back to the states hub"),
        ("minnesota-extension.html", "Minnesota", "Neighboring state, also automatic"),
        ("master-extension-matrix.html", "Master Matrix", "Every jurisdiction, one table"),
    ),
    "Authority: N.D. Cent. Code sect 57-38-34(6). Sources: tax.nd.gov/filing-extension; codes.findlaw.com/nd/title-57-taxation/nd-cent-code-sect-57-38-34.html. Verified against primary source September 23, 2026.",
)

# ---------------- OKLAHOMA ----------------
page(
    "oklahoma-extension.html",
    "Oklahoma Tax Extension Guide | Extension Guide",
    "Oklahoma individual income tax extension - the automatic federal extension is honored if no additional Oklahoma tax is due; otherwise Form 504-I, capped at 6 months, 90% payment condition. 68 Okla. Stat. sect 216.",
    "Oklahoma - State Tax Extension",
    "Individuals &nbsp;&bull;&nbsp; Conditionally automatic &nbsp;&bull;&nbsp; Verified 9-23-2026",
    ["Federal extension honored if no OK tax due", "Form 504-I otherwise", "90% payment condition"],
    "states-hub.html",
    SLOGAN + '''
<p class="lead">The Oklahoma Tax Commission administratively honors the automatic federal extension as an Oklahoma extension when no additional Oklahoma tax is due. If tax is owed, the taxpayer files Form 504-I and pays at least 90% of the tax liability by the original due date. Extensions under the statute cannot exceed one-half of the accounting period covered by the return - a 6-month extension for a 12-month tax year.</p>

<div class="green-box"><strong>Forms and guidance:</strong> <a href="https://oklahoma.gov/content/dam/ok/en/tax/documents/forms/individuals/current/504-I.pdf" target="_blank" rel="noopener">Form 504-I (PDF, oklahoma.gov)</a></div>

<table class="dt">
<tr><th>Item</th><th>Detail</th></tr>
<tr><td>Form required</td><td>None if no additional Oklahoma tax is due and the federal extension is attached; Form 504-I otherwise</td></tr>
<tr><td>Extension length</td><td>Up to 6 months (one-half the 12-month tax year), per 68 Okla. Stat. &sect;216</td></tr>
<tr><td>Payment condition</td><td>At least 90% of the tax liability must be paid by the original due date</td></tr>
<tr><td>Authority</td><td>68 Okla. Stat. &sect;216</td></tr>
</table>
''' + related(
        ("states-hub.html", "All States", "Back to the states hub"),
        ("kansas-extension.html", "Kansas", "Neighboring state, similar 90% test"),
        ("master-extension-matrix.html", "Master Matrix", "Every jurisdiction, one table"),
    ),
    "Authority: 68 Okla. Stat. sect 216. Sources: law.justia.com/codes/oklahoma/title-68/section-68-216; oklahoma.gov Form 504-I instructions. Verified against primary source September 23, 2026.",
)

# ---------------- RHODE ISLAND ----------------
page(
    "rhode-island-extension.html",
    "Rhode Island Tax Extension Guide | Extension Guide",
    "Rhode Island personal income tax extension - automatic if a federal extension is attached to the return; otherwise Form RI-4868, capped at 6 months, 80% payment condition. 280-RICR-20-55-2.6.",
    "Rhode Island - State Tax Extension",
    "Individuals &nbsp;&bull;&nbsp; Conditionally automatic &nbsp;&bull;&nbsp; Verified 9-23-2026",
    ["Federal extension sufficient if attached", "Form RI-4868 otherwise", "80% payment condition"],
    "states-hub.html",
    SLOGAN + '''
<p class="lead">Rhode Island does not require its own extension form if a proper federal extension is filed for the same period and a copy is attached to the Rhode Island return - no payment needs to accompany that route. A taxpayer who instead files a separate Rhode Island extension (Form RI-4868 for individuals, RI-8736 for pass-throughs and fiduciaries) must pay at least 80% of the actual tax liability with the request or the extension is void and penalties apply. No extension exceeds six months, except for taxpayers outside the United States.</p>

<div class="green-box"><strong>Forms and guidance:</strong> <a href="https://tax.ri.gov/forms/personal-income-tax-forms" target="_blank" rel="noopener">RI Division of Taxation - Personal Income Tax Forms</a></div>

<table class="dt">
<tr><th>Item</th><th>Detail</th></tr>
<tr><td>Form required</td><td>None if a federal extension for the same period is attached to the RI return; Form RI-4868 (individuals) or RI-8736 (fiduciaries/pass-throughs) otherwise</td></tr>
<tr><td>Extension length</td><td>Up to 6 months (no cap for taxpayers outside the U.S.)</td></tr>
<tr><td>Payment condition</td><td>If filing RI-4868/RI-8736 separately, at least 80% of the actual tax liability must be paid or the extension is void</td></tr>
<tr><td>Authority</td><td>280-RICR-20-55-2.6</td></tr>
</table>
''' + related(
        ("states-hub.html", "All States", "Back to the states hub"),
        ("massachusetts-extension.html", "Massachusetts", "Neighboring state, similar 80% test"),
        ("master-extension-matrix.html", "Master Matrix", "Every jurisdiction, one table"),
    ),
    "Authority: 280-RICR-20-55-2.6. Sources: law.cornell.edu/regulations/rhode-island/280-RICR-20-55-2.6; tax.ri.gov. Verified against primary source September 23, 2026.",
)

# ---------------- SOUTH CAROLINA ----------------
page(
    "south-carolina-extension.html",
    "South Carolina Tax Extension Guide | Extension Guide",
    "South Carolina individual income tax extension - not automatic unless no tax is owed and a federal extension is attached; otherwise apply with full payment, capped at 6 months. S.C. Code sect 12-6-4980.",
    "South Carolina - State Tax Extension",
    "Individuals &amp; Business &nbsp;&bull;&nbsp; Conditionally automatic &nbsp;&bull;&nbsp; Verified 9-23-2026",
    ["Federal extension sufficient if no SC tax due", "Tentative return + payment otherwise", "6 months max"],
    "states-hub.html",
    SLOGAN + '''
<p class="lead">South Carolina allows the Department of Revenue to grant an extension of up to six months for filing income tax returns. If no South Carolina tax is owed and a federal extension was filed, a taxpayer may simply attach a copy of the federal extension to the state return instead of applying separately. If tax is owed, the taxpayer must file a tentative South Carolina return and pay the full estimated tax by the original due date to request the extension; taxes owed remain due on the original date regardless.</p>

<div class="green-box"><strong>Forms and guidance:</strong> <a href="https://dor.sc.gov/income-tax-income-tax-extensions-0" target="_blank" rel="noopener">South Carolina DOR - Income Tax Extensions</a></div>

<table class="dt">
<tr><th>Item</th><th>Detail</th></tr>
<tr><td>Form required</td><td>None if no SC tax is due and the federal extension is attached; a tentative SC return with full payment otherwise</td></tr>
<tr><td>Extension length</td><td>Up to 6 months</td></tr>
<tr><td>Payment</td><td>Tax owed is due on the original filing deadline regardless of the extension</td></tr>
<tr><td>Authority</td><td>S.C. Code &sect;12-6-4980</td></tr>
</table>
''' + related(
        ("states-hub.html", "All States", "Back to the states hub"),
        ("north-carolina-extension.html", "North Carolina", "Neighboring state, automatic with federal instead"),
        ("master-extension-matrix.html", "Master Matrix", "Every jurisdiction, one table"),
    ),
    "Authority: S.C. Code sect 12-6-4980. Sources: law.justia.com/codes/south-carolina/title-12/chapter-6/section-12-6-4980; dor.sc.gov/income-tax-income-tax-extensions-0. Verified against primary source September 23, 2026.",
)

# ---------------- SOUTH DAKOTA ----------------
page(
    "south-dakota-extension.html",
    "South Dakota Tax Extension Guide | Extension Guide",
    "South Dakota has no individual income tax and no general corporate income tax. Only financial institutions pay the Bank Franchise Tax under SDCL ch. 10-43.",
    "South Dakota - State Tax Extension",
    "No general income tax &nbsp;&bull;&nbsp; N/A &nbsp;&bull;&nbsp; Verified 9-23-2026",
    ["No individual income tax", "No general corporate income tax", "Bank Franchise Tax is separate"],
    "states-hub.html",
    SLOGAN + '''
<p class="lead">South Dakota does not impose an individual income tax or a general corporate income tax, so there is no income tax extension for most filers to request. The only income-based tax is the Bank Franchise Tax, which applies solely to financial institutions and is administered separately from a general corporate income tax regime.</p>

<div class="green-box"><strong>Guidance:</strong> <a href="https://dor.sd.gov/businesses/taxes/bank-franchise-tax/" target="_blank" rel="noopener">South Dakota DOR - Bank Franchise Tax</a></div>

<table class="dt">
<tr><th>Item</th><th>Detail</th></tr>
<tr><td>Individual income tax</td><td>None</td></tr>
<tr><td>General corporate income tax</td><td>None</td></tr>
<tr><td>Bank Franchise Tax</td><td>Applies only to financial institutions; administered under SDCL ch. 10-43</td></tr>
<tr><td>Authority</td><td>SDCL ch. 10-43</td></tr>
</table>

<div class="note-box">South Dakota is one of the states with no individual income tax, alongside Alaska, Florida, Nevada, Tennessee, Texas, Washington, and Wyoming.</div>
''' + related(
        ("states-hub.html", "All States", "Back to the states hub"),
        ("wyoming-extension.html", "Wyoming", "Also no individual or corporate income tax"),
        ("texas-extension.html", "Texas", "Also no individual income tax"),
    ),
    "Authority: SDCL ch. 10-43 (Bank Franchise Tax). Sources: dor.sd.gov/businesses/taxes/bank-franchise-tax. Verified against primary source September 23, 2026.",
)

# ---------------- TENNESSEE ----------------
page(
    "tennessee-extension.html",
    "Tennessee Tax Extension Guide | Extension Guide",
    "Tennessee repealed its individual Hall income tax effective January 1, 2021. The Franchise and Excise Tax extension is automatic for 7 months if the 90%/100% payment safe harbor is met. Tenn. Code Ann. sect 67-4-2015(h).",
    "Tennessee - State Tax Extension",
    "Business (F&amp;E Tax) &nbsp;&bull;&nbsp; Automatic &nbsp;&bull;&nbsp; Verified 9-23-2026",
    ["No individual income tax (since 2021)", "F&amp;E Tax: 7 months", "90%/100% payment safe harbor"],
    "states-hub.html",
    SLOGAN + '''
<p class="lead">Tennessee's Hall income tax on interest and dividends was repealed effective for tax years beginning January 1, 2021, so Tennessee now has no individual income tax at all. Businesses subject to the Franchise and Excise Tax get an automatic 7-month extension to file, provided they pay by the original due date the lesser of 90% of the current year's liability or 100% of the prior year's tax shown due. Falling short of that safe harbor causes penalty and interest to apply as if no extension had been granted.</p>

<div class="green-box"><strong>Forms and guidance:</strong> <a href="https://www.tn.gov/content/dam/tn/revenue/documents/forms/fae/fae173.pdf" target="_blank" rel="noopener">Form FAE-173 (PDF, tn.gov)</a></div>

<table class="dt">
<tr><th>Item</th><th>Detail</th></tr>
<tr><td>Individual income tax</td><td>None (Hall income tax repealed for tax years beginning January 1, 2021)</td></tr>
<tr><td>Franchise &amp; Excise Tax extension</td><td>Automatic 7 months</td></tr>
<tr><td>Payment safe harbor</td><td>Lesser of 90% of the current year's liability or 100% of the prior year's tax shown due, paid by the original due date</td></tr>
<tr><td>Authority</td><td>Tenn. Code Ann. &sect;67-4-2015(h)</td></tr>
</table>
''' + related(
        ("states-hub.html", "All States", "Back to the states hub"),
        ("texas-extension.html", "Texas", "Also no individual income tax"),
        ("master-extension-matrix.html", "Master Matrix", "Every jurisdiction, one table"),
    ),
    "Authority: Tenn. Code Ann. sect 67-4-2015(h). Sources: law.justia.com/codes/tennessee/title-67/chapter-4/part-20/section-67-4-2015; revenue.support.tn.gov HIT-3 (Hall Income Tax repeal). Verified against primary source September 23, 2026.",
)

# ---------------- UTAH ----------------
page(
    "utah-extension.html",
    "Utah Tax Extension Guide | Extension Guide",
    "Utah individual income tax - automatic extension to file, no form required if no tax is owed; at least 90% of the tax must be paid by the original due date. Utah Code Ann. sect 59-10-516.",
    "Utah - State Tax Extension",
    "Individuals &amp; Business &nbsp;&bull;&nbsp; Automatic &nbsp;&bull;&nbsp; Verified 9-23-2026",
    ["No application required", "6 months", "90% payment to avoid penalty"],
    "states-hub.html",
    SLOGAN + '''
<p class="lead">Utah grants an automatic extension to file without requiring an application. The tradeoff is a 90% payment test: at least 90% of the tax due must be paid by the original filing deadline (through withholding, credits, and any prepayment) to avoid the extension penalty. Form TC-546 is a prepayment coupon used only when a payment is being submitted with the extension, not an application for the extension itself.</p>

<div class="green-box"><strong>Guidance:</strong> <a href="https://tax.utah.gov/billing/extensions" target="_blank" rel="noopener">Utah State Tax Commission - Filing Extensions</a></div>

<table class="dt">
<tr><th>Item</th><th>Detail</th></tr>
<tr><td>Form required</td><td>None to obtain the extension; Form TC-546 only if remitting a prepayment</td></tr>
<tr><td>Extension length</td><td>6 months</td></tr>
<tr><td>Payment threshold</td><td>At least 90% of the tax due must be paid by the original due date to avoid the extension penalty</td></tr>
<tr><td>Authority</td><td>Utah Code Ann. &sect;59-10-516</td></tr>
</table>
''' + related(
        ("states-hub.html", "All States", "Back to the states hub"),
        ("colorado-extension.html", "Colorado", "Also automatic with a 90% payment test"),
        ("master-extension-matrix.html", "Master Matrix", "Every jurisdiction, one table"),
    ),
    "Authority: Utah Code Ann. sect 59-10-516. Sources: law.cornell.edu/regulations/utah/Utah-Admin-Code-R865-9I-23; tax.utah.gov/billing/extensions. Verified against primary source September 23, 2026.",
)

# ---------------- VERMONT ----------------
page(
    "vermont-extension.html",
    "Vermont Tax Extension Guide | Extension Guide",
    "Vermont income tax extension - automatic, matching the federal extended due date for individuals; corporations get one additional month beyond the federal date. 32 V.S.A. sect 5868.",
    "Vermont - State Tax Extension",
    "Individuals &amp; Business &nbsp;&bull;&nbsp; Automatic &nbsp;&bull;&nbsp; Verified 9-23-2026",
    ["Matches federal extension", "Corp: +1 month beyond federal", "Payment not extended"],
    "states-hub.html",
    SLOGAN + '''
<p class="lead">Vermont's Commissioner of Taxes must extend the time for filing a Vermont income tax return to match the extended federal due date whenever the taxpayer has been granted either an automatic or a good-cause federal extension. For a corporation, the Vermont extension runs one additional month beyond the federal extended due date. Filing extensions do not extend the deadline for paying the tax liability.</p>

<div class="green-box"><strong>Guidance:</strong> <a href="https://tax.vermont.gov/individuals/request-extension" target="_blank" rel="noopener">Vermont Department of Taxes - Request an Extension</a></div>

<table class="dt">
<tr><th>Item</th><th>Detail</th></tr>
<tr><td>Form required</td><td>None separately for individuals relying on the federal extension</td></tr>
<tr><td>Extension length</td><td>Matches the federal extended due date (individuals); federal extended date plus one month (corporations)</td></tr>
<tr><td>Payment</td><td>Not extended - the tax liability remains due on the original date</td></tr>
<tr><td>Authority</td><td>32 V.S.A. &sect;5868</td></tr>
</table>
''' + related(
        ("states-hub.html", "All States", "Back to the states hub"),
        ("massachusetts-extension.html", "Massachusetts", "Neighboring state"),
        ("master-extension-matrix.html", "Master Matrix", "Every jurisdiction, one table"),
    ),
    "Authority: 32 V.S.A. sect 5868. Sources: legislature.vermont.gov/statutes/section/32/151/05868; tax.vermont.gov/individuals/request-extension. Verified against primary source September 23, 2026.",
)

# ---------------- WEST VIRGINIA ----------------
page(
    "west-virginia-extension.html",
    "West Virginia Tax Extension Guide | Extension Guide",
    "West Virginia personal income tax extension - automatic, matching the federal extension, capped at 6 months for taxpayers within the United States. W. Va. Code St. R. sect 110-21-57.",
    "West Virginia - State Tax Extension",
    "Individuals &nbsp;&bull;&nbsp; Automatic &nbsp;&bull;&nbsp; Verified 9-23-2026",
    ["Matches federal extension", "Capped at 6 months", "Payment not extended"],
    "states-hub.html",
    SLOGAN + '''
<p class="lead">West Virginia automatically extends the time to file a Personal Income Tax Return for the same period as a federal extension, capped at six months for taxpayers within the United States. This automatic extension applies to filing only - it does not extend the time to pay the balance of West Virginia tax due, which remains due on the original date.</p>

<div class="green-box"><strong>Guidance:</strong> <a href="https://tax.wv.gov/individuals" target="_blank" rel="noopener">West Virginia Tax Division - Individuals</a></div>

<table class="dt">
<tr><th>Item</th><th>Detail</th></tr>
<tr><td>Form required</td><td>None separately - attach a copy of the federal extension when filing the West Virginia return</td></tr>
<tr><td>Extension length</td><td>Matches the federal extension, capped at 6 months for taxpayers within the U.S.</td></tr>
<tr><td>Payment</td><td>Not extended - the balance of West Virginia tax due remains due on the original date</td></tr>
<tr><td>Authority</td><td>W. Va. Code St. R. &sect;110-21-57</td></tr>
</table>
''' + related(
        ("states-hub.html", "All States", "Back to the states hub"),
        ("virginia-extension.html", "Virginia", "Neighboring state, also automatic"),
        ("master-extension-matrix.html", "Master Matrix", "Every jurisdiction, one table"),
    ),
    "Authority: W. Va. Code St. R. sect 110-21-57. Sources: law.cornell.edu/regulations/west-virginia/W-Va-C-S-R-SS-110-21-57; tax.wv.gov/individuals. Verified against primary source September 23, 2026.",
)

# ---------------- WISCONSIN ----------------
page(
    "wisconsin-extension.html",
    "Wisconsin Tax Extension Guide | Extension Guide",
    "Wisconsin individual income tax extension - automatic 6-month extension if a copy of the federal extension is attached to the Wisconsin return. Wis. Stat. sect 71.03(8).",
    "Wisconsin - State Tax Extension",
    "Individuals &amp; Business &nbsp;&bull;&nbsp; Automatic with federal &nbsp;&bull;&nbsp; Verified 9-23-2026",
    ["Attach federal extension copy", "6 months", "Interest still accrues"],
    "states-hub.html",
    SLOGAN + '''
<p class="lead">Wisconsin gives an automatic six-month extension to any taxpayer who has a federal extension, as long as a copy of the federal extension application is attached to the Wisconsin income tax return when it is filed. No separate Wisconsin extension form or application is required. Interest continues to accrue on any unpaid tax during the extension period, and the taxpayer may qualify for a combat-zone or federally-declared-disaster exception from that interest.</p>

<div class="green-box"><strong>Guidance:</strong> <a href="https://www.revenue.wi.gov/Pages/FAQS/pcs-extensn.aspx" target="_blank" rel="noopener">Wisconsin DOR - Tax Filing Extensions FAQ</a></div>

<table class="dt">
<tr><th>Item</th><th>Detail</th></tr>
<tr><td>Form required</td><td>None separately - attach a copy of the federal extension application to the Wisconsin return</td></tr>
<tr><td>Extension length</td><td>6 months</td></tr>
<tr><td>Payment</td><td>Interest accrues on unpaid tax during the extension, except for combat-zone service or federally-declared disaster relief</td></tr>
<tr><td>Authority</td><td>Wis. Stat. &sect;71.03(8)</td></tr>
</table>
''' + related(
        ("states-hub.html", "All States", "Back to the states hub"),
        ("minnesota-extension.html", "Minnesota", "Neighboring state, also automatic"),
        ("master-extension-matrix.html", "Master Matrix", "Every jurisdiction, one table"),
    ),
    "Authority: Wis. Stat. sect 71.03(8). Sources: docs.legis.wisconsin.gov/statutes/statutes/71/i/03/8; revenue.wi.gov/Pages/FAQS/pcs-extensn.aspx. Verified against primary source September 23, 2026.",
)

# ---------------- WYOMING ----------------
page(
    "wyoming-extension.html",
    "Wyoming Tax Extension Guide | Extension Guide",
    "Wyoming has no individual income tax and no corporate income tax - it has never enacted either. Wyo. Stat. Ann. tit. 39 (no income tax chapter exists).",
    "Wyoming - State Tax Extension",
    "No income tax &nbsp;&bull;&nbsp; N/A &nbsp;&bull;&nbsp; Verified 9-23-2026",
    ["No individual income tax", "No corporate income tax", "No extension needed"],
    "states-hub.html",
    SLOGAN + '''
<p class="lead">Wyoming has never enacted an individual or corporate income tax. There is no income tax chapter in Title 39 of the Wyoming Statutes imposing one, and no extension mechanism exists because there is no income tax return to extend. Wyoming businesses instead deal with sales, use, and severance taxes administered by the Wyoming Department of Revenue.</p>

<div class="green-box"><strong>Guidance:</strong> <a href="https://revenue.wyo.gov/home" target="_blank" rel="noopener">Wyoming Department of Revenue - Home</a></div>

<table class="dt">
<tr><th>Item</th><th>Detail</th></tr>
<tr><td>Individual income tax</td><td>None</td></tr>
<tr><td>Corporate income tax</td><td>None</td></tr>
<tr><td>Extension to file</td><td>Not applicable - no income tax return exists to extend</td></tr>
<tr><td>Authority</td><td>Wyo. Stat. Ann. tit. 39 (Taxation and Revenue) - no income tax is imposed under this title</td></tr>
</table>

<div class="note-box">Wyoming is one of the states with no individual or corporate income tax, alongside Nevada and South Dakota.</div>
''' + related(
        ("states-hub.html", "All States", "Back to the states hub"),
        ("nevada-extension.html", "Nevada", "Also no individual or corporate income tax"),
        ("south-dakota-extension.html", "South Dakota", "Also no individual or general corporate income tax"),
    ),
    "Authority: Wyo. Stat. Ann. tit. 39 (Taxation and Revenue). Sources: revenue.wyo.gov/home; taxfoundation.org/location/wyoming. Verified against primary source September 23, 2026.",
)

print("batch 5 done - 22 jurisdictions")
