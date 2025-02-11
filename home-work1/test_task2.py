# test_task2.py
from task2 import example_data_types

def test_data_types():
    data = example_data_types()
    assert isinstance(data["integer"], int)
    assert isinstance(data["float"], float)
    assert isinstance(data["string"], str)
    assert isinstance(data["boolean"], bool)