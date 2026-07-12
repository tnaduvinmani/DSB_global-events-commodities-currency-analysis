Global Events, Commodities and Currency Markets

Applied Data Analytics and Market Research — Assignment Report

Course: Data Science & Business (DSB)

Team: Tabassum (Team Lead) · Hadi · Sagar · Parvesh · Sameep · Rimsha

Date: June 2026

Datasets: Brent Oil · Gold (100 years) · Silver (100 years) · SWIFT Global Currency Tracker · USDG


# Executive Summary

Purpose

This report presents an applied data analytics and market research study of historical datasets covering Brent Crude Oil, Gold, Silver, and SWIFT global currency payment indicators. The study identifies how major commodity prices and currency market shares have evolved over time and interprets these changes in the context of global economic and geopolitical developments.

Key Insights

Gold reached its highest recorded monthly average of $5,277.89/oz in February 2026 (an intraday all-time high of $5,595/oz was reached on 29 January 2026) — trading at approximately 12× its long-run historical average, driven by geopolitical uncertainty, central bank accumulation, and sustained safe-haven demand.

Silver surged to $113.95/oz in January 2026, reflecting both precious metal demand and growing industrial use in solar energy and EV batteries.

Brent Crude Oil reached $102.86/barrel in March 2026, exhibiting the highest monthly volatility (9.05% std. dev.) of the three commodities, driven primarily by the 2026 Iran–Hormuz crisis.

The USD retains dominance at 51.14% of global payment share (April 2026), while the Chinese Yuan (CNY) has risen to 5th place at 3.10%, surpassing CAD in recent months.

Recommendations

Hedge oil exposure through forward contracts due to its high price volatility and sensitivity to geopolitical events.

Invest in gold as a portfolio risk buffer, given its proven safe-haven characteristics during crises [8].

Monitor and diversify currency exposure as the CNY gains ground and alternative payment systems develop.


# Table of Contents

1. Introduction

1.1 Background

1.2 Objective

1.3 Scope

2. Data and Methodology

2.1 Data Source

2.2 Data Preprocessing

2.3 Methodology

2.4 Assumption

3.  Analysis and Insights

3.1  Data Preparation and Understanding (Q1–Q5)

3.2  Descriptive Analytics (Q6–Q12)

3.3  Trend and Visual Analytics (Q13–Q18)

3.4  Currency Tracker Analytics (Q19–Q24)

3.5  Simple Comparison Questions (Q25–Q30)

3.6  Bonus Analytics (B1–B6)

4.  Part II — Market Research Findings

4.1 Event Identification

4.2 Linking Events to Commodity Data

4.3 Linking Events to Currency Data

4.4 Business Interpretation and Recommendations

5.  Final Recommendations for Management

6.  Conclusion

7. Appendix

8. References


# 1. Introduction


## 1.1 Background

Commodity markets — oil, gold, and silver — are key indicators of global economic stability and investor sentiment. Brent Oil reflects global energy supply and demand conditions, while gold and silver are widely used as investment assets influenced by inflation, uncertainty, and financial crises. Global currency markets play a critical role in international trade, where changes in currency dominance reflect shifts in global economic power.


## 1.2 Objective

The objective of this study is to develop evidence-based insights by combining quantitative data analysis with qualitative market interpretation, understanding not only how commodity and currency markets have changed over time but also why these changes may have occurred in response to global events.


## 1.3 Scope

The assignment covers two main components: (1) data analytics — data cleaning, descriptive statistics, trend analysis, and visualisation; and (2) market research — connecting observed data patterns with real-world global events such as energy supply shocks, geopolitical tensions, sanctions, and changes in international trade systems. An extended econometric/ML forecasting pipeline (Appendix A) was also developed to validate the descriptive trends with formal time-series models.


# 2. Data and Methodology


## 2.1 Data Sources

| Dataset | Time Period | Frequency | Rows | Variables |
|---|---|---|---|---|
| Brent Oil | 1946–2026 | Monthly | 963 | Date, Value |
| Gold | 1915–2026 | Monthly | 1,336 | Date, Value |
| Silver | 1915–2026 | Monthly | 1,336 | Date, Value |
| SWIFT | Jan–Apr 2026 | Monthly reports | 330 | 10 columns |
| USDG | Apr 2025–Apr 2026 | Daily | 366 | 4 columns |
| FRED (VIX, DXY, TIPS) | 1990–2026 (VIX/DXY); 2003–2026 (TIPS) | Monthly (resampled from daily) | - | vix, dxy, tips |

Table 2.1  Overview of datasets used in this study. FRED series were used only for the extended forecasting pipeline (Appendix A) and the companion interactive dashboard — not part of the core Part I/Part II analysis.


## 2.2 Data Preprocessing

All commodity datasets were complete with no missing values. The USDG dataset contained one duplicate date, removed via drop_duplicates(). The SWIFT dataset's 388 structural missing values are by design. All date columns are in MM/DD/YYYY format (monthly data, day always = 1) and were converted to datetime using `pd.to_datetime(..., format="%m/%d/%Y")`, with Year, Month, and MonthName columns extracted for analysis.

| Dataset | Missing Values | Issues | Action Taken |
|---|---|---|---|
| Brent Oil | 0 | None | No action |
| Gold | 0 | None | No action |
| Silver | 0 | None | No action |
| USDG | 0 | 1 duplicate date | Removed duplicate |
| SWIFT | 388 | Structural missing values | No action required |

Table 2.2  Data Quality Summary.


## 2.3 Methodology

Analytical techniques include trend analysis, descriptive statistics (mean, std. deviation, min/max), moving averages (MA-12, MA-60), linear regression forecasting, and correlation analysis. Visual tools include time series line charts, bar charts, scatter plots, a correlation heatmap, and a summary dashboard.


## 2.4 Assumptions

Stable exchange rates during the analysis period.

Reported commodity production/export and price data is accurate.

SWIFT data reflects genuine payment behaviour without systematic reporting bias.


# 3. Analysis and Insights


## 3.1 Data Preparation and Understanding (Q1–Q5)

Q1 — Start and End Dates of Each Dataset

| Dataset | Start | End | Coverage |
|---|---|---|---|
| Brent Oil | 1 January 1946 | 1 March 2026 | ~80 years, monthly |
| Gold | 1 January 1915 | 1 April 2026 | ~111 years, monthly |
| Silver | 1 January 1915 | 1 April 2026 | ~111 years, monthly |
| SWIFT | 1 January 2026 | 1 April 2026 | 4 report months |
| USDG | 29 April 2025 | 28 April 2026 | 366 days, daily |

Table 3.1  Dataset date ranges. Gold and Silver provide the longest historical coverage at over 111 years.

Q2 — Dataset Row and Column Counts

| Dataset | Rows | Columns |
|---|---|---|
| Brent Oil | 963 | 2 (Date, Value) |
| Gold | 1,336 | 2 (Date, Value) |
| Silver | 1,336 | 2 (Date, Value) |
| SWIFT | 330 | 10 (report_month, data_month, metric, category, currency_or_economy, value, unit, rmb_global_rank, notes...) |
| USDG | 366 | 4 (Date, Price_USD, MarketCap_USD, Volume_USD) |

Table 3.2  Dataset row and column counts.

Q3 — Data Quality Check

| Dataset | Missing Values | Duplicate Dates | Negative/Zero Prices |
|---|---|---|---|
| Brent Oil | 0 | 0 | 0 |
| Gold | 0 | 0 | 0 |
| Silver | 0 | 0 | 0 |
| USDG | 0 | 1 ⚠️ | 0 |
| SWIFT | 388 ⚠️ | 0 | (no price column) |

Table 3.3  Data quality summary. SWIFT's 388 missing values are structural by design.

Q4 — Date Formatting (Sample Output)

| Row | Date (formatted) | Year | Month | Value ($/bbl) |
|---|---|---|---|---|
| 0 | 1946-01-01 | 1946 | 1 | 21.23 |
| 1 | 1946-02-01 | 1946 | 2 | 21.35 |
| 2 | 1946-03-01 | 1946 | 3 | 21.11 |
| 3 | 1946-04-01 | 1946 | 4 | 22.79 |
| 4 | 1946-05-01 | 1946 | 5 | 22.67 |

Table 3.4  Sample output of date formatting step for Brent Oil data.

Q5 — SWIFT Dataset Metrics

| Metric | Rows | Topic |
|---|---|---|
| Global Payment Share | 80 | Global payment share (%) |
| International Payment Share (ex-Eurozone) | 80 | Payment share excluding Eurozone |
| Offshore RMB by Economy | 60 | Offshore RMB share by country |
| Trade Finance Share | 40 | Trade finance share |
| FX Spot Currency Ranking | 40 | FX spot market ranking |
| FX Spot Economies (RMB) | 24 | RMB FX spot economies |
| RMB MoM Payment Growth | 4 | RMB month-on-month growth (%) |
| All Currencies MoM Payment Growth | 2 | All currencies MoM growth |

Table 3.5  Metrics in the SWIFT Currency Tracker dataset.


## 3.2 Descriptive Analytics (Q6–Q12)

Q6–Q8 — All-Time Highest and Lowest Prices

| Commodity | Highest Price | Year | Lowest Price | Year |
|---|---|---|---|---|
| Brent Oil | $211.21 / barrel | 2008 | $21.11 / barrel | 1946 |
| Gold | $5,277.89 / oz | 2026 | $19.25 / oz | 1915 |
| Silver | $113.95 / oz | 2026 | $0.28 / oz | 1932 |

Table 3.6  All-time highest and lowest prices. Gold and Silver set new all-time records in 2026.

Q9 — Annual Average Prices (2017–2026)

| Year | Brent ($/bbl) | Gold ($/oz) | Silver ($/oz) |
|---|---|---|---|
| 2017 | 69.85 | 1,269.34 | 17.24 |
| 2018 | 84.91 | 1,265.60 | 15.64 |
| 2019 | 74.03 | 1,405.32 | 16.36 |
| 2020 | 49.19 | 1,784.66 | 20.80 |
| 2021 | 83.02 | 1,792.73 | 24.97 |
| 2022 | 106.45 | 1,798.96 | 21.67 |
| 2023 | 84.19 | 1,953.69 | 23.58 |
| 2024 | 79.83 | 2,404.58 | 28.13 |
| 2025 | 65.93 | 3,472.54 | 41.50 |
| 2026* | 78.67 | 4,881.62 | 96.08 |

Table 3.7  Annual average prices (2017–2026). *2026 reflects the months available so far: January–March for Brent (3 months), January–April for Gold and Silver (4 months).

Q10–Q12 — Top 5 Years by Average Price

Brent Oil — Top 5 Years:

| Rank | Year | $/bbl |
|---|---|---|
| 1 | 2008 | $150.96 |
| 2 | 1980 | $149.86 |
| 3 | 2011 | $142.12 |
| 4 | 2013 | $138.30 |
| 5 | 2012 | $135.27 |

Gold — Top 5 Years:

| Rank | Year | $/oz |
|---|---|---|
| 1 | 2026 | $4,881.62 |
| 2 | 2025 | $3,472.54 |
| 3 | 2024 | $2,404.58 |
| 4 | 2023 | $1,953.69 |
| 5 | 2022 | $1,798.96 |

Silver — Top 5 Years:

| Rank | Year | $/oz |
|---|---|---|
| 1 | 2026 | $96.08 |
| 2 | 2025 | $41.50 |
| 3 | 2011 | $35.56 |
| 4 | 2012 | $31.63 |
| 5 | 2024 | $28.13 |

Tables 3.8a–c  Top 5 highest annual average price years per commodity. Gold's top 5 are all consecutive years 2022–2026.


## 3.3 Trend and Visual Analytics (Q13–Q18)

Q13 — Brent Crude Oil Time Series (Figure 3.1)

The chart reveals four major price eras: (1) post-war low-price era before 1973; (2) OPEC shock period 1973–1985; (3) moderate pricing 1986–2003; and (4) modern high-volatility era from 2004. The 2008 spike to $211 was the historical peak. COVID-19 caused the steepest crash in 2020. The 2022 Ukraine war and 2026 Iran–Hormuz crisis both pushed prices above $100/barrel.

Figure 3.1 — Brent Crude Oil Monthly Price (USD/barrel), 1946–2026. Key crisis events marked: 2008 Peak, COVID Crash, Hormuz Crisis.  
*[Image: `04_Outputs/brent_line.png`]*

Q14 — Gold Time Series (Figure 3.2)

A flat segment from 1915 to 1971 reflects the Bretton Woods system, under which gold was pegged at $35/oz. The 1971 Nixon Shock ended convertibility and allowed the price to float freely. The sharpest bull run phase began in 2020, driven by pandemic monetary policy, the Ukraine war, BRICS gold accumulation, and the Iran–Hormuz crisis, reaching an all-time high of $5,277.89/oz in February 2026.

Figure 3.2 — Gold Monthly Price (USD/oz), 1915–2026. Flat Bretton Woods era visible 1915–1971. All-time high of $5,277.89/oz reached in February 2026.  
*[Image: `04_Outputs/gold_line.png`]*

Q15 — Silver Time Series (Figure 3.3)

Silver traded below $5/oz for most of the 20th century. The 1980 Hunt Brothers corner attempt drove prices to $48. A second peak occurred in 2011 during post-2008 monetary stimulus. The 2026 all-time high of $113.95/oz was driven by safe-haven demand and growing industrial use in solar energy and EV batteries.

Figure 3.3 — Silver Monthly Price (USD/oz), 1915–2026. All-time high of $113.95/oz reached in January 2026.  
*[Image: `04_Outputs/silver_line.png`]*

Q16 — Combined Gold and Silver Chart (Figure 3.4)

The two assets move in close tandem over long periods, reflecting their shared safe-haven characteristics and a long-run correlation of approximately 0.95. Silver shows consistently wider swings, particularly at the 1980, 2011, and 2026 peaks, due to its additional industrial demand role. Both axes are shown to allow direct comparison.

Figure 3.4 — Gold and Silver combined monthly price trend (1915–2026). Dual axes: Gold (left, USD/oz) and Silver (right, USD/oz). Wider Silver swings reflect its dual precious/industrial metal nature.  
*[Image: `04_Outputs/gold_silver_combined.png`]*

Q17 — Annual Average Brent Prices: Last 10 Years (Figure 3.5)

The 2020 dip to $49/bbl reflects COVID-19 demand collapse, followed by a sharp recovery in 2021 and peak in 2022 driven by the Russia–Ukraine war and associated supply disruptions. Prices moderated in 2023–2025 before rising again in early 2026 due to the Iran–Hormuz crisis.

Figure 3.5 — Average annual Brent Oil price (USD/barrel), 2016–2026. The 2022 peak at $106/bbl is clearly visible. 2020 shows the COVID-19 demand collapse.  
*[Image: `04_Outputs/brent_bar_10yr.png`]*

Q18 — Most Recent Values

| Asset | Latest Value | Date |
|---|---|---|
| Brent Oil | $102.86 / barrel | 1 March 2026 |
| Gold | $4,712.89 / oz | 1 April 2026 |
| Silver | $88.36 / oz | 1 April 2026 |
| USDG | $0.9998 / unit | 28 April 2026 |

Table 3.9  Latest available commodity values. All three commodities trade well above their long-term historical averages.


## 3.4 Currency Tracker Analytics (Q19–Q24)

Q19 — Top 10 Currencies by Global Payment Share (April 2026)

| Rank | Currency | Share (%) |
|---|---|---|
| 1 | USD | 51.14% |
| 2 | EUR | 21.30% |
| 3 | GBP | 6.54% |
| 4 | JPY | 3.53% |
| 5 | CNY | 3.10% |
| 6 | CAD | 3.03% |
| 7 | HKD | 1.76% |
| 8 | AUD | 1.61% |
| 9 | SGD | 1.23% |
| 10 | CHF | 1.07% |

Table 3.10  Top 10 currencies by global payment share, April 2026 (SWIFT). USD + EUR account for over 72% of all global payments.

Figure 3.6 — Global Payment Share by Currency, April 2026 (Top 10). USD dominates at 51.14%. CNY/RMB is in 5th place at 3.10%.  
*[Image: `04_Outputs/swift_top10_apr2026.png`]*

Q20 — USD Global Payment Share

USD Global Payment Share (April 2026): 51.14%. The USD remains dominant, though well below its historical peak (~85%). It has not yet fallen below the geopolitically significant 50% threshold, which has become a key discussion point in BRICS and de-dollarisation debates.

Q21 — CNY/RMB Share and Ranking

CNY/RMB Global Payment Share (April 2026): 3.10% — Global Rank: 5th. CNY moved from 6th in January 2026 to 5th by April 2026, overtaking CAD (JPY remained ahead of CNY throughout, in 4th place). This is a directionally meaningful shift, though still small in absolute terms.

Q22 — Top 5 Currency Appearances Across All Report Months

| Currency | Months in Top 5 (out of 4) |
|---|---|
| USD | 4/4 |
| EUR | 4/4 |
| GBP | 4/4 |
| JPY | 4/4 |
| CNY | 2/4 |
| CAD | 2/4 |

Table 3.11  The top four positions were completely stable all four months. The 5th position was contested between CAD and CNY, with CNY taking over in the two most recent months.

Q23 — Top Economies by Offshore RMB Share

| Rank | Economy | Offshore RMB Share (%) |
|---|---|---|
| 1 | Hong Kong | 75.23% |
| 2 | United Kingdom | 6.90% |
| 3 | Singapore | 4.37% |
| 4 | United States | 2.81% |
| 5 | France | 1.80% |

Table 3.12  Hong Kong handles ~75% of all offshore RMB transactions, reinforcing its role as the primary RMB clearing hub outside mainland China.


## 3.5 Simple Comparison Questions (Q25–Q30)

Q25 — Gold: Latest vs Long-Term Average

| Metric | Value (USD/oz) |
|---|---|
| Latest value (April 2026) | $4,712.89 |
| Long-term average (1915–2026) | $397.55 |
| Difference | +1,085.5% (~12× the historical average) |

Table 3.13  Gold is currently trading at ~12× its long-run average, reflecting cumulative inflation and the recent geopolitical/safe-haven premium.

Q26 — Brent Oil: Latest vs Long-Term Average

| Metric | Value (USD/bbl) |
|---|---|
| Latest value (March 2026) | $102.86 |
| Long-term average (1946–2026) | $62.71 |
| Difference | +64.0% above average |

Table 3.14  Brent is 64% above its all-time average — consistent with geopolitical risk premium rather than a structural new price level.

Q27 — Price Volatility Comparison (Figure 3.7)

| Commodity | Monthly % Change Std. Deviation |
|---|---|
| Brent Oil | 9.05% — most volatile |
| Silver | 7.69% |
| Gold | 4.30% — most stable |

Table 3.15  Monthly price volatility. Brent Oil is ~2× as volatile as Gold, explaining why Gold is preferred as a long-term reserve asset.

Figure 3.7 — Price Volatility Comparison: Monthly Std. Dev. (%). Brent Oil (9.05%) leads, followed by Silver (7.69%) and Gold (4.30%).  
*[Image: `04_Outputs/log_returns.png`]*

Q28 — Commodity Movements During 2022 Ukraine War

| Commodity | Jan 2022 | Dec 2022 | Change | Year Peak |
|---|---|---|---|---|
| Brent | $104.72 | $89.19 | -14.8% | $129.22 |
| Gold | $1,796.12 | $1,824.32 | +1.6% | $1,953.04 |
| Silver | $22.39 | $23.96 | +7.0% | $25.13 |

Table 3.16  2022 Ukraine war commodity impact. Brent spiked early in the year (peak $129.22, +23% above the January start) on the Russian invasion, then eased back below its starting level by year-end (-14.8%) as markets adjusted. Gold and Silver both ended the year modestly higher, consistent with their safe-haven role.

Q29 — Summary Dashboard (Figure 3.8)

The following six-panel dashboard provides a concise visual overview: recent commodity price trends (2016–2026), top currency rankings, volatility comparison, and a latest-values snapshot.

Figure 3.8 — DSB Market Dashboard (2026). Six panels: Brent Oil trend, Gold price trend, Silver price trend, Global Payment Share (Top 5), Price Volatility Comparison, and Latest Values Snapshot.  
*[Image: `04_Outputs/dashboard.png`]*

Q30 — Three Insights for Non-Technical Executives

Insight 1 — Gold has become the most reliable store of value in recent years

Gold rose from ~$1,100 in 2015 to over $4,700 in 2026 — a fourfold increase in ten years. During every major crisis (2008, 2020, 2022, 2026), gold attracted strong investor interest as a safe-haven asset. Companies holding gold received meaningful protection against geopolitical shocks and inflation.

Insight 2 — The USD remains dominant, but alternatives are gaining ground

The US Dollar accounts for 51% of global payments (April 2026). However, the CNY rose to 5th place in just four months. BRICS countries are developing alternative payment systems. For companies with high international transaction volumes, over-reliance on a single currency system is a growing operational risk.

Insight 3 — Crude oil reacts to geopolitical crises faster and harder than any other commodity

Brent Oil has a monthly price standard deviation of 9.0%, making it ~2× as volatile as Gold (4.3%). The Iran–Hormuz crisis drove Brent +52% in a single month (March 2026). Energy-intensive businesses should consider forward contracts or hedging strategies.


## 3.6 Bonus Analytics (B1–B6)

B1 — Monthly/Annual Percentage Change

The following tables show Month-on-Month (MoM) and Year-on-Year (YoY) percentage changes for the last 10 months of data for each commodity.

Brent Oil — Last 10 Months:

| Date | Value ($/bbl) | MoM % | YoY % |
|---|---|---|---|
| 2025-06 | 66.33 | +6.23% | -22.60% |
| 2025-07 | 71.87 | +8.35% | -9.05% |
| 2025-08 | 65.45 | -8.93% | -15.17% |
| 2025-09 | 64.22 | -1.88% | -10.04% |
| 2025-10 | 63.12 | -1.71% | -14.55% |
| 2025-11 | 59.68 | -5.45% | -16.14% |
| 2025-12 | 58.35 | -2.23% | -22.24% |
| 2026-01 | 65.48 | +12.22% | -13.14% |
| 2026-02 | 67.66 | +3.33% | -6.78% |
| 2026-03 | 102.86 | +52.02% | +43.60% |

Table B1a: Brent Oil MoM and YoY % changes. The exceptional +52.02% MoM in March 2026 reflects the Iran–Hormuz crisis.

Gold — Last 10 Months:

| Date | Value ($/oz) | MoM % | YoY % |
|---|---|---|---|
| 2025-07 | 3,285.78 | +0.59% | +36.36% |
| 2025-08 | 3,415.77 | +3.96% | +36.45% |
| 2025-09 | 3,836.23 | +12.31% | +43.98% |
| 2025-10 | 4,002.77 | +4.34% | +45.73% |
| 2025-11 | 4,217.36 | +5.36% | +59.07% |
| 2025-12 | 4,322.36 | +2.49% | +64.69% |
| 2026-01 | 4,865.35 | +12.56% | +73.87% |
| 2026-02 | 5,277.89 | +8.48% | +83.50% |
| 2026-03 | 4,670.35 | -11.51% | +51.32% |
| 2026-04 | 4,712.89 | +0.91% | +43.97% |

Table B1b: Gold MoM and YoY % changes. YoY growth remained consistently high at 36–84%.

Silver — Last 10 Months:

| Date | Value ($/oz) | MoM % | YoY % |
|---|---|---|---|
| 2025-07 | 37.12 | +3.73% | +30.93% |
| 2025-08 | 39.02 | +5.12% | +35.18% |
| 2025-09 | 46.86 | +20.11% | +47.50% |
| 2025-10 | 48.69 | +3.91% | +49.08% |
| 2025-11 | 56.54 | +16.12% | +84.74% |
| 2025-12 | 71.65 | +26.72% | +148.14% |
| 2026-01 | 113.95 | +59.04% | +263.93% |
| 2026-02 | 93.66 | -17.81% | +199.93% |
| 2026-03 | 88.36 | -5.66% | +158.37% |
| 2026-04 | 88.36 | 0.00% | +170.79% |

Table B1c: Silver MoM and YoY % changes. YoY peaked at +263.93% in January 2026.

B2 — Correlation Table

|  | Brent | Gold | Silver |
|---|---|---|---|
| Brent | 1.00 | 0.46 | 0.51 |
| Gold | 0.46 | 1.00 | 0.95 |
| Silver | 0.51 | 0.95 | 1.00 |

Table B2: Correlation matrix of annual average commodity prices. Gold–Silver correlation (0.95) is the strongest pair.

B3 — Correlation Heatmap (Figure B3)

The heatmap confirms the correlation matrix visually. Gold–Silver show the strongest relationship (0.95). Brent Oil has a moderate correlation with both precious metals (0.46–0.51), lower than the text-based estimate due to use of full historical annual data rather than recent years only.

Figure B3 — Correlation Matrix Heatmap: Brent Oil, Gold, Silver (Annual Average Prices). Red = strong positive correlation. Gold–Silver at 0.95 is the strongest pair.  
*[Image: `04_Outputs/correlation_heatmap.png`]*

B4 — Gold vs Silver Scatter Plot (Figure B4)

The scatter plot illustrates the strong positive linear association between annual average Gold and Silver prices. The upward-sloping trend line confirms the high correlation coefficient. Silver experiences larger percentage movements than Gold at higher price levels.

Figure B4 — Gold vs Silver Annual Average Price Scatter Plot. Strong positive linear association confirmed (r ≈ 0.95). Each dot represents one year's average prices.  
*[Image: `04_Outputs/gold_silver_scatter.png`]*

B5 — Gold with Moving Averages (Figure B5)

The MA-12 (12-month) and MA-60 (60-month) moving averages smooth short-term price fluctuations to reveal underlying trend structure. The persistent upward trend in Gold prices is confirmed by both moving averages rising continuously since the mid-2000s.

Figure B5 — Gold Price with 12-Month and 60-Month Moving Averages (1915–2026). The MA-12 (orange) tracks medium-term movements; the MA-60 (red) reveals the long-term structural bull trend.  
*[Image: `04_Outputs/gold_moving_avg.png`]*

B6 — Linear Trend Forecast: Gold 12-Month Outlook (Figure B6)

The linear regression model fitted to historical Gold prices from 2016 to 2026 is extended 12 months forward. The model projects a continued upward direction based on the long-term trend. Note that the projection is based on trend extrapolation and does not account for short-term geopolitical shocks or market corrections.

Figure B6 — Gold Price: Historical Data + Linear Trend Forecast (12-month projection). The red dashed line shows the forecast trajectory from April 2026 onward based on fitted linear regression.  
*[Image: `04_Outputs/gold_forecast.png`]*


# 4. Part II — Market Research Findings

**Supporting materials:** *Critical New Context: The 2026 Iran War & GCC Crisis*; *A New Financial Order II*; *Reserve Storm*; *The Wall Street Ledger* — market/geopolitical briefing reports (April 2026), used for event-timeline context alongside the core datasets.


## 4.1. Event Identification

Q1 — Three Major Global Events

2026 Iran–Hormuz crisis: affected global oil supply, reflected in Figure 3.1's March 2026 +52% spike.

2025–2026 Gold accumulation and geopolitical uncertainty: explains the continuous Gold uptrend (Figure 3.2).

BRICS payment discussions and sanctions developments: influence global currency structures (Table 3.10).

Q2 — Timeline of Events

| Date | Event | Market Affected | Data Signal |
|---|---|---|---|
| Nov 2024 | USDG (Global Dollar stablecoin) launches — Paxos | Currency / Digital | USDG.csv: market cap starts at ~$259M |
| 20 Oct 2025 | Gold closes above $4,268; Silver above $50 | Gold, Silver | gold100years.csv, silver100years.csv |
| 22–24 Oct 2025 | BRICS Kazan Summit: Turkey joins; BRICS Pay processes $1.03B in first week | Currency | SWIFT CNY rank trend Jan→Apr 2026 |
| Oct 2025 | Saudi Arabia's first yuan oil invoice (post-1974 petrodollar) | Oil, Currency | Brent + USD SWIFT share |
| 29 Jan 2026 | Gold intraday ATH $5,595/oz | Gold | gold100years.csv: $4,712 April close |
| 28 Feb 2026 | US strikes on Iranian nuclear facilities | Oil, Gold, Silver | All three commodities surge |
| 1–2 Mar 2026 | Hormuz blockade; flow drops to ~7% of normal | Oil | Brent +52% MoM (March 2026) |
| 8 Apr 2026 | Saudi East-West pipeline attacked (−600k bbl/day) | Oil | Brent additional spike |
| 12 Apr 2026 | US formal Hormuz naval blockade | Oil, Currency | Brent + DXY movement |
| Apr 2026 | BRICS Pay reaches $4B/month; BRIC stablecoin emergency launch | Currency | SWIFT CNY rises to Rank 5 |
| Apr 2026 | USDG market cap reaches $2.42B (~9.3× in 12 months) | Digital Currency | USDG.csv |

Table 4.1: Timeline of major global events and observed market impact.

Q3 — Brent Oil Link (Figure 3.1)

The Hormuz crisis is most directly linked to Brent Oil because it affects key supply routes through the Strait of Hormuz. In Figure 3.1, major price spikes clearly align with geopolitical crisis periods, confirming oil's high sensitivity to supply disruptions.

Q4 — Gold and Silver Link (Figures 3.2 & 3.3)

Gold is strongly influenced by uncertainty, visible in its consistent upward trend in Figure 3.2. Silver also increases but shows larger fluctuations in Figure 3.3 due to both investment demand and its additional industrial use in manufacturing, solar panels, and EV batteries.


## 4.2. Linking Events to Commodity Data

Q5 — Oil Supply Shock

Oil supply disruptions reduce availability and increase transport costs, causing prices to rise sharply. In Figure 3.1, price spikes align with 1973 OPEC, 1980, 2008, 2022, and 2026 crisis periods, confirming Brent Oil's high geopolitical sensitivity.

Q6 — Gold Behaviour

Gold increases during uncertainty as investors prefer safe assets. Its low monthly volatility (4.30%) and consistent upward trend during crisis periods (Figure 3.2) makes it a preferred institutional reserve asset.

Q7 — Silver Behaviour

Using Figure 3.4, Silver follows Gold but shows larger movements. This is consistent with Silver's dual role: precious metal demand (safe-haven) plus industrial demand (solar, EV batteries), which amplifies price movements beyond those of Gold alone.

Q8 — Crisis Comparison

| Commodity | Behaviour | Change to Peak | Primary Driver |
|---|---|---|---|
| Brent Oil | Sharp spikes and rapid corrections | +22.5% | Supply shocks and geopolitical events |
| Gold | Stable, consistent increase | +18.7% | Safe-haven demand and central bank buying |
| Silver | High volatility, wider swings | +37.7% | Mixed: precious metal + industrial demand |

Table 4.2: Commodity behaviour patterns during crisis periods, as evidenced by Figures 3.1–3.4.


## 4.3. Linking Events to Currency Data

Q9 — USD Role

Table 3.10 shows the USD at 51.14% — confirming structural dominance. USD and EUR together account for over 72% of all SWIFT-tracked global payment flows.

Q10 — CNY/RMB Role

CNY at 3.10% (5th rank) shows directional growth — overtaking CAD — but remains much smaller than the USD, and behind JPY throughout. The shift is gradual rather than disruptive.

Q11 — Sanctions and Alternative Payment Systems

Sanctions and BRICS Pay discussions encourage alternative systems. However, Table 3.10 shows the USD still dominates structurally due to deeply embedded correspondent banking and clearing infrastructure. Changes are gradual and not yet disruptive.

Q12 — Offshore RMB

Hong Kong dominates offshore RMB at 75.23% (Table 3.12), indicating high concentration in one financial centre. The UK and Singapore serve as secondary hubs. The presence of the US and France in the top five indicates even Western financial centres are participating in RMB internationalisation at small scales.


## 4.4. Business Interpretation and Recommendations

Q13 — Market Sensitivity (Figure 3.7)

Figure 3.7 confirms Brent Oil has the highest monthly price volatility (9.05% std. dev.), making it most sensitive to global events. Gold is the most stable (4.30%), while Silver occupies a middle position (7.69%) reflecting its mixed precious-industrial nature.

Q14 — Oil Risk Note

Companies exposed to oil prices face risk from sudden spikes. Figure 3.1 shows prices can increase over 50% in a single month during crises. Businesses in energy-intensive sectors — manufacturing, aviation, logistics — should consider forward contracts or hedging strategies.

Q15 — Currency and Asset Risk Note

USD remains dominant but carries concentration risk (Table 3.10). Gold provides proven crisis protection (Figure 3.2), while the RMB offers long-term growth potential but is in early stages of internationalisation (Table 3.12). Portfolio and currency diversification are recommended.

Q16 — Three Practical Recommendations

R1 — Hedge Oil Exposure

Given Brent Oil's monthly price standard deviation of 9.05% and demonstrated sensitivity to supply disruptions, businesses with significant energy cost exposure should implement forward contracts or options-based hedging. The March 2026 +52% MoM increase illustrates the magnitude of unhedged risk.

R2 — Invest in Gold for Risk Protection

Gold has provided consistent safe-haven performance across multiple crisis periods. Its relatively low monthly volatility (4.30%) and strong YoY appreciation (over 43% YoY in April 2026) make it an effective portfolio risk buffer.

R3 — Monitor Currency Diversification Trends

The USD dominates at 51.14% of global payment flows, but CNY's rise to 5th place and BRICS-driven alternative payment initiatives signal a longer-term structural shift. Companies with high-volume cross-border transactions should monitor these trends and explore diversified currency exposure strategies.

| Recommendation | Asset / Area | Key Data Point | Priority |
|---|---|---|---|
| Hedge oil exposure | Brent Oil | 9.05% monthly std dev; +52% MoM Mar 2026 | High |
| Invest in gold for protection | Gold | +43.97% YoY Apr 2026; $4,712.89/oz | High |
| Monitor currency diversification | USD / CNY | USD 51.14%; CNY 3.10% (5th place) | Medium |

Table 5.1: Summary of recommendations with supporting data points.


# 5. Final Recommendation for Management

Summary for a non-technical decision-maker:

This report analysed over 111 years of commodity price data and 4 months of SWIFT currency tracking data, covering a period of exceptional market turbulence — the 2026 Iran-Hormuz Crisis, record gold prices, and the operational launch of BRICS Pay's alternative payment infrastructure.

Three conclusions stand out above all others:

First, oil risk is real and immediate. Brent crude's 22% spike during the Hormuz blockade is not unusual by historical standards — the 1973, 1979, and 2022 shocks all produced similar or larger moves. Any organisation with oil exposure that does not have a hedging policy is operating without a seatbelt on a road with a documented accident history.

Second, gold is telling us something important about the monetary system. The fact that central banks — sovereign governments — are buying gold at record rates is a signal worth taking seriously. They are not doing this for speculative profit; they are doing it to reduce reliance on USD-denominated reserve assets. This structural shift is underway regardless of any single geopolitical event, and it provides a durable floor under gold prices even as valuations look stretched by historical norms.

Third, the currency landscape is changing, slowly but surely. The USD is not losing its dominance in any near-term timeframe. But the 15-percentage-point decline in USD reserve share over two decades[7], combined with BRICS Pay processing $4B/month and the growing offshore RMB ecosystem, means the multi-currency payment world is arriving — not as a theoretical future scenario, but as an operational present. Starting to test alternative settlement lanes now is prudent risk management, not speculation.

6. Conclusion

This report has presented a comprehensive data analytics and market research study of Brent Crude Oil, Gold, Silver, and SWIFT global currency payment data, spanning from historical long-term trends (1915–2026) to current market conditions (April 2026).

Gold has entered an unprecedented bull run, rising from ~$1,100 in 2015 to an all-time high of $5,277.89/oz in February 2026. Silver reached $113.95/oz in January 2026, underpinned by precious metal demand and growing clean energy industrial consumption. Brent Crude Oil remains the most volatile commodity (9.05% monthly std. dev.), with the March 2026 Iran–Hormuz crisis driving a single-month +52% spike.

In currency markets, the USD retains structural dominance at 51.14% of global payment share. The CNY continues its gradual internationalisation, rising to 5th place by April 2026. The pace is directional but not yet disruptive.

These findings support three clear actionable recommendations: hedge energy cost exposure, use gold as a portfolio risk buffer, and monitor evolving currency dynamics for international transaction strategy.


## 7. Appendix


## A. Extended Forecasting Pipeline Summary

As part of the extended analytics work for this project, a multi-tier forecasting pipeline was developed and validated across Gold, Silver, and Brent (walk-forward validation, monthly frequency, out-of-sample test window 2024-04-01 to 2026-04-01, 24 months):

| Tier | Method | Gold MAPE | Silver MAPE | Brent MAPE |
|---|---|---|---|---|
| T1 (baseline) | Naive Random Walk | 4.30% | 8.45% | 6.50% |
| T1 | ARIMA(1,1,2) / (3,1,3) / (1,1,2) [12] | 3.90% | 8.58% | 6.55% |
| T1 | ARIMAX + FRED [11] exogenous (VIX / DXY) | 4.14% | — | 8.05% |
| T1 | GARCH [13] / EGARCH [14] (1,1) | Leverage effect confirmed; volatility cone for 12-month CI |  |  |
| T2 | Random Forest (500 trees) [10] | 4.07% | 12.43% | 6.49% |
| T2 | LightGBM | 4.80% | 10.54% | 6.79% |
| T2 | LSTM(64) | 3.88% | 8.45% | 6.61% |
| T2 | BiGRU(32) (Gold only) [9] | 3.94% | — | — |
| T3 | Johansen [15] + VECM (Gold-Silver) | VECM Gold MAPE: 3.98%; cointegration rank = 0 (111-year structural breaks) |  |  |
| T3 | Markov Regime-Switching (Brent) [16] | 2 regimes; stress σ² ≈ 680× calm σ² |  |  |
| T3 | USDG Peg Analysis [6] | Peg deviation σ = 6.8×10⁻⁵ USD (near-perfect stability); mean SWIFT USD share over the 4 report months = 50.14% (vs. 51.14% for the April snapshot used elsewhere in this report) |  |  |

LSTM gives the narrowest edge for Gold (3.88%, just ahead of ARIMA's 3.90%); Random Forest remains the (marginal) leader for Brent. Across Gold's four best-performing models (LSTM, ARIMA, BiGRU, VECM) the spread is only 0.10 percentage points — effectively a tie given the 24-month test window — so this should be read as "several approaches are competitive," not as proof that any single model or model family is decisively superior (see Figures 7.1–7.11 below).

Caveat on model "wins": for Silver, no model in this table shows a practically meaningful improvement over the Naive Random Walk baseline (8.45%) — LSTM's nominal edge (8.4469% vs. 8.4503%) is a 0.003 percentage-point difference, well within noise. For Brent, Random Forest's edge over Naive (6.49% vs. 6.50%) is likewise only 0.01 percentage points. Only Gold shows a modest, consistent edge for modelled approaches over the naive baseline (LSTM, −0.42pp vs. Naive).

Figure 7.1: forecast_gold  
*[Image: `04_Outputs/forecast_gold.png`]*

Figure 7.2: forecast_brent  
*[Image: `04_Outputs/forecast_brent.png`]*

Figure 7.3: forecast_silver  
*[Image: `04_Outputs/forecast_silver.png`]*

Figure 7.4: tier3_markov_brent  
*[Image: `04_Outputs/tier3_markov_brent.png`]*

Figure 7.5: tier3_usdg_peg  
*[Image: `04_Outputs/tier3_usdg_peg.png`]*

Figure 7.6: garch_volatility — GARCH(1,1) conditional volatility, confirming the leverage effect referenced in the table above.  
*[Image: `04_Outputs/garch_volatility.png`]*

Figure 7.7: garch_forecast_cone — GARCH 12-month volatility forecast cone.  
*[Image: `04_Outputs/garch_forecast_cone.png`]*

Figure 7.8: tier3_vecm_gold — Gold-Silver VECM cointegrating relationship.  
*[Image: `04_Outputs/tier3_vecm_gold.png`]*

Figure 7.9: structural_breaks — Structural break test across the 111-year Gold/Silver series referenced in the VECM row above.  
*[Image: `04_Outputs/structural_breaks.png`]*

Figure 7.10: rmse_heatmap — RMSE comparison across all models and assets, summarising the table above in a single view.  
*[Image: `04_Outputs/rmse_heatmap.png`]*

Figure 7.11: tier3_usdg_swift — USDG market cap growth vs. SWIFT USD payment share, supporting the Part II de-dollarisation narrative.  
*[Image: `04_Outputs/tier3_usdg_swift.png`]*


## B. Forecast vs. Actual Validation — May–June 2026

Figure 7.12: forecast_validation_jun2026  
*[Image: `04_Outputs/forecast_validation_jun2026.png`]*

Naive random-walk forecasts were compared against actual spot prices retrieved from yfinance for May and June 2026:

| Asset | Month | Forecast | Actual | Error | In 95% CI? |
|---|---|---|---|---|---|
| Gold | May 2026 | $4,790 | $4,590 | −4.2% | Yes |
| Gold | Jun 2026 | $4,869 | $4,309 | −11.5% | Yes |
| Silver | May 2026 | $90.19 | $78.14 | −13.4% | Yes |
| Silver | Jun 2026 | $92.05 | $69.21 | −24.8% | No |
| Brent | Apr 2026 | $103.43 | $102.46 | −0.9% | Yes |
| Brent | May 2026 | $104.01 | $104.09 | +0.1% | Yes |
| Brent | Jun 2026 | $104.58 | $89.04 | −14.9% | Yes |

Seven of eight actuals fell within the 95% confidence interval — confirming that the forecast uncertainty bands are well-calibrated. Silver's June 2026 reading fell outside the band, suggesting a volatility spike from industrial demand disruption beyond what the 60-month rolling window anticipated.


## C. Interactive Dashboard (Companion Tool)

Beyond the static figures above, a companion interactive dashboard was built to let a reader explore the full Tier 1–3 forecasting pipeline directly. It provides: animated historical price charts (Gold, Silver, Brent) with global-event markers and a 12-month forecast band (GARCH-based where available); a live model-comparison view with Diebold-Mariano [17] significance tests against the naive baseline; a USDG panel showing the logistic adoption S-curve (with parameter uncertainty) and peg-stability chart; a normalised cross-asset comparison view; and a macro-context view overlaying VIX, the US Dollar Index, and TIPS real yields against commodity prices.


## 8. Key Source References

[1]  Macrotrends, "Brent Crude Oil Prices - 10 Year Daily Chart," dataset (brentOil.csv).

[2]  Macrotrends, "Gold Prices - 100 Year Historical Chart," dataset (gold100years.csv).

[3]  Macrotrends, "Silver Prices - 100 Year Historical Chart," dataset (silver100years.csv).

[4]  SWIFT, "Global Currency Tracker — Monthly Reports," dataset (swift_currency_tracker_all_reports.csv).

[5]  CoinGecko, "USDG Historical Price and Market Cap," dataset (USDG.csv), collected Apr. 2026.

[6]  R. Ahmed and I. Aldasoro, "Stablecoins and safe asset prices," BIS Working Papers, no. 1270, Bank for International Settlements, Basel, Switzerland, May 2025.

[7]  International Monetary Fund, "Currency Composition of Official Foreign Exchange Reserves (COFER)," Q3 2025.

[8]  World Gold Council, "Gold as a Strategic Asset — Safe-Haven Framework," 2025.

[9]  P. Foroutan and S. Lahmiri, "Deep learning systems for forecasting the prices of crude oil and precious metals," Financial Innovation, vol. 10, Art. no. 111, 2024, doi: 10.1186/s40854-024-00637-z.

[10] R. Gupta, S. Karmakar, and C. Pierdzioch, "Safe havens, machine learning, and the sources of geopolitical risk: A forecasting analysis using over a century of data," Computational Economics, vol. 64, pp. 487–513, 2024, doi: 10.1007/s10614-023-10452-w.

[11] Federal Reserve Bank of St. Louis, "FRED: VIXCLS, DTWEXBGS, DFII10," Federal Reserve Economic Data.

[12] G. E. P. Box and G. M. Jenkins, Time Series Analysis: Forecasting and Control. San Francisco, CA, USA: Holden-Day, 1976.

[13] R. F. Engle, "Autoregressive conditional heteroscedasticity with estimates of the variance of United Kingdom inflation," Econometrica, vol. 50, no. 4, pp. 987–1007, 1982.

[14] D. B. Nelson, "Conditional heteroskedasticity in asset returns: A new approach," Econometrica, vol. 59, no. 2, pp. 347–370, 1991.

[15] S. Johansen, "Statistical analysis of cointegration vectors," Journal of Economic Dynamics and Control, vol. 12, no. 2–3, pp. 231–254, 1988.

[16] J. D. Hamilton, "A new approach to the economic analysis of nonstationary time series and the business cycle," Econometrica, vol. 57, no. 2, pp. 357–384, 1989.

[17] F. X. Diebold and R. S. Mariano, "Comparing predictive accuracy," Journal of Business & Economic Statistics, vol. 13, no. 3, pp. 253–263, 1995.
