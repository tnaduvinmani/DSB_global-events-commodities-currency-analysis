# The Great De-Dollarization: How Gold Is Reshaping the Global Economy

**Author:** Kowser Ali Jan (Annamalai University, Tamil Nadu, India)
**Platform:** Preprints.org
**Publication Date:** March 17, 2026
**DOI:** 10.20944/preprints202603.1197v1
**JEL:** F31, F33, E58, G11

> ⚠️ **IMPORTANT WARNING:** This paper is **NOT peer-reviewed**. Findings may be less reliable. Cite with caution.

---

## Abstract

Using data from the 2000–2026 period, this study quantitatively examines the de-dollarization process, showing that the dollar's share of global reserves has fallen to 57.74%, while official gold reserves have approached the level of Treasury securities holdings. Using **Quantile-on-Quantile (QQ) regression** and **Causality-in-Quantiles (CiQ)** tests, the gold-equity relationship is shown to be U-shaped and regime-dependent.

---

## Key Terms and Concepts

### De-Dollarization and the Global Monetary System

| Term | Description |
|-------|-------|
| **De-Dollarization** | The process of moving away from the USD in international transactions and reserves |
| **Reserve Currency** | An international currency held by central banks as foreign reserves |
| **COFER** | The IMF's Currency Composition of Official Foreign Exchange Reserves database; tracks central bank reserve composition |
| **Petrodollar** | The system, established after 1973, in which oil transactions are conducted in dollars; the US-Saudi agreement ended in 2024 |
| **BRICS** | Brazil, Russia, India, China, South Africa, and new members; developing alternative payment systems |
| **Bretton Woods** | The 1944–1973 fixed exchange rate system; established the dollar as the global reserve currency |
| **Hegemonic Stability Theory** | Kindleberger's (1973) thesis that a stable international monetary system cannot be sustained without a strong hegemon |
| **Currency Network Externality** | The increase in a currency's usage value as more people use it (Krugman 1984) |
| **Monetary Pluralism** | A system in which multiple reserve currencies coexist |
| **Weaponization of Finance** | The use of financial sanctions as a geopolitical tool (e.g., the freezing of Russian central bank assets) |

### The Role of Gold

| Term | Description |
|-------|-------|
| **Official Gold Holdings** | Official gold reserves held by central banks |
| **Safe Haven** | An asset that preserves value during periods of market stress — for gold, this is **regime-dependent and conditional** |
| **Hedge** | An asset that is on average negatively correlated with a portfolio |
| **Diversifier** | An asset that is positively but weakly correlated with a portfolio |
| **Flight-to-Quality** | Investors shifting from risky assets to safe havens during crises |
| **Central Bank Gold Agreement (CBGA)** | A 1999–2019 agreement limiting European central banks' gold sales; Western CBs were net sellers during this period |
| **Selling Era (2002–2008)** | The world sold an average of 590.9 tonnes of gold annually (coordinated selling by European CBs) |
| **Buying Era (2009–present)** | The world bought an average of 404.3 tonnes of gold annually (mainly emerging markets) |
| **LBMA** | London Bullion Market Association; the reference for setting the gold spot price |

### Econometric Methods Used

#### 1. Quantile-on-Quantile (QQ) Regression — Sim & Zhou (2015)

| Term | Description |
|-------|-------|
| **Quantile Regression** | Estimates different percentiles (quantiles) of the conditional distribution of the dependent variable; focuses on the distribution rather than the mean |
| **QQ Regression** | Computes the effect conditional on the independent variable also being at a specific percentile of its own distribution |
| **β(τ,θ)** | The QQ coefficient: the contribution of gold's τ-th percentile to the equity market's θ-th percentile |
| **τ (tau)** | The percentile of the gold return (the target variable's quantile) |
| **θ (theta)** | The percentile of the S&P 500 return (the independent variable's quantile) |
| **U-shaped Pattern** | Gold shows its strongest performance at the extremes: both during equity crashes (θ≈0.05) and during exceptional bull markets (θ≈0.90–0.95) |

#### 2. Causality-in-Quantiles (CiQ) Test — Nishiyama et al. (2011), Jeong et al. (2012)

| Term | Description |
|-------|-------|
| **CiQ Test** | Tests Granger causality across different percentiles of the conditional distribution; captures relationships missed by linear causality tests |
| **T_n(τ) statistic** | The CiQ test statistic; a positive value → the restricted model has higher forecast error → causality is present |
| **p_asy** | The asymptotic p-value |
| **p_boot** | The bootstrap p-value (B=499 resamples) |
| **Causality finding** | At τ=0.90 (p=0.046) and τ=0.95 (p=0.013) → equities predict gold only when gold is performing **exceptionally well** |

#### 3. Cross-Quantilogram

| Term | Description |
|-------|-------|
| **Cross-Quantilogram** | Measures lagged dependence between two variables across different tail regions of the distribution |

---

### Key Data Sources

| Variable | Source | Period |
|----------|--------|-------|
| USD Reserve Share | IMF COFER | 1999Q1–2025Q1 |
| Global Gold Reserves | IMF; World Gold Council | 2000M1–2025M9 |
| Gold Prices | LBMA (London PM fix) | 2000–2025 |
| Equity Indices | Bloomberg; Refinitiv | 2000–2024 |
| Central Bank Gold Purchases | World Gold Council | 2000Q1–2025Q3 |
| Sanctions Data | Global Sanctions Database | 2000–2025 |
| US Treasury Holdings | US Treasury TIC | 2000M1–2025M6 |
| Geopolitical Risk Index | Economic Policy Uncertainty | 2000–2025 |
| DXY (Dollar Index) | Bloomberg | 2001–2026 |

---

## Key Findings

### 1. De-Dollarization Is Real But Slow
- USD share of global reserves: 71.01% (1999) → **57.74% (2025)** → a 13.27-point decline
- The pace of decline is roughly 0.5 points per year; at this pace, 50% could be reached within two decades
- But this is not an active flight from the dollar — it is **passive diversification** (2025 World Gold Council survey: only 32% of central banks cited de-dollarization as a motive for gold purchases)

### 2. Gold Reserves Have Reached a Historic Threshold
| | Value |
|-|-------|
| Official Gold Reserves (2025) | **$3.909 trillion** |
| Foreign Governments' US Treasury Holdings | **$3.920 trillion** |
| → For the first time in history, the two assets are nearly equal | |

### 3. Gold Buying Has Become Centralized — the West Sold, the East Bought
**Major Buyers (2002–2025):**
| Country | Net Change |
|---------|-----------|
| Russia | +1,894.2 tonnes |
| China | +1,806.8 tonnes |
| Turkey | ~705 tonnes |
| India | +522.6 tonnes |
| Poland | +447.3 tonnes |

**Major Sellers (2002–2025):**
| Country | Net Change |
|---------|-----------|
| Euro Area (total) | -1,691.3 tonnes |
| Switzerland | -1,158.5 tonnes |
| France | -587.6 tonnes |

### 4. QQ Regression — The Gold-Equity Relationship Is U-Shaped
- **θ=0.75 (strong bull market):** β values are positive → gold rises together with equities (risk-on)
- **θ=0.05–0.10 (equity crash) + high τ:** β is negative → **genuine safe-haven behavior**
- **Middle θ values:** β ≈ 0 → gold moves independently, neither a hedge nor a safe haven
- **Conclusion:** Gold's safe-haven property is **conditional and regime-dependent**; not universal

### 5. CiQ — Causality Only in the Tail
- Equity returns predict gold only at τ=0.90 and τ=0.95 (when gold is unusually high)
- Equity declines do **not** systematically predict gold increases → the simple safe-haven narrative does not hold

### 6. DXY-Gold Relationship (2001–2026)
| Period | DXY Change | Gold Change |
|--------|-----------|-------------|
| 2001–2008 USD Decline | -34% | +252% |
| 2008 GFC Dollar Spike | +18% | -21% |
| 2009–2011 QE Period | -15% | +100% |
| 2014–2016 USD Super Rally | +28% | -27% |
| 2025 Tariff Shock | -9% | +55% |

---

## Theoretical Framework

| School | Argument |
|--------|----------|
| **Structural Transformation School** | De-dollarization is passive; a natural reflection of emerging markets' growing economic weight |
| **Geopolitical Fragmentation School** | Sanctions triggered active de-dollarization; the Russia case is a pivot point |
| **Skeptical School** | Gold accumulation is not systematic; for most CBs it is an ordinary portfolio management decision |

---

## Relevance to the Project

This paper provides contextual framing for the project's **de-dollarization, gold's role in the monetary system, and safe-haven analysis** dimensions. However, since it is not peer-reviewed, it should be cited with caution and is more appropriately used as a supporting source. Its QQ regression methodology offers a distinctive analytical tool for the project.

---

## References

1. Arslanalp, S., Eichengreen, B., & Simpson-Bell, C. (2025). The structural transformation of global reserves: Economic weight and portfolio composition. *Journal of International Economics*, 142(3), 103-128.

2. Baur, D. G., & McDermott, T. K. (2010). Is gold a safe haven? International evidence. *Journal of Banking & Finance*, 34(8), 1886-1898.

3. Beckmann, J., Berger, T., & Czudaj, R. (2019). Gold price dynamics and the role of uncertainty. *Quantitative Finance*, 19(4), 663-682.

4. Bouri, E., Gupta, R., & Roubaud, D. (2021). Quantile connectedness between gold and stock markets: Evidence from the QQ regression approach. *Resources Policy*, 72, 102-118.

5. Carrillo-Pina, M., & Sharov, K. (2025). Geopolitical fragmentation and the weaponization of finance: Implications for reserve currency status. *International Finance*, 28(1), 45-72.

6. Eichengreen, B. (2011). *Exorbitant privilege: The rise and fall of the dollar and the future of the international monetary system*. Oxford University Press.

7. International Monetary Fund. (2026). *Global financial stability report: Geopolitical risk and safe-haven dynamics*. International Monetary Fund.

8. Jeong, K., Härdle, W. K., & Song, S. (2012). A consistent nonparametric test for causality in quantile. *Econometric Theory*, 28(4), 861-887.

9. Kindleberger, C. P. (1973). *The world in depression, 1929-1939*. University of California Press.

10. Koenker, R., & Bassett, G. (1978). Regression quantiles. *Econometrica*, 46(1), 33-50.

11. Krugman, P. (1984). The international role of the dollar: Theory and prospect. In J. F. O. Bilson & R. C. Marston (Eds.), *Exchange rate theory and practice* (pp. 261-278). University of Chicago Press.

12. Nishiyama, Y., Hitomi, K., Kawasaki, Y., & Jeong, K. (2011). A consistent nonparametric test for nonlinear causality specification in time series regression. *Journal of Econometrics*, 165(1), 112-127.

13. Sachs, J., & Fares, M. (2026). Financial sanctions and currency collapse: The Iranian case. *Journal of International Money and Finance*, 118, 102-145.

14. Sim, N., & Zhou, H. (2015). Oil prices, US stock return, and the dependence between their quantiles. *Journal of Banking & Finance*, 55, 1-8.

15. Silverman, B. W. (1986). *Density estimation for statistics and data analysis*. Chapman and Hall.

16. Weiss, M. A. (2025). De-dollarization or diversification? Evidence from country-level reserve data. *Review of International Political Economy*, 32(2), 267-295.

17. World Gold Council. (2025). *Central bank gold survey 2025: Reserve management trends and motivations*. World Gold Council.

18. World Gold Council. (2026). *Gold demand trends: Q1 2026*. World Gold Council.

19. Xinhua News Agency. (2026, March 15). From Venezuela to Iran: The law of the jungle in international relations. Xinhua News Agency.

20. Zhang, Y., Ma, F., Liu, J., & Zhou, W. (2025). Quantile-on-quantile analysis of gold-stock market relationships in G7 and E7 economies. *Journal of International Financial Markets, Institutions and Money*, 84, 101-124.
