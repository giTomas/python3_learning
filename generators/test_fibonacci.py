#!/usr/bin/python3

import unittest
from fibonacci import fib


class Golden_ratio(unittest.TestCase):
    def setUp(self):
        self.fibonacci = fib(10)

    def test_sequence(self):
        self.assertEqual(next(self.fibonacci), 0)
        self.assertEqual(next(self.fibonacci), 1)
        self.assertEqual(next(self.fibonacci), 1)
        self.assertEqual(next(self.fibonacci), 2)
        self.assertEqual(list(fib(1000)),
                          [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987])
