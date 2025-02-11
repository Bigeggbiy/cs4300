# test_task3.py
from task3 import check_number, first_n_primes, sum_to_n

def test_check_number():
    assert check_number(10) == "positive"
    assert check_number(-5) == "negative"
    assert check_number(0) == "zero"

def test_first_n_primes():
    assert first_n_primes(5) == [2, 3, 5, 7, 11]

def test_sum_to_n():
    assert sum_to_n(100) == 5050