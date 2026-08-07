"""
GDP Dashboard — Advanced Forecast & Slot Analytics Module
"""
import pandas as pd


def calculate_growth_rate(df: pd.DataFrame, col: str) -> float:
    if col not in df.columns or len(df[col]) < 2:
        return 0.0
    first = float(df[col].iloc[0])
    last = float(df[col].iloc[-1])
    if first == 0:
        return 0.0
    return round(((last - first) / first) * 100, 2)
