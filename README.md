# 📊 Applied Data Science & Machine Learning Portfolio

Welcome to my technical portfolio! This repository contains applied data science projects, end-to-end feature engineering pipelines, and machine learning architectures. It serves as a showcase of my ability to clean messy real-world data, extract insights, and build solid foundations for predictive modeling.

---

## 🚀 Featured Projects & Pipelines

### 1. XGBoost: Regularized Boosting, Survey-Design Leakage & a Silent Scope Bug
*Two studies on the tabular-data workhorse — and the most expensive bug in this repository so far.*
* **SDSS Stellar Classification — 99% Accuracy Across Three Imbalanced Classes:** An `XGBClassifier` (300 trees, `learning_rate=0.1`, `max_depth=5`) separates 10,000 Sloan Digital Sky Survey DR14 objects into **STAR / GALAXY / QSO** at **99% accuracy**, holding **recall = 0.96** on quasars despite their being only **8.5% of the data** (850 of 10,000). `stratify=y` on the split is what keeps that minority class proportionally represented on both sides. Three columns were dropped before training as structurally uninformative: `objid` (a single distinct value across the entire file), `rerun` (constant `301`), and `specobjid` (a bare record number). *([Published on Kaggle](https://www.kaggle.com/code/efekaravul/sdss-stellar-classification-xgboost-classifier).)*
* **Reading a 99% Honestly — Physics vs. Survey Bookkeeping:** Most of that score comes from `redshift`, which is a *legitimate* feature: in astrophysics it is a real measurement tied directly to object type (stars ≈ 0, galaxies small positive, quasars reaching 5.35 in this sample). But `run`, `camcol`, `plate` and `mjd` survived into the feature matrix, and those are scheduling codes from the telescope's observing program — because SDSS targets specific object classes with specific plates, they offer the model a slice of **leakage by survey design** rather than physical signal. The notebook documents this rather than presenting the 99% unqualified.
* **California Housing Regression — a Nine-Model Benchmark:** `XGBRegressor` won a head-to-head against eight alternatives at **test R² = 0.8082** (MAE $28,781), against **0.6145** for Linear/Lasso/Ridge and **0.7949** for `RandomForestRegressor`; tuning `colsample_bytree=0.7` alongside `max_depth=6` lifted it to **R² = 0.8161** (MAE $27,952). The same table doubles as two textbook illustrations: `DecisionTreeRegressor` scored **train R² = 1.0000 against test R² = 0.5937** — pure memorization, and the precise failure the ensembles exist to fix — while `KNeighborsRegressor` came last at **0.1500**, purely because the features were never scaled and a distance metric over unscaled columns is dominated by whichever column carries the largest units. *([Published on Kaggle](https://www.kaggle.com/code/efekaravul/california-housing-xgboost-regression).)*
* **A Silent Scope Bug That Deleted the Most Expensive Category:** `remove_outliers_from_column(df, target_col)` was written with `df[col]` in its body instead of `df[target_col]`. `col` is not local to that function, so Python resolved it in the **global** namespace — where it still held the final value of a loop variable left over from an earlier boxplot cell: `ocean_proximity`. The call meant to trim the target therefore applied the IQR rule to a **0–3 ordinal encoding**, whose upper fence lands at **2.5**, silently deleting all **2,295 `NEAR BAY` rows** — the most expensive category in the dataset. No exception was raised, and the resulting row count (18,345) looked entirely plausible. It surfaced only when the corrected code returned **19,569** rows in a second environment: *the same code producing two different numbers is the signal worth chasing.* Every metric in the notebook had been computed on data stripped of its priciest category; correcting it moved XGBoost's test R² from an inflated **0.8348 down to 0.8082**.
* **`ISLAND`: What a Five-Row Category Can and Cannot Tell You:** `ocean_proximity` carries a category holding exactly **5 of 20,640 rows** (0.02%). It shows the *highest* mean house value of any category — **$380,440** against **$259,212** for `NEAR BAY` — which is precisely the trap: at n = 5 that mean carries no usable information, and a train/test split would leave four rows on one side and one on the other. It was merged into the geographically nearest category rather than kept as a dummy column the model could only memorize.
* **A Censored Target Is Not an Outlier:** `median_house_value` stops at a hard wall of **$500,001** — **965 blocks** sit exactly at that cap, including 9% of all `NEAR BAY` rows. An IQR filter on the target flags 1,071 rows, of which those 965 are the bulk; they are not measurement errors but **censored** real data, and removing them means the model never sees the top of the price range while the reported scores grow quietly more optimistic. The notebook applies the filter but states the cost, and flags a second issue in the same breath: the cleaning runs *before* `train_test_split`, so the test set is trimmed along with the training set.

### 2. Gradient Boosting: Residual Fitting, Metric Choice & the Threshold as a Hyperparameter
*Two studies on the boosting family's workhorse — where the gain actually comes from, and how the choice of metric decides what the model optimizes.*
* **Concrete Compressive Strength Regression — R² 0.883 → 0.921:** A `GradientBoostingRegressor` on 1,030 UCI concrete mixtures scored **R² = 0.883** out of the box. A 5-fold `GridSearchCV` over `loss`, `learning_rate`, `n_estimators` and `max_depth` lifted it to **R² = 0.921**, cutting MSE from 30.2 to **20.3** (RMSE 5.5 → 4.5 MPa). The winning combination — `learning_rate=0.05` paired with `n_estimators=400` — is a direct demonstration of the **inverse relationship** between learning rate and tree count: the baseline's default 100 trees were simply too few to finish learning at a low rate. *([Published on Kaggle](https://www.kaggle.com/code/efekaravul/concrete-strength-gradient-boosting-regression).)*
* **A Silent `GridSearchCV` Failure, Caught in the Warning Log:** An early version of the grid listed `loss="squared_loss"`, which is not a valid scikit-learn value (the correct name is `squared_error`). `GridSearchCV` did not raise an error — it scored **150 of 300 fits as `nan`** behind a single `FitFailedWarning`, so half the search never ran and `huber` "won" against an opponent that never competed. A hyperparameter search is only as trustworthy as the validity of its grid.
* **Correlation Is Not Feature Importance:** The correlation heatmap ranks `Cement` (Pearson **0.498**) above `Age` (**0.329**), yet the trained model ranks `Age` first (**0.366** vs. 0.309). The reason is that the age–strength relationship is **logarithmic**, not linear (+27 MPa over the first 28 days, only +7 MPa over the following 337), and Pearson measures only the linear component — while tree splits are indifferent to functional form. Rank-based **Spearman** correlation reverses the ranking (`Age` 0.596 vs. `Cement` 0.478), and `permutation_importance` on the held-out set confirms it independently (`Age` 0.799, `Cement` 0.439), ruling out the known impurity-bias artifact of `feature_importances_`.
* **Heart Disease Classification — Optimizing the Metric That Matters:** A `GradientBoostingClassifier` on the UCI Cleveland data (303 patients, stratified split) reached **82% accuracy** at **AUC = 0.879**, missing 3 of 33 true cases. Tuning with `scoring="recall"` instead of `"accuracy"` — deliberately, because a false negative sends an untreated cardiac patient home while a false positive costs only a follow-up test — cut missed patients from **3 to 1** and raised positive-class recall from **0.91 to 0.97** for the price of one additional false positive. *([Published on Kaggle](https://www.kaggle.com/code/efekaravul/heart-disease-gradient-boosting-classifier).)*
* **The Decision Threshold Is a Hyperparameter:** `predict()` hides a fixed 0.5 cut-off applied to `predict_proba`. Sweeping that threshold moves recall from 0.76 to 0.97 **without retraining the model**, and the ROC curve plots the whole trade-off at once. The analysis also identifies where the curve stops paying: beyond FPR ≈ 0.46 the TPR is already 1.0, so lowering the threshold further buys nothing but false alarms.
* **Reading a 61-Sample Test Set Honestly:** With 61 test rows, a single patient is worth **0.0164 accuracy** — so a 0.02 "improvement" is one sample changing hands. Running the same model across 15 random splits produced test accuracies from **0.738 to 0.869** (σ ≈ 0.046), which is why the cross-validated score and AUC, rather than a single test accuracy, are treated as the primary metrics.

### 3. AdaBoost: Boosting, Encoding by Cardinality & What Tuning Actually Buys You
*Two studies on sequential ensembles — where boosting transforms a model, and where it barely moves.*
* **Used Car Price Regression — R² 0.63 → 0.91 through tuning:** An `AdaBoostRegressor` on 15,411 CarDekho listings scored **R² = 0.633** out of the box. A 240-fit `GridSearchCV` over `n_estimators`, `learning_rate`, `loss` and weak-learner depth lifted it to **R² = 0.907**, cutting MSE to **a quarter** of its original value (2.76×10¹¹ → 7.01×10¹⁰). The search settled on `max_depth=5` stumps with `learning_rate=0.1` and `n_estimators=200` — a concrete demonstration of the **inverse relationship** between learning rate and estimator count, and evidence that AdaBoost's default `max_depth=3` learner was simply too weak for the problem. `loss="linear"` beat `"square"` and `"exponential"`, as predicted: a handful of Ferraris and Rolls-Royces in the data make squared/exponential error weighting actively harmful. *([Published on Kaggle](https://www.kaggle.com/code/efekaravul/used-car-price-adaboost-regression).)*
* **Encoding Chosen by Cardinality, Not by Habit:** The dataset mixes 3-category columns with a 120-category `model` column. One-hot encoding everything would have added ~150 sparse columns, so `OneHotEncoder` was applied only to the low-cardinality columns while `brand` and `model` went through scikit-learn's cross-fitted **`TargetEncoder`**, collapsing 152 categories into 2 numeric columns without leaking the target. A third column, `car_name`, was identified as the literal concatenation of `brand` + `model` and dropped as redundant.
* **A `ColumnTransformer` Misconception, Caught by an Error:** An early version listed `StandardScaler` as a third entry in the `ColumnTransformer`, expecting it to scale the target-encoded output. It failed with `could not convert string to float: 'Volvo'` — because a `ColumnTransformer`'s transformers run **in parallel** on the original raw columns, never on each other's output. The scaler had to be *chained inside* the encoder's own `Pipeline` instead.
* **Diabetes Classification — Where Accuracy Lies:** An `AdaBoostClassifier` on the Pima Indians dataset hit **73.9% accuracy** while recalling only **44%** of actual diabetics. Tuning with `scoring="f1"` rather than `"accuracy"` — deliberately, because optimizing accuracy on an imbalanced target rewards leaning on the majority class — moved accuracy just one point to **75.0%**, but raised positive-class recall to **0.50** and F1 from **0.56 → 0.60**. The honest read: boosting was near its ceiling on this dataset, and the value of the tuning was in *where* the error moved, not in the headline number. *([Published on Kaggle](https://www.kaggle.com/code/efekaravul/diabetes-prediction-adaboost-classifier).)*
* **Missing Values That `isnull()` Cannot See:** `isnull().sum()` reported zero missing values in the diabetes data — but `describe()` showed a **minimum of 0** for `Glucose`, `BloodPressure`, `SkinThickness`, `Insulin` and `BMI`, all physiologically impossible. The missing entries were encoded as `0`, hiding **374 absent `Insulin` readings (49% of the column)**. They were converted to `NaN` and mean-imputed, and outliers were then removed with the IQR rule — a step that matters more for boosting than for most algorithms, since AdaBoost actively *increases* the weight of the points it predicts worst.

### 4. Income Evaluation: Random Forest & the Silent-Column-Drop Pitfall
*Binary income classification (`<=50K` / `>50K`) on the UCI Adult / Census Income dataset (30,139 rows after cleaning). [Published on Kaggle](https://www.kaggle.com/code/efekaravul/income-evaluation-random-forest-classification).*
* **A `ColumnTransformer` Pitfall, Caught and Fixed:** `ColumnTransformer`'s default `remainder="drop"` silently discards any column not explicitly listed in a transformer. An early version only listed the 6 nominal categorical columns for one-hot encoding, which meant `age`, `education-num`, `capital-gain`, `capital-loss`, `hours-per-week`, and `sex` were dropped from the model with no error raised. Fixed with `remainder="passthrough"` — confirmed by the fact that after the fix, every one of the top-5 most important features in the trained model turned out to be one of the previously-dropped numeric columns.
* **Mixed-Type Encoding Strategy:** Applied `OneHotEncoder` to 6 nominal categorical columns (`workclass`, `marital-status`, `occupation`, `relationship`, `race`, `native-country`, expanding to 80 dummy columns) to avoid implying a false order, while a binary column (`sex`) was mapped directly rather than one-hot encoded.
* **Results & Interpretability:** **84.7% accuracy** with a stratified train/test split on a 76/24 imbalanced target; per-class F1 of 0.90 (`<=50K`) and 0.67 (`>50K`). `feature_importances_` ranked `age` (22.7%), `education-num` (12.9%), `hours-per-week` (11.4%), and `capital-gain` (10.7%) as the strongest predictors.

### 5. Decision Trees: Depth, Regularization & the Cost of an Untuned Tree
*Two studies on how a single hyperparameter decides what a tree can and cannot see.*
* **When a Fixed Depth Hides Entire Classes:** On the UCI Car Evaluation dataset, a hand-picked `max_depth=3` scored 79% accuracy — but with **0 precision and 0 recall on both minority classes** (`good`, `vgood`). Accuracy alone concealed a model that had simply defaulted to the majority label. A 5-fold `GridSearchCV` over `criterion`, `splitter`, `max_depth` and `max_features` selected unlimited depth and lifted accuracy to **98.4%**, with strong per-class scores across all four classes.
* **Order-Preserving Encoding:** Applied `OrdinalEncoder` with explicitly declared category orders (`low < med < high < vhigh`) rather than relying on the default alphabetical mapping, which would have ranked `high` below `low`; encoding is fit inside a `ColumnTransformer` on the training split only.
* **California Housing Regression:** Tuned a `DecisionTreeRegressor` on 20,640 districts, searching `criterion`, `max_depth` and `min_samples_leaf` by `r2` — the search settled on unlimited depth paired with `min_samples_leaf=20`, showing that depth and leaf-size regularization must be tuned *together*. **R² ≈ 0.73**, MAE ≈ 0.40. *([Published on Kaggle](https://www.kaggle.com/code/efekaravul/california-housing-decision-tree-regression).)*

### 6. Mobile Price Classification: K-Nearest Neighbors & the Limits of Feature Scaling
*Four-class price-bracket prediction from phone hardware specs. [Published on Kaggle](https://www.kaggle.com/code/efekaravul/mobile-price-range-knn-classification).*
* **A Counter-Example to a Rule of Thumb:** Scaling is usually treated as mandatory for distance-based models, but here `StandardScaler` **cost 32 accuracy points** (93.2% → 60.8%). With one feature (`ram`) correlating 0.917 with the target while the other 19 hover near noise, standardizing strips away the natural weight of the only informative signal — a result established by tuning both variants independently rather than asserting it.
* **Leakage-Safe Architecture:** All preprocessing lives inside a `Pipeline` + `ColumnTransformer`, so imputation and scaling statistics are refit on each fold's training portion during cross-validation — a guarantee manual preprocessing cannot offer.
* **Systematic Tuning:** 5-fold `GridSearchCV` over 52 combinations of `n_neighbors` and `weights`, with the resulting bias-variance curve plotted to show the overfitting/underfitting boundary. **93.2% test accuracy** against a 25% baseline, with errors concentrated between adjacent price brackets as expected for an ordered target.

### 7. SMS Spam Detection: Text Classification with Naive Bayes
*Natural language classification on the UCI SMS Spam Collection (5,572 messages). [Published on Kaggle](https://www.kaggle.com/code/efekaravul/sms-spam-multinomial-naive-bayes-practice).*
* **Text Vectorization:** Converted raw message text into a Bag-of-Words matrix with `CountVectorizer`, fitting the vocabulary **exclusively on the training split** to prevent data leakage (4,135 × 7,596 sparse feature matrix).
* **Data Integrity:** Diagnosed and removed 403 duplicate messages that would otherwise leak between train and test sets, and handled non-UTF-8 (`latin-1`) source encoding.
* **Imbalanced Classification:** Applied **stratified splitting** (`stratify=y`) on a 13% minority class and evaluated with a confusion matrix and per-class precision/recall/F1 rather than accuracy alone — achieving **98.7% accuracy** with **0.98 precision / 0.92 recall** on the spam class.

### 8. Iris Species Classification: Gaussian Naive Bayes
*Probabilistic multiclass classification on continuous measurements. [Published on Kaggle](https://www.kaggle.com/code/efekaravul/iris-species-gaussian-naive-bayes).*
* **Algorithm Selection:** Contrasted `GaussianNB` (continuous, normally distributed features) against `MultinomialNB` (discrete count data), demonstrating how the distributional assumption drives model choice.
* **EDA & Visualization:** Used Seaborn pairplots to verify class separability and the per-class normality assumption before modeling.
* **Results:** 100% accuracy on the held-out test set, reported with the caveats of a small (30-row) evaluation sample.

### 9. Support Vector Machines: The Kernel Trick, Classification & Regression
*Two studies on how kernels reshape decision boundaries.*
* **Kernel Trick, Demonstrated:** On a non-linearly separable seismic dataset, manually engineered polynomial features (squares and interaction terms) and visualized the transformed space in 3D with `Plotly` — then showed an **RBF-kernel `SVC`** solving the same problem implicitly on the raw features, reaching 100% test accuracy where a linear kernel collapses to 40%.
* **Kernel Comparison & Tuning:** Benchmarked linear vs. RBF kernels on a loan-risk dataset and searched `C`, `kernel`, `degree` and `gamma` via 5-fold `GridSearchCV`.
* **Diamond Price Regression:** Tuned an **SVR** model against a Linear Regression baseline on ~54,000 records, with duplicate removal, outlier treatment, ordinal encoding of categorical grades, and feature scaling. *([Published on Kaggle](https://www.kaggle.com/code/efekaravul/diamond-price-svm-regression-practice).)*

### 10. Google Play Store: Data Preprocessing & Feature Engineering
*A complete pipeline to prepare unstructured data for machine learning.*
* **Data Cleaning:** Handled missing values safely and standardized complex string metrics (`Size`, `Installs`, `Price`) into usable numeric formats.
* **Categorical Encoding:** Applied **Ordinal Encoding** (e.g., Content Rating) and **Label Encoding** (e.g., Free vs. Paid).
* **Exploratory Data Analysis (EDA):** Generated correlation heatmaps to uncover mathematical relationships between app metrics.

### 11. Predictive Modeling: Capturing Non-Linear Relationships (Polynomial Regression)
*Advanced feature engineering to model complex, curved datasets.*
* **Architectures:** Modeled industrial manufacturing quality and biological metrics (Fish Weight prediction).
* **Feature Engineering:** Utilized `PolynomialFeatures(degree=2)` to create interaction terms and squared features, allowing the algorithm to learn non-linear patterns.
* **Model Evaluation:** Effectively minimized error metrics and achieved $R^2$ scores exceeding 0.92 across complex datasets.

### 12. Predictive Modeling: Market & Health Metrics (Linear Regression)
*End-to-end machine learning workflows using Simple and Multiple Linear Regression.*
* **Pipelines:** Predicted student performance indices, medical insurance charges, and phone market prices.
* **Data Integrity:** Executed strict Train-Test splits and applied **Z-Score Standardization** (`StandardScaler`) before model training to absolutely prevent data leakage.
* **Algorithm Implementation:** Developed robust `Scikit-Learn` regression models, handling binary categorical mapping smoothly. 

### 13. Wine Quality: Exploratory Data Analysis (EDA)
*Statistical analysis and visualization of raw data.*
* **Insights:** Conducted deep correlation analysis and inspected raw data distributions to identify key features affecting wine quality. *(Published on Kaggle!)*
* **Visualization:** Utilized advanced Matplotlib and Seaborn techniques for statistical plotting.

### 14. Advanced Missing Data Management
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
    *   `Ensemble Techniques And Random Forest/`: Bagging vs. boosting — `RandomForestClassifier` on the Adult/Census Income dataset (`random_forest.ipynb`), plus `AdaBoostClassifier` on the Pima Indians Diabetes data (`adaboost_classifier.ipynb`) and `AdaBoostRegressor` on the CarDekho used-car data (`adaboost_regression.ipynb`) — cardinality-driven encoding (`TargetEncoder` vs. `OneHotEncoder`), hidden missing values encoded as `0`, IQR outlier removal, and a documented `ColumnTransformer` `remainder="drop"` pitfall caught via feature-importance analysis. Gradient boosting is covered in `gradient_boosting_regression.ipynb` (UCI concrete compressive strength — residual fitting, the `learning_rate`/`n_estimators` trade-off, and correlation vs. permutation importance) and `gradient_boosting_classifier.ipynb` (UCI Cleveland heart disease — recall-scored tuning, ROC/AUC, and decision-threshold analysis). XGBoost is covered in `xg_boost_classifier.ipynb` (SDSS DR14 star/galaxy/quasar classification — constant-column removal and stratified splitting for an 8.5% minority class) and `xg_boost_regression.ipynb` (California housing prices — a nine-model benchmark, an IQR outlier-strategy comparison, and a documented scope bug that silently deleted an entire category).
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
* **Ensemble Methods:** Bagging (`RandomForestClassifier`) and boosting (`AdaBoostClassifier`, `AdaBoostRegressor`, `GradientBoostingClassifier`, `GradientBoostingRegressor`, `XGBClassifier`, `XGBRegressor`) — weak-learner depth, `learning_rate`/`n_estimators` trade-off, XGBoost's `colsample_bytree` column subsampling and L1/L2 regularization, boosting `loss` functions (including `loss="exponential"`, which makes gradient boosting equivalent to AdaBoost), residual/gradient fitting, and feature-importance analysis for model interpretability and pipeline debugging
* **Natural Language Processing:** Text vectorization with `CountVectorizer` (Bag of Words), sparse matrix handling
* **Preprocessing:** Train/Test Split (incl. stratified sampling), `StandardScaler`, Imputers, One-Hot/Ordinal/Label/**Target** Encoding (cross-fitted for high-cardinality columns), IQR-based outlier removal, duplicate removal, leakage-safe `fit`/`transform` discipline
* **ML Pipelines:** `Pipeline` and `ColumnTransformer` for per-column-group preprocessing, with transformers refit inside every cross-validation fold to eliminate leakage end-to-end
* **Data Manipulation & Analysis:** `Pandas`, `NumPy`
* **Model Evaluation:** MAE, MSE, RMSE, $R^2$ Score; Confusion Matrix, Precision, Recall, F1-Score for imbalanced classification; ROC curves, AUC, and `predict_proba` decision-threshold tuning; metric selection driven by asymmetric error cost rather than by default
* **Hyperparameter Tuning:** `GridSearchCV` with 5-fold cross-validation, tree regularization (`max_depth`, `min_samples_leaf`), ablation studies to attribute score changes to individual pipeline decisions
* **Model Interpretability:** Decision tree structure visualization with `sklearn.tree.plot_tree`; `feature_importances_` cross-checked against `permutation_importance` to control for impurity bias; Pearson vs. Spearman correlation as a diagnostic for non-linear monotonic relationships
* **Data Visualization:** `Matplotlib`, `Seaborn` (Statistical plots, correlation heatmaps)
* **Software Engineering:** Modular code architecture, Git version control (Conventional Commits), bilingual technical documentation.

---

## 🎯 Current Focus
Transitioning from data analysis to **Data Engineering & Machine Learning**. My current goal is building scalable data pipelines, developing predictive machine learning models, and applying data-driven solutions to real-world business problems.