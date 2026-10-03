from pathlib import Path
import pandas as pd


def load_sales(path: str | Path) -> pd.DataFrame:
    """Load the sales CSV and normalise column names."""
    df = pd.read_csv(path, encoding="latin-1")
    df.columns = [c.strip().lower().replace(" ", "_").replace("-", "_") for c in df.columns]
    df["order_date"] = pd.to_datetime(df["order_date"])
    return df