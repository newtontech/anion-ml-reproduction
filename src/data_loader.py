"""Data loading utilities for anion optimization ML reproduction."""
import pandas as pd
from pathlib import Path


DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def load_dataset(filename: str = "dataset.csv") -> pd.DataFrame:
    """Load the PH anion dataset.

    Returns a DataFrame with 267 rows × 20 columns (19 features + target).
    Target column is 'Binding energy' (1 = high Eb > 3 eV, 0 = low Eb <= 3 eV).
    """
    path = DATA_DIR / filename
    df = pd.read_csv(path)
    return df
