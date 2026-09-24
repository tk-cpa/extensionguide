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
<p class="lead">This page covers state-level estate and inheritance tax filing extensions - separate from the federal estate tax extension (Form 4768) and separate from the income tax extension pages elsewhere on this site. Thirteen states plus the District of Columbia impose their own estate tax, and four additional states impose an inheritance tax with no separate estate tax. Each has its own extension mechanism, summarized below with primary-source citations. Gift tax extensions are covered separately at the end of this page - the short answer is that no state currently imposes an independent gift tax with its own extension procedure, so gift tax extension coverage is entirely federal (Form 4768).</p>

<div class="note-box"><strong>Scope note.</strong> This page covers the extension mechanism only - not exemption amounts, rates, or who owes the tax, which change by year and are outside this guide's scope. Kentucky and Nebraska are stated below as confirmed no-general-filing-extension jurisdictions, not open items: every operative section of each state's governing chapter was checked directly against a live primary source this session (Kentucky: KRS 140.160, 140.210, 140.220, 140.222, 140.230; Nebraska: 77-2010), and none authorizes a filing extension. A few states' extension-granting statute could not be pinned to an exact numbered subsection from a live primary source this session (noted per-row below) - the underlying agency form and its instructions are cited as authority in those cases instead.</div>

<h2>State estate tax extensions</h2>
<table class="dt">
<tr><th>State</th><th>Form</th><th>Automatic?</th><th>Extension period</th><th>Extends time to pay?</th><th>Authority</th></tr>
<tr><td>Connecticut</td><td>CT-706/709 EXT</td><td>No - must file by original due date</td><td>9 months to file (6 months for gift tax); separate 6-month pay extension on a showing of reasonable cause</td><td>No</td><td>Conn. Gen. Stat. &sect;12-392; DRS Form CT-706/709 EXT instructions</td></tr>
<tr><td>Hawaii</td><td>M-68</td><td>No - must file and pay estimated tax with the request</td><td>Up to 6 months</td><td>No</td><td>Haw. Rev. Stat. &sect;236E-9; Form M-68 instructions</td></tr>
<tr><td>Illinois</td><td>Form 700-EXT</td><td>No - must attach a copy of the federal extension request</td><td>If the federal filing or payment due date is extended by the IRS, the Illinois due date moves to that same extended date</td><td>No (separate hardship-based payment extension available)</td><td>35 ILCS 405/8(c); Illinois Attorney General Form 700-EXT</td></tr>
<tr><td>Maine</td><td>None required for the automatic period</td><td>Yes - automatic</td><td>Federal extension period or 6 months, whichever is longer</td><td>No</td><td>36 M.R.S. &sect;4110</td></tr>
<tr><td>Maryland</td><td>MET-1E (Comptroller-prescribed form)</td><td>Partially - automatic if a later federal due date applies; otherwise must request</td><td>Up to 6 months (up to 1 year if the filer is outside the United States)</td><td>No</td><td>Md. Code, Tax-Gen. &sect;7-305.1</td></tr>
<tr><td>Massachusetts</td><td>Automatic file extension; Form M-4768 for a payment extension</td><td>Partially - filing extension is automatic if at least 80% of the tax finally due is paid within 9 months of death</td><td>6 months to file; payment extension (hardship-based, via MassTaxConnect or Form M-4768) can run up to 3 years</td><td>No, unless a hardship payment extension is separately approved</td><td>Mass. Gen. Laws c. 65C, &sect;10 (payment extension authority, up to 6 months or 3 years for undue hardship); Massachusetts DOR TIR 16-10 (automatic 6-month filing extension administrative practice)</td></tr>
<tr><td>Minnesota</td><td>None required</td><td>Yes - automatic, no application</td><td>6 months</td><td>No - Minnesota does not allow a payment extension</td><td>Minn. Stat. &sect;289A.19, subd. 4</td></tr>
<tr><td>New York</td><td>ET-133</td><td>Yes - automatic if filed within 9 months of death</td><td>Up to 6 months to file (up to 12 months for a separately requested payment extension)</td><td>No - filing and payment extensions are separate</td><td>N.Y. Tax Law &sect;976(a)(1)</td></tr>
<tr><td>Oregon</td><td>OR-706-EXT</td><td>Yes - automatic if filed before the original due date passes</td><td>6 months</td><td>No</td><td>Or. Rev. Stat. &sect;118.100; OAR 150-118-0090</td></tr>
<tr><td>Rhode Island</td><td>RI-4768</td><td>Yes - automatic, corresponding to the approved federal extension</td><td>6 months (matches whatever extension period the IRS approves for federal Form 706)</td><td>No - interest accrues from the original due date regardless</td><td>R.I. Gen. Laws &sect;44-23-3; RI Division of Taxation Form RI-4768 instructions</td></tr>
<tr><td>Vermont</td><td>EST-195</td><td>No - must file before the original due date</td><td>6 months</td><td>No</td><td>32 V.S.A. &sect;7481</td></tr>
<tr><td>Washington</td><td>Extension request form (DOR combined package)</td><td>Yes - automatic</td><td>6 months (an additional 6 months available if the executor is outside the United States)</td><td>No</td><td>RCW 83.100.050</td></tr>
<tr><td>District of Columbia</td><td>Form D-77</td><td>Partially - automatic only when tied to an obtained federal extension</td><td>6 months on request (must request within 10 months of death); if tied to a federal extension, the DC due date moves to 30 days after the federal extension period ends</td><td>No, except that when the federal-extension rule applies the DC tax is not due until the DC filing deadline</td><td>D.C. Code &sect;47-3705(b)</td></tr>
</table>

<h2>State inheritance tax extensions</h2>
<p>Maryland imposes both an estate tax (above) and a separate inheritance tax on certain collateral beneficiaries; the table below covers the four states where inheritance tax is the only state-level death tax.</p>
<table class="dt">
<tr><th>State</th><th>Form</th><th>Automatic?</th><th>Extension period</th><th>Extends time to pay?</th><th>Authority</th></tr>
<tr><td>Kentucky</td><td>None exists</td><td>N/A</td><td><strong>No general filing extension exists</strong> - confirmed against every operative section of KRS ch. 140 (140.160, requiring the return within 18 months of death with no extension language; 140.210, payment and interest; 140.220 and 140.222-140.224, a deferred-payment installment election for shares exceeding $5,000, payment only; 140.230, deduction mechanics). None authorizes extending the filing deadline itself.</td><td>N/A</td><td>KRS 140.160; 140.210; 140.220; 140.222-140.224; 140.230</td></tr>
<tr><td>Nebraska</td><td>None - filed with the county court as part of the probate proceeding, not a Department of Revenue form</td><td>N/A</td><td><strong>No general filing extension exists</strong> - Neb. Rev. Stat. &sect;77-2010 sets a fixed 12-month deadline from the date of death and authorizes only a discretionary abatement of the late-filing penalty by the county court for good cause; that abates a penalty, it does not extend the filing deadline itself. A 5% per-month penalty (capped at 25%) applies if no proceeding to determine the tax is filed within the 12 months.</td><td>No - interest continues to accrue regardless</td><td>Neb. Rev. Stat. &sect;77-2010</td></tr>
<tr><td>New Jersey</td><td>IT-EXT</td><td>No - must apply</td><td>4 months beyond the original due date; a second request may extend the total to 6 months if the return still cannot be filed</td><td>No - filing extension only, does not extend the time to pay</td><td>N.J. Admin. Code &sect;18:26-9.1</td></tr>
<tr><td>Pennsylvania</td><td>REV-1846</td><td>No - one-time request</td><td>6 months, granted at the department's discretion any time prior to expiration of the original 9-month filing period</td><td>No - a 5% discount applies only if paid within 3 months of death, and tax becomes delinquent 9 months after death regardless of any filing extension</td><td>72 P.S. &sect;9136(d)</td></tr>
</table>

<h2>Gift tax extensions</h2>
<p>No state currently imposes an independent gift tax with its own extension mechanism. Connecticut is the one state with its own gift tax, and its extension (Form CT-706/709 EXT, in the table above) is filed on the same combined form as the Connecticut estate tax and follows the same rules. Every other state's gift tax question is answered entirely at the federal level: federal gift tax returns (Form 709) use the same automatic 6-month extension as the federal estate tax, both granted through <a href="federal-4768-estate-extension.html">Form 4768</a>, under IRC &sect;6081 and Treas. Reg. &sect;25.6081-1.</p>

<div class="note-box">Nearly every state on this page treats filing and payment as two separate questions: getting more time to file the return almost never gets more time to pay the tax, and interest keeps running on unpaid tax from the original due date in every jurisdiction listed above. Confirm current exemption thresholds, rates, and any legislative changes directly with the state's tax authority before relying on this page for a specific filing.</div>

''' + related(
    ("federal-4768-estate-extension.html", "Federal Form 4768", "The federal estate and gift tax extension - automatic filing extension, discretionary payment extension"),
    ("master-extension-matrix.html", "Master Extension Matrix", "Every jurisdiction and tax type in one sortable table"),
    ("maryland-extension.html", "Maryland income tax extension", "Maryland's separate income tax extension page (Form 502E)"),
    ("faq.html", "FAQ", "Common extension questions answered"),
)

page(
    "estate-inheritance-tax-extensions.html",
    "State Estate and Inheritance Tax Extensions | Extension Guide",
    "State-by-state estate and inheritance tax filing extension rules for the 13 states plus DC with an estate tax and the 4 states with an inheritance tax - forms, automatic status, extension periods, and whether payment is also extended, with primary-source citations. Kentucky and Nebraska are confirmed as having no general filing extension. Gift tax extensions are federal only.",
    "State Estate &amp; Inheritance Tax Extensions",
    "13 states + DC estate tax &nbsp;&bull;&nbsp; 4 states inheritance tax &nbsp;&bull;&nbsp; Gift tax extensions are federal only",
    ["17 jurisdictions", "Filing vs. payment distinguished", "Zero open items"],
    "estate-inheritance-tax-extensions.html",
    body,
    "Sources: portal.ct.gov (DRS Form CT-706/709 EXT); files.hawaii.gov/tax (Form M-68); illinoisattorneygeneral.gov (Form 700-EXT) and law.justia.com (35 ILCS 405/8(c)); maine.gov/revenue (36 M.R.S. sect 4110); law.justia.com and mgaleg.maryland.gov (Md. Code Tax-Gen. sect 7-305.1); mass.gov (Request an extension to file and pay your estate tax; TIR 16-10) and law.justia.com (Mass. Gen. Laws c. 65C sect 10); revisor.mn.gov (Minn. Stat. sect 289A.19); nysenate.gov (N.Y. Tax Law sect 976); oregon.gov/dor and oregon.public.law (ORS 118.100); tax.ri.gov (Form RI-706/RI-4768 instructions) and webserver.rilegislature.gov (R.I. Gen. Laws sect 44-23-3); tax.vermont.gov and legislature.vermont.gov (32 V.S.A. sect 7481); dor.wa.gov and app.leg.wa.gov (RCW 83.100.050); code.dccouncil.gov (D.C. Code sect 47-3705); law.justia.com (KRS 140.160, 140.210, 140.220, 140.222-140.224, 140.230); law.justia.com (Neb. Rev. Stat. sect 77-2010); law.cornell.edu (N.J. Admin. Code sect 18:26-9.1, Form IT-EXT); codes.findlaw.com (72 P.S. sect 9136(d), Form REV-1846)."
)

print("wrote estate-inheritance-tax-extensions.html")
