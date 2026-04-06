#!/usr/bin/env python
# coding: utf-8

# # Feature Engineering & Preprocessing
# 
# 1. Remove highly correlated features (MPI, La) based on correlation analysis
# 2. Split data 85%/15% using StratifiedShuffleSplit
# 3. Standardize features

# In[1]:


import sys
sys.path.insert(0, '..')
import numpy as np
import pandas as pd
import pickle

from src.data_loader import load_dataset
from src.preprocessing import (
    preprocess_data, split_data, standardize,
    DROPPED_FEATURES, TOP4_FEATURES
)

df = load_dataset()
print(f"Original features: {len(df.columns) - 1}")
print(f"Features to drop (highly correlated): {DROPPED_FEATURES}")
print(f"Top 4 features (paper): {TOP4_FEATURES}")


# In[2]:


# Round 1: Remove MPI and La
X, y = preprocess_data(df, drop_features=DROPPED_FEATURES)
print(f"\nFeatures after round 1: {X.shape[1]}")
print(f"Feature list: {list(X.columns)}")


# In[3]:


# Stratified train/test split (85/15)
X_train, X_test, y_train, y_test = split_data(X, y, test_size=0.15)
print(f"Train: {X_train.shape[0]} samples (high Eb: {(y_train==1).sum()}, low Eb: {(y_train==0).sum()})")
print(f"Test:  {X_test.shape[0]} samples (high Eb: {(y_test==1).sum()}, low Eb: {(y_test==0).sum()})")


# In[4]:


# Standardize
X_train_s, X_test_s, scaler = standardize(X_train, X_test)
print("Features standardized to zero mean, unit variance")


# In[5]:


# Save for subsequent notebooks
import os
os.makedirs('../data', exist_ok=True)

prep = {
    'X_train': X_train, 'X_test': X_test,
    'X_train_s': X_train_s, 'X_test_s': X_test_s,
    'y_train': y_train, 'y_test': y_test,
    'scaler': scaler, 'feature_names': list(X.columns),
}
with open('../data/preprocessed_round1.pkl', 'wb') as f:
    pickle.dump(prep, f)
print("Saved to data/preprocessed_round1.pkl")

