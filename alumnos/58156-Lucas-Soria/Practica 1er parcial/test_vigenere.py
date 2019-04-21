import unittest
from vigenere import vigenere



class TestVigenere(unittest.TestCase):
    def test_palabra_normal(self):
        result = vigenere('elefante')
        self.assertEqual(result, 'gzhngbvs')

    def test_palabra_con_espacios(self):
        result = vigenere('como estas')
        self.assertEqual(result, 'edowkhvov')
    
    def test_palabra_con_signos(self):
        result = vigenere('como estas!')
        self.assertEqual(result, 'Ingresaste un caracter no permitido')
    
    def test_palabra_con_numero(self):
        result = vigenere('tengo 3 patos')
        self.assertEqual(result, 'Ingresaste un caracter no permitido')
    
    def test_palabra_corto(self):
        result = vigenere('hola')
        self.assertEqual(result, 'Ingresaste un caracter no permitido')


if __name__ == "__main__":
    unittest.main()
