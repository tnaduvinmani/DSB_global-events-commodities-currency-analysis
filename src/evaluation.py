"""
Forecast evaluation: RMSE, MAE, MAPE and Diebold-Mariano test.
"""
import numpy as np
from scipy import stats


def compute_metrics(actual, pred, in_log: bool = False) -> dict:
    """
    Compute RMSE, MAE, MAPE on price level.
    Set in_log=True when inputs are log-prices (auto-converts via exp).
    """
    a = np.exp(np.asarray(actual, float)) if in_log else np.asarray(actual, float)
    p = np.exp(np.asarray(pred,   float)) if in_log else np.asarray(pred,   float)
    rmse = float(np.sqrt(np.mean((a - p) ** 2)))
    mae  = float(np.mean(np.abs(a - p)))
    mape = float(np.mean(np.abs((a - p) / a)) * 100)
    return {'RMSE': round(rmse, 4), 'MAE': round(mae, 4), 'MAPE_%': round(mape, 4)}


def diebold_mariano(actual, pred1, pred2, loss: str = 'MSE') -> tuple[float, float]:
    """
    Diebold-Mariano test for equal predictive accuracy (two-sided).
    H0: pred1 and pred2 have equal forecast accuracy.
    Negative DM stat → pred1 is worse; positive → pred2 is worse.

    Parameters
    ----------
    actual, pred1, pred2 : array-like  (price level, not log)
    loss : 'MSE' | 'MAE'

    Returns
    -------
    (dm_statistic, p_value)
    """
    a, p1, p2 = map(lambda x: np.asarray(x, float), [actual, pred1, pred2])
    e1 = (a - p1) ** 2 if loss == 'MSE' else np.abs(a - p1)
    e2 = (a - p2) ** 2 if loss == 'MSE' else np.abs(a - p2)
    d = e1 - e2
    n = len(d)
    d_bar = d.mean()
    gamma0 = np.var(d, ddof=1)
    gamma1 = float(np.cov(d[1:], d[:-1])[0, 1]) if n > 2 else 0.0
    lrv = max(gamma0 + 2 * gamma1, 1e-12)
    dm_stat = d_bar / np.sqrt(lrv / n)
    p_val = 2 * (1 - stats.norm.cdf(abs(dm_stat)))
    return round(float(dm_stat), 4), round(float(p_val), 4)
