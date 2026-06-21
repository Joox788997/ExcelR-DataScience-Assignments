# ExcelR Data Science Assignments — Complete Submission

## Overview

14 professional data science assignments completed, covering the full machine learning pipeline — from EDA and statistics through deep learning and deployment. Each assignment is organized in its own folder with a fully executed Jupyter notebook, README, and requirements file.

---

## Assignments

| # | Assignment | Folder | Dataset | Key Techniques |
|---|-----------|--------|---------|----------------|
| 1 | **Data Transformation** | `Data_Transformation/` | Adult Census (32,561 rows) | EDA, Missing values, Standard/MinMax Scaling, One-Hot & Label Encoding, Feature Engineering, Log Transform |
| 2 | **Multiple Linear Regression** | `Multiple_Linear_Regression/` | Toyota Corolla (1,436 rows) | 3 models (all/selected/interaction), Ridge (L2), Lasso (L1), Residual Analysis, Coefficient Interpretation |
| 3 | **Logistic Regression** | `Logistic_Regression/` | Pima Diabetes (768 rows) | Outlier Treatment, VIF, ROC Curve, Cross-Validation, **Streamlit app.py + model.pkl** |
| 4 | **Decision Tree** | `Decision_Tree/` | Heart Disease (908 rows) | GridSearchCV Tuning, Tree Visualization, Feature Importance, Learning Curve |
| 5 | **Random Forest** | `Random_Forest/` | Glass Classification (214 rows) | OOB Score, Bagging, AdaBoost, Gradient Boosting, Ensemble Comparison |
| 6 | **SVM** | `SVM/` | Drug Response (500 rows) | 4-Kernel Comparison (linear/poly/rbf/sigmoid), ROC Curve, Confusion Matrix |
| 7 | **PCA** | `PCA/` | Wine (178 rows) | Scree Plot, Explained Variance, 2D Visualization, Feature Loadings |
| 8 | **Neural Networks** | `Neural_Networks/` | Sonar Mines vs Rocks (208 rows) | MLPClassifier (60→24→12→6→2), Training Loss, ROC-AUC |
| 9 | **XGBoost & LightGBM** | `XGBoost_LightGBM/` | Pima Diabetes (768 rows) | XGBoost vs LightGBM, Feature Importance Comparison, Confusion Matrices |
| 10 | **Clustering** | `Clustering/` | Airlines Loyalty (3,999 rows) | K-Means (Elbow + Silhouette), DBSCAN, Hierarchical Dendrogram, Cluster Profiling |
| 11 | **Recommendation System** | `Recommendation_System/` | Anime (12,294 rows) | TF-IDF + Cosine Similarity, Threshold Tuning, Content-Based Filtering |
| 12 | **Time Series** | `Timeseries/` | USD/AUD Exchange Rate (7,588 days) | ARIMA(1,1,1), Exponential Smoothing, ADF Test, ACF/PACF |
| 13 | **Hypothesis Testing** | `Hypothesis_Testing/` | Bombay Hospitality (n=25) | One-Tailed t-Test, Formulas Shown, Confidence Interval, Business Interpretation |
| 14 | **RNN / LSTM / GRU** | `RNN/` | Milk Production (168 months) | SimpleRNN vs LSTM vs GRU, Training Curves, Time Series Forecasting |

---

## Special Deliverables

### Logistic Regression — Deployment Ready
- **`Logistic_Regression/model.pkl`** — Trained model with scaler and feature names
- **`Logistic_Regression/app.py`** — Streamlit web app for interactive diabetes prediction
- Run with: `cd Logistic_Regression && streamlit run app.py`

### Data Transformation — Validation Checklist
- **`Data_Transformation/validation_checklist.md`** — 24-point validation checklist confirming all requirements met

---

## Folder Structure

```
submissions/
├── Data_Transformation/
│   ├── Data_Transformation.ipynb
│   ├── README.md
│   ├── requirements.txt
│   └── validation_checklist.md
├── Multiple_Linear_Regression/
│   ├── Multiple_Linear_Regression.ipynb
│   ├── README.md
│   └── requirements.txt
├── Logistic_Regression/
│   ├── Logistic_Regression.ipynb
│   ├── README.md
│   ├── requirements.txt
│   ├── model.pkl
│   └── app.py
├── Decision_Tree/
│   ├── Decision_Tree.ipynb
│   ├── README.md
│   └── requirements.txt
├── Random_Forest/
│   ├── Random_Forest.ipynb
│   ├── README.md
│   └── requirements.txt
├── SVM/
│   ├── SVM.ipynb
│   ├── README.md
│   └── requirements.txt
├── PCA/
│   ├── PCA.ipynb
│   ├── README.md
│   └── requirements.txt
├── Neural_Networks/
│   ├── Neural_Networks.ipynb
│   ├── README.md
│   └── requirements.txt
├── XGBoost_LightGBM/
│   ├── XGBoost_LightGBM.ipynb
│   ├── README.md
│   └── requirements.txt
├── Clustering/
│   ├── Clustering.ipynb
│   ├── README.md
│   └── requirements.txt
├── Recommendation_System/
│   ├── Recommendation_System.ipynb
│   ├── README.md
│   └── requirements.txt
├── Timeseries/
│   ├── Timeseries.ipynb
│   ├── README.md
│   └── requirements.txt
├── Hypothesis_Testing/
│   ├── Hypothesis_Testing.ipynb
│   ├── README.md
│   └── requirements.txt
└── RNN/
    ├── RNN.ipynb
    ├── README.md
    └── requirements.txt
```

---

## Validation Summary

| Check | Result |
|-------|--------|
| Total notebooks | **14/14** |
| Total code cells executed | **185** |
| Execution errors | **0** |
| All outputs visible | ✅ |
| All charts displayed | ✅ |
| Markdown explanations | ✅ Every section |
| Interview questions answered | ✅ All answered |
| Blank sections | **None** |
| README per assignment | ✅ 14 |
| requirements.txt per assignment | ✅ 14 |
| Streamlit deployment | ✅ model.pkl + app.py |
| Notebooks NOT blank | ✅ All populated |

---

## How to Run

Each assignment is self-contained. Navigate to its folder and run:

```bash
cd submissions/<Assignment_Name>
pip install -r requirements.txt
jupyter notebook
```

For Streamlit deployment:

```bash
cd submissions/Logistic_Regression
pip install -r requirements.txt
streamlit run app.py
```

---

## Requirements Coverage

| Library | Assignments |
|---------|-------------|
| pandas, numpy | All 14 |
| matplotlib, seaborn | All 14 |
| scikit-learn | 1–9, 11–12, 14 |
| scipy | 10, 13 |
| statsmodels | 2, 3 |
| xgboost, lightgbm | 9 |
| tensorflow | 14 |
| streamlit | 3 |
| openpyxl | 1, 4 |
| python-docx | Used during build |

---

## Ready for ExcelR Submission ✅

All assignments meet the evaluation criteria:
- Notebooks fully executed with visible outputs
- Charts and plots displayed inline
- Markdown explanations before every section
- All interview questions answered completely
- No blank sections or placeholder code
- Zero execution errors across all notebooks
