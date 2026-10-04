"""Synchronize the marked website multi-sector section from generated results."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
path = ROOT / "index.html"
text = path.read_text(encoding="utf-8")
start_marker = "<!-- MULTISECTOR-UPGRADE-START -->"
end_marker = "<!-- MULTISECTOR-UPGRADE-END -->"
section = """<section class="reveal"><h2>Multi-sector robustness and noise</h2><div class="grid"><div class="card"><span>Supported combined depth</span><strong>6910.9 ± 50.3 ppm</strong></div><div class="card"><span>Supported / fitted sectors</span><strong>5 / 5</strong></div><div class="card"><span>Depth consistency</span><strong>Q = 1.97; p = 0.740</strong></div><div class="card"><span>Residual beta range</span><strong>1.12–1.51</strong></div></div><p>The archive prediction was timing-adjusted independently in Sectors 44, 45, 46, 71, and 72; all five meet ΔBIC ≥ 10. Formal depth errors were inflated by sqrt(max(reduced χ², 1)) and the residual time-averaging beta factor. The inverse-variance depth is 6910.9 ± 50.3 ppm, and the five-sector Q diagnostic finds no excess depth dispersion (Q = 1.97 for 4 dof; p = 0.740). These scaled errors address underestimated scatter and short-timescale correlation, but they are not a full Gaussian-process or global physical transit fit.</p><figure class="figure reveal"><img src="figures/gj3470b_multisector_transits.png" alt="Independent sector transit fits for GJ 3470 b"><figcaption>Five independent sector fits from committed public TESS SPOC 2-minute light curves.</figcaption></figure><figure class="figure reveal"><img src="figures/gj3470b_depth_consistency.png" alt="Sector depth consistency for GJ 3470 b"><figcaption>Depth consistency across Sectors 44, 45, 46, 71, and 72.</figcaption></figure><figure class="figure reveal"><img src="figures/gj3470b_noise_diagnostics.png" alt="Residual RMS time-averaging diagnostic for GJ 3470 b"><figcaption>Residual time-averaging curves used to inflate formal per-sector errors.</figcaption></figure></section>"""
prefix, remainder = text.split(start_marker, 1)
_, suffix = remainder.split(end_marker, 1)
path.write_text(prefix + start_marker + section + end_marker + suffix, encoding="utf-8")
text = path.read_text(encoding="utf-8")
text = text.replace(
    "The observed photometry is the public MAST file <code>tess2021284114741-s0044-0000000019028197-0215-s_lc.fits</code>, TESS Sector 44,",
    "The observed photometry comprises five public MAST SPOC 2-minute files from TESS Sectors 44, 45, 46, 71, and 72,",
).replace(
    "It is stored unmodified.",
    "They are stored unmodified.",
).replace(
    "; Sector 44 used here.</li>",
    "; Sectors 44, 45, 46, 71, and 72 used here.</li>",
)
path.write_text(text, encoding="utf-8")
