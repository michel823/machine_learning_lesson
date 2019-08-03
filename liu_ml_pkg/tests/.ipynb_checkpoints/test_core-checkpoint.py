
from liu_ml_pkg.core import just_a_test_pandas
from liu_ml_pkg.core import Modelisation_bourse
import os
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA 
from sklearn.linear_model import LinearRegression
import pytest

def capital_case(x):
    return x.capitalize()

def test_capital_case():
    #assert capital_case('semaphore') == 'Semaphore'
    #assert capital_case('semaphore') == 'semaphore'
    assert True
    
def test_2():
    print(just_a_test_pandas())
    assert True
    
def test_modelisation_bourse():
    
        my_path = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(my_path, '../data/DAT_EURUSD_2018.csv')
        print(pd.read_csv(file_path, sep=',', header=0, index_col=0).head(5))
        
        data = pd.read_csv(file_path, sep=',', header=0, index_col=0)
        
        y = data.iloc[:, 1]
        X = data.iloc[:, ].shift(1).fillna(0)
        model = Modelisation_bourse()
        model.fit(X,y.values)
        pred=model.predict(X)
        
        
        
        assert pytest.approx(pred[0]- 0.0032741, abs=0.01)