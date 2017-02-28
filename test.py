#!/usr/bin/python3

import unittest

def add(x,y):
    return x + y;

def isBiggerThen10(x):
    return x > 10


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)

    def test_add(self):
        self.assertEqual(add(20,30), 50)

    def test_is_bigger(self):
        self.assertTrue(isBiggerThen10(20))
        self.assertFalse(isBiggerThen10(8))
        with self.assertRaises(TypeError):
            isBiggerThen10('10')

if __name__ == '__main__':
    unittest.main()
