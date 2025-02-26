import unittest
from app import add, multiply, divide, greet


class TestAddFunction(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 5), -5)
        self.assertEqual(multiply(0, 10), 0)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertIsNone(divide(5, 0))  # Utilisation de assertIsNone pour tester None
        self.assertEqual(divide(0, 5), 0)

    def test_greet(self):
        sel
