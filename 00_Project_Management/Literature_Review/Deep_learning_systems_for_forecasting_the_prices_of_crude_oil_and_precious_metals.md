# Deep Learning Systems for Forecasting the Prices of Crude Oil and Precious Metals

**Authors:** Parisa Foroutan, Salim Lahmiri (Concordia University, Montreal)
**Journal:** Financial Innovation (2024) 10:111
**DOI:** https://doi.org/10.1186/s40854-024-00637-z
**Access:** Open Access

---

## Abstract

Twelve deep learning models, two ensemble machine learning models, and two baseline machine learning models are compared for forecasting crude oil (WTI and Brent) and precious metal (gold and silver) prices. Best-performing model: **TCN (WTI, Brent, Silver)** and **BiGRU (Gold)**.

---

## Key Terms and Concepts

### Markets Forecasted

| Asset | Description | Average Price |
|--------|----------|----------------|
| **WTI** | West Texas Intermediate — US crude oil benchmark | $61.47 |
| **Brent** | North Sea crude oil — international benchmark | $64.27 |
| **Gold** | Precious metal, portfolio diversification instrument | $1,020.98 |
| **Silver** | Precious metal, used for both investment and industrial purposes | $15.73 |

### Deep Learning Models

| Model | Full Name | Function |
|-------|-----------|----------|
| **LSTM** | Long Short-Term Memory | Learns long-range dependencies; overcomes the vanishing-gradient problem |
| **BiLSTM** | Bidirectional LSTM | Two LSTM layers running forward and backward — less sensitive to sequence order |
| **GRU** | Gated Recurrent Unit | A lighter version of LSTM; no output gate, trains faster |
| **BiGRU** | Bidirectional GRU | Bidirectional version of GRU |
| **T2V-BiLSTM** | Time2Vector + BiLSTM | Converts timestamps into a vector representation fed into a BiLSTM |
| **T2V-BiGRU** | Time2Vector + BiGRU | Converts timestamps into a vector representation fed into a BiGRU |
| **CNN** | Convolutional Neural Network | Captures local patterns and short-term features |
| **CNN-BiLSTM** | CNN + BiLSTM hybrid | CNN feature extraction → BiLSTM temporal learning |
| **CNN-BiGRU** | CNN + BiGRU hybrid | CNN feature extraction → BiGRU temporal learning |
| **TCN** | Temporal Convolutional Network | Efficiently learns long-range dependencies via dilated causal convolutions |
| **TCN-BiLSTM** | TCN + BiLSTM hybrid | TCN feature extraction → BiLSTM |
| **TCN-BiGRU** | TCN + BiGRU hybrid | TCN feature extraction → BiGRU |

### Machine Learning (Baseline) Models

| Model | Description | Strength |
|-------|--------------|------------|
| **Random Forest** | Ensemble (bagging) of many decision trees | Robust to outliers, resistant to overfitting |
| **LightGBM** | Histogram-based gradient boosting | Fast and efficient on large datasets; performed comparably to TCN in this study |
| **SVR** | Support Vector Regression | Captures linear and nonlinear relationships; sensitive to hyperparameter selection |
| **KNN** | K-Nearest Neighbors | No training phase; suffers from the curse of dimensionality and slow prediction |

### Key Technical Terms

| Term | Description |
|-------|-------|
| **Sliding Window** | Approach using the past N days as input to predict the next day; window sizes of 5, 30, 60, 90 days were tested |
| **Time-based Split** | Train/validation/test data split chronologically (no random split — prevents data leakage) |
| **Time2Vector (T2V)** | A learnable vector-embedding technique that decomposes time information into periodic (sine) and aperiodic (linear) components |
| **Dilated Causal Convolution** | The core of TCN; convolution that spans a wide time range without leaking future information |
| **Residual Connection** | Skip connection that adds a layer's output to its input to prevent vanishing gradients |
| **Dropout** | Regularization that randomly deactivates neurons during training to prevent overfitting (rate: 0.2) |
| **Adam Optimizer** | Optimizer with adaptive learning rate; lr₀=0.001, exponential decay after epoch 5 |
| **Data Normalization** | Min-max scaling: x' = (x - min) / (max - min), rescaled to the [0,1] range |
| **MAE** | Mean Absolute Error — average of absolute errors |
| **MAPE** | Mean Absolute Percentage Error — scale-free relative error metric |
| **RMSE** | Root Mean Squared Error — penalizes large errors more heavily |
| **Gradient Vanishing** | Gradients approaching zero during backpropagation in deep networks; addressed by LSTM/GRU |
| **Bagging** | Bootstrap Aggregating — averaging models trained on different data subsets (the Random Forest method) |
| **Gradient Boosting** | Method that sequentially combines weak learners; used by LightGBM |

---

## Dataset

- **Source:** WTI and Brent → US Energy Information Administration (EIA); Gold and Silver → KITCO
- **Period:** 2000-01-04 to 2022-03-25
- **Observations:** 5,426 (matching trading days across all 4 markets)
- **Split:**
  - Train: 65% → 2000-01-04 to 2014-06-15
  - Validation: 25% → 2014-06-16 to 2020-01-02
  - Test: 10% → 2020-01-03 to 2022-03-25 *(covers the COVID-19 crisis and the Russia-Ukraine war period)*

---

## Methodology Summary

1. Daily closing prices were collected and normalized to the [0,1] range
2. Input sequences were built using the sliding window method (5, 30, 60, 90 days)
3. Train/validation/test sets were created via time-based splitting
4. Hyperparameters for 16 models were optimized via grid search
5. Models were trained with the Adam optimizer using MSE loss (50 epochs, batch size 32)
6. Compared on the test set using MAE, MAPE, RMSE

---

## Key Findings

| Market | Best Model | MAE |
|--------|-------------|-----|
| WTI | **TCN** | 1.444 |
| Brent | **TCN** | 1.295 |
| Gold | **BiGRU** | 15.188 (30-day window) |
| Silver | **TCN** | 0.346 |

- **LightGBM** performed comparably to TCN → the best machine learning model
- Longer windows (30, 60, 90 days) are not always better; it depends on the market
- Hybrid models (CNN-BiLSTM, TCN-BiGRU, etc.) did not always outperform single models
- The test period (COVID + Ukraine war) made price forecasting especially difficult

---

## Relevance to the Project

This paper is directly relevant to the project's **crude oil and precious metal price forecasting** theme. Its model architectures (especially TCN and LightGBM) and evaluation metrics (MAE, MAPE, RMSE) provide a strong reference for the project's methodology choices.

---

## References

- Abdullah Ahmed R, Bin Shabri A (2014) Daily crude oil price forecasting model using Arima, generalized autoregressive conditional heteroscedastic and support vector machines. *Am J Appl Sci* 11(3):425–432
- Adekoya OB, Akinseye AB, Antonakakis N, Chatziantoniou I, Gabauer D, Oliyide J (2022) Crude oil and Islamic sectoral stocks: Asymmetric TVP-VAR connectedness and investment strategies. *Resour Policy* 78:102877
- Akbar M, Iqbal F, Noor F (2019) Bayesian analysis of dynamic linkages among gold price, stock prices, exchange rate and interest rate in Pakistan. *Resour Policy* 62:154–164
- Alameer Z, Elaziz MA, Ewees AA, Ye H, Jianhua Z (2019) Forecasting gold price fluctuations using improved multilayer perceptron neural network and whale optimization algorithm. *Resour Policy* 61:250–260
- Almeida F, Xexéo G (2019) Word embeddings: a survey
- Amirifar T, Lahmiri S, Zanjani MK (2023) An NLP-deep learning approach for product rating prediction based on online reviews and product features. *IEEE Trans Comput Soc Syst*. https://doi.org/10.1109/TCSS.2023.3290558
- Amirshahi B, Lahmiri S (2023a) Hybrid deep learning and GARCH-family models for forecasting volatility of cryptocurrencies. *Mach Learn Appl* 12:100465
- Amirshahi B, Lahmiri S (2023b) Investigating the effectiveness of Twitter sentiment in cryptocurrency close price prediction by using deep learning. *Expert Syst*. https://doi.org/10.1111/exsy.13428
- Arbane M, Benlamri R, Brik Y, Alahmar AD (2023) Social media-based COVID-19 sentiment classification model using Bi-LSTM. *Expert Syst Appl* 212:118710
- Baek C (2019) How are gold returns in the U.S. market? Evidence from the past 10-year gold market. *Appl Econ* 51(50):5490–5497
- Bai Y, Li X, Yu H, Jia S (2022) Crude oil price forecasting incorporating news text. *Int J Forecast* 38(1):367–383
- Balcilar M, Gabauer D, Umar Z (2021) Crude Oil futures contracts and commodity markets: new evidence from a TVP-VAR extended joint connectedness approach. *Resour Policy* 73:102219
- ben Khelifa S, Guesmi K, Urom C (2021) Exploring the relationship between cryptocurrencies and hedge funds during COVID-19 crisis. *Int Rev Financ Anal* 76:101777
- Bhowmik R, Wang S (2020) Stock market volatility and return analysis: a systematic literature review. *Entropy* 22(5):522
- Boongasame L, Viriyaphol P, Tassanavipas K, Terndee P (2022) Gold-price forecasting method using long short-term memory and the association rule. *J Mob Multimedia* 19(1):165–186
- Borisov V, Leemann T, Seßler K, Haug J, Pawelczyk M, Kasneci G (2021) Deep neural networks and tabular data: a survey. *IEEE Trans Neural Netw Learn Syst*:1–21
- Chen T, Guestrin C (2016) XGBoost: a scalable tree boosting system. In: Proceedings of the 22nd ACM SIGKDD international conference on knowledge discovery and data mining, pp 785–794
- Cho K, van Merrienboer B, Bahdanau D, Bengio Y (2014) On the properties of neural machine translation: encoder-decoder approaches
- Chung J, Gulcehre C, Cho K, Bengio Y (2014) Empirical evaluation of gated recurrent neural networks on sequence modeling
- Das S, Nayak J, Kamesh Rao B, Vakula K, Ranjan Routray A (2022) Gold price forecasting using machine learning techniques: review of a decade. *Adv Intell Syst Comput Book Ser (AISC)* 1349:679–695
- Devlin J, Chang MW, Lee K, Google KT (2018) BERT: pre-training of deep bidirectional transformers for language understanding
- Drachal K (2022) Forecasting the crude oil spot price with Bayesian symbolic regression. *Energies* 16(1):4
- Enwereuzoh PA, Odei-Mensah J, Owusu Junior P (2021) Crude oil shocks and African stock markets. *Res Int Bus Financ* 55:101346
- Fang T, Zheng C, Wang D (2023a) Forecasting the crude oil prices with an EMD-ISBM-FNN model. *Energy* 263:125407
- Fang Y, Wang W, Wu P, Zhao Y (2023b) A sentiment-enhanced hybrid model for crude oil price forecasting. *Expert Syst Appl* 215:119329
- Gharghory SM (2021) A hybrid model of bidirectional long-short term memory and CNN for multivariate time series classification of remote sensing data. *J Comput Sci* 17(9):789–802
- Gono DN, Napitupulu H (2023) Silver price forecasting using extreme gradient boosting (XGBoost) method. *Mathematics* 11(18):3813
- Gopali S, Abri F, Siami-Namini S, Namin AS (2021) A comparison of TCN and LSTM models in detecting anomalies in time series data. *IEEE Int Conf Big Data* 2021:2415–2420
- Gruber N, Jockisch A (2020) Are GRU Cells more specific and LSTM Cells more sensitive in motive classification of text? *Front Artif Intell* 3
- Guo J, Zhao Z, Sun J, Sun S (2022) Multi-perspective crude oil price forecasting with a new decomposition-ensemble framework. *Resour Policy* 77:102737
- He P, Liu X, Gao J, Chen W (2020) DeBERTa: Decoding-enhanced BERT with Disentangled Attention. International Conference on Learning Representations
- He Z, Zhou J, Dai HN, Wang H (2019) Gold price forecast based on LSTM-CNN model. In: 2019 IEEE international conference on dependable, autonomic and secure computing, pp 1046–1053
- Hochreiter S, Schmidhuber J (1997) Long short-term memory. *Neural Comput* 9(8):1735–1780
- Huang Y, Liu Q, Peng H, Wang J, Yang Q, Orellana-Martín D (2023) Sentiment classification using bidirectional LSTM-SNP model and attention mechanism. *Expert Syst Appl* 221:119730
- Hussain Shahzad SJ, Raza N, Shahbaz M, Ali A (2017) Dependence of stock markets with gold and bonds under bullish and bearish market states. *Resour Policy* 52:308–319
- Jiang H, Hu W, Xiao L, Dong Y (2022) A decomposition position ensemble based deep learning approach for crude oil price forecasting. *Resour Policy* 78:102855
- Junttila J, Pesonen J, Raatikainen J (2018) Commodity market based hedging against stock market risk in times of financial crisis: the case of crude oil and gold. *J Int Finan Markets Inst Money* 56:255–280
- Kazemi SM, Goel R, Eghbali S, Ramanan J, Sahota J, Thakur S, Wu C, Poupart P, Brubaker M (2019) Time2Vec: learning a vector representation of time
- Ke G, Meng Q, Finley T, Wang T, Chen W, Ma W, Ye Q, Liu TY (2017) LightGBM: a highly efficient gradient boosting decision tree. *Adv Neural Inf Process Syst* 30:3146–3154
- Kertlly de Medeiros R, da Nóbrega BC, Pitta de Jesus D, Phillipe de Albuquerquemello V (2022) Forecasting oil prices: new approaches. *Energy* 238:121968
- Khan M, Wang H, Riaz A, Elfatyany A, Karim S (2021) Bidirectional LSTM-RNN-based hybrid deep learning frameworks for univariate time series classification. *J Supercomput* 77(7):7021–7045
- Kou G, Olgu Akdeniz O, Dinçer H, Yüksel S (2021) Fintech investments in European banks: a hybrid IT2 fuzzy multidimensional decision-making approach. *Financ Innov* 7:39
- Kou G, Yüksel S, Dinçer H (2022) Inventive problem-solving map of innovative carbon emission strategies for solar energy-based transportation investment projects. *Appl Energy* 311:118680
- Lahmiri S (2023a) Multifractals and multiscale entropy patterns in energy markets under the effect of the COVID-19 pandemic. *Decis Anal J* 7:100247
- Lahmiri S (2023b) A comparative study of statistical machine learning methods for condition monitoring of electric drive trains in supply chains. *Supply Chain Anal* 2:100011
- Lahmiri S, Bekiros S (2019) Cryptocurrency forecasting with deep chaotic neural networks. *Chaos, Solitons Fractals* 118:35–40
- Lahmiri S, Bekiros S (2020) Intelligent forecasting with machine learning trading systems in chaotic intraday Bitcoin market. *Chaos, Solitons Fractals* 133:109641
- Lahmiri S, Bekiros S (2021) Deep learning forecasting in cryptocurrency high-frequency trading. *Cogn Comput* 13:485–487
- Lahmiri S, Bekiros S, Avdoulas C (2023) A comparative assessment of machine learning methods for predicting housing prices using Bayesian optimization. *Decis Anal J* 6:100166
- Lahmiri S, Bekiros S, Bezzina B (2022) Complexity analysis and forecasting of variations in cryptocurrency trading volume with support vector regression tuned by Bayesian optimization under different kernels: an empirical comparison from a large dataset. *Expert Syst Appl* 209:118349
- Lara-Benítez P, Carranza-García M, Luna-Romera JM, Riquelme JC (2020) Temporal convolutional networks applied to energy-related time series forecasting. *Appl Sci* 10(7):2322
- Lea C, Flynn MD, Vidal R, Reiter A, Hager GD (2016) Temporal convolutional networks for action segmentation and detection
- Lecun Y, Bottou L, Bengio Y, Haffner P (1998) Gradient-based learning applied to document recognition. *Proc IEEE* 86(11):2278–2324
- Li G, Yin S, Yang H (2022a) A novel crude oil prices forecasting model based on secondary decomposition. *Energy* 257:124684
- Li T, Kou G, Peng Y, Yu PS (2022b) An integrated cluster detection, optimization, and interpretation approach for financial data. *IEEE Trans Cybern* 52(12):13848–13861
- Li X, Shang W, Wang S (2019) Text-based crude oil price forecasting: a deep learning approach. *Int J Forecast* 35(4):1548–1560
- Li Y, Du N, Bengio S (2017) Time-dependent representation for neural event sequence prediction
- Liang X, Luo P, Li X, Wang X, Shu L (2023) Crude oil price prediction using deep reinforcement learning. *Resour Policy* 81:103363
- Lim B, Zohren S (2021) Time-series forecasting with deep learning: a survey. *Philos Trans R Soc Math Phys Eng Sci* 379(2194):20200209
- Lin Y, Chen K, Zhang X, Tan B, Lu Q (2022) Forecasting crude oil futures prices using BiLSTM-Attention-CNN model with Wavelet transform. *Appl Soft Comput* 130:109723
- Liu G, Guo J (2019) Bidirectional LSTM with attention mechanism and convolutional layer for text classification. *Neurocomputing* 337:325–338
- Liu Y, Ott M, Goyal N, Du J, Joshi M, Chen D, Levy O, Lewis M, Zettlemoyer L, Stoyanov V (2019) RoBERTa: a robustly optimized BERT pretraining approach
- Lu W, Li J, Li Y, Sun A, Wang J (2020) A CNN-LSTM-based model to forecast stock prices. *Complexity* 2020:1–10
- Madziwa L, Pillalamarry M, Chatterjee S (2022) Gold price forecasting using multivariate stochastic model. *Resour Policy* 76:102544
- Mikolov T, Sutskever I, Chen K, Corrado G, Dean J (2013) Distributed representations of words and phrases and their compositionality
- Mohamed NA, Messaadia M (2023) Artificial intelligence techniques for the forecasting of crude oil price: a literature review. In: International conference on cyber measurement and engineering (CyMaEn), pp 340–343
- Murshed M, Tanha MM (2021) Oil price shocks and renewable energy transition: empirical evidence from net oil-importing South Asian economies. *Energy Ecol Environ* 6(3):183–203
- Orojo O, Tepper J, McGinnity TM, Mahmud M (2019) A multi-recurrent network for crude oil price prediction. In: IEEE symposium series on computational intelligence (SSCI)
- Pennington J, Socher R, Manning C (2014) Glove: global vectors for word representation. In: Proceedings of the 2014 conference on empirical methods in natural language processing (EMNLP), pp 1532–1543
- Periwal A (2023) The impact of crude oil price fluctuations on Indian economy. *Int J Res Appl Sci Eng Technol* 11(4):3173–3202
- Phan DHB, Sharma SS, Narayan PK (2016) Intraday volatility interaction between the crude oil and equity markets. *J Int Finan Markets Inst Money* 40:1–13
- Prokhorenkova L, Gusev G, Vorobev A, Dorogush AV, Gulin A (2018) CatBoost: unbiased boosting with categorical features. *Adv Neural Inf Process Syst* 31
- Pullen T, Benson K, Faff R (2014) A Comparative analysis of the investment characteristics of alternative gold assets. *Abacus* 50(1):76–92
- Qin Q, Huang Z, Zhou Z, Chen C, Liu R (2023) Crude oil price forecasting with machine learning and Google search data: an accuracy comparison of single-model versus multiple-model. *Eng Appl Artif Intell* 123:106266
- Qin Q, Xie K, He H, Li L, Chu X, Wei YM, Wu T (2019) An effective and robust decomposition-ensemble energy price forecasting paradigm with local linear prediction. *Energy Econ* 83:402–414
- Raza S, Schwartz B (2023) Entity and relation extraction from clinical case reports of COVID-19: a natural language processing approach. *BMC Med Inform Decis Mak* 23(1):20
- Reboredo JC (2013) Is gold a safe haven or a hedge for the US dollar? Implications for risk management. *J Bank Finance* 37(8):2665–2676
- Risse M (2019) Combining wavelet decomposition with machine learning to forecast gold returns. *Int J Forecast* 35(2):601–615
- Salisu AA, Ogbonna AE, Adewuyi A (2020) Google trends and the predictability of precious metals. *Resour Policy* 65
- Sarwar S, Shahbaz M, Anwar A, Tiwari AK (2019) The importance of oil assets for portfolio optimization: the analysis of firm level stocks. *Energy Econ* 78:217–234
- Siami-Namini S, Tavakoli N, Namin AS (2019) The Performance of LSTM and BiLSTM in forecasting time series. *IEEE Int Conf Big Data* 2019:3285–3292
- Sroka Ł (2022) Applying block bootstrap methods in silver prices forecasting. *Econometrics* 26(2):15–29
- Su M, Liu H, Yu C, Duan Z (2022) A new crude oil futures forecasting method based on fusing quadratic forecasting with residual forecasting. *Digital Signal Process* 130:103691
- Sun J, Zhao P, Sun S (2022) A new secondary decomposition-reconstruction-ensemble approach for crude oil price forecasting. *Resour Policy* 77:102762
- Swamy V, Lagesh MA (2023) Does happy Twitter forecast gold price? *Resour Policy* 81:103299
- Szarek D, Bielak Ł, Wyłomarska A (2020) Long-term prediction of the metals' prices using non-Gaussian time-inhomogeneous stochastic process. *Phys A Stat Mech Appl* 555
- Tang L, Zhang C, Li J, Li L, Wang S (2020) A multi-scale model for forecasting oil price with multi-factor search engine data. *Appl Energy* 257:114033
- Uzo-Peters A, Laniran T, Adenikinju A (2018) Brent prices and oil stock behaviors: evidence from Nigerian listed oil stocks. *Financ Innov* 4(1):8
- Vaswani A, Shazeer N, Parmar N, Uszkoreit J, Jones L, Gomez AN, Kaiser L, Polosukhin I (2017) Attention is all you need
- Vidal A, Kristjanpoller W (2020) Gold volatility prediction using a CNN-LSTM approach. *Expert Syst Appl* 157(1348):1
- Wang J, Athanasopoulos G, Hyndman RJ, Wang S (2018) Crude oil price forecasting based on internet concern using an extreme learning machine. *Int J Forecast* 34(4):665–677
- Wang J, Niu T, Du P, Yang W (2020) Ensemble probabilistic prediction approach for modeling uncertainty in crude oil price. *Appl Soft Comput J* 95:106509
- Wang L, Ma F, Niu T, Liang C (2021) The importance of extreme shock: examining the effect of investor sentiment on the crude oil futures market. *Energy Econ* 99:105319
- Xiuzhen X, Zheng W, Umair M (2022) Testing the fluctuations of oil resource price volatility: a hurdle for economic recovery. *SSRN Electron J*
- Xu D, Ruan C, Korpeoglu E, Kumar S, Achan K (2021) A Temporal kernel approach for deep learning with continuous-time information
- Xu D, Ruan C, Kumar S, Korpeoglu E, Achan K (2019) Self-attention with functional time representation learning
- Yan J, Mu L, Wang L, Ranjan R, Zomaya AY (2020) Temporal convolutional networks for the advance prediction of ENSO. *Sci Rep* 10(1):8055
- Yang M, Li X, Liu Y (2021) Sequence to point learning based on an attention neural network for nonintrusive load decomposition. *Electronics* 10(14):1657
- Yang M, Wang J (2022) Adaptability of financial time series prediction based on BiLSTM. *Procedia Comput Sci* 199:18–25
- Yang S, Chen D, Li S, Wang W (2020) Carbon price forecasting based on modified ensemble empirical mode decomposition and long short-term memory optimized by improved whale optimization algorithm. *Sci Total Environ* 716:137117
- Yu Y, Si X, Hu C, Zhang J (2019) A review of recurrent neural networks: LSTM cells and network architectures. *Neural Comput* 31(7):1235–1270
- Yuan Z (2023) Gold and bitcoin price prediction based on KNN, XGBoost and LightGBM model. *Highlights Sci Eng Technol* 39:720–725
- Zhang P, Ci B (2020) Deep belief network for gold price forecasting. *Resour Policy* 69:101806
- Zhang S, Chen Y, Zhang W, Feng R (2021) A novel ensemble deep learning model with dynamic error correction and multi-objective ensemble pruning for time series forecasting. *Inf Sci* 544:427–445
- Zhang Y, Wang J, Yu L, Wang S (2022a) An extreme bias-penalized forecast combination approach to commodity price forecasting. *Inf Sci* 615:774–793
- Zhang Z, He M, Zhang Y, Wang Y (2022b) Geopolitical risks and crude oil price predictability. *Energy* 258:124824
- Zhao L, Cheng L, Wan Y, Zhang H, Zhang Z (2015) A VAR-SVM model for crude oil price forecasting. *Int J Glob Energy Issues* 38(1/2/3):126
- Zhao LT, Wang Y, Guo SQ, Zeng GR (2018) A novel method based on numerical fitting for oil price trend forecasting. *Appl Energy* 220:154–163
- Zhao Y, Li J, Yu L (2017) A deep learning ensemble approach for crude oil price forecasting. *Energy Econ* 66:9–16
- Zhou S, Wu JN, Wu Y, Zhou X (2015) Exploiting local structures with the kronecker layer in convolutional networks
