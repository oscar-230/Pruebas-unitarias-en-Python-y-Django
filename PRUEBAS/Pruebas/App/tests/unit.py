from django.test import TestCase
import unittest

import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('foo'.isupper())

    def test_split(self):
        s = 'hola mundo'
        self.assertEqual(s.split(), ['hola', 'mundo'])
        # comprueba que s.split falla cuando el separador no es una cadena
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
    
    
    