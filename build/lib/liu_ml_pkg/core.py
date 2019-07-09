import pandas as pd
import os

__all__ = ['just_a_test_pandas']

def just_a_test_pandas():
    my_path = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(my_path, './data/DAT_EURUSD_2018.csv')
    print(pd.read_csv(file_path, sep=',', header=0, index_col=0).head(5))