# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 18:34:10 2022

@author: arash

# estimator
LinearRegression
Lasso
RandomForestRegressor

# search over specified parameter values for an estimator
GridSearchCV			=>neg_mean_absolute_error

# test ensembles		=>combine the predictions of several base estimators built with a given learning algorithm

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression, Lasso
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import  RandomForestRegressor
from sklearn.model_selection import GridSearchCV

df = pd.read_csv(r'D:\project\DataScience_HR Analytics\data\data_clean_enrich.csv')
df['rate'] = df['rate'].replace(np.nan, 0)

df = df.dropna()

X = df.drop('avg_salary', axis=1)
y= df.avg_salary.values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# multiple linear rergression
X_sm =  sm.add_constant(X)
model = sm.OLS(y,X_sm.astype(float))


print(model.fit().summary())



lm = LinearRegression()
lm.fit(X_train, y_train)


print(np.mean(cross_val_score(lm, X_train, y_train,scoring='neg_mean_absolute_error')))


#lasso regression
lm_l = Lasso(alpha=0.13)
lm_l.fit(X_train, y_train)
print(np.mean(cross_val_score(lm_l, X_train, y_train,scoring='neg_mean_absolute_error',cv=3)))


alpha = []
error = []

for i in range(1,100):
    alpha.append(i/100)
    lml=Lasso(alpha=(i/100))
    error.append(np.mean(cross_val_score(lml,X_train,y_train, scoring='neg_mean_absolute_error', cv=3)))


plt.plot(alpha,error)



err=tuple(zip(alpha,error))
df_err = pd.DataFrame(err,columns=['alpha','error'])
df_err[df_err.error == max(df_err.error)]


rf = RandomForestRegressor()

np.mean(cross_val_score(rf,X_train,y_train,scoring='neg_mean_absolute_error',cv=3))



parameters= {'n_estimators':range(10,300,10),'criterion':('mse','mae'),'max_features':('auto','sqrt','log2')}

gs = GridSearchCV(rf,parameters,scoring='neg_mean_absolute_error',cv=3)
gs.fit(X_train,y_train)

gs.best_score_
gs.best_estimator_

# test ensembles
tpred_lm = lm.predict(X_test)
tpred_lml = lm_l.predict(X_test)
tpred_rf = gs.best_estimator_.predict(X_test)

from sklearn.metrics import mean_absolute_error
mean_absolute_error(y_test, tpred_lm)
mean_absolute_error(y_test, tpred_lml)
mean_absolute_error(y_test, tpred_rf)

mean_absolute_error(y_test, (tpred_lm + tpred_rf)/2)



import pickle
pickl = {'model':gs.best_estimator_}
pickle.dump( pickl, open( './/flaskAPI//models//model_file' + ".p", "wb" ) )

file_name = 'model_file.p'

with open(file_name,'rb') as pickled:
    data = pickle.load(pickled)
    model = data['model']
    
model.predict(np.array(list(X_test.iloc[1, :])).reshape(1,-1))[0]

