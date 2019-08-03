import pandas as pd
import os
from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA 
from sklearn.linear_model import LinearRegression

__all__ = ['just_a_test_pandas', 'modelisation_bourse']

def just_a_test_pandas():
    my_path = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(my_path, './data/DAT_EURUSD_2018.csv')
    print(pd.read_csv(file_path, sep=',', header=0, index_col=0).head(5))
    
    
def Modelisation_bourse():
     return Pipeline([('abc',PCA()),('def',LinearRegression() )])
    