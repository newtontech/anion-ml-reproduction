#!/usr/bin/env python
# coding: utf-8

# # Round 1: ML Training with 17 Features
# 
# Train 5 classification models:
# 1. Random Forest
# 2. Gradient Boosting
# 3. XGBoost
# 4. Logistic Regression
# 5. Support Vector Classifier
# 
# Protocol: 85%/15% split, StratifiedShuffleSplit 10-fold CV

# In[1]:


import sys
sys.path.insert(0, '..')
import pickle
import numpy as np
import warnings
warnings.filterwarnings('ignore')

with open('../data/preprocessed_round1.pkl', 'rb') as f:
    data = pickle.load(f)

X_train, X_test = data['X_train_s'], data['X_test_s']
y_train, y_test = data['y_train'], data['y_test']
feature_names = data['feature_names']
print(f"Train: {X_train.shape}, Test: {X_test.shape}")


# In[2]:


from src.models import get_models, train_and_evaluate

models = get_models()
results_r1 = train_and_evaluate(X_train, X_test, y_train, y_test, models)

print("\n" + "=" * 65)
print(f"{'Model':<25} {'AUC':>8} {'Accuracy':>10}")
print("=" * 65)
for name, res in results_r1.items():
    print(f"{name:<25} {res['auc']:>8.4f} {res['accuracy']:>10.4f}")
print("=" * 65)


# In[3]:


# 10-fold CV for Random Forest
from src.models import cross_validate_model
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(n_estimators=100, random_state=42)
cv_r1 = cross_validate_model(data['X_train_s'], y_train, rf, n_splits=10)
print(f"Random Forest 10-fold CV (Round 1, 17 features):")
print(f"  AUC:      {cv_r1['auc_mean']:.4f} +/- {cv_r1['auc_std']:.4f}")
print(f"  Accuracy: {cv_r1['acc_mean']:.4f} +/- {cv_r1['acc_std']:.4f}")


# In[4]:


# Feature importance from Random Forest
from src.models import get_feature_importance
from src.visualization import plot_feature_importance, save_fig
import matplotlib.pyplot as plt

rf_model = results_r1['Random Forest']['model']
importance = get_feature_importance(rf_model, feature_names)
fig = plot_feature_importance(importance, title="Feature Importance (Round 1, Random Forest)")
save_fig(fig, "feature_importance_r1.png")
plt.show()

print("\nFeature importance ranking:")
for feat, imp in sorted(importance.items(), key=lambda x: x[1], reverse=True):
    print(f"  {feat:>10}: {imp:.4f}")


# In[5]:


# Save round 1 results
with open('../data/results_round1.pkl', 'wb') as f:
    pickle.dump({'results': results_r1, 'feature_names': feature_names, 'cv': cv_r1}, f)
print("Round 1 results saved.")

