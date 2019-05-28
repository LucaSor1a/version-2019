class calculadora (object):

    def __init__ (self):

        self.ingresando = True
        
        self.acumulador = ''
        self.regb = ''
        self.operandos = ''
        self.num = ''


    def ingresar(self, usuario):   

        try:
            int(l)
            self.num += usuario
        except:
            if usuario == '=':

            else:
                self.operandos += usuario


        
    
    def display (self):

        display = str(self.acumulador + self.operando + self.regb)

        return display