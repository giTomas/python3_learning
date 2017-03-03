#!/usr/bin/python3

import unittest
import plural3

class Plural_form(unittest.TestCase):
    def test_plural(self):
        self.assertEqual(plural3.plural('box'),'boxes')
        self.assertEqual(plural3.plural('couch'),'couches')
        self.assertEqual(plural3.plural('ivy'),'ivies')
        self.assertEqual(plural3.plural('light'),'lights')

if __name__ == '__main__':
    unittest.main()
