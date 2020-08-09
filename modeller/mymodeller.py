import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def regressor(X,y):
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
    r2 = r2_score(y_test,y_pred))

    return r2