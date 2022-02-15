import hypothesis
import pytest

def func(x):
	y=1
    return x + 1


def test_answer():
    assert func(3) == 4