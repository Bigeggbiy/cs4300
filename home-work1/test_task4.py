# test_task4.py
from task4 import calculate_discount

def test_calculate_discount():
    assert calculate_discount(100, 10) == 90
    assert calculate_discount(50.5, 20) == 40.4