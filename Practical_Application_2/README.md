## University of California Berkley - MLAI Professional Certification Practical Application 2 

In this assignment, we aim to develop a predictive model for estimating used car prices leveraging a vehicles.csv dataset. This dataset contains various car attributes like mileage, year of manufacture, make, model,transmission, and additional features. Model once developed should be able to estimate price of a used car and aid car dealerships in identifying what consumers value in a car so informed decisions can be made.

This assignment submission has following artifacts
* 1. Link to [Jupyter Notebook](practical_application_2.ipynb)
* 2. Link to [Data Folder](data/)
* 3. Link to [Images Folder](images/)
* 4. Link to [License File](LICENSE.md)


#### Steps Involved
* 1. Data Exploration and Preprocessing (Data Understanding): Import and clean the dataset to handle any missing or inconsistent data, followed by Exploratory Data Analysis (EDA) to understand the distribution and relationships between variables. 
* 2. Feature Selection and Engineering (Data Preparation): Utilize statistical methods  to identify key features that have a significant impact on car prices. Create new features or transform existing ones to better capture underlying patterns in the data.
* 3. Model Development (Modeling): Split the dataset into training and testing subsets to evaluate model performance. Experiment with three different regression models linear regression, decision tree regression, and finally random forest regression to identify the best-performing algorithm.
* 4. Model Evaluation (Evaluation): Assess the model's performance by using Mean Squared Error (MSE), and R-squared as performane metrices.

#### Expected Outcome
* 1. The model should estimate the prices for used cars, even for those not present in the training set. 
* 2. The model will aid used car dealership in identifying what consumers value in a used car.

#### Findings
* 1. Three different models 1/Linear Regression; 2/Decision Tree Regression; and 3/Random Forest Regression were used.
* 2. Models were evaluated on 1/Mean Squared Error (MSE) and R-squared(R2) were used.
* 3. Of the 3 models Random Forest Regression performed btter with least MSE and highest R2. GridSearchCV was used to tune and idenitfy best model and best params. 
* 3. Negative Coorelation was established for Price with Age and Odometer reading of car. Other variables remaiing unchanged, a used car will demand less price as its age increases. Similarly, a used car will demand less price if its odomter reading increases.