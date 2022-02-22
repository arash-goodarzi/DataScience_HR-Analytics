# <span style="color:#DAB11D">Project Overview: End to End Data Science Salary Estimator</span>
DataScience_HR Analytics
* Created a tool that estimates data science salaries (MAE ~ $ 11K) to help data scientists negotiate their income when they get a job.
* Scraped over 1000 job descriptions from glassdoor using python and selenium
* Engineered features from the text of each job description to quantify the value companies put on 125 variables.
* Optimized Linear, Lasso, and Random Forest Regressors using GridsearchCV to reach the best model.
* Built a client facing API using flask

# <span style="color:#DAB11D">Project Phase</span>

[comment]: <> (### ![#F0ED00]&#40;https://via.placeholder.com/15/fDAB11D/000000?text=+&#41; Phase 0 <span style="color:#E94B3CFF">--</span> Problem   <span style="color:#E94B3CFF">=></span>   Brainstorming   <span style="color:#E94B3CFF">=></span>   Glassdoor)
### ![#F0ED00](https://via.placeholder.com/15/fDAB11D/000000?text=+) Phase 1 <span style="color:#E94B3CFF">--</span> Data Collection    <span style="color:#E94B3CFF">=></span>  scraping  <span style="color:#E94B3CFF">=></span>   Selenium</span>
### ![#F0ED00](https://via.placeholder.com/15/fDAB11D/000000?text=+) Phase 2 <span style="color:#E94B3CFF">--</span> Integrate Data
### ![#F0ED00](https://via.placeholder.com/15/fDAB11D/000000?text=+) Phase 3 <span style="color:#E94B3CFF">--</span> Data Cleaning        <span style="color:#E94B3CFF">=></span>      Pandas
### ![#F0ED00](https://via.placeholder.com/15/fDAB11D/000000?text=+) Phase 4 <span style="color:#E94B3CFF">--</span> Extract data    

### ![#F0ED00](https://via.placeholder.com/15/fDAB11D/000000?text=+) Phase 5 <span style="color:#E94B3CFF">--</span> Exploratory Data analysis 
### ![#F0ED00](https://via.placeholder.com/15/fDAB11D/000000?text=+) Phase 6 <span style="color:#E94B3CFF">--</span> Model Building</span>
### ![#F0ED00](https://via.placeholder.com/15/fDAB11D/000000?text=+) Phase 7 <span style="color:#E94B3CFF">--</span> Flask configuration and server side of application (flaskAPI/app.py) </span>
### ![#F0ED00](https://via.placeholder.com/15/fDAB11D/000000?text=+) Phase 8 <span style="color:#E94B3CFF">--</span> Client side </span>

<span style="color:#DAB11D">Developer: *Arash Goodarzi*  </span>


# Data Science Salary Estimator: Project Overview


## Code and Resources Used
**Python Version:** 3.9  
**Packages:** pandas, numpy, sklearn, matplotlib, seaborn, selenium, flask, json, pickle, nltk, statsmodels  
**For Web Framework Requirements:**  ```pip install -r requirements.txt```  
**Flask Productionization:** https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2



I tried three different models:
* **Multiple Linear Regression** – Baseline for the model
* **Gaussian Process Regression** – Because it is flexible and inherent uncertain measures over predictions
* **Decision Tree Regression** – for verification that data structure has a tree format
* **Lasso Regression** – Because of the sparse data from the many categorical variables, I thought a normalized regression like lasso would be effective.
* **ridge regression** – by adding a degree of bias, reducing the standard errors.
* **Random Forest** – Again, with the sparsity associated with the data, I thought that this would be a good fit.

## Model performance
The Random Forest model far outperformed the other approaches on the test and validation sets.
* **Multiple Linear Regression**: MAE = 20.42 - MSE = 892.68
* **Gaussian Process Regression**: MAE = 22.10 - MSE = 918.61
* **Decision Tree Regression**: MAE = 13.61 - MSE = 528.11
* **Lasso Regression**: MAE = 17.97 - MSE = 656.63
* **ridge regression**: MAE = 18.36 - MSE = 640.89
* **Random Forest**: MAE = 12.39 - MSE = 410.40
* 
## Productionization
In this step, I built a flask API endpoint that was hosted on a local webserver by following along with the TDS tutorial in the reference section above. The API endpoint takes in a request with a list of values from a job listing and returns an estimated salary. 

