## University of California Berkley - MLAI Professional Certification Capstone Project

### Project Title - Using Machine Leaning to detect anomalies in network traffic

**Author: Arun Chaturvedi**

#### Executive summary
Network anomaly detection using machine learning is critically important today as organizations face an ever-growing threat of cyber attacks, data breaches, and malicious activity. Traditional rule-based methods often struggle to keep up with the evolving tactics of attackers, making machine learning an essential tool for identifying abnormal patterns in network behavior.
I have used [Network Intrusion dataset (CIC-IDS-2017)](https://www.unb.ca/cic/datasets/ids-2017.html) to develop a model that can distinguish between benign and malicious network traffic.

#### Rationale
Today’s networks are vast, dynamic, and filled with complex data traffic, making it difficult for traditional detection methods to identify potential risks or malicious activity. In a world dependent on connectivity and data integrity, machine learning-based anomaly detection ensures robust protection for personal, business, and governmental networks, making it a critical element of modern cybersecurity strategies.

#### Research Question
Can Machine Learning models effectively identify malicious network traffic - What constitutes 'normal' behavior in my dataset, and how can I reliably identify deviations from this norm that may indicate anomalies or outliers?

#### Data Sources
[Network Intrusion dataset (CIC-IDS-2017)](https://www.unb.ca/cic/datasets/ids-2017.html) made available by University of New Brunswick, Canadian Institute for Cybersecurity.

#### Methodology
* Data Preparation/Pre-processing: 
    - Selected dataset had 695K+ records, which were reduced to 100K records. Proportion of target variable was kept intact.
    - Non-impacting features like ones with no variance, unique record identifiers, or with infinite value were removed.
    - Dataset was cleaned for NaN and other similar values
    - Since that dataset was not normally distributed (identified using Q-Q plot), MinMaxScaler was used for scaling.
* Data Analysis:
    - Proportion of Benign vs malicious traffic was identified
    - PCA was done to reduce the number of feature (70+) to more meaningful levels
    - K-means clustering was done on the dataset 
    - Correlation heatmap was created 
* Baseline Model:
    - A base model for classifying benign vs malicious network traffic was crated using Logistic Regression
    - Model was evaluated using metrics like confusion matrix, classification report, ROC AUC Score and ROC AUC curve.

#### Results
* Table below shows different evaluation metrics and their value for Base Logistic Regression model

    | Model | Accuracy |Precision | Recall | F1-Score | ROC AUC | 
    | ----- | ----- | ----- | ----- | ----- | ----- | 
    | Logistic Regression | 0.99 |0.99 | 0.99 | 0.99 | 0.9987 |
    | Logistic Regression with GridSearchCV| 1.0 |1.0 |1.0 |1.0 |1.0 |
    | Random Forest | 1.0 |1.0 |1.0 |1.0 |1.0 |
    | XGBoost | 1.0 |1.0 |1.0 |1.0 |1.0 |

* XGBoost and Random Forest achieved almost perfect score with 0 wrongly classified records
* Confusion matrices visually confirmed the performance of all 4 models
* Initial model training was done on 100K records, which ws increased to 300K records and results were similar

#### Next steps
* Build visualization for prediction output
* Automate deployment of model as a Webapp creating a pipeline 
* Deploy model on public cloud infrastructure

#### Tech Stack Utilized
* Python: pandas, NumPy, scikit-learn, 
* Data Visualization: Matplotlib
* Machine Learning Techniques: Logistic Regression, Logistic Regression with GridSearchCV, Random Forest, XGBoost
* Model Evaluation Metrics: Confusion metrics, AUC ROC
* Feature Engineering: Scaling, Dimensionality Reduction, Imputation
* Web Application & Deployment: Flask

#### Outline of project
* [Jupyter notebook](network_anomaly_detection.ipynb)
* [App folder](app/)
* [Data folder](data/)
* [License File](LICENSE.md)

##### Contact and Further Information
I can be contacted at arunkchaturvedi@gmail.com 
