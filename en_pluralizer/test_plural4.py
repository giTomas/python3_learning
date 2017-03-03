#!/usr/bin/python3

import unittest
import plural4

class Plural_form(unittest.TestCase):
    def test_plural(self):
        self.assertEqual(plural4.plural('box'),'boxes')
        self.assertEqual(plural4.plural('couch'),'couches')
        self.assertEqual(plural4.plural('ivy'),'ivies')
        self.assertEqual(plural4.plural('light'),'lights')

if __name__ == '__main__':
    unittest.main()
