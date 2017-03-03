#!/usr/bin/python3

import unittest
import plural5

class Plural_form(unittest.TestCase):
    def test_plural(self):
        self.assertEqual(plural5.plural('box'),'boxes')
        self.assertEqual(plural5.plural('couch'),'couches')
        self.assertEqual(plural5.plural('ivy'),'ivies')
        self.assertEqual(plural5.plural('light'),'lights')

if __name__ == '__main__':
    unittest.main()
