import hypothesis
import pytest

def func(x):
    return x


def test_answer():
    assert func(3) == 3