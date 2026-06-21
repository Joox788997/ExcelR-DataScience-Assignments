# Multiple Linear Regression - Toyota Corolla Price Prediction

## Assignment #2

### Objective
Predict Toyota Corolla offer price using multiple linear regression with Ridge and Lasso regularization.

### Dataset
- 1,436 Toyota Corolla vehicles
- Target: Price (EURO)
- Features: Age, KM, Fuel Type, HP, Automatic, CC, Doors, Weight

### Models Built
1. **Model 1 (All Features):** Full feature set with standard scaling
2. **Model 2 (Selected Features):** Top correlated features (Age, KM, HP, Weight, Automatic, Fuel_Diesel)
3. **Model 3 (Interaction Terms):** Age×KM and Age×Weight interaction features

### Regularization
- **Ridge (L2):** Tested alpha values [0.01, 0.1, 1.0, 10.0, 100.0]
- **Lasso (L1):** Tested alpha values [0.001, 0.01, 0.1, 1.0, 10.0] with feature selection

### Evaluation Metrics
- R² Score, RMSE, MAE
- Residual analysis (distribution, Q-Q plot, scatter plots)

### Key Findings
- Vehicle Age is the strongest predictor (negative correlation)
- Weight and HP positively correlate with price
- Diesel vehicles command higher prices
- R² ≈ 0.86 explaining ~86% of price variance

### Files
- `Multiple_Linear_Regression.ipynb`: Complete notebook
- `requirements_MLR.txt`: Dependencies
