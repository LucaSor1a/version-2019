class Cafezote():

    def __init__(self,agua,cafe,azucar,leche,vaso,dinero):
        self.vaso = vaso
        self.agua = agua
        self.cafe = cafe
        self.azucar = azucar
        self.leche = leche
        self.dinero = dinero
    
    def hay_todo(self):
        pass

    def desc(self):
        pass

    def hacer_cafe (self):
        if self.hay_todo():
            print("Haciendo cafe...")
            self.desc()
            return True
        else:
            print("Perdon, no se pudo hacer el cafe")
            return False


class Cafecito(Cafezote):

    money = int(input("Ingrese su dinero: "))
    azucaf = int(input("Queres el cafe con azucar? 1 o 0: "))

    def azuca(self):
        if self.azucaf == 1:
            azucaf = 5
        else: 
            azucaf = 0
        return azucaf

    def plata(self,money):
        if money != 0:
            return True
        else:
            return False

    def hay_todo(self):
        if not self.plata(self.money):
            print ("Falta dinero")
            return False
        elif self.agua < 100:
            print ("Falta agua") 
            return False
        elif self.cafe < 5:
            print ("Falta cafe")
            return False
        elif self.azucar < self.azuca():
            print ("Falta azucar")
            return False
        else:
            return True

    def desc(self):
        self.agua -= 100
        #print("Agua: {}".format(self.agua))
        self.cafe -= 20
        #print("Cafe: {}".format(self.cafe))
        if self.azuca() == 5:
            self.azucar -= 5 
        #print("Azucar: {}".format(self.azucar))
        self.dinero += self.money 
        #print("Dinero: {}".format(self.dinero))


#cafecito = Cafecito(500,200,200,0,False,100)
#hola = cafecito.hacer_cafe()

class Premium(Cafezote):

    money = int(input("Ingrese su dinero: "))
    cafcaf = int(input("Cuanto cafe queres? 5, 10, 15, 20: "))
    azucaf = int(input("Queres el cafe con azucar? 0, 1, 2 , 3, 4, 5: "))
    leccaf = int(input("Queres el cafe con leche? 0, 10, 20, 30, 40, 50: "))

    def plata(self,money):
        if money != 0:
            return True
        else:
            return False

    def hay_todo(self):
        if not self.plata(self.money):
            print ("Falta dinero")
            return False
        elif self.vaso == False:
            print ("Falta un vaso") 
            return False
        elif self.agua < (100 - self.leccaf):
            print ("Falta agua") 
            return False
        elif self.cafe < self.cafcaf:
            print ("Falta cafe")
            return False
        elif self.azucar < self.azucaf:
            print ("Falta azucar")
            return False
        elif self.leche < self.leccaf:
            print ("Falta leche")
            return False
        else:
            return True

    def desc(self):
        self.agua -= (100 - self.leccaf)
        #print("Agua: {}".format(self.agua))
        self.cafe -= self.cafcaf
        #print("Cafe: {}".format(self.cafe))
        self.azucar -= self.azucaf 
        #print("Azucar: {}".format(self.azucar))
        self.leche -= self.leccaf
        #print("Leche: {}".format(self.leche))
        self.dinero += self.money 
        #print("Dinero: {}".format(self.dinero))
        


#cafecito = Premium(500,200,200,500,True,100)
#hola = cafecito.hacer_cafe()