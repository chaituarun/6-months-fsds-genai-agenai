# -*- coding: utf-8 -*-
"""
Created on Mon Aug 18 13:24:18 2025

@author: DELL
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv(r'C:\Users\DELL\Downloads\Salary_Data.csv')
# Check the shape of the dataset
print("Dataset Shape:", dataset.shape)  # (30, 2)

x = dataset.iloc[:, :-1]  # Years of experience (Independent variable)
y = dataset.iloc[:, -1]   # Salary (Dependent variable)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20,random_state=0)

x_train = x_train.values.reshape(-1, 1)
x_test = x_test.values.reshape(-1, 1)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)

y_pred = regressor.predict(x_test)

plt.scatter(x_train, y_train, color = 'red')  # Real salary data (training)
plt.plot(x_train, regressor.predict(x_train), color = 'blue')  # Predicted regression line
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

plt.scatter(x_test, y_test, color = 'red')  # Real salary data (testing)
plt.plot(x_train, regressor.predict(x_train), color = 'blue')  # Regression line from training set
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

print(f"Intercept: {regressor.intercept_}")
print(f"Coefficient: {regressor.coef_}")


bias = regressor.score(x_train, y_train)
print(bias)

variance = regressor.score(x_test,y_test)
print(variance)


# stats for ml 


comparison = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(comparison)

#STATISTICS FOR MACHINE LEARNING

dataset.mean()

dataset['Salary'].mean() 

dataset.median() 

dataset['Salary'].mode()

dataset.describe()

dataset.var() 

dataset.std()

dataset.corr()


# ssr 
y_mean = np.mean(y)
SSR = np.sum((y_pred-y_mean)**2)
print(SSR)

#sse
y = y[0:6]
SSE = np.sum((y-y_pred)**2)
print(SSE)

#sst 
mean_total = np.mean(dataset.values) # here df.to_numpy()will convert pandas Dataframe to Nump
SST = np.sum((dataset.values-mean_total)**2)
print(SST)

#r2 
r_square = 1 - SSR/SST
print(r_square)


bias = regressor.score(x_train, y_train)
print(bias)

variance = regressor.score(x_test, y_test)
print(variance)
