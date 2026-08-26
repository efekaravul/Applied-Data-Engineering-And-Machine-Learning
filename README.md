# 📊 Applied Data Science & Machine Learning Portfolio

Welcome to my technical portfolio! This repository contains applied data science projects, end-to-end feature engineering pipelines, and machine learning architectures. It serves as a showcase of my ability to clean messy real-world data, extract insights, and build solid foundations for predictive modeling.

---

## 🚀 Featured Projects & Pipelines

### 1. Decision Trees: Depth, Regularization & the Cost of an Untuned Tree
*Two studies on how a single hyperparameter decides what a tree can and cannot see.*
* **When a Fixed Depth Hides Entire Classes:** On the UCI Car Evaluation dataset, a hand-picked `max_depth=3` scored 79% accuracy — but with **0 precision and 0 recall on both minority classes** (`good`, `vgood`). Accuracy alone concealed a model that had simply defaulted to the majority label. A 5-fold `GridSearchCV` over `criterion`, `splitter`, `max_depth` and `max_features` selected unlimited depth and lifted accuracy to **98.4%**, with strong per-class scores across all four classes.
* **Order-Preserving Encoding:** Applied `OrdinalEncoder` with explicitly declared category orders (`low < med < high < vhigh`) rather than relying on the default alphabetical mapping, which would have ranked `high` below `low`; encoding is fit inside a `ColumnTransformer` on the training split only.
* **California Housing Regression:** Tuned a `DecisionTreeRegressor` on 20,640 districts, searching `criterion`, `max_depth` and `min_samples_leaf` by `r2` — the search settled on unlimited depth paired with `min_samples_leaf=20`, showing that depth and leaf-size regularization must be tuned *together*. **R² ≈ 0.73**, MAE ≈ 0.40. *([Published on Kaggle](https://www.kaggle.com/code/efekaravul/california-housing-decision-tree-regression).)*

### 2. Mobile Price Classification: K-Nearest Neighbors & the Limits of Feature Scaling
*Four-class price-bracket prediction from phone hardware specs. [Published on Kaggle](https://www.kaggle.com/code/efekaravul/mobile-price-range-knn-classification).*
* **A Counter-Example to a Rule of Thumb:** Scaling is usually treated as mandatory for distance-based models, but here `StandardScaler` **cost 32 accuracy points** (93.2% → 60.8%). With one feature (`ram`) correlating 0.917 with the target while the other 19 hover near noise, standardizing strips away the natural weight of the only informative signal — a result established by tuning both variants independently rather than asserting it.
* **Leakage-Safe Architecture:** All preprocessing lives inside a `Pipeline` + `ColumnTransformer`, so imputation and scaling statistics are refit on each fold's training portion during cross-validation — a guarantee manual preprocessing cannot offer.
* **Systematic Tuning:** 5-fold `GridSearchCV` over 52 combinations of `n_neighbors` and `weights`, with the resulting bias-variance curve plotted to show the overfitting/underfitting boundary. **93.2% test accuracy** against a 25% baseline, with errors concentrated between adjacent price brackets as expected for an ordered target.

### 3. SMS Spam Detection: Text Classification with Naive Bayes
*Natural language classification on the UCI SMS Spam Collection (5,572 messages). [Published on Kaggle](https://www.kaggle.com/code/efekaravul/sms-spam-multinomial-naive-bayes-practice).*
* **Text Vectorization:** Converted raw message text into a Bag-of-Words matrix with `CountVectorizer`, fitting the vocabulary **exclusively on the training split** to prevent data leakage (4,135 × 7,596 sparse feature matrix).
* **Data Integrity:** Diagnosed and removed 403 duplicate messages that would otherwise leak between train and test sets, and handled non-UTF-8 (`latin-1`) source encoding.
* **Imbalanced Classification:** Applied **stratified splitting** (`stratify=y`) on a 13% minority class and evaluated with a confusion matrix and per-class precision/recall/F1 rather than accuracy alone — achieving **98.7% accuracy** with **0.98 precision / 0.92 recall** on the spam class.

### 4. Iris Species Classification: Gaussian Naive Bayes
*Probabilistic multiclass classification on continuous measurements. [Published on Kaggle](https://www.kaggle.com/code/efekaravul/iris-species-gaussian-naive-bayes).*
* **Algorithm Selection:** Contrasted `GaussianNB` (continuous, normally distributed features) against `MultinomialNB` (discrete count data), demonstrating how the distributional assumption drives model choice.
* **EDA & Visualization:** Used Seaborn pairplots to verify class separability and the per-class normality assumption before modeling.
* **Results:** 100% accuracy on the held-out test set, reported with the caveats of a small (30-row) evaluation sample.

### 5. Support Vector Machines: The Kernel Trick, Classification & Regression
*Two studies on how kernels reshape decision boundaries.*
* **Kernel Trick, Demonstrated:** On a non-linearly separable seismic dataset, manually engineered polynomial features (squares and interaction terms) and visualized the transformed space in 3D with `Plotly` — then showed an **RBF-kernel `SVC`** solving the same problem implicitly on the raw features, reaching 100% test accuracy where a linear kernel collapses to 40%.
* **Kernel Comparison & Tuning:** Benchmarked linear vs. RBF kernels on a loan-risk dataset and searched `C`, `kernel`, `degree` and `gamma` via 5-fold `GridSearchCV`.
* **Diamond Price Regression:** Tuned an **SVR** model against a Linear Regression baseline on ~54,000 records, with duplicate removal, outlier treatment, ordinal encoding of categorical grades, and feature scaling. *([Published on Kaggle](https://www.kaggle.com/code/efekaravul/diamond-price-svm-regression-practice).)*

### 6. Google Play Store: Data Preprocessing & Feature Engineering
*A complete pipeline to prepare unstructured data for machine learning.*
* **Data Cleaning:** Handled missing values safely and standardized complex string metrics (`Size`, `Installs`, `Price`) into usable numeric formats.
* **Categorical Encoding:** Applied **Ordinal Encoding** (e.g., Content Rating) and **Label Encoding** (e.g., Free vs. Paid).
* **Exploratory Data Analysis (EDA):** Generated correlation heatmaps to uncover mathematical relationships between app metrics.

### 7. Predictive Modeling: Capturing Non-Linear Relationships (Polynomial Regression)
*Advanced feature engineering to model complex, curved datasets.*
* **Architectures:** Modeled industrial manufacturing quality and biological metrics (Fish Weight prediction).
* **Feature Engineering:** Utilized `PolynomialFeatures(degree=2)` to create interaction terms and squared features, allowing the algorithm to learn non-linear patterns.
* **Model Evaluation:** Effectively minimized error metrics and achieved $R^2$ scores exceeding 0.92 across complex datasets.

### 8. Predictive Modeling: Market & Health Metrics (Linear Regression)
*End-to-end machine learning workflows using Simple and Multiple Linear Regression.*
* **Pipelines:** Predicted student performance indices, medical insurance charges, and phone market prices.
* **Data Integrity:** Executed strict Train-Test splits and applied **Z-Score Standardization** (`StandardScaler`) before model training to absolutely prevent data leakage.
* **Algorithm Implementation:** Developed robust `Scikit-Learn` regression models, handling binary categorical mapping smoothly. 

### 9. Wine Quality: Exploratory Data Analysis (EDA)
*Statistical analysis and visualization of raw data.*
* **Insights:** Conducted deep correlation analysis and inspected raw data distributions to identify key features affecting wine quality. *(Published on Kaggle!)*
* **Visualization:** Utilized advanced Matplotlib and Seaborn techniques for statistical plotting.

### 10. Advanced Missing Data Management
*Handling incomplete datasets robustly for ML models.*
* **Mechanisms:** Examined missing data types (**MCAR**, **MAR**, **MNAR**).
* **Imputation Techniques:** Applied practical imputation methods including median/mean filling and **KNN Imputer** via Scikit-Learn.

---

## 📂 Repository Structure

The repository is organized as a numbered learning path, from Python fundamentals to applied machine learning:

*   `01 - Python Fundamentals/`: List comprehensions, lambda/built-in functions, and error handling exercises.
*   `02 - Numpy/`: Array creation, indexing, and vectorized operations.
*   `03 - Pandas/`: DataFrame manipulation, indexing, grouping, merging, and missing-data handling.
*   `04 - Data Visualization - Matplotlib/`: Core plotting fundamentals and styling.
*   `05 - Data Visualization - Seaborn/`: Statistical plotting, EDA, and styled visualizations.
*   `06 - Feature Engineering/`: Encoding, missing data strategies, and exploratory feature analysis.
*   `07 - Machine Learning/`
    *   `Linear Regression/`: End-to-end notebooks for simple & multiple linear regression models (e.g., `phone_price_prediction.ipynb`).
    *   `Polynomial Regression/`: Modular notebooks for modeling non-linear data with polynomial feature engineering.
    *   `Logistic Regression/`: Binary/multiclass classification, hyperparameter tuning, and applied practice notebooks.
    *   `Support Vector Machine/`: Kernel-based classification (`SVC`) and regression (`SVR`), covering the kernel trick and `GridSearchCV` hyperparameter search.
    *   `Naive Bayes/`: Probabilistic classification — `GaussianNB` on continuous features (`naive_bayes_iris.ipynb`) and `MultinomialNB` on Bag-of-Words text features (`naive_bayes_practice.ipynb`).
    *   `KNN/`: Distance-based classification and regression — the effect of `k` on the bias-variance trade-off, leakage-safe `Pipeline` + `ColumnTransformer` preprocessing, and an empirical case where feature scaling *hurts* (`KNN_pratice_2.ipynb`).
    *   `Decision Trees/`: Tree-based classification (`Decision_Tree_Classifier.ipynb`) and regression (`Decision_Tree_Regression_Practice.ipynb`) — ordinal encoding with explicit category order, tree visualization with `plot_tree`, and depth/leaf-size regularization tuned via `GridSearchCV`.
    *   `Daily Model Practice/`: Short, self-contained daily modeling exercises on new datasets (`practice_1.ipynb`: rice grain classification with a scaled KNN pipeline, 99% accuracy).

> Datasets referenced by the notebooks live in a local `Data/` folder, which is intentionally excluded from version control (see `.gitignore`) to keep the repository lightweight.

---

## 🛠️ Technical Skills & Stack

* **Regression:** `Scikit-Learn` — Simple/Multiple Linear Regression, Polynomial Features, Support Vector Regression (SVR), Decision Tree Regression
* **Classification:** Logistic Regression, Support Vector Machines, Gaussian & Multinomial Naive Bayes, K-Nearest Neighbors, Decision Trees (binary & multiclass)
* **Natural Language Processing:** Text vectorization with `CountVectorizer` (Bag of Words), sparse matrix handling
* **Preprocessing:** Train/Test Split (incl. stratified sampling), `StandardScaler`, Imputers, One-Hot/Ordinal/Label Encoding, duplicate & outlier removal, leakage-safe `fit`/`transform` discipline
* **ML Pipelines:** `Pipeline` and `ColumnTransformer` for per-column-group preprocessing, with transformers refit inside every cross-validation fold to eliminate leakage end-to-end
* **Data Manipulation & Analysis:** `Pandas`, `NumPy`
* **Model Evaluation:** MAE, MSE, RMSE, $R^2$ Score; Confusion Matrix, Precision, Recall, F1-Score for imbalanced classification
* **Hyperparameter Tuning:** `GridSearchCV` with 5-fold cross-validation, tree regularization (`max_depth`, `min_samples_leaf`), ablation studies to attribute score changes to individual pipeline decisions
* **Model Interpretability:** Decision tree structure visualization with `sklearn.tree.plot_tree`
* **Data Visualization:** `Matplotlib`, `Seaborn` (Statistical plots, correlation heatmaps)
* **Software Engineering:** Modular code architecture, Git version control (Conventional Commits), bilingual technical documentation.

---

## 🎯 Current Focus
Transitioning from data analysis to **Data Engineering & Machine Learning**. My current goal is building scalable data pipelines, developing predictive machine learning models, and applying data-driven solutions to real-world business problems.