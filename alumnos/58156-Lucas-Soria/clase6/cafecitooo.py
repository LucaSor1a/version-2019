class cafezote():

    def __init__(self,agua,cafe,azucar,moneda):
        self.mc = False
        self.agua = agua
        self.cafe = cafe
        self.azucar = azucar
        self.moneda = moneda

class cafecito (cafezote):
    
    def startcoffee(self,az):
        self.agua -= 100
        self.cafe -= 5
        self.azucar -= az
        self.moneda += 1 

    def mcrn(self,money):
        if money == False:
            return "Poner una moneda"
        elif self.mc == True:
            return "Todavia se esta haciendo un cafe, espere"
        elif self.agua < 100:
            return "No hay suficiente agua"
        elif self.cafe < 5:
            return "Perdon, no hay suficiente cafe"
        else:
            azucar = int(input("Cafe con azucar? 0g ó 5g: "))
            if self.azucar < azucar:
                return "Perdon, no hay suficiente azucar"
            else:
                self.mc = True
                self.startcoffee(azucar)
                return "Haciendo cafe..."

class premium (cafezote):

    def startcoffee(self,az,ca):
        self.agua -= 100
        self.cafe -= ca
        self.azucar -= az
        self.moneda += 1 

    def mcrn(self,money):
        if money == False:
            return "Poner una moneda"
        elif self.mc == True:
            return "Todavia se esta haciendo un cafe, espere"
        elif self.agua < 100:
            return "No hay suficiente agua"
        else:
            cafe = int(input("Cuanto cafe desea? 3g ó 5g: "))
            if self.cafe < cafe:
                return "Perdon, no hay suficiente cafe"
            else:
                azucar = int(input("Cafe con azucar? 0g, 1g, 3g, 5g: "))
                if self.azucar < azucar:
                    return "Perdon, no hay suficiente azucar"
                else:
                    self.mc = True
                    self.startcoffee(azucar,cafe)
                    return "Haciendo cafe..."
