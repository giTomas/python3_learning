#!/usr/bin/python3

import unittest
import plural2

class Plural_form(unittest.TestCase):

    def test_sxz(self):
        self.assertTrue(plural2.match_sxz('box'))
        self.assertFalse(plural2.match_sxz('lamb'))
        self.assertEqual(plural2.apply_sxz('box'), 'boxes')

    def test_h(self):
        self.assertTrue(plural2.match_h('rash'))
        self.assertFalse(plural2.match_h('list'))
        self.assertEqual(plural2.apply_h('rash'), 'rashes')

    def test_y(self):
        self.assertTrue(plural2.match_y('ivy'))
        self.assertFalse(plural2.match_y('way'))
        self.assertEqual(plural2.apply_y('ivy'), 'ivies')

    def test_default(self):
        self.assertTrue(plural2.match_default('book'))
        # self.assertFalse(plural2.match_default('vacancy'))
        self.assertEqual(plural2.apply_default('book'), 'books')

    def test_plural(self):
        self.assertEqual(plural2.plural('box'),'boxes')
        self.assertEqual(plural2.plural('couch'),'couches')
        self.assertEqual(plural2.plural('ivy'),'ivies')
        self.assertEqual(plural2.plural('light'),'lights')

if __name__ == '__main__':
    unittest.main()
