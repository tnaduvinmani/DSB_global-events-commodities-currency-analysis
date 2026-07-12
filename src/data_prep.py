"""
Data preparation utilities shared by notebook and Streamlit app.
All functions work on the raw CSVs in 01_Raw_Data/.
"""
from pathlib import Path
import numpy as np
import pandas as pd

DATA_DIR = Path(__file__).parent.parent / '01_Raw_Data'
EXTERNAL_DIR = Path(__file__).parent.parent / 'data' / 'external'
EXTERNAL_DIR.mkdir(parents=True, exist_ok=True)

# Known global events: {date_str: label}
EVENTS = {
    '1971-08': 'Nixon Shock',
    '1980-01': 'Hunt Silver Corner',
    '2008-09': 'GFC 2008',
    '2011-09': 'Gold ATH $1,900',
    '2020-03': 'COVID-19',
    '2022-02': 'Russia-Ukraine',
    '2026-01': 'Iran-Hormuz Crisis',
}


def load_monthly(filename: str, col: str) -> pd.DataFrame:
    """Load a monthly commodity CSV (Date, Value) and add log features."""
    df = pd.read_csv(DATA_DIR / filename)
    df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')
    df = df.rename(columns={'Value': col}).set_index('Date').sort_index()
    df.index = df.index.to_period('M').to_timestamp()
    df['log_p'] = np.log(df[col])
    df['ret'] = df['log_p'].diff()
    return df


def load_usdg() -> pd.DataFrame:
    """Load USDG daily data and add peg deviation + log market cap features."""
    df = pd.read_csv(DATA_DIR / 'USDG.csv', parse_dates=['Date'], index_col='Date')
    df = df[~df.index.duplicated(keep='first')].sort_index()
    df['peg_dev'] = df['Price_USD'] - 1.0
    df['log_mktcap'] = np.log(df['MarketCap_USD'])
    df['mktcap_ret'] = df['log_mktcap'].diff()
    return df


def time_split(df: pd.DataFrame, cutoff) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Split df into train (< cutoff) and test (>= cutoff) without shuffling."""
    return df[df.index < cutoff].copy(), df[df.index >= cutoff].copy()


def load_fred_monthly() -> pd.DataFrame | None:
    """
    Return cached FRED monthly data (VIX, DXY, TIPS).
    Returns None if cache file not found.
    Run the notebook cell 'cell-fred' to download and cache.
    """
    cache = EXTERNAL_DIR / 'fred_monthly.csv'
    if not cache.exists():
        return None
    return pd.read_csv(cache, index_col=0, parse_dates=True)
