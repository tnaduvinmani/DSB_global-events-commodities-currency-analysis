# Forecasting Extension — Tier 1/2/3

This folder contains an econometric/ML forecasting pipeline (see `Research_Background/RESEARCH_PROMPT.md`). Results are summarized in Appendix A of `05_Report/DSB_Report_Final.md`.

## Execution order

| Notebook | Dependency |
|---|---|
| `forecasting_pipeline.ipynb` (Tier 1) | Runs independently. Covers stationarity (ADF/KPSS), structural breaks (CUSUM/PELT), ARIMA/ARIMAX, GARCH/EGARCH, and Diebold-Mariano model comparison. |
| `forecasting_pipeline_tier2.ipynb` (Tier 2) | Runs independently. If Tier 1 has already run in the same kernel session, it reuses those variables directly; otherwise it reloads the data itself. Either way, `04_Outputs/tier1_results.json` is loaded for comparison if available. |
| `forecasting_pipeline_tier3.ipynb` (Tier 3) | Runs independently — loads its own data. Covers Johansen cointegration + VECM (Gold–Silver), Markov regime-switching (Brent), and USDG peg-deviation / logistic adoption modelling. |

**Saved results** (`04_Outputs/tier1_results.json`, `tier2_results.json`, `tier3_results.json`) are already generated — re-running the notebooks is not required to read the current report figures; the JSON files can be read directly.
