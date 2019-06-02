class MaquinaCafeBasica(object):
    def __init__(self, agua, polvo_cafe, azucar, monedas):
        self.agua = agua
        self.polvo_cafe = polvo_cafe
        self.azucar = azucar
        self.monedas = monedas
        self.azucar_seleccionada = False

    def seleccionar_azucar(self):
        self.azucar_seleccionada = True

    def verificar_cafetera(self):
        # para hacer un cafe necesito:
        #    100 ml de agua
        #    50 g de cafe
        #    20 g de azucar (si hay azucar seleccionada)
        #    1 moneda
        if(self.agua >= 100 and self.polvo_cafe >= 50 and self.monedas > 1):
            if (self.azucar_seleccionada and self.azucar < 20):
                return False
            return True
        return False

    def descontar_usados(self):
        if self.azucar_seleccionada:
            self.azucar -= 20
        self.agua -= 100
        self.monedas -= 1
        self.polvo_cafe -= 50

    def hacer_cafe(self):
        if not self.verificar_cafetera():
            return False
        self.descontar_usados()
        self.azucar_seleccionada = False
        return True