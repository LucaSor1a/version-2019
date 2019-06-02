# -*- coding: utf-8 -*-

import unittest
from maquina_cafe import MaquinaCafeBasica


# maquina café (premium)
#    nivel agua (ml)
#    cantidad café (g)
#    monedas (1 moneda = 1 café)
#    controla vaso
#    con leche s/n
#    azúcar 0 a 5 (g)


class TestMaquinaCafeBasica(unittest.TestCase):
    # maquina café (básica)
    #    nivel agua (ml)
    #    cantidad café (g)
    #    azúcar (g) s/n
    #    monedas (1 moneda = 1 café)
    #    no controla vaso
    # para hacer un cafe necesito:
    #    100 ml de agua
    #    50 g de cafe
    #    20 g de azucar
    #    1 moneda
    def test_hacer_cafe_basico_sin_seleccion_azucar(self):
        self.maquina_comun = MaquinaCafeBasica(agua=1000, polvo_cafe=200, azucar=100, monedas=10)
        cafe_realizado = self.maquina_comun.hacer_cafe()
        self.assertTrue(cafe_realizado)
        self.assertEqual(self.maquina_comun.agua, 900)
        self.assertEqual(self.maquina_comun.polvo_cafe, 150)
        self.assertEqual(self.maquina_comun.azucar, 100)
        self.assertEqual(self.maquina_comun.monedas, 9)

    def test_hacer_cafe_basico_sin_seleccion_azucar_maquina(self):
        self.maquina_comun = MaquinaCafeBasica(agua=1000, polvo_cafe=200, azucar=0, monedas=10)
        cafe_realizado = self.maquina_comun.hacer_cafe()
        self.assertTrue(cafe_realizado)
        self.assertEqual(self.maquina_comun.agua, 900)
        self.assertEqual(self.maquina_comun.polvo_cafe, 150)
        self.assertEqual(self.maquina_comun.azucar, 0)
        self.assertEqual(self.maquina_comun.monedas, 9)

    def test_hacer_cafe_basico_con_seleccion_azucar(self):
        self.maquina_comun = MaquinaCafeBasica(agua=1000, polvo_cafe=200, azucar=100, monedas=10)
        self.maquina_comun.seleccionar_azucar()
        cafe_realizado = self.maquina_comun.hacer_cafe()
        self.assertTrue(cafe_realizado)
        self.assertEqual(self.maquina_comun.agua, 900)
        self.assertEqual(self.maquina_comun.polvo_cafe, 150)
        self.assertEqual(self.maquina_comun.azucar, 80)
        self.assertEqual(self.maquina_comun.monedas, 9)

    def test_tratar_hacer_cafe_basico_sin_agua(self):
        self.maquina_comun = MaquinaCafeBasica(agua=50, polvo_cafe=200, azucar=100, monedas=10)
        cafe_realizado = self.maquina_comun.hacer_cafe()
        self.assertFalse(cafe_realizado)
        self.assertEqual(self.maquina_comun.agua, 50)
        self.assertEqual(self.maquina_comun.polvo_cafe, 200)
        self.assertEqual(self.maquina_comun.azucar, 100)
        self.assertEqual(self.maquina_comun.monedas, 10)

    def test_tratar_hacer_cafe_basico_sin_polvo_cafe(self):
        self.maquina_comun = MaquinaCafeBasica(agua=1000, polvo_cafe=5, azucar=100, monedas=10)
        cafe_realizado = self.maquina_comun.hacer_cafe()
        self.assertFalse(cafe_realizado)
        self.assertEqual(self.maquina_comun.agua, 1000)
        self.assertEqual(self.maquina_comun.polvo_cafe, 5)
        self.assertEqual(self.maquina_comun.azucar, 100)
        self.assertEqual(self.maquina_comun.monedas, 10)


if __name__ == '__main__':
    unittest.main()