import pandas as pd
import warnings
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
warnings.filterwarnings('ignore')

'''
This file is the main run file!
'''

def import_file(filepath):
    '''
    This function is used to import files form a selected filepath
    It returns a variable with the read file
    It is currently only possible to import filetypes 'csv' or 'xlsx'
    '''
    dataframe = ""
    try:
        dataframe = pd.read_csv(filepath)
    except:
        dataframe = pd.read_excel(filepath)
    return dataframe

'''
Uses the import_file function to import the relevant files for datacleaning
'''
df_roads = import_file('./data/_roads3.csv')
df_bridges = import_file('./data/BMMS_overview.xlsx')

exec(open("preparing_data.py").read())

'''
This function runs the model_run file, this file automatically runs all the scenario's that..
were discribed in the assignment. The current settings are set to LB mode, for UB mode please...
change the file output name and the file input name in the model.py and model_run.py files.
'''
exec(open("model_run.py").read())

