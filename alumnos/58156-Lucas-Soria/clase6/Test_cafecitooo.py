import unittest
from cafecitooo import (
   Cafezote,
   Cafecito,
   Premium)

#-------------------------------------------Cafecito------------------------------------------

class TestCafecito(unittest.TestCase):


    def setUp(self):
        self.cafecito = Cafecito(500,200,200,0,False,100)
        self.cafecito.money = 400
        self.cafecito.azucaf = 1

    def test_hacercafe_EXITO(self):
        self.assertTrue(self.cafecito.hacer_cafe())
        self.assertEqual(self.cafecito.agua, 400)
        self.assertEqual(self.cafecito.cafe, 180)
        self.assertEqual(self.cafecito.azucar, 195)
        self.assertEqual(self.cafecito.dinero, 500)

    def test_hacercafe_no_agua(self):
        self.cafecito.agua = 0
        self.assertFalse(self.cafecito.hacer_cafe())
        self.assertEqual(self.cafecito.agua, 0)
        self.assertEqual(self.cafecito.cafe, 200)
        self.assertEqual(self.cafecito.azucar, 200)
        self.assertEqual(self.cafecito.dinero, 100)

    def test_hacercafe_no_cafe(self):
       self.cafecito.cafe = 0
       self.assertFalse(self.cafecito.hacer_cafe())
       self.assertEqual(self.cafecito.agua, 500)
       self.assertEqual(self.cafecito.cafe, 0)
       self.assertEqual(self.cafecito.azucar, 200)
       self.assertEqual(self.cafecito.dinero, 100)
    
    def test_hacercafe_no_azucar_y_quiere(self):
       self.cafecito.azucar = 0
       self.assertFalse(self.cafecito.hacer_cafe())
       self.assertEqual(self.cafecito.agua, 500)
       self.assertEqual(self.cafecito.cafe, 200)
       self.assertEqual(self.cafecito.azucar, 0)
       self.assertEqual(self.cafecito.dinero, 100)
    
    def test_hacercafe_no_azucar_y_no_quiere(self):
       self.cafecito.azucar = 0
       self.cafecito.azucaf = 0
       self.assertTrue(self.cafecito.hacer_cafe())
       self.assertEqual(self.cafecito.agua, 400)
       self.assertEqual(self.cafecito.cafe, 180)
       self.assertEqual(self.cafecito.azucar, 0)
       self.assertEqual(self.cafecito.dinero, 500)
    
#-------------------------------------------Premium-------------------------------------------

class TestPremium(unittest.TestCase):


    def setUp(self):
        self.premium = Premium(500,200,200,500,True,100)
        self.premium.money = 400
        self.premium.azucaf = 5
        self.premium.cafcaf = 20
        self.premium.leccaf = 50

    def test_hacercafe_EXITO_default(self):
        self.assertTrue(self.premium.hacer_cafe())
        self.assertEqual(self.premium.agua, 450)
        self.assertEqual(self.premium.cafe, 180)
        self.assertEqual(self.premium.azucar, 195)
        self.assertEqual(self.premium.leche, 450)
        self.assertEqual(self.premium.dinero, 500)

    def test_hacercafe_no_agua(self):
        self.premium.agua = 0
        self.assertFalse(self.premium.hacer_cafe())
        self.assertEqual(self.premium.agua, 0)
        self.assertEqual(self.premium.cafe, 200)
        self.assertEqual(self.premium.azucar, 200)
        self.assertEqual(self.premium.leche, 500)
        self.assertEqual(self.premium.dinero, 100)

    def test_hacercafe_no_cafe(self):
       self.premium.cafe = 0
       self.assertFalse(self.premium.hacer_cafe())
       self.assertEqual(self.premium.agua, 500)
       self.assertEqual(self.premium.cafe, 0)
       self.assertEqual(self.premium.azucar, 200)
       self.assertEqual(self.premium.leche, 500)
       self.assertEqual(self.premium.dinero, 100)
    
    def test_hacercafe_no_azucar_y_quiere(self):
       self.premium.azucar = 0
       self.assertFalse(self.premium.hacer_cafe())
       self.assertEqual(self.premium.agua, 500)
       self.assertEqual(self.premium.cafe, 200)
       self.assertEqual(self.premium.azucar, 0)
       self.assertEqual(self.premium.leche, 500)
       self.assertEqual(self.premium.dinero, 100)
    
    def test_hacercafe_no_azucar_y_no_quiere(self):
       self.premium.azucar = 0
       self.premium.azucaf = 0
       self.assertTrue(self.premium.hacer_cafe())
       self.assertEqual(self.premium.agua, 450)
       self.assertEqual(self.premium.cafe, 180)
       self.assertEqual(self.premium.azucar, 0)
       self.assertEqual(self.premium.leche, 450)
       self.assertEqual(self.premium.dinero, 500)

#---------------------------------------------------------------------------------------------
if __name__ == "__main__":
   unittest.main()