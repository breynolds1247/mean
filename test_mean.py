from mean import *

def test_ints():
    num_list = [3,4,5]
    obs = mean(num_list)
    exp = 4
    assert obs == exp

def test_zero():
    num_list = [0,2,4,6]
    obs = mean(num_list)
    exp = 3
    assert obs == exp
