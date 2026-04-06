"""ML model definitions and training/evaluation pipeline."""
import numpy as np
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.metrics import (
    roc_auc_score,
    accuracy_score,
    roc_curve,
    classification_report,
)
from xgboost import XGBClassifier


def get_models(random_state=42):
    """Return the 5 classification models used in the paper."""
    return {
        "Random Forest": RandomForestClassifier(
            n_estimators=100,
            max_depth=None,
            min_samples_split=2,
            min_samples_leaf=1,
            random_state=random_state,
        ),
        "Gradient Boosting": GradientBoostingClassifier(
            n_estimators=100,
            max_depth=3,
            learning_rate=0.1,
            random_state=random_state,
        ),
        "XGBoost": XGBClassifier(
            n_estimators=100,
            max_depth=3,
            learning_rate=0.1,
            use_label_encoder=False,
            eval_metric="logloss",
            random_state=random_state,
        ),
        "Logistic Regression": LogisticRegression(
            max_iter=1000,
            C=1.0,
            penalty="l2",
            random_state=random_state,
        ),
        "SVC": SVC(
            kernel="rbf",
            C=1.0,
            probability=True,
            random_state=random_state,
        ),
    }


def train_and_evaluate(X_train, X_test, y_train, y_test, models=None):
    """Train all models and return evaluation results.

    Returns dict with model_name -> {model, y_pred, y_prob, auc, accuracy, fpr, tpr}
    """
    if models is None:
        models = get_models()

    results = {}
    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        y_prob = model.predict_proba(X_test)[:, 1]

        auc = roc_auc_score(y_test, y_prob)
        acc = accuracy_score(y_test, y_pred)
        fpr, tpr, _ = roc_curve(y_test, y_prob)

        results[name] = {
            "model": model,
            "y_pred": y_pred,
            "y_prob": y_prob,
            "auc": auc,
            "accuracy": acc,
            "fpr": fpr,
            "tpr": tpr,
        }

    return results


def cross_validate_model(X, y, model, n_splits=10):
    """StratifiedShuffleSplit cross-validation matching paper protocol."""
    from sklearn.model_selection import StratifiedShuffleSplit

    splitter = StratifiedShuffleSplit(n_splits=n_splits, test_size=0.15, random_state=42)
    aucs = []
    accs = []

    for train_idx, test_idx in splitter.split(X, y):
        X_tr, X_te = X.iloc[train_idx], X.iloc[test_idx]
        y_tr, y_te = y[train_idx], y[test_idx]

        model.fit(X_tr, y_tr)
        y_prob = model.predict_proba(X_te)[:, 1]
        y_pred = model.predict(X_te)

        aucs.append(roc_auc_score(y_te, y_prob))
        accs.append(accuracy_score(y_te, y_pred))

    return {
        "auc_mean": np.mean(aucs),
        "auc_std": np.std(aucs),
        "acc_mean": np.mean(accs),
        "acc_std": np.std(accs),
        "aucs": aucs,
        "accs": accs,
    }


def get_feature_importance(model, feature_names):
    """Extract feature importance from tree-based models or LR coefficients."""
    if hasattr(model, "feature_importances_"):
        return dict(zip(feature_names, model.feature_importances_))
    elif hasattr(model, "coef_"):
        return dict(zip(feature_names, model.coef_[0]))
    return {}
