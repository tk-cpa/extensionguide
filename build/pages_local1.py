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

# ---------------- NEW YORK CITY ----------------
page(
    "new-york-city-extension.html",
    "New York City Tax Extension Guide | Extension Guide",
    "NYC individual income tax rides on the New York State return (Form IT-370) - no separate NYC extension form. NYC business income and excise taxes use Form NYC-6, automatic 6 months. NYC Rules citing Admin. Code sect 11-605(1).",
    "New York City - Local Tax Extension",
    "Individuals &amp; Business &nbsp;&bull;&nbsp; Automatic &nbsp;&bull;&nbsp; Verified 9-23-2026",
    ["Individual: rides on NY State IT-370", "Business: Form NYC-6, 6 months", "Estimated payment required (business)"],
    "states-hub.html",
    SLOGAN + '''
<p class="lead">New York City does not have a separate personal income tax return - NYC resident tax is computed and filed on the New York State return (Form IT-201 or IT-203), so an individual who extends the state return with Form IT-370 automatically extends the NYC portion of the liability with it. There is no standalone NYC individual extension form. Businesses subject to NYC's own taxes (General Corporation Tax, Business Corporation Tax, Unincorporated Business Tax) file Form NYC-6 for an automatic 6-month extension, provided a properly estimated tax is paid by the original due date; the NYC Department of Finance may grant up to two further 3-month extensions for good cause.</p>

<div class="green-box"><strong>Guidance:</strong> <a href="https://www.nyc.gov/site/finance/business/business-general-corporation-tax-gct.page" target="_blank" rel="noopener">NYC Department of Finance - General Corporation Tax</a> &nbsp;&bull;&nbsp; <a href="https://www.tax.ny.gov/pdf/2025/inc/it370pfi_2025.pdf" target="_blank" rel="noopener">Form IT-370 Instructions (individual, PDF)</a></div>

<table class="dt">
<tr><th>Item</th><th>Detail</th></tr>
<tr><td>Individual NYC tax</td><td>Computed on the NY State resident/nonresident return - extended automatically by filing state Form IT-370; no separate NYC form</td></tr>
<tr><td>Business extension form</td><td>NYC-6 (Application for Automatic Extension), for General Corporation Tax, Business Corporation Tax, and Unincorporated Business Tax filers</td></tr>
<tr><td>Extension length</td><td>Automatic 6 months for businesses; up to two additional 3-month extensions available for good cause</td></tr>
<tr><td>Payment condition</td><td>A properly estimated tax must be paid with Form NYC-6 by the original due date - the extension is for filing only</td></tr>
<tr><td>Authority</td><td>NYC Rules (title 19, ch. 11) implementing N.Y.C. Admin. Code &sect;11-605(1)</td></tr>
</table>

<div class="note-box">This page covers New York City's own local taxes. See the <a href="new-york-extension.html">New York state page</a> for the state-level individual and corporate extension rules that also apply to NYC residents and businesses.</div>
''' + related(
        ("states-hub.html", "All States", "Back to the states hub"),
        ("new-york-extension.html", "New York (State)", "The state return NYC individual tax rides on"),
        ("philadelphia-extension.html", "Philadelphia", "Another major city with its own business taxes"),
    ),
    "Authority: N.Y.C. Admin. Code sect 11-605(1); NYC Rules title 19, ch. 11 (Form NYC-6). Sources: codelibrary.amlegal.com/codes/newyorkcity/latest/NYCrules; nyc.gov/site/finance/business/business-general-corporation-tax-gct.page; tax.ny.gov Form IT-370 instructions. Verified against primary source September 23, 2026.",
)

# ---------------- PHILADELPHIA ----------------
page(
    "philadelphia-extension.html",
    "Philadelphia Tax Extension Guide | Extension Guide",
    "Philadelphia honors the automatic federal 6-month extension for BIRT and Net Profits Tax filers - no separate city form. Payment is still due on the original date.",
    "Philadelphia - Local Tax Extension",
    "Business (BIRT &amp; NPT) &nbsp;&bull;&nbsp; Automatic with federal &nbsp;&bull;&nbsp; Verified 9-23-2026",
    ["No separate city form", "6 months", "Payment due on original date"],
    "states-hub.html",
    SLOGAN + '''
<p class="lead">Philadelphia does not require a separate city extension application for its Business Income and Receipts Tax (BIRT) or Net Profits Tax (NPT): the Department of Revenue honors the same automatic 6-month extension the IRS grants for the federal return. There is no city form to file to get the extension itself. As with every other jurisdiction on this site, the extension covers filing only - Philadelphia taxes owed remain due on the original date, and late payments accrue interest and penalties. Philadelphia's Wage Tax is withheld and remitted by employers and does not have an individual filing-extension mechanism in the way an income tax return does.</p>

<div class="green-box"><strong>Guidance:</strong> <a href="https://www.phila.gov/services/payments-assistance-taxes/taxes/business-taxes/business-taxes-by-type/business-income-receipts-tax-birt/" target="_blank" rel="noopener">City of Philadelphia - Business Income &amp; Receipts Tax (BIRT)</a></div>

<table class="dt">
<tr><th>Item</th><th>Detail</th></tr>
<tr><td>Form required</td><td>None - the federal extension is honored automatically for BIRT and NPT</td></tr>
<tr><td>Extension length</td><td>6 months, matching the federal extension</td></tr>
<tr><td>Payment</td><td>Not extended - BIRT/NPT payments are due on the original date; interest and penalties apply to late payments</td></tr>
<tr><td>Authority</td><td>Philadelphia Department of Revenue guidance (BIRT/NPT extension policy)</td></tr>
</table>
''' + related(
        ("states-hub.html", "All States", "Back to the states hub"),
        ("pennsylvania-extension.html", "Pennsylvania (State)", "The state extension rules that also apply to Philadelphia filers"),
        ("new-york-city-extension.html", "New York City", "Another major city with its own business taxes"),
    ),
    "Authority: Philadelphia Department of Revenue, BIRT/NPT extension guidance. Sources: phila.gov/2018-10-04-tax-filing-extensions-dont-miss-oct-15-deadline; phila.gov business-income-receipts-tax-birt. Verified against primary source September 23, 2026.",
)

# ---------------- OHIO MUNICIPAL (RITA / CCA) ----------------
page(
    "ohio-municipal-extension.html",
    "Ohio Municipal Tax Extension Guide (RITA &amp; CCA) | Extension Guide",
    "Ohio's roughly 600 municipal income taxes are governed by one uniform state statute - ORC 718.05(G). A federal extension automatically extends the municipal return; without one, a 6-month extension must be granted on timely request. Covers RITA and CCA member cities alike.",
    "Ohio Municipalities - Local Tax Extension (RITA &amp; CCA)",
    "Individuals &amp; Business &nbsp;&bull;&nbsp; Automatic with federal &nbsp;&bull;&nbsp; Verified 9-23-2026",
    ["Covers all ~600 OH municipalities", "Automatic with federal extension", "6 months if requested without federal extension"],
    "states-hub.html",
    SLOGAN + '''
<p class="lead">Ohio is unusual among states in that its municipal income taxes - imposed by roughly 600 cities and villages - are not each governed by a separate local ordinance on this point. Ohio Revised Code &sect;718.05(G) is a single state statute that applies uniformly to every Ohio municipality with an income tax, whether the municipality is administered by the Regional Income Tax Agency (RITA), the Central Collection Agency (CCA), another third-party administrator, or its own tax department. A taxpayer who requested an automatic 6-month federal extension automatically receives the same extension for the municipal return - no separate municipal request is needed. A taxpayer without a federal extension may still request a 6-month municipal extension from the tax administrator (RITA, CCA, or the city), and the administrator must grant it if requested before the due date. Either way, the extension is for filing only; municipal tax owed remains due on the original date.</p>

<div class="green-box"><strong>Guidance:</strong> <a href="https://www.ritaohio.com/Individuals/Faqs?category=I&amp;subcategory=Filing&amp;questionID=2" target="_blank" rel="noopener">RITA - Individual FAQs on Filing Extensions</a> &nbsp;&bull;&nbsp; <a href="https://www.ccaohio.gov/" target="_blank" rel="noopener">CCA - Division of Taxation (Cleveland)</a></div>

<table class="dt">
<tr><th>Item</th><th>Detail</th></tr>
<tr><td>Scope</td><td>Every Ohio municipality with an income tax - RITA member cities, CCA member cities, and self-administered cities alike, under one statewide statute</td></tr>
<tr><td>Form required</td><td>None if a federal extension was obtained (attach a copy to the municipal return); a written request to the administrator otherwise (RITA's Form 32 EST-EXT, or the equivalent for CCA/self-administered cities)</td></tr>
<tr><td>Automatic</td><td>Yes, when tied to a federal extension; a request-based 6-month extension is available without one and must be granted if timely requested</td></tr>
<tr><td>Extension length</td><td>Matches the federal extension, or 6 months if requested independently</td></tr>
<tr><td>Payment</td><td>Not extended - municipal tax due remains due on the original date unless the tax administrator separately extends the payment date</td></tr>
<tr><td>Authority</td><td>Ohio Rev. Code &sect;718.05(G)(2)</td></tr>
</table>

<div class="note-box">Because this rule is set at the state level, it is the same whether a specific city's tax is collected by RITA, by CCA, or by the city itself - there is no need for separate per-city extension pages for Ohio's municipal income tax.</div>
''' + related(
        ("states-hub.html", "All States", "Back to the states hub"),
        ("ohio-extension.html", "Ohio (State)", "Ohio's own state income tax extension rules"),
        ("michigan-cities-extension.html", "Michigan Cities", "Michigan's parallel uniform city income tax rule"),
    ),
    "Authority: Ohio Rev. Code sect 718.05(G)(2). Sources: codes.ohio.gov/ohio-revised-code/section-718.05; ritaohio.com/Individuals/Faqs (Filing/Extensions); ccaohio.gov. Verified against primary source September 23, 2026.",
)

# ---------------- MICHIGAN CITIES ----------------
page(
    "michigan-cities-extension.html",
    "Michigan Cities Tax Extension Guide | Extension Guide",
    "Michigan's roughly two dozen cities with an income tax (including Detroit) operate under one state law, the Uniform City Income Tax Ordinance - written request required, up to 6 months, 70% payment threshold. MCL 141.664.",
    "Michigan Cities - Local Tax Extension",
    "Individuals &amp; Business &nbsp;&bull;&nbsp; Not automatic &nbsp;&bull;&nbsp; Verified 9-23-2026",
    ["Covers all ~24 MI cities with a city tax", "Written request required", "Up to 6 months, 70% payment threshold"],
    "states-hub.html",
    SLOGAN + '''
<p class="lead">Michigan is the other state, alongside Ohio, where city-level income tax extension rules are set once at the state level rather than city by city. Roughly two dozen Michigan cities - including Detroit, Grand Rapids, Lansing, and Flint - levy a city income tax under the Uniform City Income Tax Ordinance, part of the City Income Tax Act. A taxpayer must make a written request to the city administrator (or the Michigan Department of Treasury, for cities that have an agreement with the state) for an extension of up to 6 months. No penalty or interest applies if the return is filed and tax paid within the extended period and the estimated tax already paid equals at least 70% of the tax shown due on the final return (or 70% of the prior year's tax).</p>

<div class="green-box"><strong>Guidance:</strong> <a href="https://www.michigan.gov/treasury/reference/taxpayer-notices/2020/04/28/automatic-extension-city-of-detroit-income-tax-filing-deadlines" target="_blank" rel="noopener">Michigan Department of Treasury - City Income Tax Notices</a></div>

<table class="dt">
<tr><th>Item</th><th>Detail</th></tr>
<tr><td>Scope</td><td>All Michigan cities levying an income tax under the Uniform City Income Tax Ordinance (about two dozen cities, including Detroit)</td></tr>
<tr><td>Form required</td><td>A written request to the city administrator or, for cities under a state collection agreement, the Michigan Department of Treasury</td></tr>
<tr><td>Automatic</td><td>No - the extension must be requested; it is not tied automatically to the federal extension</td></tr>
<tr><td>Extension length</td><td>Up to 6 months</td></tr>
<tr><td>Payment threshold</td><td>No penalty or interest if estimated tax already paid equals at least 70% of the tax shown due on the final return (or 70% of the prior year's tax) and the balance is paid with the return</td></tr>
<tr><td>Authority</td><td>MCL 141.664(1),(2)</td></tr>
</table>
''' + related(
        ("states-hub.html", "All States", "Back to the states hub"),
        ("michigan-extension.html", "Michigan (State)", "Michigan's own state income tax extension rules"),
        ("ohio-municipal-extension.html", "Ohio Municipalities", "Ohio's parallel statewide local tax rule"),
    ),
    "Authority: MCL 141.664(1),(2) (Uniform City Income Tax Ordinance, City Income Tax Act, Act 284 of 1964). Sources: law.justia.com/codes/michigan/2006/mcl-chap141/mcl-141-664.html; michigan.gov/treasury city income tax notices. Verified against primary source September 23, 2026.",
)

# ---------------- KANSAS CITY, MO ----------------
page(
    "kansas-city-extension.html",
    "Kansas City Earnings Tax Extension Guide | Extension Guide",
    "Kansas City, Missouri earnings tax extension - Form RD-112 (wage earners) or RD-111 (profits), automatic upon timely filing and paying the tax shown due.",
    "Kansas City, Missouri - Local Tax Extension",
    "Earnings Tax &nbsp;&bull;&nbsp; Automatic upon timely request &nbsp;&bull;&nbsp; Verified 9-23-2026",
    ["Form RD-112 (wage) / RD-111 (profits)", "Automatic with timely filing + payment", "Pay tax due with request"],
    "states-hub.html",
    SLOGAN + '''
<p class="lead">Kansas City, Missouri imposes a 1% earnings tax on wages and net profits earned in the city. A wage earner who needs more time to file the annual earnings tax return (Form RD-109) files Form RD-112; a business or self-employed filer of the profits return (Form RD-108) files Form RD-111. Either extension is granted automatically upon timely receipt of the tax shown due and a completed extension application - there is no separate approval step once those conditions are met. As with every jurisdiction on this site, the extension covers filing only, not payment.</p>

<div class="green-box"><strong>Forms and guidance:</strong> <a href="https://www.kcmo.gov/city-hall/departments/finance/tax-home/tax-forms" target="_blank" rel="noopener">City of Kansas City, MO - Tax Forms</a></div>

<table class="dt">
<tr><th>Item</th><th>Detail</th></tr>
<tr><td>Form required</td><td>RD-112 (wage earners) or RD-111 (profits/business)</td></tr>
<tr><td>Automatic</td><td>Yes, upon timely receipt of the tax shown due and a completed application</td></tr>
<tr><td>Payment</td><td>The tax due shown on the extension application must be paid by the original due date; instructions for the annual return separately note a 90% payment threshold to avoid penalty</td></tr>
<tr><td>Authority</td><td>Kansas City, MO Code of Ordinances ch. 68, art. VI (Earnings and Profits Tax)</td></tr>
</table>
''' + related(
        ("states-hub.html", "All States", "Back to the states hub"),
        ("st-louis-extension.html", "St. Louis, Missouri", "Missouri's other earnings-tax city"),
        ("missouri-extension.html", "Missouri (State)", "Missouri's own state income tax extension rules"),
    ),
    "Authority: Kansas City, MO Code of Ordinances ch. 68, art. VI. Sources: kcmo.gov/city-hall/departments/finance/tax-home/tax-forms (Form RD-112 instructions). Verified against primary source September 23, 2026.",
)

# ---------------- ST. LOUIS, MO ----------------
page(
    "st-louis-extension.html",
    "St. Louis Earnings Tax Extension Guide | Extension Guide",
    "St. Louis, Missouri earnings tax extension - Form E-8, Application for Extension of Time to File Form E-234.",
    "St. Louis, Missouri - Local Tax Extension",
    "Earnings Tax &nbsp;&bull;&nbsp; Request required &nbsp;&bull;&nbsp; Verified 9-23-2026",
    ["Form E-8", "For business Form E-234", "Payment due with request"],
    "states-hub.html",
    SLOGAN + '''
<p class="lead">St. Louis, Missouri imposes a 1% earnings tax on wages and net profits earned in the city, administered by the Collector of Revenue. A business or self-employed filer who needs more time to file the annual earnings tax return (Form E-234) requests an extension using Form E-8. As with Kansas City's parallel earnings tax, the extension is for filing only - payment of the tax due remains required by the original filing deadline.</p>

<div class="green-box"><strong>Forms and guidance:</strong> <a href="https://www.stlouis-mo.gov/government/departments/collector/earnings-tax/documents/index.cfm" target="_blank" rel="noopener">City of St. Louis Collector of Revenue - Earnings Tax Forms and Documents</a></div>

<table class="dt">
<tr><th>Item</th><th>Detail</th></tr>
<tr><td>Form required</td><td>E-8 (Application for Extension of Time to File Form E-234)</td></tr>
<tr><td>Automatic</td><td>Granted upon timely, complete request with payment of tax due</td></tr>
<tr><td>Payment</td><td>Not extended - tax due must accompany the extension request</td></tr>
<tr><td>Authority</td><td>City of St. Louis Collector of Revenue, Earnings Tax administration (Form E-8)</td></tr>
</table>
''' + related(
        ("states-hub.html", "All States", "Back to the states hub"),
        ("kansas-city-extension.html", "Kansas City, Missouri", "Missouri's other earnings-tax city"),
        ("missouri-extension.html", "Missouri (State)", "Missouri's own state income tax extension rules"),
    ),
    "Authority: City of St. Louis Collector of Revenue, Earnings Tax Form E-8. Sources: stlouis-mo.gov/government/departments/collector/earnings-tax/documents/index.cfm. Verified against primary source September 23, 2026.",
)

# ---------------- PORTLAND / MULTNOMAH COUNTY ----------------
page(
    "portland-multnomah-extension.html",
    "Portland / Multnomah County Tax Extension Guide | Extension Guide",
    "Portland and Multnomah County, Oregon combined business tax extension - Form EXT, automatic 6 months, 90%/100% payment safe harbor.",
    "Portland / Multnomah County, Oregon - Local Tax Extension",
    "Business Tax &nbsp;&bull;&nbsp; Automatic (with Form EXT) &nbsp;&bull;&nbsp; Verified 9-23-2026",
    ["Form EXT required", "6 months", "90%/100% payment safe harbor"],
    "states-hub.html",
    SLOGAN + '''
<p class="lead">The City of Portland and Multnomah County jointly administer a Combined Business Tax (covering the Portland Business License Tax and the Multnomah County Business Income Tax) through the Revenue Division. Filing a federal extension does not by itself extend the local filing deadline - a taxpayer must file Form EXT and attach a copy of the federal extension, checking the "Extension Filed" box on the return when it is eventually filed. Doing so grants a 6-month extension to file, generally to October 15 for calendar-year filers. The tradeoff is a payment safe harbor: at least 90% of the current year's tax or 100% of the prior year's tax must be paid by the original due date to avoid underpayment penalties.</p>

<div class="green-box"><strong>Forms and guidance:</strong> <a href="https://www.portland.gov/revenue/business-tax" target="_blank" rel="noopener">City of Portland Revenue Division - Business Tax Filing and Payment</a></div>

<table class="dt">
<tr><th>Item</th><th>Detail</th></tr>
<tr><td>Form required</td><td>Form EXT, with a copy of the federal extension attached</td></tr>
<tr><td>Extension length</td><td>6 months, generally to October 15 for calendar-year filers</td></tr>
<tr><td>Payment safe harbor</td><td>At least 90% of current-year tax or 100% of prior-year tax paid by the original due date</td></tr>
<tr><td>Authority</td><td>City of Portland / Multnomah County Revenue Division, Combined Business Tax extension guidance (Form EXT)</td></tr>
</table>
''' + related(
        ("states-hub.html", "All States", "Back to the states hub"),
        ("oregon-extension.html", "Oregon (State)", "Oregon's own state income tax extension rules"),
        ("san-francisco-extension.html", "San Francisco", "Another major West Coast city with its own business tax"),
    ),
    "Authority: City of Portland / Multnomah County Revenue Division, Combined Business Tax Form EXT. Sources: portland.gov/revenue/business-tax; portland.gov/revenue/documents/form-ext-request-extension-time-file-fill-print. Verified against primary source September 23, 2026.",
)

# ---------------- SAN FRANCISCO ----------------
page(
    "san-francisco-extension.html",
    "San Francisco Tax Extension Guide | Extension Guide",
    "San Francisco Annual Business Tax Return (Gross Receipts Tax) extension - must be requested, not automatic, full payment of the current-year liability due by the original filing deadline.",
    "San Francisco - Local Tax Extension",
    "Business Tax &nbsp;&bull;&nbsp; Not automatic &nbsp;&bull;&nbsp; Verified 9-23-2026",
    ["Extension request required", "Not tied to federal extension", "Full payment due by original date"],
    "states-hub.html",
    SLOGAN + '''
<p class="lead">San Francisco's Annual Business Tax Return (covering the city's Gross Receipts Tax and related business taxes) is administered by the Office of the Treasurer &amp; Tax Collector. An extension is not automatic and is not tied to the federal extension - a business must affirmatively submit an extension request. Payment of the current year's tax liability is still required by the original filing deadline; a request submitted without that payment is rejected and penalties apply. Because the current year's exact extended deadline and request process are set annually by the Treasurer's office, confirm the current filing calendar before relying on a specific date.</p>

<div class="green-box"><strong>Guidance:</strong> <a href="https://sftreasurer.org/business/taxes-fees/gross-receipts-tax-gr-0" target="_blank" rel="noopener">SF Office of the Treasurer &amp; Tax Collector - Gross Receipts Tax</a></div>

<table class="dt">
<tr><th>Item</th><th>Detail</th></tr>
<tr><td>Form required</td><td>An extension request submitted through the Treasurer &amp; Tax Collector's office (procedure set annually)</td></tr>
<tr><td>Automatic</td><td>No - not automatic, and not tied to a federal extension</td></tr>
<tr><td>Payment</td><td>Full payment of the current year's tax liability is required by the original filing deadline; a request without full payment is rejected</td></tr>
<tr><td>Authority</td><td>SF Office of the Treasurer &amp; Tax Collector, Annual Business Tax Return extension guidance</td></tr>
</table>

<div class="note-box">Confirm the current tax year's exact deadlines and extension request procedure directly with the Treasurer &amp; Tax Collector's office, since San Francisco's business tax calendar and extension mechanics are republished each filing season.</div>
''' + related(
        ("states-hub.html", "All States", "Back to the states hub"),
        ("california-extension.html", "California (State)", "California's own state income tax extension rules"),
        ("portland-multnomah-extension.html", "Portland / Multnomah County", "Another West Coast local business tax"),
    ),
    "Authority: SF Office of the Treasurer and Tax Collector, Annual Business Tax Return extension guidance. Sources: sftreasurer.org/business/taxes-fees/gross-receipts-tax-gr-0; sftreasurer.org/annual-business-tax-return-instructions-2024. Verified against primary source September 23, 2026.",
)

# ---------------- PENNSYLVANIA LOCAL EARNED INCOME TAX (ACT 32) ----------------
page(
    "pennsylvania-local-eit-extension.html",
    "Pennsylvania Local Earned Income Tax (Act 32) Extension Guide | Extension Guide",
    "Pennsylvania's local Earned Income Tax, filed statewide through Act 32 tax collection districts (Berkheimer, Keystone, Jordan Tax, and others), has no statutory extension provision - the underlying Local Tax Enabling Act sets an April 15 due date with no extension language anywhere in the act. Collectors uniformly grant a filing extension as administrative practice only, tied to the federal or state extension, with no citable statutory authority.",
    "Pennsylvania Local Earned Income Tax (Act 32) - Local Tax Extension",
    "Applies statewide outside Philadelphia &nbsp;&bull;&nbsp; No statutory extension provision &nbsp;&bull;&nbsp; Verified 9-23-2026",
    ["~20 tax collection districts, 1 rule", "No statutory extension exists", "Collector practice, not law"],
    "states-hub.html",
    SLOGAN + '''
<p class="lead">Every Pennsylvania municipality and school district outside Philadelphia imposes a local Earned Income Tax (EIT) under Act 32 of 2008, collected not by the state but by one of roughly 20 regional tax collection districts (Berkheimer/HAB, Keystone Collections Group, Jordan Tax Service, Berks EIT Bureau, and others, depending on where the taxpayer lives and works). All of them use the same statewide-prescribed return, Form CLGS-32-1, so the extension rule below applies uniformly regardless of which collector serves a given address.</p>

<div class="red-box"><strong>No statutory extension of time to file exists.</strong> The Local Tax Enabling Act (53 P.S. &sect;6924.502(c)(1), the section governing the final return) sets the due date at April 15 of the succeeding year and contains no extension-of-time language anywhere in the section, or anywhere else in the act - confirmed this session by a section-by-section text search of the full act (66 pages) for every instance of the word "extension"; the only matches concern an unrelated dispute-mediation process, not the taxpayer filing deadline. 12 Pa. Code Chapter 151 (the implementing regulation) likewise has no extension section - it covers only definitions, withholding, and tax-officer administration. This is a definitive negative finding, not an unresolved search.</div>

<p>What exists instead is a uniform administrative practice, not a codified right: the major collectors (confirmed against Berkheimer's and Keystone's own current instructions) allow a taxpayer who has filed a federal or state extension to submit a copy of that extension, along with an estimated payment, by the original April 15 due date, in exchange for treating the local return as not yet delinquent until the extended federal/state due date (typically October 15). This is the collector's own administrative accommodation, adopted uniformly across the state's tax collection districts, not a right created by Act 32, the Local Tax Enabling Act, or 12 Pa. Code Chapter 151 - no statute or regulation was found authorizing it. Payment of the estimated local tax due is still required by April 15 regardless; only the paperwork deadline moves.</p>

<div class="green-box"><strong>Forms and guidance:</strong> <a href="https://dced.pa.gov/local-government/local-income-tax-information/" target="_blank" rel="noopener">PA DCED - Act 32 Local Income Tax Information</a> &nbsp;&bull;&nbsp; <a href="https://www.hab-inc.com/local-earned-income-tax-return-faq/" target="_blank" rel="noopener">Berkheimer (HAB) - Local EIT Return FAQ</a> &nbsp;&bull;&nbsp; <a href="https://keystonecollects.com/download/ITRInstructions.pdf" target="_blank" rel="noopener">Keystone Collections Group - CLGS-32-1 Instructions (PDF)</a></div>

<table class="dt">
<tr><th>Item</th><th>Detail</th></tr>
<tr><td>Governing law</td><td>The Local Tax Enabling Act, 53 P.S. &sect;6924.502(c)(1) (final return due date); implementing regulation at 12 Pa. Code Chapter 151</td></tr>
<tr><td>Statutory due date</td><td>April 15 of the succeeding year, fixed by statute with no extension provision</td></tr>
<tr><td>Statutory extension mechanism</td><td>None exists - confirmed by direct text search of the full act and its implementing regulation</td></tr>
<tr><td>Collector administrative practice</td><td>Submit a copy of the federal or state extension plus an estimated payment by April 15; the collector then treats the return as timely if filed by the federal/state extended date (typically October 15). This is collector practice, not statutory or regulatory authority.</td></tr>
<tr><td>Extends time to pay?</td><td>No - estimated tax is still due April 15 regardless of any extension paperwork</td></tr>
<tr><td>Form</td><td>CLGS-32-1 (Taxpayer Annual Local Earned Income Tax Return), statewide-prescribed by DCED; collector-specific extension request forms available (e.g., Keystone's online extension request)</td></tr>
</table>

<div class="note-box">This page covers the Act 32 local EIT return, which applies to every PA municipality except Philadelphia (which has its own Wage Tax and Net Profits Tax system - see the Philadelphia page). It does not cover Philadelphia, or the separate Local Services Tax (a flat per-capita occupational tax withheld by employers, not an income-based return with a comparable annual filing deadline).</div>
''' + related(
        ("states-hub.html", "All States", "Back to the states hub"),
        ("pennsylvania-extension.html", "Pennsylvania (State)", "Pennsylvania's own state income tax extension rules"),
        ("philadelphia-extension.html", "Philadelphia", "Philadelphia's separate Wage Tax and Net Profits Tax system"),
    ),
    "Authority: 53 P.S. sect 6924.502(c)(1) (Local Tax Enabling Act); 12 Pa. Code Chapter 151. Sources: legis.state.pa.us and captax.com (full text of Act 511 of 1965 as amended, 66-page PDF, searched directly this session for every instance of \"extension\"); pacodeandbulletin.gov (12 Pa. Code Chapter 151 table of contents); dced.pa.gov/local-government/local-income-tax-information; hab-inc.com/local-earned-income-tax-return-faq; keystonecollects.com/download/ITRInstructions.pdf; keystonecollects.com/form/application-for-extension-of-time-to-file-local-tax-return. Verified against primary source September 23, 2026.",
)

# ---------------- KENTUCKY LOCAL OCCUPATIONAL LICENSE TAX ----------------
page(
    "kentucky-local-occupational-tax-extension.html",
    "Kentucky Local Occupational License Tax Extension Guide | Extension Guide",
    "Kentucky's net profits occupational license fee is imposed separately by roughly 200 individual cities, counties, and school districts, each under its own ordinance. No statewide statute governs extension of time to file - HB 277 (2012) standardized the return forms (OL-S, OL-D) but left extension procedure to each taxing jurisdiction. Two sampled ordinances show a consistent pattern (automatic extension matching the federal period, payment not extended), disclosed as a sample, not an exhaustive county-by-county verification.",
    "Kentucky Local Occupational License Tax - Local Tax Extension",
    "~200 taxing jurisdictions statewide &nbsp;&bull;&nbsp; No statewide extension statute &nbsp;&bull;&nbsp; Verified 9-23-2026",
    ["Governed by ~200 local ordinances", "No statewide extension statute", "Sample, not exhaustive verification"],
    "states-hub.html",
    SLOGAN + '''
<p class="lead">Kentucky is unusual in that its net profits occupational license fee is levied independently by roughly 200 separate taxing jurisdictions - cities, counties, and (unlike anywhere else on this site) school districts - each acting under its own local ordinance rather than a single statewide statute. House Bill 277 (2012) required uniform statewide return forms (OL-S for a single tax district, OL-D for a dual city/county district), administered through the Kentucky One Stop Business Portal, but did not create a uniform extension rule.</p>

<div class="red-box"><strong>No statewide statute governs the extension of time to file.</strong> A direct check of the Kentucky statutes most likely to contain it - KRS 160.482 to 160.488 (school district occupational license fees) and KRS 92.281 (city occupational license tax, uniform provisions) - found no due-date or extension language in either. Kentucky's occupational license tax framework standardizes the return form, not the filing calendar or extension procedure; that is left entirely to each jurisdiction's own ordinance.</div>

<p>Two representative county ordinances were checked directly against their own current instructions this session, and both showed the same pattern: an automatic extension matching the length of the federal extension granted for the same year, on written request (or a copy of federal Form 4868/7004) submitted by the original due date, with payment of the estimated fee still required by that original date regardless. Whether this pattern holds across all roughly 200 Kentucky taxing jurisdictions was not, and could not reasonably be, verified this session - each jurisdiction sets and can change its own ordinance independently, and no central registry of extension terms exists. This is disclosed as a sample finding, not a completed county-by-county survey.</p>

<div class="green-box"><strong>Guidance and sampled sources:</strong> <a href="https://onestop.ky.gov/Pages/Default.aspx" target="_blank" rel="noopener">Kentucky One Stop Business Portal</a> &nbsp;&bull;&nbsp; <a href="https://jessamineky.gov/wp-content/uploads/2024/12/Net-Profit-Instructions.pdf" target="_blank" rel="noopener">Jessamine County/Nicholasville Net Profit Instructions (PDF)</a> &nbsp;&bull;&nbsp; <a href="https://logancountyky.gov/DocumentCenter/View/139/Net-Profit-Instructions-PDF" target="_blank" rel="noopener">Logan County Net Profit Instructions (PDF)</a></div>

<table class="dt">
<tr><th>Item</th><th>Detail</th></tr>
<tr><td>Governing law</td><td>No single statewide statute - each of roughly 200 cities, counties, and school districts imposes its own occupational license tax under its own ordinance; statewide statutes (KRS 160.482-.488, KRS 92.281) govern only jurisdictional and classification questions, not filing deadlines</td></tr>
<tr><td>Statewide standardized form</td><td>OL-S (single tax district) or OL-D (dual city/county district), via HB 277 (2012) and the Kentucky One Stop Business Portal - the form is uniform, the deadline and extension rule are not</td></tr>
<tr><td>Pattern observed (2 sampled counties)</td><td>Automatic extension matching the federal extension period, on written request or a copy of the federal extension filed by the original due date; payment of the estimated fee is not extended</td></tr>
<tr><td>Verification scope</td><td>Sample of 2 jurisdictions this session, not all ~200 - individual ordinance terms can and do vary, and this page does not claim otherwise</td></tr>
</table>

<div class="note-box">A specific Kentucky city, county, or school district's occupational license ordinance may set a different extension rule (or none at all) than the pattern above. Confirm directly with that jurisdiction's tax administrator or its published ordinance before relying on this page for a specific filing.</div>
''' + related(
        ("states-hub.html", "All States", "Back to the states hub"),
        ("kentucky-extension.html", "Kentucky (State)", "Kentucky's own state income tax extension rules"),
        ("pennsylvania-local-eit-extension.html", "Pennsylvania Local EIT", "Another state-specific local income tax system, unified by statute rather than by ordinance"),
    ),
    "Authority: no statewide statute - KRS 160.482-.488 and KRS 92.281 checked directly and contain no extension provision. Sources: klc.org (Local Occupational Tax: A Vetted System That Works; House Bill 277 background); statecodesfiles.justia.com (KRS 160.488, KRS 92.281 full text); onestop.ky.gov (OL-S/OL-D standardized forms); jessamineky.gov and logancountyky.gov (sampled county net profit return instructions). Verified against primary source September 23, 2026.",
)

# ---------------- DENVER OCCUPATIONAL PRIVILEGE TAX ----------------
page(
    "denver-opt-extension.html",
    "Denver Occupational Privilege Tax Extension Guide | Extension Guide",
    "Denver's Occupational Privilege Tax (OPT), a flat per-employee monthly, quarterly, or annual remittance under DRMC ch. 53, art. XI, has no extension mechanism - confirmed by a direct text search of Denver's general tax information booklet and every relevant Tax Guide topic, none of which mentions an extension of time to file.",
    "Denver Occupational Privilege Tax - Local Tax Extension",
    "Monthly/quarterly/annual remittance &nbsp;&bull;&nbsp; No extension mechanism &nbsp;&bull;&nbsp; Verified 9-23-2026",
    ["DRMC ch. 53, art. XI", "No extension mechanism found", "4 primary sources searched directly"],
    "states-hub.html",
    SLOGAN + '''
<p class="lead">Denver's Occupational Privilege Tax (OPT, sometimes called the "head tax") is a flat monthly amount owed on both the employee and the employer for each individual who performs sufficient work in the city, imposed under Denver Revised Municipal Code Chapter 53, Article XI (DRMC &sect;&sect;53-237 through 53-244). It is structurally closer to a payroll remittance than an income tax return: businesses with 10 or more employees file monthly, smaller businesses may file quarterly, and individuals, sole proprietors, and partnerships without employees may elect an annual filing due January 31.</p>

<div class="red-box"><strong>No extension mechanism was found.</strong> Denver's own general tax information booklet and its OPT-specific Tax Guide (Topic No. 61), Filing Periods guide (Topic No. 30), and Rules and Regulations guide (Topic No. 68) - more than 60,000 characters of primary guidance searched directly this session - contain no mention of an extension of time to file for OPT at any filing frequency. The annual OPT return form itself likewise has no extension line or reference. This mirrors the pattern already documented for federal payroll tax on this site: a periodic remittance tax structured around short, fixed filing windows rather than an annual return with a request-based extension.</div>

<div class="green-box"><strong>Guidance:</strong> <a href="https://www.denvergov.org/content/dam/denvergov/Portals/571/documents/TaxGuide/TaxGuideTopic61_OccupationalPrivilegeTaxes.pdf" target="_blank" rel="noopener">Denver Tax Guide Topic 61 - Occupational Privilege Taxes (PDF)</a></div>

<table class="dt">
<tr><th>Item</th><th>Detail</th></tr>
<tr><td>Filing frequency</td><td>Monthly (10+ employees), quarterly (fewer than 10 employees), or annual by election for individuals/sole proprietors/partnerships without employees</td></tr>
<tr><td>Due dates</td><td>Monthly: last day of the following month. Quarterly: last day of the month following the quarter. Annual: January 31.</td></tr>
<tr><td>Extension of time to file</td><td>None found in any primary Denver source checked this session</td></tr>
<tr><td>Authority</td><td>DRMC &sect;&sect;53-237 to 53-244 (Article XI, Employee and Business Occupational Privilege Tax)</td></tr>
</table>
''' + related(
        ("states-hub.html", "All States", "Back to the states hub"),
        ("colorado-extension.html", "Colorado (State)", "Colorado's own state income tax extension rules"),
        ("san-francisco-extension.html", "San Francisco", "Another city-level business tax, extension required rather than automatic"),
    ),
    "Authority: Denver Revised Municipal Code sect 53-237 to 53-244. Sources: denvergov.org General Tax Information Booklet; Tax Guide Topic 61 (Occupational Privilege Taxes), Topic 30 (Filing Periods), Topic 68 (Rules and Regulations); Denver Occupational Privilege Tax Return (Annual) form - all searched directly for the word \"extension\" this session, no matches found. Verified against primary source September 23, 2026.",
)

# ---------------- WILMINGTON, DELAWARE ----------------
page(
    "wilmington-de-extension.html",
    "Wilmington, Delaware Net Profits Tax Extension Guide | Extension Guide",
    "Wilmington's Net Profits Tax return honors a federal IRS extension - a copy must be filed with the city's Earned Income Tax Division by the original due date. Confirmed directly from the current WCWT-6 return instructions and the city's Earned Income Tax Regulations.",
    "Wilmington, Delaware - Local Tax Extension",
    "Net Profits Tax &nbsp;&bull;&nbsp; Federal extension honored &nbsp;&bull;&nbsp; Verified 9-23-2026",
    ["Form WCWT-6", "Copy of IRS extension required by due date", "Payment not extended"],
    "states-hub.html",
    SLOGAN + '''
<p class="lead">The City of Wilmington imposes both a Wage Tax (withheld by employers on wages earned within the city, not an annual filer-side return) and a Net Profits Tax (filed by individuals, partnerships, associations, trusts, and estates conducting business in the city), both administered by the city's Earned Income Tax Division. Only the Net Profits Tax has a filer-facing annual return with its own extension question - the Wage Tax is a withholding obligation with no comparable annual filing-extension mechanism to extend.</p>

<div class="green-box"><strong>Extension mechanism, confirmed from the current return instructions:</strong> "Later filing is accepted, providing a copy of your IRS extension is filed with the Earned Income Tax Division on or before the initial filing due date." (Form WCWT-6, City of Wilmington Net Profits Tax Return instructions)</div>

<table class="dt">
<tr><th>Item</th><th>Detail</th></tr>
<tr><td>Form</td><td>WCWT-6 (Net Profits Tax Return)</td></tr>
<tr><td>Original due date</td><td>April 15 (calendar-year filers), or 105 days after the close of a fiscal year</td></tr>
<tr><td>Extension mechanism</td><td>A copy of the taxpayer's federal IRS extension must be filed with the city's Earned Income Tax Division on or before the original due date - there is no separate city extension form</td></tr>
<tr><td>Extends time to pay?</td><td>No - the unpaid balance on a return filed under extension is subject to a one-time 5% penalty plus 1.5% monthly interest from the original due date, provided the return is filed and paid by the extension date; a return neither filed nor under extension faces a steeper 5%-per-month penalty instead</td></tr>
<tr><td>Wage Tax (withholding)</td><td>No comparable filer-side annual extension question - the Wage Tax is withheld and remitted by employers, not separately filed and extended by the individual</td></tr>
<tr><td>Authority</td><td>City of Wilmington Earned Income Tax Regulations, Section 220 (Net Profits Tax) and Section 601a (penalty and interest on returns filed under extension)</td></tr>
</table>
''' + related(
        ("states-hub.html", "All States", "Back to the states hub"),
        ("delaware-extension.html", "Delaware (State)", "Delaware's own state income tax extension rules"),
        ("philadelphia-extension.html", "Philadelphia", "Another city with a separate net-profits-style local tax"),
    ),
    "Authority: City of Wilmington Earned Income Tax Regulations, sect 220 and sect 601a. Sources: Form WCWT-6 (City of Wilmington Net Profits Tax Return) current instructions, searched directly for the word \"extension\" this session; wilmingtonde.gov/residents/earned-income-tax-and-net-profits-tax. Verified against primary source September 23, 2026.",
)

# ---------------- MARYLAND COUNTY (LOCAL) INCOME TAX ----------------
page(
    "maryland-county-local-tax-extension.html",
    "Maryland County Local Income Tax Extension Guide | Extension Guide",
    "Maryland's 23 counties and Baltimore City do not administer a separate local income tax return or a separate local extension. Local tax is computed as a line item on the same Form 502 as state tax, under the same automatic 6-month extension. Confirmed against Md. Code Ann., Tax-Gen. sect 10-823 and the Comptroller's Administrative Release No. 4.",
    "Maryland Counties - Local Income Tax Extension",
    "23 counties + Baltimore City &nbsp;&bull;&nbsp; No separate local return or extension &nbsp;&bull;&nbsp; Verified 9-23-2026",
    ["Piggyback on Form 502", "Automatic 6 months with state", "No separate local filing"],
    "states-hub.html",
    SLOGAN + '''
<p class="lead">Maryland is a "piggyback" local income tax state: each of its 23 counties and Baltimore City sets its own local income tax rate (2.25% to 3.20% of Maryland taxable income), but none of them administers its own return, its own filing deadline, or its own extension process. There is no county-level equivalent of a Form 502E.</p>

<div class="green-box"><strong>How this is confirmed:</strong> The state's own resident income tax instruction booklet computes the local tax directly on Form 502 (the same form used for state tax), based on the taxpayer's county of residence, and combines "Total Maryland tax, local tax and contributions" into a single return total. There is no separate local income tax return anywhere in the Comptroller's form set for individuals.</div>

<table class="dt">
<tr><th>Item</th><th>Detail</th></tr>
<tr><td>Local return</td><td>None - county/Baltimore City income tax is computed as a line item on the same Form 502 (residents) or Form 505 (nonresidents) as state tax</td></tr>
<tr><td>Local extension</td><td>None separate from the state extension - because there is no separate local return to extend</td></tr>
<tr><td>State extension mechanism that covers it</td><td>Automatic 6-month extension via Form 502E, or no filing required at all if a federal extension was obtained and no Maryland tax is due; up to 12 months for individuals outside the United States, for reasonable cause</td></tr>
<tr><td>Payment</td><td>Not extended - full payment of expected tax (state and local combined) is due by the original due date regardless of any extension</td></tr>
<tr><td>Authority</td><td>Md. Code Ann., Tax-Gen. &sect;10-823 (extension of time to file); Comptroller of Maryland, Administrative Release No. 4 (extension mechanics); Form 502 resident instructions (local tax computed on the same return)</td></tr>
</table>

<div class="note-box">This is structurally the same finding already documented for Indiana county tax on this site: local income tax is not a separately filed obligation, so there is nothing local to independently extend once the single combined return's extension is granted.</div>
''' + related(
        ("states-hub.html", "All States", "Back to the states hub"),
        ("maryland-extension.html", "Maryland (State)", "Maryland's own state income tax extension rules"),
        ("indiana-extension.html", "Indiana", "Same piggyback structure - county tax rides on the state return"),
    ),
    "Authority: Md. Code Ann., Tax-Gen. sect 10-823. Sources: Comptroller of Maryland Administrative Release No. 4 (Extension of Time for Filing Maryland Income Tax Returns and Estate Tax Returns), marylandcomptroller.gov; 2025 Resident Income Tax instruction booklet (Form 502, local tax computation), marylandcomptroller.gov. Verified against primary source September 23, 2026.",
)

print("local batch 1 done - 13 local jurisdictions")
