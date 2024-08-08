from Employee import Employee
import pytest

@pytest.fixture
def jack():
    jack = Employee('Jack', 'Sparrow', 13000)
    return jack

def test_give_default_raise(jack):
    jack.give_raise()
    assert jack.annual_salary == 18000

def test_give_custom_raise(jack):
    jack.give_raise(7000)
    assert jack.annual_salary == 20000