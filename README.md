# 📊 Applied Data Science & Machine Learning Portfolio

Welcome to my technical portfolio! This repository contains applied data science projects, end-to-end feature engineering pipelines, and machine learning architectures. It serves as a showcase of my ability to clean messy real-world data, extract insights, and build solid foundations for predictive modeling.

---

## 🚀 Featured Projects & Pipelines

### 1. Google Play Store: Data Preprocessing & Feature Engineering
*A complete pipeline to prepare unstructured data for machine learning.*
* **Data Cleaning:** Handled missing values safely and standardized complex string metrics (`Size`, `Installs`, `Price`) into usable numeric formats.
* **Categorical Encoding:** Applied **Ordinal Encoding** (e.g., Content Rating) and **Label Encoding** (e.g., Free vs. Paid).
* **Exploratory Data Analysis (EDA):** Generated correlation heatmaps to uncover mathematical relationships between app metrics.

### 2. Predictive Modeling: Capturing Non-Linear Relationships (Polynomial Regression)
*Advanced feature engineering to model complex, curved datasets.*
* **Architectures:** Modeled industrial manufacturing quality and biological metrics (Fish Weight prediction).
* **Feature Engineering:** Utilized `PolynomialFeatures(degree=2)` to create interaction terms and squared features, allowing the algorithm to learn non-linear patterns.
* **Model Evaluation:** Effectively minimized error metrics and achieved $R^2$ scores exceeding 0.92 across complex datasets.

### 3. Predictive Modeling: Market & Health Metrics (Linear Regression)
*End-to-end machine learning workflows using Simple and Multiple Linear Regression.*
* **Pipelines:** Predicted student performance indices, medical insurance charges, and phone market prices.
* **Data Integrity:** Executed strict Train-Test splits and applied **Z-Score Standardization** (`StandardScaler`) before model training to absolutely prevent data leakage.
* **Algorithm Implementation:** Developed robust `Scikit-Learn` regression models, handling binary categorical mapping smoothly. 

### 4. Wine Quality: Exploratory Data Analysis (EDA)
*Statistical analysis and visualization of raw data.*
* **Insights:** Conducted deep correlation analysis and inspected raw data distributions to identify key features affecting wine quality. *(Published on Kaggle!)*
* **Visualization:** Utilized advanced Matplotlib and Seaborn techniques for statistical plotting.

### 5. Advanced Missing Data Management
*Handling incomplete datasets robustly for ML models.*
* **Mechanisms:** Examined missing data types (**MCAR**, **MAR**, **MNAR**).
* **Imputation Techniques:** Applied practical imputation methods including median/mean filling and **KNN Imputer** via Scikit-Learn.

---

## 📂 Repository Structure

*   `Machine Learning/Linear Regression/`: Contains end-to-end notebooks for multiple linear regression models (e.g., `phone_price_prediction.ipynb`, `linear_regression_practice.ipynb`).
*   `Machine Learning/PolynomialRegression/`: Contains modular notebooks for handling non-linear data using polynomial feature engineering.
*   `Feature Engineering/`: Contains modular notebooks for encoding, missing data handling, and EDA.
*   `Data Visualization - Matplotlib & Seaborn/`: Fundamentals of statistical plotting and heatmaps.
*   `Pandas & Numpy/`: Advanced array manipulations, missing data management, and data aggregations.

---

## 🛠️ Technical Skills & Stack

* **Machine Learning & Modeling:** `Scikit-Learn` (Linear & Polynomial Regression, Train/Test Split, StandardScaler, Imputers, Encoders)
* **Data Manipulation & Analysis:** `Pandas`, `NumPy`
* **Model Evaluation:** MAE, MSE, RMSE, $R^2$ Score
* **Data Visualization:** `Matplotlib`, `Seaborn` (Statistical plots, correlation heatmaps)
* **Software Engineering:** Modular code architecture, Git version control (Conventional Commits), bilingual technical documentation.

---

## 🎯 Current Focus
Transitioning from data analysis to **Data Engineering & Machine Learning**. My current goal is building scalable data pipelines, developing predictive machine learning models, and applying data-driven solutions to real-world business problems.