import pandas as pd



def fix_fips(df):
    """ Changes 4 digit fips to 5 digit fips"""
    
    col = 'fips'
    data[col] = data[col].apply(lambda x: '0'+x if len(x)==4 else x)
    return None