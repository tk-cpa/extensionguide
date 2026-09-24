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
    "puerto-rico-extension.html",
    "Puerto Rico Tax Extension Guide | Extension Guide",
    "Puerto Rico individual and business income tax extensions both use Formulario Modelo SC 2644, automatic upon timely filing, typically 6 months. Payment is not extended. P.R. Internal Revenue Code sect 1061.03(c), 1061.16.",
    "Puerto Rico - Tax Extension",
    "Individuals &amp; Business &nbsp;&bull;&nbsp; Automatic upon timely filing &nbsp;&bull;&nbsp; Verified 9-23-2026",
    ["Form SC 2644 (Modelo SC 2644)", "Automatic, typically 6 months", "Payment due by original date"],
    "states-hub.html",
    SLOGAN + '''
<p class="lead">Puerto Rico administers its own income tax system through the Departamento de Hacienda (Puerto Rico Treasury Department), separate from the IRS - most Puerto Rico-source income is reported on a Puerto Rico return (Planilla de Contribucion sobre Ingresos), not a federal Form 1040, and PR residents generally do not use IRS Form 4868. Both individuals and business entities (corporations, partnerships, special partnerships, and fiduciaries) request their filing extension using the same form, Modelo SC 2644 ("Solicitud de Prorroga para Rendir la Planilla de Contribucion sobre Ingresos"), filed electronically through SURI (Sistema Unificado de Rentas Internas). Hacienda's own guidance describes the extension as automatic once a timely request is filed by the original due date, and Hacienda re-confirms this each year in a Carta Circular de Rentas Internas (the most recent for the 2025 tax year is CC RI 26-01). The extension covers filing only - it does not extend the deadline to pay any balance due, and interest, surcharges, and penalties continue to accrue on unpaid tax from the original due date regardless of the extension.</p>

<div class="note-box">Puerto Rico residents who are US citizens still have certain federal filing obligations (for example, on non-Puerto-Rico-source income, or under IRC &sect;933) - this page covers the Puerto Rico Treasury (Hacienda) extension only. Federal filing questions for Puerto Rico residents involve IRC &sect;933 and related federal guidance and are outside the scope of this page.</div>

<div class="green-box"><strong>Guidance:</strong> <a href="https://hacienda.pr.gov/individuos/contribucion-sobre-ingresos/prorrogas/solicitar-prorroga" target="_blank" rel="noopener">Departamento de Hacienda - Solicitar Prorroga</a> &nbsp;&bull;&nbsp; <a href="https://hacienda.pr.gov/downloads/pdf/formularios/sc%202644.pdf" target="_blank" rel="noopener">Modelo SC 2644 (PDF)</a></div>

<table class="dt">
<tr><th>Item</th><th>Detail</th></tr>
<tr><td>Filer</td><td>Individuals and business entities (corporations, partnerships, special partnerships, fiduciaries) - same form for all</td></tr>
<tr><td>Form</td><td>Modelo SC 2644, filed electronically through SURI</td></tr>
<tr><td>Automatic?</td><td>Yes, upon a timely request filed on or before the original due date</td></tr>
<tr><td>Length</td><td>Typically 6 months from the original due date, per Hacienda's published extension guidance</td></tr>
<tr><td>Payment condition</td><td>Not extended - any balance due must still be paid by the original due date to avoid interest, surcharges, and penalties</td></tr>
<tr><td>Authority</td><td>P.R. Internal Revenue Code of 2011, as amended, 13 L.P.R.A. &sect;&sect; 1061.03(c), 1061.06(c), 1061.07(c), 1061.09(b)(4), 1061.10(b)(2), 1061.16; re-confirmed annually by Carta Circular de Rentas Internas (CC RI 26-01 for tax year 2025)</td></tr>
</table>

''' + related(
        ("new-york-city-extension.html", "New York City", "Another jurisdiction with its own local extension mechanism"),
        ("federal-4868-individual-extension.html", "Federal Form 4868", "The federal individual extension - generally not used by PR-source filers"),
        ("master-extension-matrix.html", "Master Matrix", "Every jurisdiction, one sortable table"),
    ),
    "Authority: P.R. Internal Revenue Code of 2011, as amended, 13 L.P.R.A. &sect;&sect; 1061.03(c), 1061.06(c), 1061.07(c), 1061.09(b)(4), 1061.10(b)(2), 1061.16 (automatic extension provision, cited in Departamento de Hacienda Carta Circular de Rentas Internas Num. 26-01, radicacion del Formulario Modelo SC 2644 del ano contributivo 2025). Extension length and payment-not-extended rule confirmed against Departamento de Hacienda guidance at hacienda.pr.gov. Verified against primary source September 23, 2026."
)

print("wrote puerto-rico-extension.html")
