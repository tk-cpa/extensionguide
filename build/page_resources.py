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
    "resources.html",
    "Extension Resources - Official and Trusted Third-Party Links | Extension Guide",
    "A curated collection of official IRS resources and reputable third-party services for filing tax extensions - IRS Free File, Direct Pay, EFTPS, the Taxpayer Advocate Service, and IRS-authorized e-file providers including TaxExtension.com and FileLater.com.",
    "Extension Resources",
    "Official IRS resources first &nbsp;&bull;&nbsp; Reputable third-party services second &nbsp;&bull;&nbsp; No endorsements, no affiliate relationships",
    ["Official sources", "IRS-authorized e-file providers", "Neutral, no endorsements"],
    "resources.html",
    SLOGAN + '''
<p class="lead">This page collects official government resources and reputable third-party services related to filing a tax extension, in one place. Official sources always come first - use a commercial service only if a direct government channel does not fit your situation. This site carries no affiliate, referral, or paid-placement relationship with any provider listed below; a listing here is not an endorsement or recommendation of any specific position or service over another, and this guide does not receive compensation for any link on this page. Every link is checked for a live, working connection before publication.</p>

<h2>Official federal resources</h2>
<table class="dt">
<tr><th>Resource</th><th>What it's for</th></tr>
<tr><td><a href="https://www.irs.gov/filing/get-an-extension-to-file-your-tax-return" target="_blank" rel="noopener"><strong>IRS - Get an Extension to File Your Tax Return</strong></a></td><td>The IRS's own overview page for individual filing extensions (Form 4868) and related guidance</td></tr>
<tr><td><a href="https://www.irs.gov/filing/free-file-do-your-federal-taxes-for-free" target="_blank" rel="noopener"><strong>IRS Free File</strong></a></td><td>File Form 4868 electronically at no cost, regardless of income - a direct IRS program, not a third-party product</td></tr>
<tr><td><a href="https://www.irs.gov/payments/direct-pay" target="_blank" rel="noopener"><strong>IRS Direct Pay</strong></a></td><td>Pay directly from a bank account and designate the payment as an extension payment - often satisfies the extension requirement without filing Form 4868 separately</td></tr>
<tr><td><a href="https://www.eftps.gov/eftps/" target="_blank" rel="noopener"><strong>EFTPS (Electronic Federal Tax Payment System)</strong></a></td><td>The Treasury's free system for scheduling federal tax payments, including extension payments, in advance</td></tr>
<tr><td><a href="https://www.taxpayeradvocate.irs.gov/" target="_blank" rel="noopener"><strong>Taxpayer Advocate Service</strong></a></td><td>Independent organization within the IRS that helps taxpayers resolve problems, including extension and penalty disputes, that haven't been resolved through normal IRS channels</td></tr>
</table>

<h2>IRS-authorized commercial e-file providers</h2>
<p>These are paid, third-party services authorized by the IRS to transmit extension filings electronically. They are useful when a filer wants a guided, paid experience, confirmation tracking, or state-extension guidance bundled together - but they charge a fee for a filing that is also available for free directly through the IRS above. Confirm current pricing and terms directly on each provider's site before using it; neither is required to complete a valid extension.</p>
<table class="dt">
<tr><th>Provider</th><th>What it offers</th></tr>
<tr><td><a href="https://www.taxextension.com/" target="_blank" rel="noopener"><strong>TaxExtension.com</strong></a></td><td>IRS-authorized e-file provider for individual (Form 4868) and business (Form 7004) extensions, plus state extension guidance across all 50 states</td></tr>
<tr><td><a href="https://www.filelater.com/" target="_blank" rel="noopener"><strong>FileLater.com</strong></a></td><td>IRS-authorized e-file provider for individual and business extensions, with real-time IRS confirmation and state-by-state extension instructions</td></tr>
</table>

<h2>This site's own tools</h2>
<p>The fastest way to find a specific jurisdiction's rule is usually one of this site's own pages rather than a search engine.</p>
<div class="pin-grid">
  <a href="map.html" class="pin-chip">Interactive Map</a>
  <a href="states-hub.html" class="pin-chip">All States, DC &amp; Puerto Rico</a>
  <a href="federal-hub.html" class="pin-chip">Federal Extensions</a>
  <a href="master-extension-matrix.html" class="pin-chip">Master Matrix</a>
  <a href="efile-and-third-party-services.html" class="pin-chip">E-File Options in Depth</a>
  <a href="extension-penalties-and-interest.html" class="pin-chip">Penalties &amp; Interest</a>
</div>

<div class="note-box">A listing on this page is informational, not a recommendation of one provider over another, and is not compensated by any listed provider. Always verify a third-party service is currently operating, uses IRS-authorized e-file transmission, and discloses its fees clearly before paying for anything that is also available free directly from the IRS.</div>

''' + related(
        ("efile-and-third-party-services.html", "E-File and Third-Party Services", "A closer look at Free File, Direct Pay, and commercial e-file options"),
        ("federal-4868-individual-extension.html", "Form 4868", "The individual federal extension itself"),
        ("faq.html", "FAQ", "Common extension questions answered"),
    ),
    "Sources: irs.gov/filing/get-an-extension-to-file-your-tax-return; irs.gov/filing/free-file-do-your-federal-taxes-for-free; irs.gov/payments/direct-pay; eftps.gov; taxpayeradvocate.irs.gov; taxextension.com; filelater.com. Each resource link checked for a live, working connection and, for the two commercial providers, confirmed as a stated IRS-authorized e-file provider on the provider's own site."
)

print("wrote resources.html")
