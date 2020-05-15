import pandas as pd
import numpy as np


def fix_fips(df):
    """ Changes 4 digit fips to 5 digit fips"""
    
    col = 'fips'
    df[col] = df[col].apply(lambda x: '0'+str(x) if len(str(x))==4 else str(x))
    return None


def get_idx(data, p1, p2, p3):
    """ Get indices for columns with values greater than those in other columns
    
    Inputs: dataframe, 3 columns
    
    Returns: 3 index arrays
    """
    
    p1_idx = (data[p1] > data[p2]) & (data[p1] > data[p3])
    p2_idx = (data[p2] > data[p1]) & (data[p2] > data[p3])    
    p3_idx = (data[p3] > data[p2]) & (data[p3] > data[p1])
    
    return p1_idx, p2_idx, p3_idx


def make_histogram(df, ax, colname, idx, label, title):
    """ Make a histogram of different features
    
    Inputs:
    dataframe
    ax
    column name (str)
    row index
    label for legend
    title for plot and x axis
    
    Returns: ax
    """
    
    ax.hist(df[colname][idx], label=label, alpha=0.7, bins=30, density=True)
    ax.legend()
    ax.set_title(title)
    ax.set_ylabel('Normalized Count')
    ax.set_xlabel(title)
    return ax
