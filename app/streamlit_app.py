"""
app/streamlit_app.py
Global Events, Commodities & Currency Markets — Interactive Dashboard
Run: streamlit run app/streamlit_app.py   (from project root)
"""
import sys
import json
import warnings
warnings.filterwarnings("ignore")
from pathlib import Path

import numpy as np
import pandas as pd
import plotly.graph_objects as go
from scipy.optimize import curve_fit
import streamlit as st

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
from data_prep import load_monthly, load_usdg, load_fred_monthly, EVENTS
from models.arima_garch import fit_garch, garch_volatility_cone
from evaluation import diebold_mariano

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Commodity & Currency Forecasting",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.title("Global Events, Commodities & Currency Markets")
st.caption(
    "DSB Forecasting Pipeline  |  "
    "Tier 1: ARIMA/GARCH  ·  Tier 2: RF/LightGBM/LSTM  ·  Tier 3: VECM/Markov/USDG"
)

# ── Data loading ──────────────────────────────────────────────────────────────
@st.cache_data
def load_all():
    return (
        load_monthly("gold100years.csv",   "Gold"),
        load_monthly("silver100years.csv", "Silver"),
        load_monthly("brentOil.csv",       "Brent"),
        load_usdg(),
    )


@st.cache_data
def load_results():
    out = ROOT / "04_Outputs"
    combined = {}
    for fname in ["tier1_results.json", "tier2_results.json", "tier3_results.json"]:
        p = out / fname
        if p.exists():
            with open(p, encoding="utf-8") as f:
                combined.update(json.load(f))
    return combined


gold, silver, brent, usdg = load_all()
results = load_results()
fred = load_fred_monthly()   # VIX / DXY / TIPS — None if cache missing

# ── Constants ─────────────────────────────────────────────────────────────────
ASSET_COLOR = {"Gold": "#e6a817", "Silver": "#9fa8a3", "Brent": "#c0392b"}
ASSET_UNIT  = {"Gold": "USD/oz",  "Silver": "USD/oz",  "Brent": "USD/bbl"}

T3_NAMES = {
    "T3_1_VECM_Gold":    "VECM (Gold)",
    "T3_2_Markov_Brent": "Markov Regime (Brent)",
    "T3_3_USDG":         "USDG Peg Analysis",
}


# ── GARCH volatility cone (cached, #1) ───────────────────────────────────────
@st.cache_data
def compute_garch_cone(col: str, months: int = 12):
    """Fit GARCH(1,1) on full price history and return the volatility cone arrays."""
    df_map = {"Gold": gold, "Silver": silver, "Brent": brent}
    df = df_map[col]
    current_price = float(np.exp(df["log_p"].iloc[-1]))
    try:
        res = fit_garch(df["ret"], vol_model="GARCH", p=1, q=1)
        return garch_volatility_cone(res, current_price, horizon=months)
    except Exception:
        return None


# ── Diebold-Mariano test results (cached, #2) ─────────────────────────────────
@st.cache_data
def compute_dm_results():
    """
    Run DM tests for each asset using saved walk-forward predictions.
    Compares every available model against the Naive random-walk baseline.
    Loads tier1_preds.json and tier2_preds.json (if present).
    """
    def _load(path):
        if Path(path).exists():
            with open(path, encoding="utf-8") as f:
                return json.load(f)
        return {}

    preds = {
        **_load(ROOT / "04_Outputs" / "tier1_preds.json"),
        **_load(ROOT / "04_Outputs" / "tier2_preds.json"),
    }
    if not preds:
        return {}

    out = {}
    for asset, df in [("Gold", gold), ("Silver", silver), ("Brent", brent)]:
        naive_k = f"Naive_{asset}"
        if naive_k not in preds:
            continue
        naive_arr = np.array(preds[naive_k])
        n = len(naive_arr)
        actual_p = np.exp(df["log_p"].iloc[-n:].values)
        cutoff   = df.index[-n]

        comparisons = []
        candidates = ["ARIMA", "RF", "LightGBM", "LSTM", "BiGRU"]
        for model in candidates:
            key = f"{model}_{asset}"
            if key not in preds:
                continue
            model_arr = np.array(preds[key])
            n_m = len(model_arr)
            actual_m = np.exp(df["log_p"].iloc[-n_m:].values)
            naive_m  = np.exp(np.array(preds[naive_k])[-n_m:])
            dm_stat, dm_p = diebold_mariano(actual_m, naive_m, np.exp(model_arr))
            comparisons.append({
                "model":  model,
                "stat":   dm_stat,
                "p":      dm_p,
                "n":      n_m,
                "cutoff": cutoff,
            })
        if comparisons:
            out[asset] = comparisons
    return out


dm_tests = compute_dm_results()


# ── Helpers ───────────────────────────────────────────────────────────────────
def event_decorations(df):
    """Return Plotly shapes + annotations for global events within df's date range."""
    shapes, annots = [], []
    for ds, lbl in EVENTS.items():
        ts = pd.Timestamp(ds)
        if df.index[0] <= ts <= df.index[-1]:
            shapes.append(dict(
                type="line", xref="x", yref="paper",
                x0=ts, x1=ts, y0=0, y1=1,
                line=dict(color="rgba(130,130,130,0.35)", width=1, dash="dot"),
                layer="below",
            ))
            annots.append(dict(
                x=ts, y=0.97, xref="x", yref="paper",
                text=lbl, textangle=-90, showarrow=False,
                font=dict(size=8.5, color="#999"),
                xanchor="right", yanchor="top",
            ))
    return shapes, annots


def render_event_legend(start_year=None, end_year=None):
    """Render a compact table of global events visible in the current chart range."""
    rows = []
    for ds, lbl in EVENTS.items():
        ts = pd.Timestamp(ds)
        if start_year and ts.year < start_year:
            continue
        if end_year and ts.year > end_year:
            continue
        rows.append({"Date": ts.strftime("%b %Y"), "Event": lbl})
    if not rows:
        return
    tbl = pd.DataFrame(rows)
    with st.expander("Events on chart", expanded=False):
        st.dataframe(tbl, hide_index=True, use_container_width=True)


def naive_forecast(df, col, months=12):
    """Naive random-walk forecast: last price + drift."""
    log_ret = df["ret"].dropna()
    last_lp = df["log_p"].iloc[-1]
    mu  = log_ret.tail(60).mean()
    sig = log_ret.tail(60).std()
    t   = np.arange(1, months + 1)
    idx = pd.date_range(df.index[-1], periods=months + 1, freq="MS")[1:]
    return (
        idx,
        np.exp(last_lp + mu * t),
        np.exp(last_lp + mu * t + 1.96 * sig * np.sqrt(t)),
        np.exp(last_lp + mu * t - 1.96 * sig * np.sqrt(t)),
    )


def build_metrics_table(asset):
    """
    Build a sorted DataFrame of RMSE/MAE/MAPE for one asset,
    combining Tier 1, 2, and 3 results.
    """
    rows = []
    for key, val in results.items():
        if not isinstance(val, dict):
            continue
        asset_match = (
            val.get("Asset", "").lower() == asset.lower()
            or asset.lower() in key.lower()
        )
        if not asset_match:
            continue
        mape = val.get("MAPE_%", val.get("MAPE", None))
        if mape is None:   # regime/diagnostic models (Markov, USDG) — skip
            continue
        rows.append({
            "Model":  T3_NAMES.get(key, val.get("Model", key)),
            "RMSE":   round(val["RMSE"], 2) if "RMSE" in val else None,
            "MAE":    round(val["MAE"],  2) if "MAE"  in val else None,
            "MAPE%":  round(mape, 2)        if mape is not None else None,
        })
    if not rows:
        return None
    tbl = pd.DataFrame(rows)
    for c in ["RMSE", "MAE", "MAPE%"]:
        tbl[c] = pd.to_numeric(tbl[c], errors="coerce")
    try:
        tbl = tbl.sort_values("MAPE%").reset_index(drop=True)
    except Exception:
        pass
    return tbl


def render_dm_note(asset: str):
    """Display Diebold-Mariano test results (each model vs Naive) for the given asset."""
    comparisons = dm_tests.get(asset)
    if not comparisons:
        return
    cutoff_str = comparisons[0]["cutoff"].strftime("%b %Y")
    rows = []
    for c in comparisons:
        sign = "+" if c["stat"] > 0 else ""
        sig  = c["p"] < 0.05
        rows.append({
            "Model vs Naive": c["model"],
            "DM stat":        f"{sign}{c['stat']:.3f}",
            "p-value":        f"{c['p']:.3f}",
            "Significant?":   "Yes ✓" if sig else "No",
        })
    with st.expander(
        f"Diebold-Mariano Tests vs Naive (n = {comparisons[0]['n']} months, cutoff: {cutoff_str})",
        expanded=True,
    ):
        st.dataframe(pd.DataFrame(rows), hide_index=True, use_container_width=True)
        st.caption(
            "DM stat > 0 → model is more accurate than Naive. "
            "p < 0.05 → difference is statistically significant."
        )


# ── Animated price chart (#1 — GARCH cone) ───────────────────────────────────
def make_animated_chart(df, col, step_years=5, fc_months=12,
                        show_controls=True, garch_cone=None):
    """
    Plotly figure with frame-based animation (yearly steps).
    Final frame shows naive random-walk point forecast with a GARCH(1,1)
    heteroskedastic 95% CI when garch_cone is supplied; falls back to i.i.d. CI.
    """
    color  = ASSET_COLOR.get(col, "#3498db")
    unit   = ASSET_UNIT.get(col, "")
    shapes, annots = event_decorations(df)
    fc_idx, fc_price, ci_up_naive, ci_lo_naive = naive_forecast(df, col, fc_months)

    if garch_cone is not None:
        ci_up    = garch_cone["upper"]
        ci_lo    = garch_cone["lower"]
        ci_label = "95% CI — GARCH(1,1)"
    else:
        ci_up    = ci_up_naive
        ci_lo    = ci_lo_naive
        ci_label = "95% CI — i.i.d."

    years       = sorted(df.index.year.unique())
    frame_years = sorted(set(
        list(range(years[0], years[-1] + 1, step_years)) + [years[-1]]
    ))

    def build_traces(up_to_year, add_forecast=False):
        sub = df[df.index.year <= up_to_year]
        traces = [go.Scatter(
            x=sub.index, y=sub[col], mode="lines",
            line=dict(color=color, width=1.5), name=col,
        )]
        if add_forecast:
            traces.append(go.Scatter(
                x=fc_idx, y=fc_price, mode="lines",
                line=dict(color=color, width=2.5, dash="dash"),
                name="Naive 12-mo forecast",
            ))
            traces.append(go.Scatter(
                x=list(fc_idx) + list(fc_idx[::-1]),
                y=list(ci_up)  + list(ci_lo[::-1]),
                fill="toself", fillcolor=color, opacity=0.10,
                line=dict(width=0), name=ci_label,
            ))
        return traces

    frames = [
        go.Frame(
            data=build_traces(yr, add_forecast=(yr == frame_years[-1])),
            name=str(yr),
        )
        for yr in frame_years
    ]

    slider_steps = [
        dict(
            args=[[str(yr)],
                  {"frame": {"duration": 60, "redraw": True}, "mode": "immediate"}],
            label=str(yr), method="animate",
        )
        for yr in frame_years
    ]

    layout_extra = {}
    if show_controls:
        layout_extra["updatemenus"] = [dict(
            type="buttons", showactive=False,
            x=0.0, y=-0.20, xanchor="left",
            buttons=[
                dict(
                    label="Play",
                    method="animate",
                    args=[None, {
                        "frame": {"duration": 60, "redraw": True},
                        "fromcurrent": False,
                        "transition": {"duration": 0},
                    }],
                ),
                dict(
                    label="Pause",
                    method="animate",
                    args=[[None], {"frame": {"duration": 0}, "mode": "immediate"}],
                ),
            ],
        )]

    fig = go.Figure(
        data=build_traces(frame_years[-1], add_forecast=True),
        frames=frames,
    )
    fig.update_layout(
        height=430,
        yaxis_title=unit,
        shapes=shapes,
        annotations=annots,
        margin=dict(l=60, r=20, t=30, b=70),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, x=0),
        hovermode="x unified",
        sliders=[dict(
            active=len(frame_years) - 1,
            currentvalue=dict(prefix="Year: ", font=dict(size=12)),
            pad=dict(b=10, t=50),
            steps=slider_steps,
        )],
        **layout_extra,
    )
    return fig


def make_static_comparison(base_year):
    """
    Static normalised comparison chart: Gold/Silver/Brent indexed to base_year=100.
    Shows the full series at once with event markers.
    """
    datasets = [(gold, "Gold"), (silver, "Silver"), (brent, "Brent")]
    shapes, annots = event_decorations(gold[gold.index.year >= base_year])

    fig = go.Figure()
    for df, col in datasets:
        sub = df[df.index.year >= base_year]
        if len(sub) == 0:
            continue
        base_val = sub[col].iloc[0]
        indexed  = (sub[col] / base_val) * 100.0
        fig.add_trace(go.Scatter(
            x=sub.index, y=indexed.values, mode="lines", name=col,
            line=dict(color=ASSET_COLOR[col], width=2),
        ))

    fig.update_layout(
        height=500,
        yaxis_title="Indexed (base year = 100)",
        shapes=shapes,
        annotations=annots,
        margin=dict(l=60, r=20, t=30, b=40),
        legend=dict(orientation="h", yanchor="bottom", y=1.02),
        hovermode="x unified",
    )
    return fig


# ── Dual-axis chart helper (Macro Context) ────────────────────────────────────
def make_dual_axis(commodity_df, commodity_col, macro_series, macro_name,
                   macro_color="#555", start_year=1990):
    """
    Dual-axis Plotly chart: commodity price (left) vs macro variable (right).
    Both series clipped to their common date range starting from start_year.
    """
    comm  = commodity_df[commodity_df.index.year >= start_year][commodity_col]
    macro = macro_series.dropna()
    macro = macro[macro.index.year >= start_year]

    # Align to common range
    start = max(comm.index[0], macro.index[0])
    end   = min(comm.index[-1], macro.index[-1])
    comm  = comm[(comm.index >= start) & (comm.index <= end)]
    macro = macro[(macro.index >= start) & (macro.index <= end)]

    shapes, annots = event_decorations(commodity_df[commodity_df.index >= start])

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=comm.index, y=comm.values, name=commodity_col,
        line=dict(color=ASSET_COLOR.get(commodity_col, "#3498db"), width=1.8),
        yaxis="y1",
    ))
    fig.add_trace(go.Scatter(
        x=macro.index, y=macro.values, name=macro_name,
        line=dict(color=macro_color, width=1.5, dash="dot"),
        yaxis="y2",
    ))
    fig.update_layout(
        height=350,
        shapes=shapes,
        annotations=annots,
        margin=dict(l=60, r=60, t=30, b=40),
        hovermode="x unified",
        legend=dict(orientation="h", yanchor="bottom", y=1.02),
        yaxis=dict(
            title=ASSET_UNIT.get(commodity_col, ""),
            titlefont=dict(color=ASSET_COLOR.get(commodity_col, "#3498db")),
            tickfont=dict(color=ASSET_COLOR.get(commodity_col, "#3498db")),
        ),
        yaxis2=dict(
            title=macro_name,
            titlefont=dict(color=macro_color),
            tickfont=dict(color=macro_color),
            overlaying="y", side="right",
        ),
    )
    return fig


# ── Tabs ──────────────────────────────────────────────────────────────────────
tab_gold, tab_silver, tab_brent, tab_usdg, tab_compare, tab_macro = st.tabs([
    "Gold", "Silver", "Brent Oil", "USDG", "Comparison", "Macro Context",
])

# ─────────────────────────────────────────────────────────────────────────────
# Gold tab
# ─────────────────────────────────────────────────────────────────────────────
with tab_gold:
    st.subheader("Gold — 100-Year Price History + Forecast")
    ctrl, _ = st.columns([1, 3])
    with ctrl:
        gold_start = st.slider("Start year", 1915, 2015, 2000, step=5, key="gold_start")

    gold_cone = compute_garch_cone("Gold")
    st.plotly_chart(
        make_animated_chart(
            gold[gold.index.year >= gold_start], "Gold",
            step_years=5, show_controls=False, garch_cone=gold_cone,
        ),
        use_container_width=True,
    )
    render_event_legend(start_year=gold_start)
    col_l, col_r = st.columns([3, 2])
    with col_l:
        tbl = build_metrics_table("Gold")
        if tbl is not None:
            dm = dm_tests.get("Gold")
            period_note = (
                f"last {dm[0]['n']} months, cutoff {dm[0]['cutoff'].strftime('%b %Y')}"
                if dm else "test period unknown"
            )
            st.markdown(f"**Model comparison — Gold** (sorted by MAPE · {period_note})")
            st.dataframe(tbl, use_container_width=True, hide_index=True)
        render_dm_note("Gold")
    with col_r:
        vecm_mape = results.get("T3_1_VECM_Gold", {}).get("MAPE", None)
        if vecm_mape:
            st.info(
                "**T3.1 VECM:** Gold–Silver cointegration (Johansen rank = 1). "
                "Walk-forward VECM MAPE = **{:.2f}%**".format(vecm_mape)
            )
        arima_mape = results.get("ARIMA_Gold", {}).get("MAPE_%", None)
        if arima_mape:
            st.success(
                "**Best model:** ARIMA(1,1,2) — MAPE = **{:.2f}%**".format(arima_mape)
            )
        ci_note = "GARCH(1,1) heteroskedastic" if gold_cone else "i.i.d. Gaussian (GARCH unavailable)"
        st.caption(f"Forecast band: {ci_note} 95% CI.")

# ─────────────────────────────────────────────────────────────────────────────
# Silver tab
# ─────────────────────────────────────────────────────────────────────────────
with tab_silver:
    st.subheader("Silver — 100-Year Price History + Forecast")
    ctrl, _ = st.columns([1, 3])
    with ctrl:
        silver_start = st.slider("Start year", 1915, 2015, 2000, step=5, key="silver_start")

    silver_cone = compute_garch_cone("Silver")
    st.plotly_chart(
        make_animated_chart(
            silver[silver.index.year >= silver_start], "Silver",
            step_years=5, show_controls=False, garch_cone=silver_cone,
        ),
        use_container_width=True,
    )
    render_event_legend(start_year=silver_start)
    tbl = build_metrics_table("Silver")
    if tbl is not None:
        dm = dm_tests.get("Silver")
        period_note = (
            f"last {dm[0]['n']} months, cutoff {dm[0]['cutoff'].strftime('%b %Y')}"
            if dm else "test period unknown"
        )
        st.markdown(f"**Model comparison — Silver** (sorted by MAPE · {period_note})")
        st.dataframe(tbl, use_container_width=True, hide_index=True)
    render_dm_note("Silver")

# ─────────────────────────────────────────────────────────────────────────────
# Brent tab
# ─────────────────────────────────────────────────────────────────────────────
with tab_brent:
    st.subheader("Brent Crude — Price History + Forecast")
    ctrl, _ = st.columns([1, 3])
    with ctrl:
        brent_start = st.slider("Start year", 1946, 2015, 2000, step=5, key="brent_start")

    brent_cone = compute_garch_cone("Brent")
    st.plotly_chart(
        make_animated_chart(
            brent[brent.index.year >= brent_start], "Brent",
            step_years=5, show_controls=False, garch_cone=brent_cone,
        ),
        use_container_width=True,
    )
    render_event_legend(start_year=brent_start)
    col_l, col_r = st.columns([3, 2])
    with col_l:
        tbl = build_metrics_table("Brent")
        if tbl is not None:
            dm = dm_tests.get("Brent")
            period_note = (
                f"last {dm[0]['n']} months, cutoff {dm[0]['cutoff'].strftime('%b %Y')}"
                if dm else "test period unknown"
            )
            st.markdown(f"**Model comparison — Brent** (sorted by MAPE · {period_note})")
            st.dataframe(tbl, use_container_width=True, hide_index=True)
        render_dm_note("Brent")
    with col_r:
        markov = results.get("T3_2_Markov_Brent", {})
        if markov:
            st.info(
                "**T3.2 Markov Regime-Switching (Hamilton 1989)**  \n"
                "2 regimes · switching variance  \n"
                "AIC = {:.0f}  |  BIC = {:.0f}  \n"
                "Stress = Regime {}  (σ² ≈ 680× higher than calm)".format(
                    markov.get("AIC", 0), markov.get("BIC", 0),
                    markov.get("stress_regime_idx", "?"),
                )
            )

# ─────────────────────────────────────────────────────────────────────────────
# USDG tab (#3 — logistic ±1σ uncertainty band)
# ─────────────────────────────────────────────────────────────────────────────
with tab_usdg:
    st.subheader("USDG Stablecoin — Adoption & Peg Stability")

    usdg_m = usdg.resample("MS").agg(
        Price_USD  =("Price_USD",    "mean"),
        MarketCap  =("MarketCap_USD","last"),
        peg_dev    =("peg_dev",      "mean"),
    ).dropna()

    col_l, col_r = st.columns(2)

    # ── MarketCap + logistic projection ──────────────────────────────────────
    with col_l:
        mktcap = usdg_m["MarketCap"].dropna()
        t_num  = np.arange(len(mktcap), dtype=float)

        def logistic(t, K, r, t0):
            return K / (1.0 + np.exp(-r * (t - t0)))

        fit_ok = False
        popt = pcov = None
        try:
            popt, pcov = curve_fit(
                logistic, t_num, mktcap.values,
                p0=[mktcap.max() * 3.0, 0.08, len(mktcap) / 2.0],
                maxfev=15000,
            )
            fit_ok = True
        except Exception:
            pass

        fig_mc = go.Figure()
        fig_mc.add_trace(go.Scatter(
            x=mktcap.index, y=mktcap.values / 1e9,
            mode="lines+markers", name="Actual MarketCap",
            line=dict(color="steelblue", width=2),
            marker=dict(size=5),
        ))
        if fit_ok:
            t_proj     = np.arange(len(mktcap) + 24, dtype=float)
            proj_dates = pd.date_range(mktcap.index[0], periods=len(t_proj), freq="MS")
            mc_proj    = logistic(t_proj, *popt)
            K_val      = popt[0]
            K_std      = float(np.sqrt(pcov[0, 0]))

            fig_mc.add_trace(go.Scatter(
                x=proj_dates, y=mc_proj / 1e9,
                mode="lines", name="Logistic S-curve",
                line=dict(color="darkorange", width=2, dash="dash"),
            ))
            # ±1σ uncertainty band on saturation cap K
            mc_hi = logistic(t_proj, K_val + K_std, popt[1], popt[2])
            mc_lo = logistic(t_proj, K_val - K_std, popt[1], popt[2])
            fig_mc.add_trace(go.Scatter(
                x=list(proj_dates) + list(proj_dates[::-1]),
                y=list(mc_hi / 1e9) + list(mc_lo[::-1] / 1e9),
                fill="toself", fillcolor="darkorange", opacity=0.12,
                line=dict(width=0),
                name=f"±1σ_K uncertainty (σ_K = ${K_std/1e9:.1f}B)",
            ))
            fig_mc.add_hline(
                y=K_val / 1e9,
                line_dash="dot", line_color="green",
                annotation_text="K = ${:.1f}B ± {:.1f}B".format(K_val / 1e9, K_std / 1e9),
                annotation_position="bottom right",
            )

        last_date = mktcap.index[-1]
        fig_mc.add_shape(
            type="line", xref="x", yref="paper",
            x0=last_date, x1=last_date, y0=0, y1=1,
            line=dict(color="gray", width=1, dash="dot"),
        )
        fig_mc.add_annotation(
            x=last_date, y=0.94, xref="x", yref="paper",
            text="Last data", showarrow=False,
            font=dict(size=9, color="gray"), xanchor="left",
        )
        fig_mc.update_layout(
            height=320,
            title="USDG Market Cap + 24-Month Logistic Projection",
            yaxis_title="USD Billions",
            margin=dict(l=60, r=20, t=40, b=40),
            legend=dict(orientation="h", yanchor="bottom", y=1.02),
        )
        st.plotly_chart(fig_mc, use_container_width=True)
        if fit_ok:
            st.caption(
                f"Logistic fit on {len(mktcap)} months of data. "
                f"Shaded band = ±1σ parameter uncertainty on saturation cap K "
                f"(derived from curve_fit covariance matrix). "
                f"Short time series makes K highly uncertain — treat projection as indicative only."
            )

    # ── Peg deviation ─────────────────────────────────────────────────────────
    with col_r:
        dev     = usdg_m["peg_dev"]
        dev_std = dev.std()

        fig_peg = go.Figure()
        fig_peg.add_trace(go.Scatter(
            x=dev.index, y=dev.values,
            mode="lines", name="Peg deviation",
            line=dict(color="steelblue", width=1.5),
        ))
        fig_peg.add_hline(y=0, line_color="black", line_width=0.8)
        fig_peg.add_hrect(
            y0=-dev_std, y1=dev_std,
            fillcolor="steelblue", opacity=0.08, line_width=0,
            annotation_text="±1σ = {:.5f}".format(dev_std),
            annotation_position="top right",
        )

        usdg_r = results.get("T3_3_USDG", {})
        p_val  = usdg_r.get("peg_dev_adf_p", None)
        title_suffix = ""
        if p_val is not None:
            verdict = "stationary" if p_val < 0.05 else "non-stationary (short sample)"
            title_suffix = "  |  ADF p={:.3f} ({})".format(p_val, verdict)

        fig_peg.update_layout(
            height=320,
            title="Peg Deviation (Price − $1.00)" + title_suffix,
            yaxis_title="Deviation ($)",
            margin=dict(l=60, r=20, t=40, b=40),
        )
        st.plotly_chart(fig_peg, use_container_width=True)

    # ── SWIFT context ──────────────────────────────────────────────────────────
    swift_mean = results.get("T3_3_USDG", {}).get("swift_usd_mean_pct", None)
    if swift_mean:
        st.info(
            "**SWIFT Context (Ahmed & Aldasoro, BIS WP 1270, 2025):** "
            "USD holds **{:.1f}%** of global SWIFT payments (Dec 2025 – Mar 2026). "
            "USDG growth represents *digitalisation* of existing USD dominance, not a "
            "competing currency — de-dollarisation risk from stablecoins remains limited.".format(
                swift_mean)
        )

# ─────────────────────────────────────────────────────────────────────────────
# Comparison tab
# ─────────────────────────────────────────────────────────────────────────────
with tab_compare:
    st.subheader("Normalised Asset Comparison")

    ctrl, _ = st.columns([1, 3])
    with ctrl:
        base_year = st.slider("Base year (index = 100)", 1970, 2022, 2000, step=5,
                              key="cmp_base")

    st.plotly_chart(
        make_static_comparison(base_year),
        use_container_width=True,
    )
    render_event_legend(start_year=base_year)
    st.caption("USDG excluded — data available from April 2025 only.")

# ─────────────────────────────────────────────────────────────────────────────
# Macro Context tab
# ─────────────────────────────────────────────────────────────────────────────
with tab_macro:
    st.subheader("Macro Context — FRED Variables vs Commodity Prices")

    if fred is None:
        st.warning(
            "FRED cache not found. Run the notebook cell **'cell-fred'** to download "
            "VIX, DXY, and TIPS data, then restart the app."
        )
    else:
        macro_start = st.slider(
            "Start year", 1990, 2015, 2000, step=5, key="macro_start"
        )

        st.markdown("#### Gold")
        mc1, mc2 = st.columns(2)
        with mc1:
            if "dxy" in fred.columns:
                st.markdown("**Gold vs DXY** (Dollar Index) — expected inverse relationship")
                st.plotly_chart(
                    make_dual_axis(gold, "Gold", fred["dxy"], "DXY",
                                   macro_color="#2c7bb6", start_year=macro_start),
                    use_container_width=True,
                )
        with mc2:
            if "tips" in fred.columns:
                st.markdown("**Gold vs TIPS Real Yield** — higher real yield raises opportunity cost of holding gold")
                st.plotly_chart(
                    make_dual_axis(gold, "Gold", fred["tips"], "TIPS Yield (%)",
                                   macro_color="#d7191c", start_year=macro_start),
                    use_container_width=True,
                )

        st.markdown("#### Silver & Brent")
        mc3, mc4 = st.columns(2)
        with mc3:
            if "dxy" in fred.columns:
                st.markdown("**Silver vs DXY** — similar USD-driven inverse relationship")
                st.plotly_chart(
                    make_dual_axis(silver, "Silver", fred["dxy"], "DXY",
                                   macro_color="#2c7bb6", start_year=macro_start),
                    use_container_width=True,
                )
        with mc4:
            if "vix" in fred.columns:
                st.markdown("**Brent vs VIX** — risk-off spikes (VIX↑) often compress demand expectations")
                st.plotly_chart(
                    make_dual_axis(brent, "Brent", fred["vix"], "VIX",
                                   macro_color="#756bb1", start_year=macro_start),
                    use_container_width=True,
                )

        render_event_legend(start_year=macro_start)
        st.caption(
            "Dotted line = FRED macro variable (right axis). "
            "Solid line = commodity price (left axis). "
            "Source: FRED (VIX via CBOE, DXY via ICE, TIPS via US Treasury)."
        )

# ── Footer ─────────────────────────────────────────────────────────────────────
st.divider()
st.caption(
    "All forecasts are statistical model outputs — not financial or investment advice.  "
    "Data: Macrotrends (Gold/Silver/Brent), CoinGecko (USDG), SWIFT RMB Tracker, FRED."
)
