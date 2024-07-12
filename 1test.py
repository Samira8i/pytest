import pytest
from first import Number()

def test_sum():
    num_set = Number([4, 3, 3, 4, 5])
    assert num_set.sum() == 19

def test_mean():
    num_set = Number([3, 4, 5])
    assert num_set.sr() == 4.0

def test_max():
    num_set = Number([13450, 2423, 23242, 15])
    assert num_set.max() == 23242

def test_min():
    num_set = Number([0, 123, -123, 5])
    assert num_set.min() == -123

