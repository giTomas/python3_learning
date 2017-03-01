#!/usr/bin/python3

import unittest
import plural1

class Plural_form(unittest.TestCase):

    def test_es1(self):
        self.assertEqual(plural1.plural('box'), 'boxes')

    def test_es2(self):
        self.assertEqual(plural1.plural('rash'), 'rashes')

    def test_ies(self):
        self.assertEqual(plural1.plural('vacancy'), 'vacancies')

    def test_s(self):
        self.assertEqual(plural1.plural('car'), 'cars')
