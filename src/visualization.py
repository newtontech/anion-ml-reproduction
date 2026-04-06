"""Visualization utilities for reproducing paper figures."""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path


FIGURES_DIR = Path(__file__).resolve().parent.parent / "figures"


def save_fig(fig, name, dpi=300):
    """Save figure to figures/ directory."""
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    path = FIGURES_DIR / name
    fig.savefig(path, dpi=dpi, bbox_inches="tight")
    print(f"Saved: {path}")
    return path


def plot_correlation_matrix(corr, title="Feature Correlation Matrix", figsize=(12, 10)):
    """Plot correlation heatmap (reproduce Supplementary Fig. 30)."""
    fig, ax = plt.subplots(figsize=figsize)
    mask = np.triu(np.ones_like(corr, dtype=bool), k=1)
    sns.heatmap(
        corr, mask=mask, annot=True, fmt=".2f", cmap="coolwarm",
        center=0, square=True, linewidths=0.5, ax=ax,
        annot_kws={"size": 7},
    )
    ax.set_title(title)
    plt.tight_layout()
    return fig


def plot_roc_curves(results, title="ROC Curves"):
    """Plot ROC curves for all models."""
    fig, ax = plt.subplots(figsize=(7, 6))
    colors = ["#e74c3c", "#3498db", "#2ecc71", "#f39c12", "#9b59b6"]

    for (name, res), color in zip(results.items(), colors):
        ax.plot(res["fpr"], res["tpr"],
                label=f'{name} (AUC = {res["auc"]:.2f})',
                color=color, linewidth=2)

    ax.plot([0, 1], [0, 1], "k--", linewidth=1, alpha=0.5)
    ax.set_xlabel("False Positive Rate", fontsize=12)
    ax.set_ylabel("True Positive Rate", fontsize=12)
    ax.set_title(title, fontsize=14)
    ax.legend(loc="lower right", fontsize=10)
    ax.set_xlim([0, 1])
    ax.set_ylim([0, 1.02])
    plt.tight_layout()
    return fig


def plot_roc_with_cv(fpr_list, tpr_list, auc_mean, auc_std, title=None):
    """Plot mean ROC curve with +/-1 std band (paper's Fig. 2c style)."""
    mean_fpr = np.linspace(0, 1, 100)
    interp_tprs = [np.interp(mean_fpr, fpr, tpr) for fpr, tpr in zip(fpr_list, tpr_list)]
    mean_tpr = np.mean(interp_tprs, axis=0)
    std_tpr = np.std(interp_tprs, axis=0)

    fig, ax = plt.subplots(figsize=(6, 5))

    for fpr, tpr in zip(fpr_list, tpr_list):
        ax.plot(fpr, tpr, color="#3498db", alpha=0.15, linewidth=1)

    ax.plot(mean_fpr, mean_tpr, color="#e74c3c", linewidth=2,
            label=f"Mean ROC (AUC = {auc_mean:.2f} +/- {auc_std:.2f})")
    ax.fill_between(mean_fpr, mean_tpr - std_tpr, mean_tpr + std_tpr,
                    color="#e74c3c", alpha=0.15)
    ax.plot([0, 1], [0, 1], "k--", linewidth=1, alpha=0.5)

    ax.set_xlabel("False Positive Rate", fontsize=12)
    ax.set_ylabel("True Positive Rate", fontsize=12)
    if title:
        ax.set_title(title, fontsize=14)
    ax.legend(loc="lower right", fontsize=11)
    plt.tight_layout()
    return fig


def plot_feature_importance(importance_dict, title="Feature Importance"):
    """Plot feature importance bar chart from Random Forest."""
    sorted_items = sorted(importance_dict.items(), key=lambda x: x[1], reverse=True)
    features, values = zip(*sorted_items)

    fig, ax = plt.subplots(figsize=(8, 6))
    highlight = ["num_O", "TPSA", "HBA", "HOMO"]
    colors = ["#e74c3c" if f in highlight else "#3498db" for f in features]
    ax.barh(range(len(features)), values, color=colors)
    ax.set_yticks(range(len(features)))
    ax.set_yticklabels(features)
    ax.set_xlabel("Importance", fontsize=12)
    ax.set_title(title, fontsize=14)
    ax.invert_yaxis()
    plt.tight_layout()
    return fig


def plot_lr_coefficients(coef_dict, title="Logistic Regression Coefficients"):
    """Plot LR coefficients (reproduce Fig. 2c bottom panel)."""
    sorted_items = sorted(coef_dict.items(), key=lambda x: x[1])
    features, values = zip(*sorted_items)

    fig, ax = plt.subplots(figsize=(8, 6))
    colors = ["#e74c3c" if v > 0 else "#3498db" for v in values]
    ax.barh(range(len(features)), values, color=colors)
    ax.set_yticks(range(len(features)))
    ax.set_yticklabels(features)
    ax.set_xlabel("Coefficient", fontsize=12)
    ax.set_title(title, fontsize=14)
    ax.axvline(x=0, color="black", linewidth=0.8)
    plt.tight_layout()
    return fig


def plot_target_distribution(y, title="Binding Energy Distribution"):
    """Plot target variable distribution."""
    fig, ax = plt.subplots(figsize=(5, 4))
    labels = ["Low Eb (<=3 eV)", "High Eb (>3 eV)"]
    counts = [(y == 0).sum(), (y == 1).sum()]
    colors = ["#3498db", "#e74c3c"]
    ax.bar(labels, counts, color=colors)
    for i, c in enumerate(counts):
        ax.text(i, c + 2, str(c), ha="center", fontsize=12, fontweight="bold")
    ax.set_ylabel("Count", fontsize=12)
    ax.set_title(title, fontsize=14)
    plt.tight_layout()
    return fig
