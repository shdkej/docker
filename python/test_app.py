import unittest
from app import fibonacci, factorial

class TestFibonacci(unittest.TestCase):
    def test_factorial_1(self):
        self.assertEqual(factorial(1), 1)
