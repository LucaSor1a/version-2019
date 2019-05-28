import unittest
from cafecitooo import (
    cafecito,
    premium,
)


class TestCafecito1(unittest.TestCase):
    def setUp(self):
        self.cafe = cafecito(500,50,50,23)
        self.cafe.agua = 500
        self.cafe.cafe = 50
        self.cafe.azucar = 50
        self.cafe.moneda = 23
        self.cafe.mc = False

    def test_startcoffee(self):
        self.assertEqual(self.cafe.startcoffee(5), None)
        self.assertEqual(self.cafe.agua, 400)
        self.assertEqual(self.cafe.cafe, 45)
        self.assertEqual(self.cafe.azucar, 45)
        self.assertEqual(self.cafe.moneda, 24)

class TestCafecito2(unittest.TestCase):
    def setUp(self):
        self.cafe = cafecito(500,50,50,23)
        self.cafe.agua = 500
        self.cafe.cafe = 50
        self.cafe.azucar = 50
        self.cafe.moneda = 23
        self.cafe.mc = False
    
    def test_mcrn(self):
        self.assertEqual(self.cafe.mcrn(False), "Poner una moneda")

class TestCafecito3(unittest.TestCase):
    def setUp(self):
        self.cafe = cafecito(500,50,50,23)
        self.cafe.agua = 500
        self.cafe.cafe = 50
        self.cafe.azucar = 50
        self.cafe.moneda = 23
        self.cafe.mc = True
    
    def test_mcrn(self):
        self.assertEqual(self.cafe.mcrn(True), "Todavia se esta haciendo un cafe, espere")

class TestCafecito4(unittest.TestCase):
    def setUp(self):
        self.cafe = cafecito(50,50,50,23)
        self.cafe.agua = 50
        self.cafe.cafe = 50
        self.cafe.azucar = 50
        self.cafe.moneda = 23
        self.cafe.mc = False
    
    def test_mcrn(self):
        self.assertEqual(self.cafe.mcrn(True), "No hay suficiente agua")

class TestCafecito5(unittest.TestCase):
    def setUp(self):
        self.cafe = cafecito(500,0,50,23)
        self.cafe.agua = 100
        self.cafe.cafe = 0
        self.cafe.azucar = 50
        self.cafe.moneda = 23
        self.cafe.mc = False
    
    def test_mcrn(self):
        self.assertEqual(self.cafe.mcrn(True), "Perdon, no hay suficiente cafe")


#--------------------------------PREMIUM--------------------------------

class TestPremium1(unittest.TestCase):
    def setUp(self):
        self.cafe = premium(500,50,50,23)
        self.cafe.agua = 500
        self.cafe.cafe = 50
        self.cafe.azucar = 50
        self.cafe.moneda = 23
        self.cafe.mc = False

    def test_startcoffee(self):
        self.assertEqual(self.cafe.startcoffee(1,3), None)
        self.assertEqual(self.cafe.agua, 400)
        self.assertEqual(self.cafe.cafe, 47)
        self.assertEqual(self.cafe.azucar, 49)
        self.assertEqual(self.cafe.moneda, 24)

class TestPremium2(unittest.TestCase):
    def setUp(self):
        self.cafe = premium(500,50,50,23)
        self.cafe.agua = 500
        self.cafe.cafe = 50
        self.cafe.azucar = 50
        self.cafe.moneda = 23
        self.cafe.mc = False
    
    def test_mcrn(self):
        self.assertEqual(self.cafe.mcrn(False), "Poner una moneda")

class TestPremium3(unittest.TestCase):
    def setUp(self):
        self.cafe = premium(500,50,50,23)
        self.cafe.agua = 500
        self.cafe.cafe = 50
        self.cafe.azucar = 50
        self.cafe.moneda = 23
        self.cafe.mc = True
    
    def test_mcrn(self):
        self.assertEqual(self.cafe.mcrn(True), "Todavia se esta haciendo un cafe, espere")

class TestPremium4(unittest.TestCase):
    def setUp(self):
        self.cafe = premium(50,50,50,23)
        self.cafe.agua = 50
        self.cafe.cafe = 50
        self.cafe.azucar = 50
        self.cafe.moneda = 23
        self.cafe.mc = False
    
    def test_mcrn(self):
        self.assertEqual(self.cafe.mcrn(True), "No hay suficiente agua")

class TestPremium5(unittest.TestCase):
    def setUp(self):
        self.cafe = premium(500,0,50,23)
        self.cafe.agua = 100
        self.cafe.cafe = 0
        self.cafe.azucar = 50
        self.cafe.moneda = 23
        self.cafe.mc = False
    
    def test_mcrn(self):
        self.assertEqual(self.cafe.mcrn(True), "Perdon, no hay suficiente cafe")

class TestPremium5(unittest.TestCase):
    def setUp(self):
        self.cafe = premium(500,0,50,23)
        self.cafe.agua = 100
        self.cafe.cafe = 50
        self.cafe.azucar = 0
        self.cafe.moneda = 23
        self.cafe.mc = False
    
    def test_mcrn(self):
        self.assertEqual(self.cafe.mcrn(True), "Perdon, no hay suficiente azucar")

#----------------------------------------------------------------------
if __name__ == "__main__":
    unittest.main()