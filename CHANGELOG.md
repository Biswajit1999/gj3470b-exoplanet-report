# Changelog

## [1.0.0] - 2026-10-04

- Expanded the homogeneous target-specific SPOC 2-minute inventory from one
  TESS sector to all five products returned by the MAST target-cone query:
  Sectors 44, 45, 46, 71, and 72.
- Preserved all five FITS products unmodified and added fail-closed SHA-256
  regression checks for every source file.
- Recomputed timing-adjusted transit fits, residual time-averaging inflation,
  inverse-variance depth, and cross-sector consistency from 33 supported events.
- Published the five-sector depth result (`6910.9 ± 50.3 ppm`) and its
  consistency diagnostic (`Q=1.97`, 4 dof, `p=0.740`) without treating a
  non-significant Q test as proof of invariant atmosphere or geometry.
- Retained the atmospheric section as a source-graded literature audit rather
  than presenting it as an independent JWST/HST/Spitzer retrieval.
- Pinned CI actions to immutable commits; Python 3.11 and 3.12 regenerate all
  products and pass the seven-test real-data suite.

## Pre-1.0 history

- Added the timing-adjusted limb-darkened Sector 44 diagnostic, correlated-noise
  scaling, atmosphere-evidence audit, accessibility checks, and explicitly
  labelled artistic concept.
