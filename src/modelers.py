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


def kfold_scores(X_train, y_train, nsplits):
    """ Kfold for linear regression
    
    Inputs:
    X_train 
    y_train PANDAS
    
    Returns:
    rmse per split
    y_hats per split
    coeffs per split
    """
    y_train = y_train.values

    kf = KFold(n_splits=nsplits, shuffle=True)  # almost always use shuffle=True
    fold_scores = []
    coeffs = []

    for train, test in kf.split(X_train):
        rmse, y_hat, coeff = lin_regression(X_train[train], 
                                              X_train[test], 
                                              y_train[train], 
                                              y_train[test])
        fold_scores.append(rmse)
        coeffs.append(coeff)
        
    return np.array(fold_scores), np.array(coeffs)
    
