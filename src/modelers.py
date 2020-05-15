import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split, KFold
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor


def standardize(X_train, X_test):
    """ Standardizes the training and testing data
    
    Inputs
    X_train: np.array
    X_test: np.array
    
    Returns
    np.array
    np.array
    """
    scaler = StandardScaler()
    scaler.fit(X_train)
    
    # Transform
    X_train_new = scaler.transform(X_train)
    X_test_new = scaler.transform(X_test)
    
    return X_train_new, X_test_new
    
    
def normalize(X_train, X_test):
    """Normalizing data
    
    Inputs
    X_train: np.array
    X_test: np.array
    
    Returns
    np.array
    np.array
    """
    
    norm = MinMaxScaler()
    norm.fit(X_train)
    
    X_trainn = norm.transform(X_train)
    X_testn = norm.transform(X_test)
    
    return X_trainn, X_testn
    
    
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
    r_sq = r2_score(y_test, y_hat)
    
    return rmse, r_sq, y_hat, model.coef_


def kfold_scores(X_train, y_train, regressor, nsplits):
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
    rmses = []
    r_sq_errors = []
    coeffs = []

    # Loop through kfold splits
    for train, test in kf.split(X_train):
        rmse, r_sq, y_hat, coeff = regressor(X_train[train], 
                                              X_train[test], 
                                              y_train[train], 
                                              y_train[test])
        rmses.append(rmse)
        r_sq_errors.append(r_sq)
        coeffs.append(coeff)        
        
    return np.array(rmses), np.array(r_sq_errors), np.array(coeffs)
    

def random_forest(X_train, X_test, y_train, y_test):
    """ Random Forest Regressor
    
    Inputs:
    X_train, X_test, y_train, y_test
    np.array, np.array, np.array, np.array
    
    Returns:
    rmse
    model coefficients"""
    
    model = RandomForestRegressor()
    model.fit(X_train, y_train)
    
    y_hat = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, y_hat))
    r_sq = model.score(X_test, y_test)
    coeff = model.feature_importances_
    
    return rmse, r_sq, y_hat, coeff

def gradient_boosting(X_train, X_test, y_train, y_test):
    """ Random Forest Regressor
    
    Inputs:
    X_train, X_test, y_train, y_test
    np.array, np.array, np.array, np.array
    
    Returns:
    rmse
    model coefficients"""
    
    model = GradientBoostingRegressor()
    model.fit(X_train, y_train)
    
    y_hat = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, y_hat))
    r_sq = model.score(X_test, y_test)
    coeff = model.feature_importances_
    
    return rmse, r_sq, y_hat, coeff