# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 01:43:13 2020

@author: arun prasad
"""

# Multiple Linear Regression
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
data_smiles = pd.read_csv("smiles.csv")
data_cal_des = pd.read_csv("Calculated_descriptors.csv")

is_notblinded = data_smiles.iloc[:,2] != 'BLINDED'
data_cal_des.shape

r2= []
#filtering the dataset
data_y = data_smiles[is_notblinded]
data_X = data_cal_des[is_notblinded]
print(data_y.shape)
print(data_X.shape)
for i in range(2,1875,1):
    X = data_X.iloc[:, i].values
#X = data_X["ALogp2", "ALogP"].values
    X = np.nan_to_num(X)

    y = data_y.iloc[:, 2].values
    
    
    print(y.shape)
    print(X.shape)
    
    # Splitting the dataset into the Training set and Test set
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)
    
    # Fitting Multiple Linear Regression to the Training set
    from sklearn.linear_model import LinearRegression
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)
    
    # Predicting the Test set results
    y_pred = regressor.predict(X_test)
    
    #evaluating the results
    from sklearn.metrics import r2_score
    print(r2_score(y_test,y_pred))
    print("progress", i)
    r2.append(r2_score(y_test,y_pred))
    
plt.plot(range(2,1875,1),r2)
