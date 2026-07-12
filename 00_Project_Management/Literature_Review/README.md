# Knowledge Base — Papers

This folder contains term and content summaries of the 4 academic papers reviewed in the project.

---

## Papers

### 1. [Deep Learning Systems — Crude Oil and Precious Metal Price Forecasting](Deep_learning_systems_for_forecasting_the_prices_of_crude_oil_and_precious_metals.md)
- **Topic:** Forecasting WTI, Brent, Gold, and Silver prices with LSTM, GRU, TCN, CNN, and hybrid deep learning models
- **Finding:** TCN is the best model (WTI/Brent/Silver); BiGRU is the best gold model; LightGBM stood out among ML models
- **Peer-reviewed:** Yes — Financial Innovation (2024)

### 2. [Safe Havens, Machine Learning & Geopolitical Risk](Safe_Havens_Machine_Learning_and_the_Sources_of_Geopolitical_Risk_A_Forecasting_Analysis_Using_Over_a_Century_of_Data.md)
- **Topic:** Contribution of 39 country-specific geopolitical risk indices to gold volatility forecasting; Lasso and Random Forest
- **Finding:** Random Forest outperformed linear models; country-level GPR was more informative than global GPR
- **Peer-reviewed:** Yes — Computational Economics (2024)

### 3. [Stablecoins and Safe Asset Prices](Stablecoins_and_safe_asset_prices.md)
- **Topic:** Effect of dollar-backed stablecoin flows on short-term US Treasury bill yields
- **Finding:** $3.5B inflow → 3-month T-bill yield -0.71 bps; effect doubles during stress periods
- **Peer-reviewed:** BIS Working Paper (high-quality technical report, not a peer-reviewed journal)

### 4. [The Great De-Dollarization ⚠️ Not peer-reviewed](The_Great_De_Dollarization_How_Gold_Is_Reshaping_the_Global_Economy_Not_peer-reviewed.md)
- **Topic:** The 2000–2026 de-dollarization process; gold reserves; the gold-equity relationship via QQ regression
- **Finding:** USD share fell to 57.74%; gold and Treasury holdings are nearly equal; gold's safe-haven property is U-shaped and conditional
- **Peer-reviewed:** NO — Preprints.org (2026) — use only as a supporting source

---

## Common Themes

| Theme | Related Papers |
|------|-----------------|
| Gold safe haven / volatility | Papers 2, 4 |
| Deep learning / ML price forecasting | Papers 1, 2 |
| Geopolitical risk and commodities | Papers 2, 4 |
| Crypto / Stablecoins and traditional markets | Paper 3 |
| De-dollarization / Treasury market | Papers 3, 4 |

---

## Frequently Used Models (Across All Papers)

| Model | Paper |
|-------|--------|
| Random Forest | 1, 2 |
| LightGBM | 1 |
| LSTM / GRU | 1 |
| TCN | 1 |
| Lasso | 2 |
| GARCH / NPGARCH | 2 |
| Local Projections + IV | 3 |
| QQ Regression | 4 |
