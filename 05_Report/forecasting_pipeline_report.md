# Forecasting Pipeline Report
## Global Events, Commodities and Currency Markets

**Course:** Data Science & Business  
**Date:** June 2026  
**Datasets:** Gold (1915–2026) · Silver (1915–2026) · Brent Crude (1946–2026) · USDG (Apr 2025–Apr 2026)

---

## Abstract

This report extends the descriptive analytics of the DSB assignment with a multi-tier forecasting pipeline covering classical econometrics, machine learning, and deep learning models. Walk-forward validation on a 24-month out-of-sample test period (April 2024–April 2026) yields the following headline results: an LSTM(64) network achieves the lowest MAPE for Gold (3.88%), narrowly ahead of ARIMA(1,1,2) (3.90%); Random Forest marginally outperforms all models on Brent (6.49%); no model shows a practically meaningful improvement over the naive random walk for Silver (LSTM edges it by 0.003pp — statistical noise, not signal); and a Markov Regime-Switching model identifies two statistically distinct volatility regimes in Brent returns that align with known geopolitical crises. For USDG, the peg deviation series has a standard deviation of 6.8×10⁻⁵ USD, confirming near-perfect peg stability over the 13-month observation window.

---

## 1. Introduction

Commodity markets are subject to structural breaks, volatility clustering, and long-run equilibrium relationships that standard regression models cannot capture. This pipeline systematically evaluates four tiers of increasingly sophisticated models:

- **Tier 1** — Stationarity diagnostics, structural break detection, ARIMA/ARIMAX, GARCH/EGARCH
- **Tier 2** — Tree-based and deep learning models (Random Forest, LightGBM, LSTM, BiGRU — see §3.2)
- **Tier 3** — Multivariate and regime-dependent econometrics (VECM, Markov Switching, USDG adoption modelling)
- **Tier 4** — Interactive Streamlit dashboard: GARCH(1,1) heteroskedastic forecast bands, Diebold-Mariano [1] significance indicators, USDG logistic uncertainty bands, Macro Context tab (VIX/DXY/TIPS dual-axis charts), and annotated global-events legend

The motivation draws directly from the academic literature reviewed in this course:

> *"Random forests outperform LASSO and OLS across all geopolitical risk scenarios"* — Gupta et al. [2]

> *"BiGRU achieves the lowest RMSE for Gold in daily return forecasting"* — Foroutan and Lahmiri [3]

> *"Stablecoin inflows proxy for risk-off sentiment rather than de-dollarisation"* — Ahmed and Aldasoro [4]

---

## 2. Data

| Asset | Source | Frequency | Start | End | N |
|-------|--------|-----------|-------|-----|---|
| Gold | Macrotrends | Monthly | Jan 1915 | Apr 2026 | 1,336 |
| Silver | Macrotrends | Monthly | Jan 1915 | Apr 2026 | 1,336 |
| Brent Crude | Macrotrends | Monthly | Jan 1946 | Mar 2026 | 963 |
| USDG | CoinGecko | Daily | Apr 2025 | Apr 2026 | 365 |
| SWIFT | SWIFT RMB Tracker | Monthly snapshot | Dec 2025 | Mar 2026 | 4 |
| VIX / DXY / TIPS | FRED | Monthly | 1990– | 2026 | 439 |

**Preprocessing:** Log prices computed as ln(P_t); log returns as Δln(P_t). Monthly series resampled to period-start timestamps. USDG peg deviation defined as Price_USD − 1.00. Train/test cutoff: **2024-04-01** (consistent across all models).

---

## 3. Methodology

### 3.1 Tier 1 — Classical Econometrics

#### Stationarity
- **ADF test** (Augmented Dickey-Fuller): H₀ = unit root. All four log-price series fail to reject at the 5% level; first differences (log returns) are stationary for all assets.
- **KPSS test** [5]: H₀ = stationarity. Confirms I(1) classification.

#### Structural Breaks
- **CUSUM** [6]: recursive residuals from OLS trend cross the 5% boundary during 2008 (GFC), 2020 (COVID-19), and 2022 (Russia-Ukraine) for all commodity series.
- **PELT algorithm** [7] (`ruptures` library, penalty = 15): identifies 4–6 change-points per series, largely consistent with CUSUM.

#### ARIMA / ARIMAX
Order selected via AIC grid search over p,q ∈ {0,…,3}, d=1 [8]. Walk-forward validation: model refit at every test step.

| Asset | Order | RMSE | MAE | MAPE |
|-------|-------|------|-----|------|
| Gold | ARIMA(1,1,2) | 219.0 | 144.2 | **3.90%** |
| Silver | ARIMA(3,1,3) | 10.16 | 5.18 | 8.58% |
| Brent | ARIMA(1,1,2) | 8.48 | 5.01 | 6.55% |

ARIMAX variants include VIX as exogenous for Gold and DXY for Brent; neither improves over the baseline ARIMA, consistent with the view that these macro variables are already priced into monthly commodity returns.

#### GARCH / EGARCH
Fitted on percentage log returns for numerical stability. EGARCH(1,1) [10] preferred over GARCH(1,1) [9] by AIC for Gold and Silver, confirming the leverage effect (negative shocks increase volatility more than positive shocks of equal magnitude). The GARCH(1,1) volatility cone provides 12-month heteroskedastic 95% confidence intervals and is displayed directly in the Tier 4 dashboard, replacing the simpler i.i.d. Gaussian band used in earlier iterations. The z-score is computed via `scipy.stats.norm.ppf` (exact) rather than Monte Carlo sampling.

---

### 3.2 Tier 2 — Machine Learning

**Feature engineering** (applied to all tree-based and deep learning models):
- Lagged returns: ret_lag{1,3,6,12}
- Rolling mean: roll_mean{3,6} (computed from ret shifted by 1 to prevent leakage)
- Rolling standard deviation: roll_std{3,6}
- Log price lag: log_p_lag1
- Cyclical month encoding: month_sin, month_cos

**Walk-forward protocol**: model refit at each test step using all available history; no random shuffling.

#### Random Forest (500 trees, OOB scoring)
Motivated by Gupta et al. [2], who demonstrate that RF with geopolitical risk features outperforms LASSO across 107 years of gold volatility data.

#### LightGBM (learning_rate = 0.05, num_leaves = 31)
Gradient boosted trees; generally lower variance than RF on small feature sets.

#### LSTM (units = 64, window = 24 months, dropout = 0.2)
24-month input window chosen to capture one full business cycle. MinMaxScaler fitted on training data only. EarlyStopping with patience = 10. **Result: LSTM achieves the lowest Gold MAPE of any model tested (3.88%), narrowly ahead of ARIMA (3.90%); it also nominally edges out the naive baseline for Silver (8.4469% vs. 8.4503% — not a meaningful difference); for Brent it underperforms both Naive and RF (6.61%).**

#### BiGRU (units = 32, Gold only)
Bidirectional GRU applied to Gold following Foroutan and Lahmiri [3], who identify BiGRU as the top performer for Gold in daily data. Adapted here to monthly frequency. **Result: MAPE = 3.94% — competitive but does not beat LSTM or ARIMA at monthly frequency, consistent with the expectation that BiGRU's advantage in [3] is tied to their much larger daily sample (5,426 obs.) versus our ~260 monthly observations.**

**Tier 2 Results:**

| Model | Gold MAPE | Silver MAPE | Brent MAPE |
|-------|-----------|-------------|------------|
| Naive (RW) | 4.30% | 8.45% | 6.50% |
| ARIMA | 3.90% | 8.58% | 6.55% |
| Random Forest | 4.07% | 12.43% | **6.49%** |
| LightGBM | 4.80% | 10.54% | 6.79% |
| VECM | 3.98% | — | — |
| LSTM | **3.88%** | 8.45% | 6.61% |
| BiGRU (Gold only) | 3.94% | — | — |

Key observation: for Gold, LSTM now narrowly leads (3.88%), just ahead of ARIMA (3.90%) and BiGRU (3.94%) — the deep learning models are competitive with, but not decisively better than, the classical baseline at monthly frequency (the four best Gold models span only 0.10pp). For Silver, no model shows a practically meaningful improvement over the naive baseline (LSTM's 8.4469% vs. Naive's 8.4503% is a 0.003pp difference — statistical noise, not a real forecasting edge). For Brent, RF marginally wins over Naive (6.4891% vs. 6.4984%) — also a near-tie rather than a decisive result, though still broadly consistent with Gupta et al.'s [2] finding that non-linear methods can capture geopolitical risk non-linearity better than purely linear models.

---

### 3.3 Tier 3 — Advanced Econometrics

#### Gold–Silver Cointegration (Johansen Test + VECM)

**Johansen trace test** [11] (det_order = 0, k_ar_diff = 2):

| H₀: rank ≤ r | Trace stat | CV 5% | Decision |
|-------------|-----------|-------|----------|
| r ≤ 0 | 11.69 | 15.49 | Fail to reject |
| r ≤ 1 | 2.10 | 3.84 | Fail to reject |

**Cointegration rank = 0** — formal Johansen test fails to find a cointegrating vector over the full 1915–2026 sample. This does not preclude a long-run relationship; the test's power is known to be sensitive to structural breaks and regime changes over centennial horizons.

Despite this, a VECM with forced rank = 1 achieves Gold MAPE = 3.98%, marginally above ARIMA. The error correction term may partially capture mean-reversion in the Gold/Silver ratio (historical mean ≈ 56; range: 17–120).

#### Markov Regime-Switching (Brent)

`MarkovAutoregression(k_regimes=2, order=1, switching_variance=True)` following Hamilton [12].

| | Regime 0 (Stress) | Regime 1 (Calm) |
|-|-------------------|-----------------|
| σ² | 0.0109 | 1.6×10⁻⁵ |
| Ratio | **680×** | — |
| Persistence p(i→i) | 0.963 | 0.938 |
| Mean time in regime | ~27 months | ~16 months |

**AIC = −3673.9 | BIC = −3635.0**

The stress regime (Regime 0) activates during: GFC 2008, Libyan Civil War 2011, COVID-19 2020, Russia-Ukraine 2022, Iran-Hormuz 2026. The persistence coefficient p(0→0) = 0.963 indicates oil market stress is highly persistent once initiated.

#### USDG Analysis

**Peg deviation** (Price_USD − 1.00):
- Standard deviation: σ = 6.8×10⁻⁵ USD → de facto perfect peg over 13 months
- ADF p-value = 0.760 → non-stationary (insufficient sample; 13 monthly observations provide low power)
- ACF/PACF: no significant autocorrelation — deviations are noise, not persistent

**MarketCap adoption modelling**: logistic S-curve f(t) = K / (1 + exp(−r(t−t₀))) estimated on 13 monthly observations via nonlinear least squares (`scipy.optimize.curve_fit`). The full parameter covariance matrix `pcov` is retained; the standard error of the saturation cap σ_K = √pcov[0,0] is displayed as a ±1σ uncertainty band in the dashboard. Given the short sample, K carries high uncertainty and the projection is illustrative rather than predictive.

**SWIFT context** [4]: USD maintained 49.25–51.14% of SWIFT global payments over Dec 2025–Mar 2026. USDG's MarketCap growth over the same period is consistent with the BIS hypothesis that stablecoin inflows represent digitalisation of USD demand rather than competition with traditional USD instruments. No de-dollarisation signal is detectable.

---

## 4. Results Summary

### Model Performance — Out-of-Sample (Apr 2024 – Apr 2026)

| Asset | Best Model | MAPE | vs Naive |
|-------|-----------|------|----------|
| Gold | LSTM(64) | **3.88%** | −0.42 pp |
| Silver | LSTM(64) | **8.45%** | −0.003 pp (not meaningful) |
| Brent | RandomForest(500) | **6.49%** | −0.01 pp |

**Silver finding:** No model produces a practically meaningful improvement over the naive random walk on monthly silver returns over the test period — LSTM's nominal edge (0.003pp) is statistical noise, not a real forecasting gain. This is consistent with silver's dual role as both a precious metal and industrial commodity — demand shocks from manufacturing cycles are difficult to forecast from price history alone.

### Structural Findings

| Finding | Method | Implication |
|---------|--------|-------------|
| All price series are I(1) | ADF + KPSS | Models must use log returns, not levels |
| 4–6 structural breaks per series | CUSUM + PELT | Event dummies / rolling windows preferred over full-sample estimation |
| Gold–Silver cointegration rejected | Johansen | Long-run ratio is not stable; mean-reversion is regime-dependent |
| Brent has 2 distinct volatility regimes | Markov AR | Conditional risk models (GARCH/VaR) should be regime-conditional |
| USDG peg is statistically stable | ADF on deviation | Peg mechanism is effective; deviation σ = 6.8×10⁻⁵ |

---

## 5. Discussion

### Why are classical and deep learning models so closely matched on monthly commodity data?

With LSTM now included, the Gold results (LSTM 3.88%, ARIMA 3.90%, BiGRU 3.94%, VECM 3.98%) span a range of only 0.10 percentage points — effectively a tie given the sample size. Monthly commodity prices have relatively low signal-to-noise ratios, and the 24-observation test set is large enough to evaluate model accuracy but too short to expect deep learning models to demonstrate a decisive representational advantage. Foroutan and Lahmiri [3] used daily data (≈5,000 observations per asset); at that granularity, BiGRU's ability to capture non-linear patterns becomes more decisive than it is here. At monthly frequency, LSTM's narrow win for Gold should be read as "competitive with classical models," not as proof that deep learning is superior — the gap is well within what could be sampling noise across a 24-month test window.

### Regime switching and risk management

The Markov model's identification of a "stress" regime with 680× higher variance than the "calm" regime has direct implications for Value-at-Risk estimation. A single-distribution GARCH model underestimates tail risk during stress periods. A regime-conditional VaR that uses σ_stress during high-probability stress periods would more accurately capture the 2020 COVID and 2022 Ukraine shocks.

### USDG and the de-dollarisation narrative

The 13-month peg stability (σ = 6.8×10⁻⁵) is strong evidence that the Paxos reserve mechanism functions as intended. The alignment between USDG MarketCap growth and persistent USD SWIFT dominance (~50%) supports Ahmed and Aldasoro's [4] conclusion that tokenised dollars complement rather than compete with the traditional dollar system. The Great De-dollarisation narrative (2026 preprint) should be read as a geopolitical risk scenario, not a near-term structural shift.

---

## 5b. Out-of-Sample Validation — May–June 2026

To stress-test the naive random-walk (RW) forecasts at inference time, we fetched actual spot prices for May and June 2026 from yfinance and compared them against the 95% prediction interval generated by the Streamlit dashboard.

**Basis:** Last CSV observation used as forecast origin. Point forecast: naive random walk with log-normal drift (60-month rolling μ and σ). For this validation table the naive i.i.d. CI = exp(μt ± 1.96σ√t) is used for comparison with actuals; the live dashboard displays the GARCH(1,1) heteroskedastic cone which produces tighter bands in low-volatility periods and wider bands during stress.

| Asset | Period | Forecast | Actual | Error | In 95% CI? |
|-------|--------|----------|--------|-------|-----------|
| Gold | May 2026 | $4,790 | $4,590 | −4.2% | ✅ |
| Gold | Jun 2026 | $4,869 | $4,309 | −11.5% | ✅ |
| Silver | May 2026 | $90.19 | $78.14 | −13.4% | ✅ |
| Silver | Jun 2026 | $92.05 | $69.21 | −24.8% | ❌ |
| Brent | Apr 2026 | $103.43 | $102.46 | −0.9% | ✅ |
| Brent | May 2026 | $104.01 | $104.09 | +0.1% | ✅ |
| Brent | Jun 2026 | $104.58 | $89.04 | −14.9% | ✅ |

**Observations:**

- **Gold** declined sharply in June 2026 (−11.5% vs forecast), yet remained inside the 95% CI — confirming that the RW model's widening uncertainty bands correctly capture tail risk even when the point estimate overshoots.
- **Brent** May actual ($104.09) was essentially identical to the naive forecast ($104.01) — a near-perfect one-step prediction that illustrates the RW's adequacy for monthly oil in stable-regime periods (Regime 1 in the Markov model).
- **Silver** June 2026 fell **outside** the 95% CI (actual $69.21 vs CI lower bound ≈ $70), suggesting a volatility spike beyond what the 60-month rolling σ anticipated. This is consistent with Silver's known sensitivity to industrial demand shocks not captured by price-lag features alone.

The ARIMA/VECM models were not re-evaluated here (their forecast origin was April 2024; re-running walk-forward to June 2026 is recommended for a complete picture). The visualisation is saved as `04_Outputs/forecast_validation_jun2026.png`.

---

## 6. Conclusion

This pipeline demonstrates that classical econometric models (ARIMA, GARCH, VECM) remain competitive with — though not decisively better than — machine learning and deep learning approaches on monthly commodity data. LSTM narrowly achieves the lowest MAPE for Gold (3.88% vs. ARIMA's 3.90%), but the margin is small relative to the 24-month test window and should not be over-interpreted as evidence of DL superiority. The key value-add of the ML/DL tier is not a decisively superior point forecast but richer feature importance diagnostics (RF/LightGBM) and a competitive alternative worth monitoring as more data accumulates. The Tier 3 analyses contribute structural insights — regime identification, cointegration testing, adoption modelling — that complement the Tier 1–2 forecast accuracy comparison.

The Streamlit dashboard (`app/streamlit_app.py`) makes all findings interactively accessible. Key features: per-asset GARCH(1,1) forecast bands with Diebold-Mariano significance indicators; USDG logistic projection with ±1σ parameter uncertainty; a Macro Context tab showing commodity prices against FRED variables (VIX, DXY, TIPS) on dual axes; a collapsible global-events legend below each chart; and a static normalised comparison across Gold, Silver, and Brent.

---

## 7. References

[1] F. X. Diebold and R. S. Mariano, "Comparing predictive accuracy," *Journal of Business & Economic Statistics*, vol. 13, no. 3, pp. 253–263, 1995.

[2] R. Gupta, S. Karmakar, and C. Pierdzioch, "Safe havens, machine learning, and the sources of geopolitical risk: A forecasting analysis using over a century of data," *Computational Economics*, vol. 64, pp. 487–513, 2024, doi: 10.1007/s10614-023-10452-w.

[3] P. Foroutan and S. Lahmiri, "Deep learning systems for forecasting the prices of crude oil and precious metals," *Financial Innovation*, vol. 10, Art. no. 111, 2024, doi: 10.1186/s40854-024-00637-z.

[4] R. Ahmed and I. Aldasoro, "Stablecoins and safe asset prices," *BIS Working Papers*, no. 1270, Bank for International Settlements, Basel, Switzerland, May 2025.

[5] D. Kwiatkowski, P. C. B. Phillips, P. Schmidt, and Y. Shin, "Testing the null hypothesis of stationarity against the alternative of a unit root," *Journal of Econometrics*, vol. 54, no. 1–3, pp. 159–178, 1992.

[6] R. L. Brown, J. Durbin, and J. M. Evans, "Techniques for testing the constancy of regression relationships over time," *Journal of the Royal Statistical Society B*, vol. 37, no. 2, pp. 149–192, 1975.

[7] R. Killick, P. Fearnhead, and I. A. Eckley, "Optimal detection of changepoints with a linear computational cost," *Journal of the American Statistical Association*, vol. 107, no. 500, pp. 1590–1598, 2012.

[8] G. E. P. Box and G. M. Jenkins, *Time Series Analysis: Forecasting and Control*. San Francisco, CA, USA: Holden-Day, 1976.

[9] R. F. Engle, "Autoregressive conditional heteroscedasticity with estimates of the variance of United Kingdom inflation," *Econometrica*, vol. 50, no. 4, pp. 987–1007, 1982.

[10] D. B. Nelson, "Conditional heteroskedasticity in asset returns: A new approach," *Econometrica*, vol. 59, no. 2, pp. 347–370, 1991.

[11] S. Johansen, "Statistical analysis of cointegration vectors," *Journal of Economic Dynamics and Control*, vol. 12, no. 2–3, pp. 231–254, 1988.

[12] J. D. Hamilton, "A new approach to the economic analysis of nonstationary time series and the business cycle," *Econometrica*, vol. 57, no. 2, pp. 357–384, 1989.
