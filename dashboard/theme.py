import streamlit as st
from pathlib import Path


THEME_PATH = Path(__file__).with_name("glass.css")


def _load_theme_css() -> str:
    css = THEME_PATH.read_text(encoding="utf-8")
    return f"<style>{css}</style>"


THEME_CSS = _load_theme_css()


def apply_dashboard_theme() -> None:
    st.markdown(THEME_CSS, unsafe_allow_html=True)


def safe_top_value(series: pd.Series, default: str = "No data available") -> str:
    cleaned = series.dropna()
    if cleaned.empty:
        return default
    return cleaned.value_counts().idxmax()


def safe_mode_value(series: pd.Series, default: str = "No data available") -> str:
    cleaned = series.dropna()
    if cleaned.empty:
        return default
    modes = cleaned.mode()
    if modes.empty:
        return default
    return modes.iloc[0]