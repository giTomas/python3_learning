#!/usr/bin/python3

import unittest
from plural6 import plural

class Plural_form(unittest.TestCase):
    def test_plural(self):
        self.assertEqual(plural('box'),'boxes')
        self.assertEqual(plural('couch'),'couches')
        self.assertEqual(plural('ivy'),'ivies')
        self.assertEqual(plural('light'),'lights')

if __name__ == '__main__':
    unittest.main()
