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
* Table below shows different evaluation metrics and their value for Logistic Regression model

    | Model | Metric | Value | 
    | ----- | ---------- | -------------  |
    | Logistic Regression | Precision |1.0 |
    | Logistic Regression | Recall |1.0 |
    | Logistic Regression | F1-score |1.0 |
    | Logistic Regression | Accuracy |1.0 |

* Correlation matrix showed only 5 misclassification out of almost 20K samples
* Logistic regression achieved almost perfect classification between benign and malicious internet traffic  

#### Next steps
* Incorporate additional data points to the model
* Introduce additional models that are known to perform better for classification problems, as is the case with network anomaly detection
* Hyperparameter tuning using GridSearchCV etc...
* Deploy model on public cloud infrastructure

#### Outline of project
* [Jupyter notebook](network_anomaly_detection.ipynb)
* [License File](LICENSE.md)

##### Contact and Further Information
I can be contacted at arunkchaturvedi@gmail.com 
