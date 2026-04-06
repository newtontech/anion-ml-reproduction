#!/usr/bin/env python
# coding: utf-8

# # Data Exploration
# 
# Reproducing the ML workflow from:
# > Xu, J. et al. Anion optimization for bifunctional surface passivation in perovskite solar cells. Nat. Mater. 22, 1507–1514 (2023).
# 
# This notebook loads and explores the 267 PH anion dataset with 19 features + binary target.

# In[1]:


import sys
sys.path.insert(0, '..')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from src.data_loader import load_dataset

df = load_dataset()
print(f"Dataset shape: {df.shape}")
print(f"Columns: {list(df.columns)}")
df.head(10)


# In[2]:


# Target distribution
print("=" * 50)
print("Target distribution (Binding energy)")
print("=" * 50)
print(df['Binding energy'].value_counts().sort_index())
print(f"\nHigh Eb (>3 eV): {(df['Binding energy']==1).sum()} ({(df['Binding energy']==1).mean()*100:.1f}%)")
print(f"Low Eb (<=3 eV):  {(df['Binding energy']==0).sum()} ({(df['Binding energy']==0).mean()*100:.1f}%)")


# In[3]:


# Summary statistics
df.describe().round(4)


# In[4]:


# Correlation matrix
from src.preprocessing import find_highly_correlated
from src.visualization import plot_correlation_matrix, save_fig

corr = df.drop(columns=['Binding energy']).corr()
fig = plot_correlation_matrix(corr, title="Feature Correlation Matrix (19 Features)")
save_fig(fig, "corr_matrix_all19.png")
plt.show()

# Find highly correlated pairs
high_corr = find_highly_correlated(corr, threshold=0.85)
print("\nHighly correlated pairs (|r| > 0.85):")
for f1, f2, r in high_corr:
    print(f"  {f1} <-> {f2}: r = {r:.4f}")


# In[5]:


# Feature distributions by class
fig, axes = plt.subplots(5, 4, figsize=(18, 18))
axes = axes.flatten()
features = [c for c in df.columns if c != 'Binding energy']

for i, feat in enumerate(features):
    ax = axes[i]
    for label, color, name in [(0, '#3498db', 'Low Eb'), (1, '#e74c3c', 'High Eb')]:
        subset = df[df['Binding energy'] == label][feat]
        ax.hist(subset, bins=15, alpha=0.6, color=color, label=name, density=True)
    ax.set_title(feat, fontsize=11)
    ax.legend(fontsize=7)

# Hide empty axes
for j in range(len(features), len(axes)):
    axes[j].set_visible(False)

plt.suptitle("Feature Distributions by Binding Energy Class", fontsize=14, fontweight='bold')
plt.tight_layout()
save_fig(fig, "feature_distributions.png")
plt.show()


# In[6]:


# Correlation with target
corr_target = df.corr()['Binding energy'].drop('Binding energy').sort_values(ascending=False)
print("Correlation with Binding Energy:")
print(corr_target.round(4))

fig, ax = plt.subplots(figsize=(8, 8))
colors = ['#e74c3c' if v > 0 else '#3498db' for v in corr_target.values]
ax.barh(range(len(corr_target)), corr_target.values, color=colors)
ax.set_yticks(range(len(corr_target)))
ax.set_yticklabels(corr_target.index)
ax.set_xlabel("Pearson Correlation with Binding Energy", fontsize=12)
ax.set_title("Feature-Target Correlation", fontsize=14)
ax.axvline(x=0, color='black', linewidth=0.8)
ax.invert_yaxis()
plt.tight_layout()
save_fig(fig, "feature_target_corr.png")
plt.show()

