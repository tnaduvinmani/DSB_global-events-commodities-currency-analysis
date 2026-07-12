# Safe Havens, Machine Learning, and the Sources of Geopolitical Risk: A Forecasting Analysis Using Over a Century of Data

**Authors:** Rangan Gupta (U. of Pretoria), Sayar Karmakar (U. of Florida), Christian Pierdzioch (Helmut Schmidt U.)
**Journal:** Computational Economics (2024) 64:487–513
**DOI:** https://doi.org/10.1007/s10614-023-10452-w
**Peer-reviewed:** Yes

---

## Abstract

Using monthly data spanning 1915–2021, this study investigates the contribution of geopolitical risk (GPR) to forecasting gold volatility. Using 39 country-specific GPR indices together with machine learning (Random Forest, Lasso), the paper shows that out-of-sample forecast accuracy can be improved.

---

## Key Terms and Concepts

### The Safe Haven Concept

| Concept | Description |
|--------|----------|
| **Safe Haven** | An asset that retains or increases its value during market crashes (e.g., gold, US Treasury bonds) |
| **Hedge** | An asset that is on average negatively or zero-correlated with another asset |
| **Diversifier** | An asset that is positively but weakly correlated with a portfolio |

### Geopolitical Risk Indices (Caldara & Iacoviello 2022)

| Index | Description |
|--------|----------|
| **GPR (Geopolitical Risk)** | The overall geopolitical risk index — constructed via automated text mining of newspaper articles |
| **GPT (Geopolitical Threats)** | Sub-index measuring threats (Categories 1–5: War Threats, Peace Treaties, Military Buildups, Nuclear Threats, Terrorist Threats) |
| **GPA (Geopolitical Acts)** | Sub-index measuring realized events (Categories 6–8: War Outbreak, War Escalation, Terrorist Acts) |
| **GPC (Country-level GPR)** | Monthly country-specific geopolitical risk indices for 39 countries |

**The 39 countries covered:** North America (Canada, Mexico, US), South America (Argentina, Brazil, Chile, Colombia, Peru, Venezuela), Europe — North-East (Denmark, Finland, Norway, Russia, Sweden, Ukraine, UK), Europe — South-West (Belgium, France, Germany, Italy, Netherlands, Portugal, Spain, Switzerland, Turkey), Middle East & Africa (Israel, Saudi Arabia, South Africa, Turkey), Asia & Oceania (Australia, China, Hong Kong, Japan, South Korea, Philippines, Taiwan, Indonesia, Malaysia, India, Thailand)

---

### Models and Methods

#### Forecasting Models

| Model | Description |
|-------|----------|
| **AR (Autoregressive)** | Simple lagged return/volatility benchmark model |
| **OLS** | Ordinary Least Squares — linear regression |
| **Lasso** | Least Absolute Shrinkage and Selection Operator — performs variable selection via an L1 penalty; shrinks the large set of GPR predictors |
| **Random Forest (RF)** | An ensemble of 1,000 decision trees; captures nonlinear relationships and predictor interactions |

#### Volatility Models

| Model | Description |
|-------|----------|
| **GARCH(1,1)** | Generalized Autoregressive Conditional Heteroskedasticity — models conditional variance |
| **TVPGARCH** | Time-Varying Parameter GARCH — parameters change over time (kernel-based) |
| **NPGARCH** | Non-Parametric GARCH — relaxes the normality assumption; the preferred model, yielding the lowest MSE |

#### Evaluation

| Term | Description |
|------|----------|
| **Out-of-sample R²** | R² = 1 − (ΣFE²_rival / ΣFE²_benchmark); a positive value means the rival model outperforms the benchmark |
| **Diebold-Mariano Test** | Tests whether the forecast errors of two models are statistically different |
| **Recursive Window** | Re-estimates the model with each new observation (expanding window) |
| **Rolling Window** | Re-estimates the model by sliding a fixed-length window forward |
| **Partial Dependence Function** | In Random Forest, shows the marginal effect of one variable on the prediction while holding the others constant |

---

### Key Statistics/Econometrics Terms

| Term | Description |
|------|----------|
| **Conditional Volatility** | Volatility computed conditional on past information; measured via GARCH-family models |
| **Heteroskedasticity** | Variance that changes over time; the core motivation for GARCH models |
| **Bootstrapping** | A method for measuring statistical uncertainty by resampling the data |
| **Lasso Shrinkage (λ)** | Lasso's penalty parameter; larger values shrink more coefficients to zero |
| **Predictor Selection** | Lasso's variable selection: predictors with zero coefficients drop out of the model |
| **Nonlinearity** | The relationship between GPR and gold volatility is not linear; Random Forest captures this |
| **Interaction Effects** | Countries' geopolitical risks affect one another (spillover effects); RF models this |

---

## Dataset

| Variable | Source | Period |
|----------|--------|-------|
| Gold price (log-return) | Macrotrends | Feb 1915 – Sep 2021 |
| Geopolitical Risk Index | Caldara & Iacoviello (2022) | from 1900 |
| Country GPR indices | Caldara & Iacoviello (2022) | 39 countries |
| Oil (WTI) price | Global Financial Data | from 1900 |
| Silver price | Macrotrends | from 1915 |

---

## Methodology Summary

1. Gold log-returns were computed; conditional volatility was measured with GARCH, TVPGARCH, and NPGARCH
2. GPR (global) and GPC (39 countries) were used as predictors
3. **Lasso:** shrank the large set of country GPRs to select the most informative ones
4. **Random Forest:** forecasting with 1,000 trees, 10-fold cross-validation, and bootstrapping
5. Out-of-sample forecasts were generated using recursive and rolling windows (h=1,3,6,12 months ahead)
6. Statistical significance was checked with the Diebold-Mariano test
7. Extended with additional analysis for oil and silver

---

## Key Findings

- **Random Forest** outperformed Lasso and all linear models, particularly in the recursive forecasting window
- **Country-level GPR** was more informative than global GPR
- The gold volatility–GPR relationship is **nonlinear and varies by country** (US: U-shaped, China: monotonically increasing)
- **NPGARCH** provided better volatility measurement than GARCH and TVPGARCH
- **For silver,** Random Forest added little value to volatility forecasting
- **For oil,** Random Forest performed well in the rolling window

---

## Relevance to the Project

This paper is the only academic source examined that explains **how geopolitical risk affects gold and other commodity prices**. It is critical for the project's safe-haven analysis and risk-management dimensions, and it demonstrates how ML techniques such as Random Forest and Lasso are applied to financial time-series analysis.

---

## References

- Agyei-Ampomah, S., Gounopoulos, D., & Mazouz, K. (2014). Does gold offer a better protection against sovereign debt crises than other metals? *Journal of Banking and Finance*, 40(C), 507–521.
- Asai, M., Gupta, R., & McAleer, M. (2020). Forecasting volatility and co-volatility of crude oil and gold futures: Effects of leverage, jumps, spillovers, and geopolitical risks. *International Journal of Forecasting*, 36(3), 933–948.
- Aye, G. C., Gupta, R., Hammoudeh, S., & Kim, W.-J. (2015). Forecasting the price of gold using dynamic model averaging. *International Review of Financial Analysis*, 41(C), 257–266.
- Balcilar, M., Bonato, M., Demirer, R., & Gupta, R. (2017). The effect of investor sentiment on gold market return dynamics: Evidence from a nonparametric causality-in-quantiles approach. *Resources Policy*, 51(C), 77–84.
- Balcilar, M., Bonato, M., Demirer, R., & Gupta, R. (2018). Geopolitical risks and stock market dynamics of the BRICS. *Economic Systems*, 42(2), 295–306.
- Balcilar, M., Demirer, R., Gupta, R., & Wohar, M. E. (2020). The effect of global and regional stock market shocks on safe haven assets. *Structural Change and Economic Dynamics*, 54(C), 297–308.
- Balcilar, M., Gupta, R., & Pierdzioch, C. (2016). Does uncertainty move the gold price? New evidence from a nonparametric causality-in-quantiles test. *Resources Policy*, 49(C), 74–80.
- Batten, J. A., Ciner, C., & Lucey, B. M. (2010). The macroeconomic determinants of volatility in precious metals markets. *Resources Policy*, 35(2), 65–71.
- Baur, D. G. (2012). Asymmetric volatility in the gold market. *Journal of Alternative Investments*, 14(4), 26–38.
- Baur, D. G., & Lucey, B. M. (2010). Is gold a hedge or a safe haven? An analysis of stocks, bonds and gold. *Financial Review*, 45(2), 217–229.
- Baur, D. G., & McDermott, T. K. (2010). Is gold a safe haven? International evidence. *Journal of Banking and Finance*, 34(8), 1886–1898.
- Baur, D. G., & Smales, L. A. (2020). Hedging geopolitical risk with precious metals. *Journal of Banking and Finance*, 117(C), 105823.
- Beckmann, J., Berger, T., & Czudaj, R. (2015). Does gold act as a hedge or safe haven for stocks? A smooth transition approach. *Economic Modelling*, 48(C), 16–24.
- Beckmann, J., Berger, T., & Czudaj, R. (2019). Gold Price dynamics and the role of uncertainty. *Economic Modelling*, 75(C), 105–116.
- Bonato, M., Demirer, R., Gupta, R., & Pierdzioch, C. (2018). Gold futures returns and realized moments: A forecasting experiment using a quantile-boosting approach. *Resources Policy*, 57(C), 196–212.
- Boubaker, H., Cunado, J., Gil-Alana, L. A., & Gupta, R. (2020). Global crises and gold as a safe haven: Evidence from over seven and a half centuries of data. *Physica A*, 540(C), 123093.
- Bouoiyour, J., Selmi, R., Hammoudeh, S., & Wohar, M. E. (2019). What are the categories of geopolitical risks that could drive oil prices higher? Acts or threats? *Energy Economics*, 84(C), 104523.
- Bouoiyour, J., Selmi, R., & Wohar, M. E. (2018). Measuring the response of gold prices to uncertainty: An analysis beyond the mean. *Economic Modelling*, 75(C), 105–116.
- Bouri, E., Çepni, O., Gabauer, D., & Gupta, R. (2021). Return connectedness across asset classes around the COVID-19 outbreak? *International Review of Financial Analysis*, 73(C), 101646.
- Bouri, E., Demirer, R., Gupta, R., & Marfatia, H. A. (2019). Geopolitical risks and movements in Islamic bond and equity markets: A note. *Defence and Peace Economics*, 30(3), 367–379.
- Breiman, L. (2001). Random forests. *Machine Learning*, 45, 5–32.
- Caldara, D., & Iacoviello, M. (2022). Measuring geopolitical risk. *American Economic Review*, 112(4), 1194–1225.
- Çepni, O., Dul, W., Gupta, R., & Wohar, M. E. (2021). The dynamics of U.S. REITs returns to uncertainty shocks: A proxy SVAR approach. *Research in International Business and Finance*, 58(C), 101433.
- Chen, J., & Politis, D. N. (2019). Optimal multi-step-ahead prediction of arch/garch models and novas transformation. *Econometrics*, 7(3), 34.
- Cheng, C. H. J., & Chiu, C.-W.J. (2018). How important are global geopolitical risks to emerging countries? *International Economics*, 136(C), 305–325.
- Clance, M. W., Gupta, R., & Wohar, M. E. (2019). Geopolitical risks and recessions in a panel of advanced economies: Evidence from over a century of data. *Applied Economics Letters*, 26(16), 1317–1321.
- Diebold, F. X., & Mariano, R. S. (1995). Comparing predictive accuracy. *Journal of Business and Economic Statistics*, 13(3), 253–263.
- Ding, Z., & Zhang, X. (2021). The impact of geopolitical risk on systemic risk spillover in commodity market: An EMD-based network topology approach. *Complexity*, 2021, 2226944.
- Dichtl, H. (2020). Forecasting excess returns of the gold market: Can we learn from stock market predictions? *Journal of Commodity Markets*, 19(C), 100106.
- Friedman, J., Hastie, T., & Tibshirani, R. (2010). Regularization paths for generalized linear models via coordinate descent. *Journal of Statistical Software*, 33(1), 1–22.
- Gkillas, G., Gupta, R., & Pierdzioch, C. (2020). Forecasting realized gold volatility: Is there a role of geopolitical risks? *Finance Research Letters*, 35(C), 101280.
- Gozgor, G., Lau, C. K. M., Sheng, X., & Yarovaya, L. (2019). The role of uncertainty measures on the returns of gold. *Economics Letters*, 185(C), 108680.
- Gupta, R., Majumdar, A., Nel, J., & Subramaniam, S. (2021). Geopolitical risks and the high-frequency movements of the US term structure of interest rates. *Annals of Financial Economics*, 16(3), 2150012.
- Gupta, R., Majumdar, A., Pierdzioch, C., & Wohar, M. E. (2017). Do terror attacks predict gold returns? Evidence from a quantile-predictive-regression approach. *Quarterly Review of Economics and Finance*, 65(C), 276–284.
- Gürgün, G., & Ünalmis, I. (2014). Is gold a safe haven against equity market investment in emerging and developing countries? *Finance Research Letters*, 11(4), 341–348.
- Harvey, D., Leybourne, S., & Newbold, P. (1997). Testing the equality of prediction mean squared errors. *International Journal of Forecasting*, 13(2), 281–291.
- Hassani, H., Silva, E. S., Gupta, R., & Segnon, M. K. (2015). Forecasting the price of gold. *Applied Economics*, 47(39), 4141–4152.
- Hastie, T., Tibshirani, R., & Friedman, J. (2009). *The elements of statistical learning: Data mining, inference, and prediction* (Vol. 2). New York: Springer.
- Hollstein, F., Prokopczuk, J., Tharann, B., & Wese Simen, C. (2021). Predictability in commodity markets: Evidence from more than a century. *Journal of Commodity Markets*, 24(C), 100171.
- Huang, J., Li, Y., Suleman, M. T., & Zhang, H. (2023). Effects of geopolitical risks on gold market return dynamics: Evidence from a nonparametric causality-in-quantiles approach. *Defence and Peace Economics*, 34(3), 308–322.
- Huynh, T. L. D. (2020). The effect of uncertainty on the precious metals market: New insights from transfer entropy and neural network VAR. *Resources Policy*, 66(C), 101623.
- Ishwaran, H., & Kogalur, U. B. (2021). Fast unified random forests for survival, regression, and classification (RF-SRC). *R Package version*, 2(12), 1.
- Karmakar, S., Richter, S., & Wu, W. B. (2021). Simultaneous inference for time-varying models. *Journal of Econometrics*. https://doi.org/10.1016/j.jeconom.2021.03.002
- Li, B., Chang, C.-P., Chu, Y., & Sui, B. (2020). Oil prices and geopolitical risks: What implications are offered via multi-domain investigations? *Energy and Environment*, 31(3), 492–516.
- Li, Y., Huang, J., & Chen, J. (2021). Dynamic spillovers of geopolitical risks and gold prices: New evidence from 18 emerging economies. *Resources Policy*, 70(C), 101938.
- Li, X., Guo, Q., Liang, C., & Umar, M. (2023). Forecasting gold volatility with geopolitical risk indices. *Research in International Business and Finance*, 64(C), 101857.
- Liu, J., Ma, F., Tang, Y., & Zhang, Y. (2019). Geopolitical risk and oil volatility: A new insight. *Energy Economics*, 84(C), 104548.
- Low, R. K. Y., Yao, Y., & Faff, R. (2016). Diamonds vs. precious metals: What shines brightest in your investment portfolio? *International Review of Financial Analysis*, 43(C), 1–14.
- Luo, J., Demirer, R., Gupta, R., & Ji, Q. (2022). Forecasting oil and gold volatilities with sentiment indicators under structural breaks. *Energy Economics*, 105(C), 105751.
- Mei, D., Ma, F., Liao, Y., & Wang, L. (2020). Geopolitical risk uncertainty and oil future volatility: Evidence from MIDAS models. *Energy Economics*, 86(C), 104624.
- Nguyen, D. B. B., Prokopczuk, M., & Wese Simen, C. (2019). The risk premium of gold. *Journal of International Money Finance*, 94(C), 140–159.
- Plakandaras, V., Gupta, R., & Wong, W.-K. (2019). Point and density forecasts of oil returns: The role of geopolitical risks. *Resources Policy*, 62(C), 580–587.
- Pierdzioch, C., & Gupta, R. (2020a). Uncertainty and forecasts of U.S. recessions. *Studies in Nonlinear Dynamics and Econometrics*, 24(4), 20180083.
- Pierdzioch, C., & Risse, M. (2020b). Forecasting precious metal returns with multivariate random forests. *Empirical Economics*, 58(3), 1167–1184.
- Pierdzioch, C., Risse, M., & Rohloff, S. (2014a). On the efficiency of the gold market: Results of a real-time forecasting approach. *International Review of Financial Analysis*, 32(C), 95–108.
- Pierdzioch, C., Risse, M., & Rohloff, S. (2014b). The international business cycle and gold-price fluctuations. *Quarterly Review of Economics and Finance*, 54(2), 292–305.
- Pierdzioch, C., Risse, M., & Rohloff, S. (2015a). A real-time quantile-regression approach to forecasting gold returns under asymmetric loss. *Resources Policy*, 45(C), 299–306.
- Pierdzioch, C., Risse, M., & Rohloff, S. (2015b). Forecasting gold-price fluctuations: A real-time boosting approach. *Applied Economics Letters*, 22(1), 46–50.
- Pierdzioch, C., Risse, M., & Rohloff, S. (2016a). A quantile-boosting approach to forecasting gold returns. *North American Journal of Economics and Finance*, 35(C), 38–55.
- Pierdzioch, C., Risse, M., & Rohloff, S. (2016b). A boosting approach to forecasting the volatility of gold-price fluctuations under flexible loss. *Resources Policy*, 47(C), 95–107.
- Pifter, M., & Podstawski, M. (2017). Identifying uncertainty shocks using the price of gold. *Economic Journal*, 128(616), 3266–3284.
- Politis, D. N. (2015). The model-free prediction principle. In: *Model-free prediction and regression* (pp. 13–30). Berlin/Heidelberg: Springer.
- Qin, Y., Hong, K., Chen, J., & Zhang, Z. (2020). Asymmetric effects of geopolitical risks on energy returns and volatility under different market conditions. *Energy Economics*, 90(C), 104851.
- R Core Team. (2023). R: A language and environment for statistical computing. R Foundation for Statistical Computing, Vienna, Austria.
- Rapach, D. E., & Zhou, G. (2013). Forecasting stock returns. In G. Elliott & A. Timmermann (Eds.), *Handbook of Economic Forecasting* (Vol. 2A, pp. 328–383). Amsterdam: Elsevier.
- Reboredo, J. C. (2013a). Is gold a safe haven or a hedge for the US dollar? Implications for risk management. *Journal of Banking and Finance*, 37(8), 2665–2676.
- Reboredo, J. C. (2013b). Is gold a hedge or safe haven against oil price movements? *Resources Policy*, 38(2), 130–137.
- Salisu, A. A., Cunado, J., & Gupta, R. (2022a). Geopolitical risks and historical exchange rate volatility of the BRICS. *International Review of Economics and Finance*, 77(C), 179–190.
- Salisu, A. A., Gupta, R., Bouri, E., & Ji, Q. (2020). The role of global economic conditions in forecasting gold market volatility: Evidence from a GARCH-MIDAS approach. *Research in International Business and Finance*, 54(C), 101308.
- Salisu, A. A., Gupta, R., Karmakar, S., & Das, S. (2021b). Forecasting output growth of advanced economies over eight centuries: The role of gold market volatility as a proxy of global uncertainty. *Resources Policy*, 75(C), 102527.
- Salisu, A. A., Lukman, L., & Tchankam, J. P. (2022b). Historical geopolitical risk and the behaviour of stock returns in advanced economies. *European Journal of Finance*, 28(9), 889–906.
- Salisu, A. A., Pierdzioch, C., & Gupta, R. (2021a). Geopolitical risk and forecastability of tail risk in the oil market: Evidence from over a century of monthly data. *Energy*, 235(C), 121333.
- Sharma, S. S. (2016). Can consumer price index predict gold price returns? *Economic Modelling*, 55(C), 269–278.
- Smales, L. A. (2021). Geopolitical risk and volatility spillovers in oil and stock markets. *Quarterly Review of Economics and Finance*, 80(C), 358–366.
- Tibshirani, R. (1996). Regression shrinkage and selection via the lasso. *Journal of the Royal Statistical Society, Series B*, 58(1), 267–288.
- Tibshirani, J., Athey, S., Sverdrup, E., & Wager, S. (2021). grf: Generalized Random Forests. R package version 2.0.2.
- Tiwari, A. K., Aye, G. C., Gupta, R., & Gkillas, K. (2020). Gold-oil dependence dynamics and the role of geopolitical risks: Evidence from a Markov-switching time-varying copula model. *Energy Economics*, 88(C), 104748.
- Tiwari, A. K., Boachie, M. K., Suleman, M. T., & Gupta, R. (2021). Structure dependence between oil and agricultural commodities returns: The role of geopolitical risks. *Energy*, 219(C), 119584.
- Wu, K., & Karmakar, S. (2021). Model-free time-aggregated predictions for econometric datasets. *Forecasting*, 3(4), 920–933.
- Wu, K., & Karmakar, S. (2023). A model-free approach to do long-term volatility forecasting and its variants. *Financial Innovation*, 9, 59.
- Yang, M., Zhang, Q., Yi, A., & Peng, P. (2021). Geopolitical risk and stock market volatility in emerging economies: Evidence from GARCH-MIDAS model. *Discrete Dynamics in Nature and Society*, 2021, 1159358.
