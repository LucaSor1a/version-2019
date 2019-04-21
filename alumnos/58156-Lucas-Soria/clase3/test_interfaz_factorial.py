import unittest
from factorial_interfaz import factorial_interfaz

class TestInterfazFactorial(unittest.TestCase):
    def test_interfaz_factorial_5(self):
        result = factorial_interfaz("5")
        self.assertEqual(result, 5)

    def test_interfaz_factorial_m5(self):
        result = factorial_interfaz("-5")
        self.assertEqual(result, "Error, el valor ingresado no es un numero entero positivo")

    def test_interfaz_factorial_hola(self):
        result = factorial_interfaz("hola")
        self.assertEqual(result, "Error, el valor ingresado no es un numero entero")
    
    def test_interfaz_factorial_51(self):
        result = factorial_interfaz("5.1")
        self.assertEqual(result, "Error, el valor ingresado no es un numero entero")
    
    def test_interfaz_factorial_52(self):
        result = factorial_interfaz("5,2")
        self.assertEqual(result, "Error, el valor ingresado no es un numero entero")

if __name__ == '__main__':
    unittest.main()
