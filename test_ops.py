from pytest import *
import J_file_ as pd


def test_add():
    assert pd.add(6,6) == 12

def test_mult():
    assert pd.multiply(5,5) == 25
