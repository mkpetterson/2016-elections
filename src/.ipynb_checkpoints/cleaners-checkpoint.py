import pandas as pd
import numpy as np


def get_percentage(df):
    """ Creates new column of percentage of votes
    
    Inputs: dataframe
    Returns: None
    """
    
    total_votes16 = df['trump16'] + df['clinton16'] + df['otherpres16']
    total_votes12 = df['romney12'] + df['obama12'] + df['otherpres12']
    
    cols16 = ['trump16', 'clinton16', 'otherpres16']
    cols12 = ['romney12', 'obama12', 'otherpres12']
    
    for colname in cols16:
        new_name = colname + '_pct'    
        df[new_name] = 100*df[colname]/total_votes16
    
    for colname in cols12:
        new_name = colname + '_pct'
        df[new_name] = 100*df[colname]/total_votes12
        
    df['cvap_pct12'] = 100*total_votes12/df['cvap']
    
    return None    


def ohe_rural(df):
    """ Creates boolean for rural/urban counties
    
    Inputs: Dataframe
    Returns: None
    """
    
    df['metro'] = df['ruralurban_cc'].apply(lambda x: 1 if x <= 3.0 else 0)
    df['rural'] = df['ruralurban_cc'].apply(lambda x: 1 if x >= 8.0 else 0)
    df['urban_metroadj'] = df['ruralurban_cc'].apply(lambda x: 1 if (x==4) or (x==6) else 0)
    df['urban_not_metroadj'] = df['ruralurban_cc'].apply(lambda x: 1 if (x==5) or (x==7) else 0)
    
    return None



def find_winner(df, col1, col2, new_col):
    """ Finds winner when comparing votes/numbers from col1 and col 2
    
    Inputs:
    dataframe
    col1, col2, new_col are strings
    
    Returns:
    dataframe
    """
    
    # Get candidate names
    if 'clinton' in col2:
        label2 = 'Clinton'
        label1 = 'Trump'
    elif 'trump' in col2:
        label2 = 'Trump'
        label1 = 'Clinton'
    else:
        return 'Check names'
    
    df[new_col] = pd.Series(np.zeros(df.shape[0]))
    
    df.loc[df[col1] > df[col2], new_col] = label1
    df.loc[df[col2] > df[col1], new_col] = label2
    
    return df