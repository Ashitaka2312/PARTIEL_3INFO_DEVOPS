import pytest


def test_example():
    assert 1 + 1 == 2  # Suppression des espaces inutiles


class TestClass:
    def test_method(self):
        assert True


def test_another():
    assert 3 * 3 == 9
