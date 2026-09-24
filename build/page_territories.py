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
    "us-territories-extension.html",
    "US Territories Tax Extension Guide - Guam, USVI, CNMI, American Samoa | Extension Guide",
    "Extension rules for the four US territories not already covered elsewhere on this site: the US Virgin Islands (confirmed - paper Form 4868 filed with the VI Bureau of Internal Revenue), the CNMI (confirmed dual-track: mirror-code income tax and three distinct local taxes), plus Guam and American Samoa, disclosed as not yet independently confirmed against a jurisdiction-specific primary source this session. Puerto Rico is covered on its own page.",
    "US Territories - Extension Rules (Guam, USVI, CNMI, American Samoa)",
    "USVI &amp; CNMI confirmed &nbsp;&bull;&nbsp; Guam &amp; American Samoa disclosed as open items &nbsp;&bull;&nbsp; Puerto Rico on its own page",
    ["USVI: paper Form 4868 with VI BIR", "CNMI: dual-track, 3 local taxes", "Guam & American Samoa not yet confirmed"],
    "states-hub.html",
    SLOGAN + '''
<p class="lead">Puerto Rico has its own page on this site. This page covers the remaining four US territories: the U.S. Virgin Islands (USVI), the Commonwealth of the Northern Mariana Islands (CNMI), Guam, and American Samoa. All four operate income tax systems that are wholly or partially based on the U.S. Internal Revenue Code ("mirror code" territories), so a bona fide resident generally files with the territory's own tax department instead of the IRS - which is also where an extension request goes.</p>

<table class="dt">
<tr><th>Territory</th><th>Extension mechanism</th><th>Status</th></tr>
<tr><td>U.S. Virgin Islands</td><td>Bona fide residents must file a <strong>paper</strong> Form 4868 with the V.I. Bureau of Internal Revenue (not the IRS) for the automatic 6-month extension. Nonresidents of the USVI with USVI-source income file separate extension requests with both the IRS and the VI BIR - the VI BIR will honor an extension timely filed with the IRS.</td><td>Confirmed - IRS Publication 570</td></tr>
<tr><td>CNMI</td><td>Dual-track system. The mirror-code Northern Mariana Territorial Income Tax (NMTIT - the CNMI's equivalent of federal income tax) follows the same Form 4868/Form 7004 extension mechanics as the federal code, filed with the CNMI Division of Revenue and Taxation instead of the IRS. Separately, CNMI's own local Wage and Salary Tax and Earnings Tax have their own extension to file "as provided by regulations prescribed by the Secretary" (4 CMC sect 1815(a)) - a mechanism exists, though the statute itself does not fix a length. CNMI's local Gross Revenue Tax has <strong>no extension to file</strong> at all (4 CMC sect 1815(b)) - only a reasonable-cause penalty waiver.</td><td>Confirmed - 4 CMC sect 1815; IRS Publication 570</td></tr>
<tr><td>Guam</td><td>Guam operates its own mirror-code income tax system; bona fide residents file with Guam's Department of Revenue and Taxation instead of the IRS. Guam's own taxpayer portal (MyGuamTax.com) references an extension resource behind a login wall.</td><td><strong>Not independently confirmed this session</strong> - the specific extension form, filing address, and length used by Guam's Department of Revenue and Taxation could not be verified against an accessible primary source. Disclosed as an open item, not assumed.</td></tr>
<tr><td>American Samoa</td><td>American Samoa has its own locally-enacted income tax code based on the Internal Revenue Code, administered by the American Samoa Government Treasury Tax Office.</td><td><strong>Not independently confirmed this session</strong> - the specific extension mechanism could not be verified against an accessible primary source. Disclosed as an open item, not assumed.</td></tr>
</table>

<div class="note-box">Guam and American Samoa are named here rather than silently omitted, consistent with this site's practice of disclosing what has not been checked rather than assuming a pattern from the other territories. A future update should target Guam's Department of Revenue and Taxation regulations and the American Samoa Code Annotated, Title 11, directly.</div>
''' + related(
        ("states-hub.html", "All States", "Back to the states hub"),
        ("puerto-rico-extension.html", "Puerto Rico", "The other major US territory, covered on its own page"),
        ("federal-4868-individual-extension.html", "Form 4868", "The federal form these territories' mirror-code systems are built around"),
    ),
    "Authority: 4 CMC sect 1815 (CNMI local tax extensions). Sources: IRS Publication 570 (2025), Tax Guide for Individuals With Income From U.S. Territories, downloaded directly from irs.gov and searched for \"extension\" this session; bir.vi.gov (VI Bureau of Internal Revenue); cnmilaw.gov (CNMI Commonwealth Code, Title 4); guamtax.com (Guam Department of Revenue and Taxation, extension detail behind a login wall, not independently verified). Verified against primary source September 23, 2026, except where disclosed as unconfirmed above.",
)

print("wrote us-territories-extension.html")
