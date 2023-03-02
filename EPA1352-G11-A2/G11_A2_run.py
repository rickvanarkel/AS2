"""
This file is the main run file of our file stru
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

def import_file(filepath):
    '''
    This function is used to import files form a selected filepath
    It returns a variable with with the read file
    It is currently only possible to import filetypes 'csv' or 'xlsx'
    '''
    dataframe = ""
    try:
        dataframe = pd.read_csv(filepath)
    except:
        dataframe = pd.read_excel(filepath)
    return dataframe

df_roads = import_file('./data/_roads3.csv')
df_bridges = import_file('./data/BMMS_overview.xlsx')

exec(open("preparing_data.py").read())
#execfile('preparing_data.py')