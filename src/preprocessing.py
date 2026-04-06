"""Preprocessing: feature selection, correlation analysis, train/test split."""
import numpy as np
import pandas as pd
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.preprocessing import StandardScaler


# Features eliminated after round 1 (highly correlated)
DROPPED_FEATURES = ["MPI", "La"]

# Top 4 features identified after round 2
TOP4_FEATURES = ["num_O", "TPSA", "HBA", "HOMO"]


def get_feature_columns(df: pd.DataFrame, exclude_target: bool = True):
    """Return feature column names, optionally excluding the target."""
    cols = [c for c in df.columns if c != "Binding energy"]
    return cols


def compute_correlation_matrix(df: pd.DataFrame):
    """Compute Pearson correlation matrix for all features."""
    features = get_feature_columns(df)
    return df[features].corr()


def find_highly_correlated(corr: pd.DataFrame, threshold: float = 0.90):
    """Return pairs of features with |correlation| > threshold."""
    pairs = []
    cols = corr.columns
    for i in range(len(cols)):
        for j in range(i + 1, len(cols)):
            if abs(corr.iloc[i, j]) > threshold:
                pairs.append((cols[i], cols[j], corr.iloc[i, j]))
    return pairs


def preprocess_data(
    df: pd.DataFrame,
    drop_features: list[str] | None = None,
    select_features: list[str] | None = None,
):
    """Prepare feature matrix X and target vector y."""
    target = "Binding energy"
    y = df[target].values

    if select_features is not None:
        X = df[select_features].copy()
    else:
        features = get_feature_columns(df)
        if drop_features:
            features = [f for f in features if f not in drop_features]
        X = df[features].copy()

    return X, y


def split_data(X, y, test_size=0.15, random_state=42):
    """Stratified train/test split matching paper's 85%/15% protocol."""
    splitter = StratifiedShuffleSplit(
        n_splits=1, test_size=test_size, random_state=random_state
    )
    train_idx, test_idx = next(splitter.split(X, y))
    return (
        X.iloc[train_idx], X.iloc[test_idx],
        y[train_idx], y[test_idx],
    )


def standardize(X_train, X_test):
    """Standardize features to zero mean and unit variance."""
    scaler = StandardScaler()
    X_train_s = pd.DataFrame(
        scaler.fit_transform(X_train), columns=X_train.columns, index=X_train.index
    )
    X_test_s = pd.DataFrame(
        scaler.transform(X_test), columns=X_test.columns, index=X_test.index
    )
    return X_train_s, X_test_s, scaler
