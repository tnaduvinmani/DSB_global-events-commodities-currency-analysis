# Stablecoins and Safe Asset Prices

**Authors:** Rashad Ahmed (Andersen Institute for Finance and Economics), Iñaki Aldasoro (BIS)
**Publication:** BIS Working Papers No. 1270
**Date:** May 2025 (revised: June 2026)
**JEL:** E42, E43, G12, G23
**Peer-reviewed:** Technical working paper, published by the BIS

> ⚠️ **Note:** This is a BIS Working Paper — not a peer-reviewed journal article, but the BIS is an institution with high academic standards.

---

## Abstract

This study investigates the effect of dollar-backed stablecoin flows on short-term US Treasury bill (T-bill) yields. Using daily data from January 2021 to March 2026, a **$3.5 billion stablecoin inflow** lowers the 3-month T-bill yield by **0.71 basis points (bps) on impact**, reaching 4 bps after 10 days.

---

## Key Terms and Concepts

### The Stablecoin Ecosystem

| Term | Description |
|-------|-------|
| **Stablecoin** | A cryptocurrency whose value is pegged to a stable asset (usually USD) |
| **Dollar-backed Stablecoin** | A stablecoin whose reserves are backed by US Treasury bills and similar assets |
| **USDT (Tether)** | The largest stablecoin; ~$184 billion as of December 2025; ~63% of reserves held in T-bills |
| **USDC (Circle)** | The second-largest stablecoin; ~$80 billion; ~32% of reserves held in T-bills |
| **TUSD, BUSD, FDUSD, PYUSD, RLUSD** | Other stablecoins included in the study |
| **Minting** | Stablecoin issuance: new tokens are created when fiat currency flows in |
| **Redemption** | Stablecoin redemption: tokens are returned and fiat currency is paid back |
| **Peg** | The stability mechanism; 1 USDT = 1 USD |
| **Depeg** | A break in the peg (e.g., USDC's temporary depeg during the SVB collapse in March 2023) |
| **Primary Market Participants** | Authorized arbitrageurs who buy/sell stablecoins directly from the issuer |

### Reserve Assets

| Term | Description |
|-------|-------|
| **T-bill (Treasury Bill)** | A US Treasury short-term debt instrument with maturity up to 1 year |
| **Reverse Repo (Rev. Repo)** | An overnight lending transaction collateralized by Treasuries |
| **GENIUS Act** | US federal legislation formalizing stablecoin regulation; permits T-bills of up to 3 months as eligible reserves |
| **Circle Reserve Fund (USDXX)** | A money market fund managed by BlackRock backing USDC; has disclosed holdings since November 2022 |

### Econometric Method

| Term | Description |
|-------|-------|
| **Local Projections (LP)** | A method for estimating the impulse response function (IRF) by running a separate regression for each horizon; Jordà (2005) |
| **Instrumental Variable (IV)** | An exogenous instrument used to address endogeneity |
| **Granular Instrumental Variable (GIV)** | Gabaix & Koijen's (2024) method — idiosyncratic shocks to large units are reflected in the aggregate; while small firms' shocks average out to near zero, large firms' shocks show up in the aggregate |
| **Endogeneity** | Correlation between an explanatory variable and the error term; here, T-bill yields also affect stablecoin demand (reverse causality) |
| **HAC-robust F-statistic** | The first-stage F-statistic computed with Heteroskedastic and Autocorrelation Consistent standard errors; F=54 (very strong) |
| **Exclusion Restriction** | The requirement that the IV affects T-bill yields only through stablecoin flows, not directly |
| **Basis Point (bps)** | A unit of interest rate change; 1 bps = 0.01 percentage points |
| **IRF (Impulse Response Function)** | A chart showing how a shock's effect on the system evolves over time |
| **State-dependent Effect** | The effect varies depending on certain conditions (stress, market size) |

### Treasury Market Concepts

| Term | Description |
|-------|-------|
| **TGA (Treasury General Account)** | The US Treasury's operational account at the Fed; its balance affects T-bill supply |
| **ON-RRP (Overnight Reverse Repo)** | The Fed's overnight reverse repo facility offered to money market funds |
| **MOVE Index** | An implied-volatility index for US Treasury bonds (the bond-market equivalent of the VIX) |
| **MCI (Treasury Market Conditions Index)** | A Treasury market stress index developed by Aldasoro et al. (2025); comprises 6 components |
| **On-the-run / Off-the-run Spread** | The yield difference between the most recently issued (on-the-run) and older (off-the-run) Treasuries; a liquidity indicator |
| **OIS (Overnight Index Swap)** | An overnight interest rate swap agreement; used to gauge monetary policy expectations |
| **Preferred Habitat** | The theory that certain investor types concentrate in certain maturity segments (Vayanos & Vila 2021) |
| **Fire-sale Risk** | The risk that stablecoins are forced to rapidly sell T-bills under redemption pressure |

---

## Dataset

| Variable | Source | Period |
|----------|--------|-------|
| Stablecoin market capitalization | CoinMarketCap + DeFiLlama + Token Terminal | Jan 2021 – Mar 2026 |
| T-bill yields (1mo, 3mo, 6mo, 1y, 2y, 10y) | FRED | Jan 2021 – Mar 2026 |
| Monetary policy surprises | LSEG Datascope (intraday OIS) | — |
| MMF flows | iMoneyNet | — |
| Treasury ETF flows | ETF.com | — |
| T-bill supply (auctions) | US Treasury | — |
| TGA, ON-RRP balances | FRED | — |
| VIX, S&P 500, gold, Brent oil | FRED, Bloomberg | — |

**Stablecoin-Chain Panel:** 226 stablecoin-blockchain pairs, ~87 active pairs/day, 166,019 unit-day observations

---

## Methodology Summary

1. The 5-day change in market capitalization (Flow) was computed for 7 stablecoins
2. Granular IV (GIV): a common factor was removed from stablecoin-chain-level growth rates to isolate idiosyncratic residuals
3. GIV was tested for correlation against 12 potential confounders (max |r| = 0.10 → independent)
4. IRFs were estimated for 0–25-day horizons using local projections
5. State dependence: the analysis was repeated under TGA-rebuild and high-MCI-stress conditions

---

## Key Findings

| Finding | Value |
|-------|-------|
| $3.5B inflow → 3-month T-bill yield (on impact) | **-0.71 bps** |
| Within 10 days | **-4 bps** |
| Deepest effect (day 13) | **~-5 bps** |
| During stress periods (TGA rebuild, high MCI) | **-8 to -10 bps** (2x baseline) |
| Post-2024 effect | 2–3x stronger than pre-2024 |
| 6-month and 10-year Treasuries | Limited/negligible effect |

- The effects are **concentrated in the short-term T-bill market** — the preferred habitat segment
- The effect grows monotonically with the stablecoin sector's size (preferred habitat segmentation)
- Combined USDT and USDC T-bill holdings have surpassed those of some foreign investors and money market funds

---

## Policy Implications

- If the stablecoin sector continues to grow, it could affect monetary policy transmission
- Fire-sale risk under redemption pressure → upward yield pressure in the T-bill market
- The GENIUS Act institutionalizes stablecoin reserves, making this channel permanent

---

## Relevance to the Project

This paper is the most current and original source examined on the **intersection of crypto assets with traditional safe assets (T-bills/Treasuries)**. It is a direct reference for the project's stablecoin–safe-asset linkage, financial stability, and monetary policy dimensions.

---

## References

- Ahmed, R., Aldasaro, I., & Duley, C. (2025). Public information and stablecoin runs. *BIS Working Paper* 91(1164).
- Ahmed, R., Karolyi, S., & Pour Rostami, L. (2024). Does sovereign default risk explain cryptocurrency adoption? International evidence from mobile apps. *Available at SSRN*.
- Ahmed, R., & Rebucci, A. (2024). Dollar reserves and U.S. yields: Identifying the price impact of official flows. *Journal of International Economics*, 152, 103974.
- Aldasaro, I., Cornelli, G., Ferrari Minesso, M., Gambacorta, L., & Habib, M. M. (2025). Stablecoins, money market funds and monetary policy. *Economics Letters*, 247, 112203.
- Aldasaro, I., & Doerr, S. (2023). Who borrows from money market funds? *BIS Quarterly Review* (December).
- Aldasaro, I., & Doerr, S. (2025). Money market funds and sponsored repo: An update. *SSRN* (April).
- Aldasaro, I., Hördahl, P., Schrimpf, A., & Zhu, X. S. (2025, March). Predicting financial market stress with machine learning. *BIS Working Papers* 1250.
- Aldasaro, I., Mehrling, P., & Neilson, D. H. (2023). On par: A money view of stablecoins. *BIS Working Paper* 1146.
- Alquist, R., Kahn, R. J., & Stedman, K. D. (2025). Central banker to the world: Foreign reserve management and us money market liquidity. *Journal of International Economics*, 104203.
- Altavilla, C., Boucinha, M., Burlon, L., Adalid, R., Fortes, R., & Maruhn, F. (2026, Mar). Stablecoins and monetary policy transmission. *Working Paper Series* 3199, European Central Bank.
- Arner, D., Auer, R., & Frost, J. (2020). Stablecoins: Potential, risks and regulation. *Revista de Establidad Financiera*, Bank of Spain (Fall).
- Auer, R., Cornelli, G., Doerr, S., Frost, J., & Gambacorta, L. (2025). Crypto trading and Bitcoin prices: Evidence from a new database of retail adoption. *IMF Economic Review* forthcoming.
- Azzimonti, M., & Quadrini, V. (2025, July). Digital economy, stablecoins, and the global financial system. *Working Paper* 34066, National Bureau of Economic Research.
- Barthelemy, J., Gardin, P., & Nguyen, B. (2023, February). Stablecoins and the financing of the real economy. *Banque de France Working Paper* (908).
- Bertsch, C. (2023, May). Stablecoins: Adoption and Fragility. *Working Paper Series* 423, Sveriges Riksbank.
- Bullmann, D., Klemm, J., & Pinna, A. (2019, August). In search for stability in crypto-assets: Are stablecoins the solution? *ECB Occasional Paper* (230).
- Cerutti, E., Firat, M., Hengge, M., & Sagawa, T. (2026, March). Stablecoin Shocks. *IMF Working Paper* WP/26/044.
- Chaudhary, M., Fu, J., & Zhou, H. (2025). Anatomy of the Treasury market: Who moves yields? Technical report, mimeo.
- D'Avernas, A., Maurin, V., & Vandeweyer, Q. (2023, October). Can Stablecoins Be Stable? Working paper, SSRN.
- D'Avernas, A., & Vandeweyer, Q. (2024). Treasury bill shortages and the pricing of short-term assets. *The Journal of Finance*, 79(6), 4083–4141.
- Doerr, S., Eren, E., & Malamud, S. (2023). Money market funds and the pricing of near-money assets. *BIS Working Paper* (1096).
- Ferrari Minesso, M., & Siena, D. (2026, January). Private money and public debt: U.S. stablecoins and the global safe asset channel. *Working Paper Series* 3174, European Central Bank.
- Gabaix, X., & Koijen, R. S. J. (2024). Granular instrumental variables. *Journal of Political Economy*, 132(7), 2274–2330.
- Goel, T., Lewrick, U., & Agarwal, I. (2025). Making stablecoins stable(r): Can regulation help? *Available at SSRN*.
- Gorton, G. B., Klee, E. C., Ross, C. P., Ross, S. Y., & Vardoulakis, A. P. (2022). Leverage and stablecoin pegs. Technical report, NBER.
- Greenwood, R., Hanson, S. G., & Stein, J. C. (2015). A comparative-advantage approach to government debt maturity. *The Journal of Finance*, 70(4), 1683–1722.
- Greenwood, R., & Vayanos, D. (2014). Bond supply and excess bond returns. *Review of Financial Studies*, 27(3), 663–713.
- Griffin, J. M., & Shams, A. (2020). Is Bitcoin really untethered? *Journal of Finance*, 75(4), 1913–1964.
- He, Z., & Krishnamurthy, A. (2013). Intermediary asset pricing. *American Economic Review*, 103(2), 732–770.
- Kim, S. (2025a). How the cryptocurrency market is connected to the financial market. *working paper*.
- Kim, S. (2025b). Macro-financial impact of stablecoin's demand for treasuries. *working paper*.
- Kosse, A., Glowka, M., Mattei, I., & Rice, T. (2023). Will the real stablecoin please stand up? *BIS Papers* No 141, November.
- Krishnamurthy, A., & Vissing-Jorgensen, A. (2012). The aggregate demand for treasury debt. *Journal of Political Economy*, 120(2), 233–267.
- Liao, G., Fishman, D., & Fox-Geen, J. (2024). Risk-based capital for stable value tokens. *Available at SSRN*.
- Lyons, R. K., & Viswanath-Natraj, G. (2023). What keeps stablecoins stable? *Journal of International Money and Finance*, 131, 102777.
- Ma, Y., Yeng, Z., & Zhang, A. L. (2023, April). Stablecoin runs and the centralization of arbitrage. Working paper, SSRN.
- Mian, A., Straub, L., & Sufi, A. (2025, December). A goldilocks theory of fiscal deficits. *American Economic Review*, 115(12), 4253–91.
- Montiel Olea, J. L., & Pflueger, C. (2013). A robust test for weak instruments. *Journal of Business & Economic Statistics*, 31(3), 358–369.
- Stein, J. C., & Wallen, J. (2025). The imperfect intermediation of money-like assets. *The Journal of Finance*, 80(6), 3185–3221.
- Stock, J. H., & Yogo, M. (2005). Testing for weak instruments in linear IV regression. In D. W. K. Andrews & J. H. Stock (Eds.), *Identification and Inference for Econometric Models* (pp. 80–108). Cambridge University Press.
- Vayanos, D., & Vila, J.-L. (2021). A preferred-habitat model of the term structure of interest rates. *Review of Financial Studies*, 34(12), 5713–5761.
