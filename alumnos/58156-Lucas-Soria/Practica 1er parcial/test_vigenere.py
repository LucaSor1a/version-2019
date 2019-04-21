import unittest
from vigenere import *



class TestVigenere(unittest.TestCase):
    def test_palabra_normal(self):
        result = vigenere('elefante')
        self.assertEqual(result, 'gzhngbvs')

    def test_palabra_con_espacios(self):
        result = vigenere('como estas')
        self.assertEqual(result, 'edowkhvov')
    
    def test_palabra_con_signos(self):
        try:
            vigenere('como estas!')
            self.fail()
        except Exception_simbolo:
            pass
    
    def test_palabra_con_numero(self):
        try:
            vigenere('tengo 3 patos')
            self.fail()
        except Exception_numero:
            pass
    
    def test_palabra_corto(self):
        try:
            vigenere('hola')
            self.fail()
        except Exception_corto:
            pass
        


if __name__ == "__main__":
    unittest.main()
