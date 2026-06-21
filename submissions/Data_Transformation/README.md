# Data Transformation Assignment

## Data Preprocessing and Feature Engineering

### Objective
To develop practical skills in data preprocessing, feature engineering, and feature selection using the Adult (Census Income) dataset. Predict whether income exceeds $50K/yr based on census data.

### Dataset
- **Source:** Adult Census Income Dataset (UCI ML Repository)
- **Records:** 32,561
- **Features:** 15 (age, workclass, fnlwgt, education, education_num, marital_status, occupation, relationship, race, sex, capital_gain, capital_loss, hours_per_week, native_country)
- **Target:** income (<=50K / >50K)

### Tasks Completed

1. **Data Loading & Exploration**
   - Loaded dataset with pandas
   - Summary statistics, data types, missing values analysis

2. **Missing Values Treatment**
   - Identified '?' placeholders as missing values in workclass, occupation, native_country
   - Applied mode imputation (best practice for categorical data with <6% missing)

3. **Scaling Techniques**
   - Standard Scaling (Z-score): mean=0, std=1
   - Min-Max Scaling: range [0, 1]
   - Discussed when to use each technique

4. **Encoding Techniques**
   - One-Hot Encoding: sex (2 categories)
   - Label Encoding: workclass, education, marital_status, occupation, relationship, race, native_country
   - Discussed pros and cons of each approach

5. **Feature Engineering**
   - capital_net: capital_gain - capital_loss
   - age_hours_interaction: age * hours_per_week
   - has_capital_gain: binary flag
   - is_full_time: binary flag

6. **Log Transformation**
   - Applied log1p transform to capital_gain (skewness reduced from 11.95 → improved)

7. **Visualizations**
   - Histograms of numerical features
   - Scaling comparison charts
   - Log transformation before/after
   - Correlation heatmap
   - Income distribution pie chart

### Key Findings
- 24.1% earn >$50K (class imbalance)
- capital_gain is extremely right-skewed (11.95)
- capital_net and age_hours_interaction show positive correlation with income
- Full-time workers earn more on average

### Files
- `Data_Transformation.ipynb`: Complete Jupyter notebook with all code, outputs, and explanations
- `requirements.txt`: Python dependencies
- `Data_Transformation_README.md`: This file

### How to Run
```bash
pip install -r requirements.txt
jupyter notebook Data_Transformation.ipynb
```
