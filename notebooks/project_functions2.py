import numpy as np
import pandas as pd

def na_filter(df,na,treshold = 0.4):
    for i in na.keys():
        if na[i]/df.shape[0] > treshold:
            df.drop(i,axis = 1)
def load_and_process(address):
    df = pd.read_csv(address).drop(['Row ID','Ship Date','Country','Postal Code','City','Product ID','Product Name', 'Region'],axis = 1).reset_index(drop = True).dropna(axis=0)  
    N_values = df.isna().sum()
    na_filter(df,N_values)
    df['Order Date'] = df['Order Date'].astype('datetime64[ns]')
    df['Month'] = df['Order Date'].dt.month_name()
    df['Year'] = df['Order Date'].dt.year
    return df