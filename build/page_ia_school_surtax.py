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
    "iowa-school-district-surtax-extension.html",
    "Iowa School District Surtax / EMS Surtax Extension Guide | Extension Guide",
    "Iowa's school district income surtax and emergency medical services (EMS) surtax are not separate returns - they are a percentage of state tax computed and paid on line 19 of the same IA 1040, covered by Iowa's own automatic 90%-payment extension. Verified against the 2025 IA 1040.",
    "Iowa School District Surtax / EMS Surtax - Extension Rules",
    "Computed on IA 1040 line 19 &nbsp;&bull;&nbsp; No separate return or extension &nbsp;&bull;&nbsp; Verified 9-23-2026",
    ["No separate return", "Rides on the IA 1040 automatic extension", "Same 90% payment test"],
    "states-hub.html",
    SLOGAN + '''
<p class="lead">Iowa allows school districts (and certain counties, for the emergency medical services surtax) to impose a surtax computed as a percentage of the taxpayer's Iowa state income tax liability. There is no separate school district or EMS surtax return, no separate form, and no separate extension mechanism - the surtax is calculated and paid as a single additional line on the taxpayer's own Iowa individual income tax return.</p>

<table class="dt">
<tr><th>Item</th><th>Detail</th></tr>
<tr><td>Where it is reported</td><td>IA 1040, line 19 ("School district surtax or EMS surtax"), computed by multiplying line 18 (Iowa tax after credits) by the applicable percentage for the taxpayer's school district or county, then added into line 20, "Total state tax and local surtax"</td></tr>
<tr><td>Separate return</td><td>None. There is no independent school district or EMS surtax filing - it is a single line item on the same IA 1040 filed for state income tax</td></tr>
<tr><td>Extension mechanism</td><td>None separate from the state return. Because the surtax is part of "Total state tax and local surtax" on the same IA 1040, it is covered by the same automatic 6-month Iowa extension: no form required, as long as at least 90% of total tax due (including the surtax) is paid by the original due date</td></tr>
<tr><td>Authority</td><td>Iowa Code &sect;257.21 (school district surtax); Iowa Code &sect;422.21 and Iowa Admin. Code r. 701-700.5 (the extension rule itself, same one that governs the state individual income tax return)</td></tr>
</table>

<div class="note-box">This is the same piggyback pattern seen elsewhere on this site (Maryland counties, Indiana county tax): a local levy computed as a percentage of the state tax and paid on the same return has no extension question of its own - whatever extends the state return extends the local levy with it.</div>
''' + related(
        ("states-hub.html", "All States", "Back to the states hub"),
        ("iowa-extension.html", "Iowa (State)", "Iowa's own automatic 90%-payment extension rule, which also covers this surtax"),
        ("maryland-county-local-tax-extension.html", "Maryland Counties", "Same piggyback pattern - local tax computed on the state return"),
        ("indiana-extension.html", "Indiana", "Same piggyback structure for county tax"),
    ),
    "Authority: Iowa Code sect 257.21; Iowa Code sect 422.21; Iowa Admin. Code r. 701-700.5. Source: 2025 IA 1040 Iowa Individual Income Tax Return (revenue.iowa.gov), line 19 instructions and computation, downloaded and extracted this session.",
)

print("wrote iowa-school-district-surtax-extension.html")
