import sys
sys.path.insert(0, "/home/claude/extensionguide/build")
from gen_states import page

# ---------------- ALABAMA ----------------
page(
"alabama-extension.html",
"Alabama Tax Extension Guide | Extension Guide",
"Alabama individual income tax extension - automatic 6 months, no application required. Corporate extension matches the federal extension plus one month. Ala. Code sect 40-18-27(c); sect 40-18-39(a).",
"Alabama - State Tax Extension",
"Individuals &amp; Business &nbsp;&bull;&nbsp; Automatic &nbsp;&bull;&nbsp; Verified 9-23-2026",
["No application required", "Individual: 6 months", "Corporate: federal + 1 month"],
"states-hub.html",
"""<div class="slogan"><p>An extension to file is not an extension to pay tax.</p></div>
<p class="lead">Alabama grants an automatic 6-month extension to file individual income tax returns - no paper or electronic extension form is required. Corporations get an automatic extension matching their federal extension plus one additional month. Neither extension extends the time to pay.</p>

<div class="green-box"><strong>If you owe tax with the extension:</strong> <a href="https://www.revenue.alabama.gov/faqs/can-i-apply-for-an-extension-to-file-my-return/" target="_blank" rel="noopener">Alabama extension FAQ (revenue.alabama.gov)</a> &nbsp;&bull;&nbsp; <a href="https://www.revenue.alabama.gov/individual-corporate/individual-income-tax-filing-information/" target="_blank" rel="noopener">Individual filing information (revenue.alabama.gov)</a></div>

<table class="dt">
<tr><th>Filer</th><th>Form required</th><th>Extension length</th><th>Payment rule</th></tr>
<tr><td>Individual</td><td>None - fully automatic, no paper or electronic form filed</td><td>6 months, to October 15</td><td>Not extended; interest and penalties accrue on unpaid tax from the original due date</td></tr>
<tr><td>Corporation (Form 20C)</td><td>None to obtain the extension - attach the federal extension to the Alabama return when filed</td><td>Federal extension period plus 1 month</td><td>Not extended; payment due by the original due date</td></tr>
</table>

<h2>Authority</h2>
<p>Individual extensions: Ala. Code &sect;40-18-27(c), which authorizes the Department of Revenue to grant a reasonable extension of time for filing returns, not to exceed six months for taxpayers within the state. Corporate extensions: Ala. Code &sect;40-18-39(a) and Ala. Admin. Code r. 810-3-39-.02, which set the corporate extension at the federal extension period plus one month.</p>

<div class="note-box">Alabama's current administrative practice (published on the Department's own FAQ page) waives the paper Form 4868A that older instructions once required for individuals - no state extension form is filed at all. Confirm this against the Department's site at the time of filing, since this is agency practice under the statute rather than a fixed form requirement.</div>

<div class="related">
  <div class="related-title">Related</div>
  <div class="related-links">
    <a href="states-hub.html" class="related-link">All States<span>Back to the states hub</span></a>
    <a href="georgia-extension.html" class="related-link">Georgia<span>Also automatic with the federal extension</span></a>
    <a href="master-extension-matrix.html" class="related-link">Master Matrix<span>Every jurisdiction, one table</span></a>
  </div>
</div>""",
"Authority: Ala. Code &sect;40-18-27(c) (individual extension authority); Ala. Code &sect;40-18-39(a) and Ala. Admin. Code r. 810-3-39-.02 (corporate extension, federal plus one month). Sources: revenue.alabama.gov/faqs/can-i-apply-for-an-extension-to-file-my-return; law.justia.com (Ala. Code &sect;40-18-27, &sect;40-18-39); law.cornell.edu (Ala. Admin. Code r. 810-3-39-.02). Verified against primary source September 23, 2026."
)

# ---------------- ARIZONA ----------------
page(
"arizona-extension.html",
"Arizona Tax Extension Guide | Extension Guide",
"Arizona individual and corporate income tax extension - automatic 6 months (7 for corporations) if at least 90% of tax liability is paid by the original due date. Form 204. A.R.S. sect 42-1107.",
"Arizona - State Tax Extension",
"Individuals &amp; Business &nbsp;&bull;&nbsp; Conditional-Automatic &nbsp;&bull;&nbsp; Verified 9-23-2026",
["90% payment required", "Individual: 6 months", "Corporate: up to 7 months"],
"states-hub.html",
"""<div class="slogan"><p>An extension to file is not an extension to pay tax.</p></div>
<p class="lead">Arizona will honor a federal extension for the equivalent period, or grants its own extension on Form 204, provided at least 90% of the tax liability is paid by the original due date. Miss that 90% threshold and the extension underpayment penalty applies even though the paperwork was timely.</p>

<div class="green-box"><strong>Get the form:</strong> <a href="https://azdor.gov/sites/default/files/document/FORMS_INDIVIDUAL_2025_204_f.pdf" target="_blank" rel="noopener">Download Form 204 (PDF, azdor.gov)</a> &nbsp;&bull;&nbsp; <a href="https://azdor.gov/making-payments-late-payments-and-filing-extensions" target="_blank" rel="noopener">Payments, late payments, and extensions (azdor.gov)</a></div>

<table class="dt">
<tr><th>Item</th><th>Detail</th></tr>
<tr><td>Form required</td><td>Form 204, unless a federal extension was filed and no Arizona Form 204 payment is being mailed (electronic federal extension payment substitutes)</td></tr>
<tr><td>Individual extension length</td><td>6 months, to October 15, 2026</td></tr>
<tr><td>Corporate extension length</td><td>Up to 7 months, to the following November 15 for calendar-year filers</td></tr>
<tr><td>Payment threshold</td><td>At least 90% of the tax liability for the period must be paid by the original due date; shortfall triggers the extension underpayment penalty of 0.5% per 30-day period</td></tr>
<tr><td>Authority</td><td>A.R.S. &sect;42-1107 (extension of time for filing returns); A.R.S. &sect;42-1125(D) (underpayment penalty)</td></tr>
</table>

<div class="note-box">Arizona's extension statute (Title 42, general tax administration) applies across tax types, including individual income tax under Title 43 - the 90% payment condition is the operative rule for both individuals and corporations, not a form technicality.</div>

<div class="related">
  <div class="related-title">Related</div>
  <div class="related-links">
    <a href="states-hub.html" class="related-link">All States<span>Back to the states hub</span></a>
    <a href="new-jersey-extension.html" class="related-link">New Jersey<span>Also uses a payment-threshold test</span></a>
    <a href="master-extension-matrix.html" class="related-link">Master Matrix<span>Every jurisdiction, one table</span></a>
  </div>
</div>""",
"Authority: A.R.S. &sect;42-1107 (extension of time for filing returns, automatic if 90% of tax paid); A.R.S. &sect;42-1125(D) (extension underpayment penalty). Sources: azleg.gov/ars/42/01107.htm; azdor.gov/sites/default/files/document/FORMS_INDIVIDUAL_2025_204i.pdf; azdor.gov/making-payments-late-payments-and-filing-extensions. Verified against primary source September 23, 2026."
)

# ---------------- ARKANSAS ----------------
page(
"arkansas-extension.html",
"Arkansas Tax Extension Guide | Extension Guide",
"Arkansas individual and corporate income tax extension - automatic if a federal extension is attached to the state return, otherwise Form AR1055. Ark. Code Ann. sect 26-51-807.",
"Arkansas - State Tax Extension",
"Individuals &amp; Business &nbsp;&bull;&nbsp; Automatic With Federal &nbsp;&bull;&nbsp; Verified 9-23-2026",
["Automatic with federal extension", "1 month beyond federal due date", "AR1055 if no federal extension"],
"states-hub.html",
"""<div class="slogan"><p>An extension to file is not an extension to pay tax.</p></div>
<p class="lead">Arkansas honors a federal extension automatically - a taxpayer who filed federal Form 4868 or Form 7004 gets an Arkansas extension to one month after the federal extended due date, with no separate state application required. A taxpayer who needs an extension without a federal one, or a longer state-only extension, files Form AR1055.</p>

<div class="green-box"><strong>Get the form:</strong> <a href="https://www.arkansas.gov/dfa/income_tax/documents/AR1155.pdf" target="_blank" rel="noopener">Download Form AR1055 (PDF, arkansas.gov)</a> &nbsp;&bull;&nbsp; <a href="https://www.dfa.arkansas.gov/office/taxes/income-tax-administration/individual-income-tax/deadlines-extensions/" target="_blank" rel="noopener">Deadlines &amp; Extensions (dfa.arkansas.gov)</a></div>

<table class="dt">
<tr><th>Item</th><th>Detail</th></tr>
<tr><td>Form required</td><td>None if a federal extension (Form 4868 or 7004) was requested - current DFA guidance does not require attaching a copy; Form AR1055 only if no federal extension applies or a state-specific extension is needed</td></tr>
<tr><td>Extension length</td><td>1 month after the federal extended due date - to November 15, 2026 for calendar-year individual and fiduciary filers</td></tr>
<tr><td>Payment rule</td><td>Not extended; interest and the failure-to-pay penalty accrue on unpaid tax from the original due date</td></tr>
<tr><td>Authority</td><td>Ark. Code Ann. &sect;26-51-807 (filing returns; extensions of time)</td></tr>
</table>

<div class="note-box">Section 26-51-807(a) technically requires attaching a copy of the federal extension request to the Arkansas return; subsection (d) lets the Secretary waive that documentation requirement by rule, which current DFA guidance does - confirm the current-year practice on the DFA site before relying on the waiver.</div>

<div class="related">
  <div class="related-title">Related</div>
  <div class="related-links">
    <a href="states-hub.html" class="related-link">All States<span>Back to the states hub</span></a>
    <a href="oregon-extension.html" class="related-link">Oregon<span>Also automatic with the federal extension</span></a>
    <a href="master-extension-matrix.html" class="related-link">Master Matrix<span>Every jurisdiction, one table</span></a>
  </div>
</div>""",
"Authority: Ark. Code Ann. &sect;26-51-807 (filing returns; extensions of time). Sources: law.justia.com/codes/arkansas/title-26/subtitle-5/chapter-51/subchapter-8/section-26-51-807; dfa.arkansas.gov/office/taxes/income-tax-administration/individual-income-tax/deadlines-extensions. Verified against primary source September 23, 2026."
)

# ---------------- COLORADO ----------------
page(
"colorado-extension.html",
"Colorado Tax Extension Guide | Extension Guide",
"Colorado individual and corporate income tax extension - automatic 6 months, no application required, but at least 90% of net tax liability must be paid by the original due date. C.R.S. sect 39-22-608.",
"Colorado - State Tax Extension",
"Individuals &amp; Business &nbsp;&bull;&nbsp; Automatic &nbsp;&bull;&nbsp; Verified 9-23-2026",
["No application required", "6 months", "90% payment to avoid penalty"],
"states-hub.html",
"""<div class="slogan"><p>An extension to file is not an extension to pay tax.</p></div>
<p class="lead">Colorado grants an automatic 6-month extension to file, with no application required to get the extension itself. DR 0158-I (individual) and DR 0158-C (corporate) are payment vouchers, not extension requests - they are used only when a payment accompanies the extension. The tradeoff for the automatic extension is a 90% payment test.</p>

<div class="green-box"><strong>Payment voucher (if tax is owed):</strong> <a href="https://tax.colorado.gov/sites/tax/files/documents/DR_0158-I_2022_0.pdf" target="_blank" rel="noopener">Download Form DR 0158-I (PDF, tax.colorado.gov)</a> &nbsp;&bull;&nbsp; <a href="https://tax.colorado.gov/income-tax-due-dates-filing-extension" target="_blank" rel="noopener">Due Dates &amp; Filing Extension (tax.colorado.gov)</a></div>

<table class="dt">
<tr><th>Item</th><th>Detail</th></tr>
<tr><td>Form required</td><td>None to obtain the extension itself; DR 0158-I / DR 0158-C used only to remit a payment with the extension</td></tr>
<tr><td>Extension length</td><td>6 months, to October 15, 2026 for calendar-year individual filers</td></tr>
<tr><td>Payment threshold</td><td>At least 90% of the net tax liability must be paid by the original April 15 due date to avoid penalty; interest still accrues on any unpaid balance</td></tr>
<tr><td>Authority</td><td>C.R.S. &sect;39-22-608(2) (Department's rulemaking authority to grant extensions under prescribed rules)</td></tr>
</table>

<div class="note-box">The 90% payment threshold and the automatic, no-form-required mechanics are published as current Department of Revenue administrative guidance implementing the Department's rulemaking authority under &sect;39-22-608(2) - confirm the current-year figure on the Department's site, since the statute itself sets the framework rather than a fixed percentage.</div>

<div class="related">
  <div class="related-title">Related</div>
  <div class="related-links">
    <a href="states-hub.html" class="related-link">All States<span>Back to the states hub</span></a>
    <a href="california-extension.html" class="related-link">California<span>Also automatic, no application required</span></a>
    <a href="master-extension-matrix.html" class="related-link">Master Matrix<span>Every jurisdiction, one table</span></a>
  </div>
</div>""",
"Authority: C.R.S. &sect;39-22-608(2) (extension rulemaking authority). Sources: tax.colorado.gov/income-tax-due-dates-filing-extension; tax.colorado.gov/DR0158I; law.justia.com/codes/colorado/2022/title-39/article-22/part-6/section-39-22-608. Verified against primary source September 23, 2026."
)

# ---------------- CONNECTICUT ----------------
page(
"connecticut-extension.html",
"Connecticut Tax Extension Guide | Extension Guide",
"Connecticut individual income tax extension - automatic only if no additional Connecticut tax is owed and a federal extension was requested; otherwise Form CT-1040 EXT with a tentative payment. Conn. Agencies Regs. sect 12-723-1.",
"Connecticut - State Tax Extension",
"Individuals &amp; Business &nbsp;&bull;&nbsp; Conditional-Automatic &nbsp;&bull;&nbsp; Verified 9-23-2026",
["Form CT-1040 EXT (if tax owed)", "6 months", "Tentative payment required"],
"states-hub.html",
"""<div class="slogan"><p>An extension to file is not an extension to pay tax.</p></div>
<p class="lead">Connecticut's extension is automatic in one narrow case - a taxpayer who requested a federal extension and expects to owe no additional Connecticut tax does not need to file anything separately. Everyone else, including any taxpayer who owes additional Connecticut tax, must file Form CT-1040 EXT and pay the tentative tax due by the original due date.</p>

<div class="green-box"><strong>Get the form:</strong> <a href="https://portal.ct.gov/-/media/drs/forms/2025/income/ct-1040-ext_1225.pdf" target="_blank" rel="noopener">Download Form CT-1040 EXT (PDF, portal.ct.gov)</a></div>

<table class="dt">
<tr><th>Item</th><th>Detail</th></tr>
<tr><td>Form required</td><td>Form CT-1040 EXT, unless a federal extension was requested and no additional Connecticut tax is owed</td></tr>
<tr><td>Extension length</td><td>6 months, matching the federal extension period, to October 15, 2026</td></tr>
<tr><td>Payment rule</td><td>The tentative Connecticut tax shown on the form must be paid by the original due date; a 10% penalty applies if the tax shown on the completed return exceeds the tentative payment (subject to limited exceptions), plus interest on any underpayment</td></tr>
<tr><td>Authority</td><td>Conn. Agencies Regs. &sect;12-723-1 (extension of time for filing returns)</td></tr>
</table>

<div class="note-box">Corporations file Form CT-1120 EXT for an automatic 6-month extension of the corporation business tax return under Conn. Gen. Stat. &sect;12-222; this page focuses on the individual (CT-1040) rule.</div>

<div class="related">
  <div class="related-title">Related</div>
  <div class="related-links">
    <a href="states-hub.html" class="related-link">All States<span>Back to the states hub</span></a>
    <a href="massachusetts-extension.html" class="related-link">Massachusetts<span>Also a conditional-automatic extension</span></a>
    <a href="master-extension-matrix.html" class="related-link">Master Matrix<span>Every jurisdiction, one table</span></a>
  </div>
</div>""",
"Authority: Conn. Agencies Regs. &sect;12-723-1 (extension of time for filing returns); Conn. Gen. Stat. &sect;12-222 (corporation business tax annual return). Sources: law.cornell.edu/regulations/connecticut/Regs-Conn-State-Agencies-SS-12-723-1; portal.ct.gov/-/media/drs/forms/2025/income/ct-1040-ext_1225.pdf. Verified against primary source September 23, 2026."
)

print("batch 3 done")
