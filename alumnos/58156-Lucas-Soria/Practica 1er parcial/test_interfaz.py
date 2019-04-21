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
        try:
            interfaz('como estas!')
            self.fail()
        except:
            pass
    
    def test_palabra_con_numero(self):
        try:
            interfaz('tengo 3 patos')
            self.fail()
        except:
            pass
    
    def test_palabra_corto(self):
        try:
            interfaz('hola')
            self.fail()
        except:
            pass

if __name__ == '__main__':
    unittest.main()