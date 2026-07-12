"""
ARIMA / ARIMAX and GARCH / EGARCH model helpers.
Used by both the notebook and the Streamlit app.
"""
import numpy as np
from scipy.stats import norm as _snorm
from statsmodels.tsa.arima.model import ARIMA
from arch import arch_model


# ── ARIMA ──────────────────────────────────────────────────────────────────

def select_arima_order(log_prices, p_max: int = 3, q_max: int = 3,
                       d: int = 1) -> tuple[int, int, int]:
    """Grid-search best ARIMA(p,d,q) order by AIC on training data."""
    best_aic, best_order = np.inf, (1, d, 1)
    for p in range(p_max + 1):
        for q in range(q_max + 1):
            if p == 0 and q == 0:
                continue
            try:
                res = ARIMA(log_prices, order=(p, d, q)).fit(
                    method_kwargs={'warn_convergence': False})
                if res.aic < best_aic:
                    best_aic, best_order = res.aic, (p, d, q)
            except Exception:
                pass
    return best_order


def arima_walk_forward(train_logp, test_logp_arr, order,
                       exog_train=None, exog_test=None) -> np.ndarray:
    """
    Walk-forward ARIMA: refit at every step, no data leakage.
    Returns array of log-price predictions aligned with test_logp_arr.
    Exog arrays must be 1-D and aligned with train/test rows.
    """
    history  = list(np.asarray(train_logp))
    exog_h   = list(exog_train) if exog_train is not None else None
    preds    = []

    for i, actual in enumerate(test_logp_arr):
        try:
            ea = np.array(exog_h).reshape(-1, 1) if exog_h  is not None else None
            en = np.array([[exog_test[i]]])       if exog_test is not None else None
            res = ARIMA(history, order=order, exog=ea).fit(
                method_kwargs={'warn_convergence': False})
            pred = res.forecast(steps=1, exog=en)[0]
        except Exception:
            pred = history[-1]   # fallback: naive
        preds.append(pred)
        history.append(actual)
        if exog_h is not None:
            exog_h.append(exog_test[i])

    return np.array(preds)


# ── GARCH ──────────────────────────────────────────────────────────────────

def fit_garch(ret_series, vol_model: str = 'GARCH', p: int = 1, q: int = 1):
    """
    Fit GARCH(p,q) or EGARCH(p,q) on log-return series.
    Input scaled to % internally for numerical stability.
    Returns fitted arch ModelResult.
    """
    ret_pct = np.asarray(ret_series.dropna()) * 100
    am = arch_model(ret_pct, vol=vol_model, p=p, q=q, dist='Normal', rescale=True)
    return am.fit(update_freq=0, disp='off')


def garch_volatility_cone(garch_result, current_price: float,
                          horizon: int = 12, ci: float = 0.95) -> dict:
    """
    Compute symmetric CI cone from GARCH variance forecast.
    Returns {'months': array, 'upper': array, 'lower': array}.
    """
    fcast = garch_result.forecast(horizon=horizon)
    vol_pct = np.sqrt(fcast.variance.iloc[-1].values)      # σ per period (%)
    cum_vol = np.sqrt(np.cumsum(vol_pct ** 2)) / 100       # cumulative σ in return space
    z = float(_snorm.ppf(1 - (1 - ci) / 2))
    upper = current_price * np.exp( z * cum_vol)
    lower = current_price * np.exp(-z * cum_vol)
    return {'months': np.arange(1, horizon + 1), 'upper': upper, 'lower': lower}
