import unittest

from calc import calculadora

class TestCalc(unittest.TestCase):
    def test_calc_1(self):
        calc = calculadora()
        calc.ingresar('1')
        calc.ingresar('+')
        calc.ingresar('2')
        calc.ingresar('=')
        self.assertEqual(calc.display(), '3')

    def test_calc_2(self):
        calc = calculadora()
        calc.ingresar('1')
        calc.ingresar('-')
        calc.ingresar('1')
        calc.ingresar('=')
        self.assertEqual(calc.display(), '0')
        
    def test_calc_3(self):
        calc = calculadora()
        calc.ingresar('2')
        calc.ingresar('*')
        calc.ingresar('3')
        calc.ingresar('=')
        self.assertEqual(calc.display(), '6')

    def test_calc_4(self):
        calc = calculadora()
        calc.ingresar('1')
        calc.ingresar('5')
        calc.ingresar('/')
        calc.ingresar('3')
        calc.ingresar('=')
        self.assertEqual(calc.display(), '5')

    def test_calc_5(self):
        calc = calculadora()
        calc.ingresar('5')
        calc.ingresar('1')
        calc.ingresar('-')
        calc.ingresar('c')

        self.assertEqual(calc.display(), '')

    def test_calc_6(self):
        calc = calculadora()
        calc.ingresar('1')
        calc.ingresar('1')
        calc.ingresar('+')
        calc.ingresar('1')
        calc.ingresar('1')
        calc.ingresar('=')
        self.assertEqual(calc.display(), '22')

    def test_calc_7(self):
        calc = calculadora()
        calc.ingresar('4')
        calc.ingresar('1')
        calc.ingresar('+')
        calc.ingresar('3')
        calc.ingresar('-')
        calc.ingresar('2')
        calc.ingresar('=')
        self.assertEqual(calc.display(), '42')



if __name__ == '__main__':
    unittest.main()