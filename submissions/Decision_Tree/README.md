# Decision Tree - Heart Disease Prediction

## Assignment #4

### Objective
Apply Decision Tree Classification to predict heart disease presence using clinical features.

### Dataset
- 908 records, 12 features, Cleveland Heart Disease dataset
- Target: Binary (0=no disease, 1-4=disease stages converted to disease present)

### Tasks Completed
- EDA: Histograms, boxplots, correlation heatmap, target distribution
- Data Cleaning: Fixed inconsistent boolean encoding (TRUE/FALSE/TURE), imputed missing oldpeak
- Hyperparameter Tuning: GridSearchCV with 5-fold CV (criterion, max_depth, min_samples_split, min_samples_leaf, max_features)
- Tree Visualization: plot_tree showing clinical decision rules
- Feature Importance: thal and cp are top predictors
- ROC Curve: AUC ~0.84
- Interview Questions: Hyperparameters, Label vs One-Hot Encoding

### Files
- `Decision_Tree.ipynb`: Complete notebook
- `requirements_dt.txt`: Dependencies
