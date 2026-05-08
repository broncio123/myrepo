import pytest

from my_script import sum_two_variables


def test_sum_two_variables():
    assert sum_two_variables(2, 3) == 5
    assert sum_two_variables(-1, 1) == 0
