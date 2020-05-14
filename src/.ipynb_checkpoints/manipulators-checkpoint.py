import numpy as np
import pandas as pd

def merge_df(pop, predict):
    """Merge populations and predictions datafames on fips
    
    Inputs:
    df1: population datafame
    df2: predictions dataframe
    
    Returns:
    single dataframe   
    """
    predict_indices = predict['index_values']
    pop_subset = pop.loc[predict_indices]
    
    new_df = predict.merge(pop_subset, on='fips')
    new_df.drop(columns='index_values', inplace=True)
    
    return new_df


def calculate_votes(df):
    """ Calculate the votes for each candidate given total_votes and percentage each candidate received
    
    Inputs
    dataframe
    
    Returns
    dataframe
    """
    
    df['trump_votes_pred'] = round(df['trump_predict']*df['total_votes16']/100)
    df['trump_votes_true'] = round(df['trump_true']*df['total_votes16']/100)
    df['clinton_votes_pred'] = round(df['clinton_predict']*df['total_votes16']/100)
    df['clinton_votes_true'] = round(df['clinton_true']*df['total_votes16']/100)
    
    return df


def get_flipped_counties(df, col1, col2):
    """ Compare predict and true winners and create a columns for flipped
    
    Inputs
    dataframe
    
    Returns
    new dataframe     
    """
    
    df['flipped'] = pd.Series(np.zeros(df.shape[0]))
    
    df['flipped'].loc[df[col1] == df[col2]] = 0
    df['flipped'].loc[df[col1] != df[col2]] = 1
    
    return df


def get_vote_totals(df):
    pass