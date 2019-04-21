import unittest
from interfaz import interfaz



class TestInterfazVigenere(unittest.TestCase):

    def test_palabra_normal(self):
        result = interfaz('elefante')
        self.assertEqual(result, 'gzhngbvs')

    def test_palabra_con_espacios(self):
        result = interfaz('como estas')
        self.assertEqual(result, 'edowkhvov')
    
    def test_palabra_con_signos(self):
        result = interfaz('como estas!')
        self.assertEqual(result, 'Ingresaste un caracter no permitido')
    
    def test_palabra_con_numero(self):
        result = interfaz('tengo 3 patos')
        self.assertEqual(result, 'Ingresaste un caracter no permitido')
    
    def test_palabra_corto(self):
        result = interfaz('hola')
        self.assertEqual(result, 'Ingresaste un caracter no permitido')


if __name__ == '__main__':
    unittest.main()