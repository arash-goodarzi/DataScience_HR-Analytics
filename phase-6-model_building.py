# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 18:34:10 2022

@author: arash

# estimator
A- statsmodels vs sklearn

B- do some trains
    Linear Regression
    Gaussian Proces Regresson
    Decision Tree Regresson
    Lasso
    Ridge regression
    Random Forest Regresson

C- search over specified parameter values for an estimator
    GridSearchCV			=>neg_mean_absolute_error

D- test ensembles		=>combine the predictions of several base estimators built with a given learning algorithm
    I compare mean_absolute_error and mean_squared_error as metrics for scoring

E- save the model

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression, Lasso
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV

df = pd.read_csv(r'D:\project\DataScience_HR Analytics\data\data_clean_enrich.csv')
df['rate'] = df['rate'].replace(np.nan, 0)

df = df.dropna()

X = df.drop('avg_salary', axis=1)
y = df.avg_salary.values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# multiple linear rergression
X_sm = sm.add_constant(X)
model = sm.OLS(y, X_sm.astype(float))

print(model.fit().summary())


lm = LinearRegression()
lm.fit(X_train, y_train)

print(np.mean(cross_val_score(lm, X_train, y_train, scoring='neg_mean_absolute_error')))


# GaussianProcessRegressor
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import DotProduct, WhiteKernel
kernel = DotProduct() + WhiteKernel()
gpr = GaussianProcessRegressor(kernel=kernel, random_state=0).fit(X, y)
print(np.mean(cross_val_score(gpr, X_train, y_train, scoring='neg_mean_absolute_error')))


# Decision Tree Regressor
from sklearn import tree
clf = tree.DecisionTreeRegressor()
clfr = clf.fit(X_train, y_train)
print(np.mean(cross_val_score(clfr, X_train, y_train, scoring='neg_mean_absolute_error')))

# lasso regression
lm_l = Lasso(alpha=0.13)
lm_l.fit(X_train, y_train)
print(np.mean(cross_val_score(lm_l, X_train, y_train, scoring='neg_mean_absolute_error', cv=3)))


# graph shows the decreasing of error
alpha = []
error = []

for i in range(1, 100):
    alpha.append(i / 100)
    lml = Lasso(alpha=(i / 100))
    error.append(np.mean(cross_val_score(lml, X_train, y_train, scoring='neg_mean_absolute_error', cv=3)))

plt.plot(alpha, error)

err = tuple(zip(alpha, error))
df_err = pd.DataFrame(err, columns=['alpha', 'error'])
df_err[df_err.error == max(df_err.error)]


# Ridge regression
from sklearn.linear_model import Ridge
linridge = Ridge(alpha=20.0).fit(X_train, y_train)
print(np.mean(cross_val_score(linridge, X_train, y_train, scoring='neg_mean_absolute_error', cv=3)))


# RandomForestRegressor
rf = RandomForestRegressor()
rfr = rf.fit(X_train, y_train)
print(np.mean(cross_val_score(rfr, X_train, y_train, scoring='neg_mean_absolute_error', cv=3)))

parameters = {'n_estimators': range(10, 300, 10), 'criterion': ('mse', 'mae'), 'max_features': ('auto', 'sqrt', 'log2')}

gs = GridSearchCV(rf, parameters, scoring='neg_mean_absolute_error', cv=3)
gs.fit(X_train, y_train)

gs.best_score_
gs.best_estimator_


# test ensembles
tpred_lm = lm.predict(X_test)
tpred_lml = lm_l.predict(X_test)
tpred_rf = gs.best_estimator_.predict(X_test)
tpred_gpr = gpr.predict(X_test)
tpred_clfr = clfr.predict(X_test)
tpred_linridge = linridge.predict(X_test)


from sklearn.metrics import mean_absolute_error

mean_absolute_error(y_test, tpred_lm)
mean_absolute_error(y_test, tpred_lml)
mean_absolute_error(y_test, tpred_rf)
mean_absolute_error(y_test, tpred_gpr)
mean_absolute_error(y_test, tpred_clfr)
mean_absolute_error(y_test, tpred_linridge)
mean_absolute_error(y_test, (tpred_lm + tpred_rf) / 2)

from sklearn.metrics import mean_squared_error

mean_squared_error(y_test, tpred_lm)
mean_squared_error(y_test, tpred_lml)
mean_squared_error(y_test, tpred_rf)
mean_squared_error(y_test, tpred_gpr)
mean_squared_error(y_test, tpred_clfr)
mean_squared_error(y_test, tpred_linridge)
mean_squared_error(y_test, (tpred_lm + tpred_rf) / 2)

import pickle

pickl = {'model': gs.best_estimator_}

with open('flaskAPI/models/model_file' + ".p", 'wb') as f:
    pickle.dump(pickl, f)




file_name = 'flaskAPI/models/model_file' + ".p"

with open(file_name, 'rb') as pickled:
    data = pickle.load(pickled)
    model = data['model']

model.predict(np.array(list(X_test.iloc[1, :])).reshape(1, -1))[0]
