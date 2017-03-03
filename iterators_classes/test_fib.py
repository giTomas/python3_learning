#!/usr/bin/python3

from fibb import Fibb
import unittest

class Test_sequence_class(unittest.TestCase):
    def test_seq_fibb(self):
        # fib = Fibb(1000)
        self.assertEqual(list(Fibb(1000)), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987])

if __name__ == '__main__':
    unittest.main()
