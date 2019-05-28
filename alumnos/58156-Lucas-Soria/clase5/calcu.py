class calculadora (object):

    def __init__ (self):

        self.ingresando = True
        self.acumulador = ''
        self.regb = ''
        self.operando = ''


    def ingresar(self, usuario):


        try:
            int(usuario)
            if self.operando == '':
                self.acumulador += usuario
            else:
                self.regb += usuario
        except:            
                
            
            if usuario == '=' or (self.operando != '' and self.regb != ''):
                if self.operando == '+':
                    self.acumulador = str(  int(   int(self.acumulador) + int(self.regb) ) )
                    
                if self.operando == '-':
                    self.acumulador = str(  int(   int(self.acumulador) - int(self.regb) ) )                  

                if self.operando == '*':
                    self.acumulador = str(  int(  int(self.acumulador) * int(self.regb)  ) )                    

                if self.operando == '/':
                    self.acumulador = str(  int(  int(self.acumulador) / int(self.regb) ) )
                
                self.regb = ''
                self.operando = ''    

                if usuario != '=':
                    self.operando = usuario
            
            elif usuario == 'c':
                self.acumulador = ''
                self.regb = ''
                self.operando = ''

            else:
                self.operando = usuario
                

                
    
    def display (self):

        display = self.acumulador + self.operando + self.regb

        return display

    


    