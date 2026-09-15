# House Price Prediction — Kaggle Competition

A complete machine learning workflow for predicting house sale prices using the Ames Housing dataset from Kaggle.

The project focuses on building a strong regression model through systematic data auditing, preprocessing, feature engineering, model comparison, hyperparameter tuning, cross-validation, and final model selection.

## Objective

Predict house sale prices while minimizing the competition's evaluation metric:

**Root Mean Squared Logarithmic Error (RMSLE)**
Because house prices are right-skewed, the target variable is transformed using:

log1p(SalePrice)

Predictions are converted back to the original price scale using:

expm1(prediction)


## Dataset

The project uses the Kaggle Ames Housing dataset.

Features: 79
Target: SalePrice

The raw Kaggle train/test CSV files are excluded from Git and must be obtained separately from the competition dataset.

## Machine Learning Workflow

Data Audit
    ↓
Data Preprocessing
    ↓
Feature Engineering
    ↓
Model Comparison
    ↓
Hyperparameter Tuning
    ↓
Cross-Validation
    ↓
Final Model Selection
    ↓
Kaggle Submission

## Data Preprocessing

Preprocessing was performed using domain-specific rules rather than indiscriminate missing-value filling.

Key steps included:

- Structural missing values were interpreted as absence of a feature.
- Numerical absence-related features were filled with 0.
- LotFrontage was imputed using neighborhood-level medians.
- Electrical and remaining categorical missing values were handled using training-data modes.
- MasVnrType was handled according to MasVnrArea.
- The anomalous GarageYrBlt = 2207 in the test data was corrected to 2007.
- Final processed datasets contain no missing values or infinite values.

## Feature Engineering

14 domain-informed features were created:

- TotalSF
- TotalBathrooms
- TotalPorchSF
- TotalBsmtFinishedSF
- HouseAge
- RemodAge
- GarageAge
- Qual_GrLivArea
- Qual_TotalSF
- Qual_TotalBsmtSF
- TotalLivingArea
- TotalRooms
- AreaPerRoom
- GarageAreaPerCar

## Modeling

Models were evaluated using 5-fold cross-validation with shuffled folds and a fixed random seed of 42.

The primary evaluation metric was RMSLE, with the target transformed using log1p(SalePrice).

### Model Comparison

Model	                Mean RMSLE

Ridge	                 0.14262
Extra Trees	             0.13688
Gradient Boosting	     0.12989
XGBoost	                 0.12611
CatBoost	             0.12517
Tuned CatBoost	         0.12300

## Hyperparameter Tuning

CatBoost was selected for further hyperparameter tuning.

The final tuned configuration was:

- iterations = 800
- learning_rate = 0.05
- depth = 7
- l2_leaf_reg = 5

The tuned CatBoost model achieved a mean RMSLE of 0.12300 with a standard deviation of 0.01700 across the five folds.

## Model Selection

Blending CatBoost and XGBoost was also evaluated, but the optimized blend did not improve upon the tuned CatBoost model.

Therefore, Tuned CatBoost was selected as the final model.

## Reproducibility

The project uses a fixed random seed of 42 and 5-fold cross-validation to ensure consistent evaluation.

The complete workflow is documented across the project notebooks, from data auditing through final model selection and Kaggle submission.

## Project Structure

house-price-prediction/
│
├── configs/
│   └── config.yaml
│
├── data/
│   ├── raw/
│   └── processed/
│
├── experiments/
│   └── experiment_log.csv
│
├── notebooks/
│   ├── 01_data_audit.ipynb
│   ├── 02_data_preprocessing.ipynb
│   ├── 03_feature_engineering.ipynb
│   └── 04_modelling.ipynb
│
├── scripts/
│   └── test_model.py
│
├── src/
│   ├── config.py
│   ├── utils.py
│   └── __init__.py
│
├── submissions/
│   └── submission.csv
│
├── .gitignore
├── README.md
└── requirements.txt

The raw Kaggle dataset files are excluded from Git to keep the repository lightweight.

The notebooks contain the complete experimentation workflow, while the source directory contains reusable project utilities.

The submissions/ directory contains the final Kaggle prediction file.

## Live Application

The trained model was packaged separately into a Django application for public testing.

Live Application:
https://house-price-predictor-088h.onrender.com/

Deployment Repository:
https://github.com/haroonpuzhakkal07-pixel/house-price-predictor

The deployment repository contains the production inference pipeline, serialized model, prediction service, Django application, and deployment configuration.

## Limitations

The model is trained on the Ames Housing dataset and should not be interpreted as a general real-estate valuation system.

The live application exposes a selected subset of the model's features for usability. Remaining model inputs are populated using representative training-data defaults.

Predictions should therefore be treated as model estimates rather than professional property appraisals.

## Installation

Clone the repository and install the required dependencies:

```bash
pip install -r requirements.txt
```

The project uses Python 3.11.9.

## License

This project is intended for educational and portfolio purposes.