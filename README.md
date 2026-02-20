# Water Quality & Potability Prediction

## Project Overview
This project applies Machine Learning to predict water potability based on various water quality metrics. Using a dataset containing physicochemical properties of water bodies, we built a Random Forest Classifier capable of determining whether water is safe for human consumption.

The goal is to demonstrate a rigorous Data Science workflow, focusing on data integrity, leakage prevention, and model interpretability.

## Dataset Features
The model analyzes 9 key parameters to decide the outcome:
* pH: Acid-base balance.
* Hardness: Calcium and magnesium concentration.
* Solids (TDS): Total Dissolved Solids in ppm.
* Chloramines/Sulfates: Residual amounts from treatment processes.
* Conductivity: Electrical conductivity of the water.
* Organic Carbon: Level of organic compounds.
* Trihalomethanes: Disinfection byproducts.
* Turbidity: Measurement of light-emitting properties of water.
* Potability (Target): 1 (Potable) or 0 (Not Potable).

## Technical Workflow

### 1. Data Integrity & Splitting
To ensure an unbiased evaluation, we performed a Train-Test Split (80/20) before any data transformation. This prevents Data Leakage, ensuring the model has no prior knowledge of the test set distribution during the cleaning phase.

### 2. Preprocessing & Imputation
Our initial analysis revealed significant missing data in three key columns:
* pH: ~14.99% missing
* Sulfate: ~23.84% missing
* Trihalomethanes: ~4.95% missing

**Handling Strategy:**
We calculated the Median from the Training Set only and applied it to both the training and test sets. This ensures the model remains "blind" to the test data statistics.

### 3. Feature Scaling
Since features like Solids (thousands) and pH (units) operate on different scales, we used Standardization (StandardScaler). This transforms the data to have a mean of 0 and a standard deviation of 1, preventing high-magnitude features from dominating the model.

### 4. Spot Checking & Model Selection
To identify the best algorithm, we compared three different approaches:

| Model | Accuracy | False Positives (Danger) | Observation |
| :--- | :--- | :--- | :--- |
| **Logistic Regression** | 0.63 | 0 | Failed to learn (classified everything as 0). |
| **Random Forest** | 0.67 | 54 | Good balance, allows for feature importance analysis. |
| **SVM** | **0.69** | **37** | **Highest accuracy and safest for health (fewer FP).** |

**Selection:** Although the **SVM** provided the best safety metrics, the **Random Forest** was selected for further evaluation and deployment due to its **interpretability**. In water management, understanding *which* chemical factors influence potability is as crucial as the prediction itself.

## Final Model Evaluation (Random Forest)

The Random Forest Classifier (100 estimators) provides a conservative but safe prediction profile.

### Classification Report
| Class | Precision | Recall | F1-Score | Support |
| :--- | :--- | :--- | :--- | :--- |
| **0 (Not Potable)** | 0.70 | 0.88 | 0.78 | 412 |
| **1 (Potable)** | 0.64 | 0.36 | 0.46 | 244 | 

### Confusion Matrix
```text
[[362  50]  <- Correctly predicted 362 "Non-Potable"
 [157  87]]  <- Correctly predicted 87 "Potable"
 ```

## How to Run
1. Ensure you have the following libraries installed:

   * pip install pandas scikit-learn seaborn matplotlib
   * Place [water_potability.csv](https://www.kaggle.com/datasets/adityakadiwal/water-potability) in the data/ folder.
   * Run the main script:
        ```bash
        python3 script.py
        ```
