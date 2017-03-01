#!/usr/bin/python3

import unittest
import plural2

class Plural_form(unittest.TestCase):

    def test_xzf(self):
        self.assertTrue(plural2.match_xyz('box'))
        self.assertFalse(plural2.match_xyz('lamb'))
        self.assertEqual(plural2.apply_xyz('box'), 'boxes')

    def test_h(self):
        self.assertTrue(plural2.match_h('rash'))
        self.assertFalse(plural2.match_h('list'))
        self.assertEqual(plural2.apply_h('rash'), 'rashes')
