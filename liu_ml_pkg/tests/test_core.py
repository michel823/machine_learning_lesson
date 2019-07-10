
from liu_ml_pkg.core import just_a_test_pandas

def capital_case(x):
    return x.capitalize()

def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'
    #assert capital_case('semaphore') == 'semaphore'
    
def test_2():
    print(just_a_test_pandas())
    assert True