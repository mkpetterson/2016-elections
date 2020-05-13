import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split, KFold
from sklearn.preprocessing import StandardScaler


def standardize(X_train, X_test):
    """ Standardizes the training and testing data
    
    Inputs
    X_train: np.array
    X_test: np.array
    
    Returns
    np.array
    np.array
    """
    scalar = StandardScaler()
    scalar.fit(X_train)
    
    # Transform
    X_train_new = scalar.transform(X_train)
    X_test_new = scalar.transform(X_test)
    
    return X_train_new, X_test_new
    
    
def lin_regression(X_train, X_test, y_train, y_test):
    """ Fits Linear Regression
    
    Inputs:
    X_train, X_test, y_train, y_test
    np.array, np.array, np.array, np.array
    
    Returns:
    rmse
    model coefficients"""
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    y_hat = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, y_hat))
    
    return rmse, y_hat, model.coef_


