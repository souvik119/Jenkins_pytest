from calculator_sample import *

def test_add():
    assert demo_add(2, 3) == 5

def test_subtract():
    assert demo_sub(2, 3) == -1

def test_multiply():
    assert demo_mul(2, 3) == 6

def test_divide():
    assert demo_div(10,5) == 2.0

def test_exponenetial():
    assert demo_exp(2, 3) == 8
