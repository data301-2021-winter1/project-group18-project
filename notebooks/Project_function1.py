import numpy as np
import pandas as pd 

def duplicate_filter(df):
    if len(df[df.duplicated()]) > 0:
      df.drop((df[df.duplicated()]), axis = 1)

def load_and_process(source):
    df = pd.read_csv(source).drop(['Country','Postal Code','Customer Name','Product ID','Row ID'], axis = 1).reset_index(drop = True)  
    df['Segment'] =df['Segment'].astype('category')
    duplicate_filter(df)  
    return df