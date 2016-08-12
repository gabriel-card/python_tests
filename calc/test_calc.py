# coding: utf-8
import unittest
import mock
import random
from calc import add, sub, rand


class CalculatorTestCase(unittest.TestCase):

    def test_calculator_does_addition(self):
        x = 10
        y = 20

        resp = add(x, y)

        self.assertEqual(resp, 30)

    def test_calculator_does_subtraction(self):
        x = 10
        y = 5

        resp = sub(x, y)
        self.assertEqual(resp, 5)

    @mock.patch('calc.random.seed')
    def test_calculator_does_random(self, fake_seed):
        fake_seed.return_value = 2
        resp = rand()

        self.assertEqual(resp, 2)

if __name__ == '__main__':
    unittest.main()
