class MonederoSensor:
    def __init__(self):
        self.dinero = 1000

    def get_dinero(self):
        return self.dinero

    def quitar_dinero(self, dinero):
        self.dinero -= dinero

    def poner_dinero(self, dinero):
        self.dinero += dinero