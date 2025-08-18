# -*- coding: utf-8 -*-
"""
Created on Mon Aug 18 13:37:05 2025

@author: DELL
"""

import numpy as np
import pandas as pd

dataset=pd.read_csv(r'C:\Users\DELL\Downloads\Salary_Data.csv')

dataset.mean()

dataset['Salary'].mean()

dataset.median()

dataset['Salary'].median()

dataset['Salary'].mode()

dataset.var()

dataset['Salary'].var

dataset.std()

dataset['Salary'].std

from scipy.stats import variation

variation(dataset.values)

variation(dataset['Salary'])

dataset.corr()

dataset['Salary'].corr(dataset['YearsExperience'])

dataset.skew()

dataset['Salary'].skew()

dataset.sem()

dataset['Salary'].sem()

import scipy.stats as stats

dataset.apply(stats.zscore)

stats.zscore(dataset['Salary'])

a = dataset.shape[0] 

b = dataset.shape[1] 

degree_of_freedom = a-b

print(degree_of_freedom)

X=dataset.iloc[:,:-1].values 

y=dataset.iloc[:,1].values   

y_mean = np.mean(y) 

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.20,random_state=0)

from sklearn.linear_model import LinearRegression

reg =  LinearRegression()

reg.fit(X_train,y_train)

y_predict = reg.predict(X_test) 

SSR = np.sum((y_predict-y_mean)**2)
 
print(SSR)

y = y[0:6]
 
SSE = np.sum((y-y_predict)**2)

print(SSE)

mean_total = np.mean(dataset.values)
 
SST = np.sum((dataset.values-mean_total)**2)

print(SST)

r_square = SSR/SST

r_square
