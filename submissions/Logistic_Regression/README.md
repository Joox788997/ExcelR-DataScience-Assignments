# Logistic Regression - Diabetes Prediction

## Assignment #3

### Objective
Build a logistic regression model to predict diabetes in Pima Indian women using diagnostic measurements.

### Dataset
- 768 records, 8 medical features, 1 binary target (Outcome)
- Features: Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age

### Preprocessing
- Missing values (zeros in biological features) treated with median imputation
- Outlier treatment via Winsorization (1%/99% capping)
- Multicollinearity check via VIF (all VIF < 3)
- Standard scaling applied

### Model Performance
- Accuracy, Precision, Recall, F1-Score
- ROC-AUC with ROC curve visualization
- 5-fold stratified cross-validation
- Confusion matrix

### Deployment
- `model.pkl`: Saved model with scaler and feature names
- `app.py`: Streamlit web app for interactive diabetes prediction
- Run with: `streamlit run app.py`

### Files
- `Logistic_Regression.ipynb`: Complete notebook
- `model.pkl`: Trained model artifact
- `app.py`: Streamlit deployment app
- `requirements_logistic.txt`: Dependencies
