## University of California Berkley - MLAI Professional Certification Practical Application 3

In this assignment, we aim to develop a predictive model for estimating whether a subscriber will avail a term deposit at a bank based on demographic, markiprevious marketing campaign and scorio-economic data.

This assignment submission has following artifacts
* Link to [Jupyter Notebook](Practical_Application_3.ipynb)
* Link to [Data Folder](data/)
* Link to [License File](LICENSE.md)

### Business Objective
Build a predicitve model that will help idenitfy whether an individual is likely to subscribe to term deposit. This model will utilize client personal data, campaign data,and socio-economic data. While building the model we will also compare performance of different classifiers like Logistic Regression, K Nearest Neighbor (KNN), Support Vector Machines (SVM), and Decision Trees. A Portugese bank dataset compiled over 17 different marketing campaigns will be utilized for this analysis

### Steps Involved
* Data Exploration and Preprocessing (Data Understanding): Import and clean the dataset to handle any missing or inconsistent data, followed by Exploratory Data Analysis (EDA) to understand the distribution and relationships between variables. 
* Feature Selection and Engineering (Data Preparation): Utilize statistical methods  to identify key features that have a significant impact on car prices. Create new features or transform existing ones to better capture underlying patterns in the data.
* Model Development (Modeling): Split the dataset into training and testing subsets to evaluate model performance. Experiment with three different regression models linear regression, decision tree regression, and finally random forest regression to identify the best-performing algorithm.
* Model Evaluation (Evaluation): Assess the model's performance by using Mean Squared Error (MSE), and R-squared as performane metrices.


Following models were used for the exercise:
* Logistic Regression
* K-Nearest Neighbors (KNN)
* Decision Tree
* Support Vector Machine (SVM)


**Dataset Used:** "_bank-additional-full.csv_" was obtained from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/222/bank+marketing).

**Establising Baseline:**: Dataset is heavily imbalanced with 88.73% "No" as comapred to only 11.27% "Yes". A model that will predict "No" will be accurate 88.73% times; leading to base line accuracy of 88.73%

#### Descriptive And Inferential Statistics
• Dataset had heavy class Imbalance as 88.73% "No" as comapred to only 11.27% "Yes"
• Subscribers had slightly highermedian age.
• Higher education levels correlated with a higher likelihood of subscription.
• Clients with fewer prior contacts had higher likelihood of subscription.


### Key Findings
#### Base Model Comparison
Table below has base model comparions using default settings
| Model | Train Time | Train Accuracy | Test Accuracy |
| ----- | ---------- | -------------  | -----------   |
| Support Vector Machine  | 69.5456 |0.8922     |0.8898|
| Logistic Regression  | 0.0616 |0.8860     | 0.8872 |
| K-Nearest Neighbors  | 0.0036 |0.9010 | 0.8834 |
| Decision Tree  | 0.689 |0.9698 |0.8338  |

#### Model Improvement 
* Introduced socio-economic features in the feature mix
* Applied Hyperparameter tuning using GridSearchCV
* Evaluated models via Precision, Recall, F-1Score, and Support using Classification Report and ROC Area Under Curve (ROC_AUC).

#### End User Outcome

* The current models have challenge identifying individulas who will subscribe to the term loan, i.e. ones who will say “Yes”.
* In the scenario above it is advisable to not rely on  accuracy alone as it cna be  misleading. We should consider precision and recall as they will be more meaningful for interpreting the results.


### Next Steps And Recommendations
* Adjust classification threshold and/or optimize for recall/F1-score for better imbalance handling.
* Support Vector Machines (SVM) can be adjusted to handle class imbalance by assigning class weights.
* Other modesl that perfom well with imbalanced datasets like  Random Forest or  Gradient Boosting (XGBoost or LightGBM or AdaBoost) coul dbe used.
* Additional features could be created that are more meaningful using existing feature set.
* Rerun the models after hyperparameter tuning done via GridSearchCV.
* Crete a dashboard or visual report for Visual Reporting for Business Users.
