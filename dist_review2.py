'''
Distribution Practice 2


'''

import matplotlib.pyplot as plt
# import numpy as np
# import scipy as sp
import pandas as pd
import seaborn
# from scipy import stats

def read_file(filename):
    return pd.read_csv(filename, dtype=object)

def drop_marks(df):
    # can pass in args columns, loop through and replace df accordingly
    return df[(df.age != '?') & (df['max_heart_rate'] != '?') & (df['resting_blod_pressuremm_hg'] != '?') & (df['cholesterol_mg/dl'] != '?') & (df.sex != '?')]

def plot_ages(dfs):
    #fig, axes = plt.subplots(4,1, figsize=(12,24))
    for df in dfs:
        df.age.astype(float).hist()
    plt.title("Age Historgrams")
    plt.legend(['Cleveland','Hungaria','Switzerland','Long Beach'], loc=2)



def main():
    file_list = ['./data/cleveland_heart.csv','./data/hungarian_heart.csv', './data/switzerland_heart.csv', './data/long_beach.csv']

    locations = []
    
    for filename in file_list:
        location_name = filename.replace('.csv', '').replace('./', '')
        location_df = drop_marks(read_file(filename))
        locations.append(location_df)

    return locations

