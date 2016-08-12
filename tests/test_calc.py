# coding: utf-8
import unittest


class CalculatorTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_this_foo(self):
        self.assertIs(1, 1)

if __name__ == '__main__':
    unittest.main()
