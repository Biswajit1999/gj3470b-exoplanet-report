"""Scientific checks for the committed multi-sector robustness analysis."""

from pathlib import Path
import hashlib

import numpy as np
import analyze_multisector as multi

EXPECTED_SHA256 = {
    "tess2021284114741-s0044-0000000019028197-0215-s_lc.fits": "b4dd4452c64df8e68bc5254cc079fb667dc73daee4a1d31c180b38a519ac716a",
    "tess2021310001228-s0045-0000000019028197-0216-s_lc.fits": "14cab27749f150defe200e6c74292dd13e1b797ad2cea03832ee11b70ecf1642",
    "tess2021336043614-s0046-0000000019028197-0217-s_lc.fits": "cdcd461255fac925255676e349f23eccaba08e8a448397e479d89bad919b64b2",
    "tess2023289093419-s0071-0000000019028197-0266-s_lc.fits": "73ba83b2785accd26cb52e96928ef48ff670bbe3773161ce05641072a3c809c1",
    "tess2023315124025-s0072-0000000019028197-0267-s_lc.fits": "2cc4a0a163231a7660556749ef051747aedf32f262679b82e2286e9071da2c40",
}


def test_all_committed_spoc_files_are_accounted_for():
    expected = list(multi.base.DATA_DIR.glob("tess*_lc.fits"))
    summary = multi.main()
    assert len(summary["sectors"]) + len(summary["skipped"]) == len(expected) == 5
    assert [item["sector"] for item in summary["sectors"]] == [44, 45, 46, 71, 72]
    if summary["supported"]:
        assert np.isfinite(summary["combined_depth_ppm"])
        assert summary["combined_error_ppm"] > 0
    else:
        assert np.isnan(summary["combined_depth_ppm"])
    for item in summary["sectors"]:
        assert item["result"]["n_in_transit"] >= 5
        assert item["result"]["n_out_of_transit"] >= 20
        assert item["beta"] >= 1
        assert item["robust_error_ppm"] >= item["result"]["depth_error_ppm"] - 1e-9
    assert len(summary["supported"]) == 5
    assert summary["q_dof"] == 4
    assert summary["q_p"] > 0.05


def test_spoc_source_files_match_manifested_checksums():
    for filename, expected in EXPECTED_SHA256.items():
        observed = hashlib.sha256((multi.base.DATA_DIR / filename).read_bytes()).hexdigest()
        assert observed == expected


def test_reproducible_outputs_are_nonempty():
    multi.main()
    for path in (multi.STATS_FILE, multi.TRANSITS_FIGURE,
                 multi.CONSISTENCY_FIGURE, multi.NOISE_FIGURE):
        assert Path(path).is_file()
        assert Path(path).stat().st_size > 100
