from random import randint

class HumanAgainstComputerGame():
    
    def __init__(self):
        self.is_playing = True
        self.secret_number1()

    def secret_number1 (self):
        self.secret_number = randint(0,100)
    
    def play(self, num):
        if self.secret_number == num:
            self.is_playing = False
            return ('You win')
        elif self.secret_number < num:
            return ('My number is smaller')
        else:
            return ('My number is bigger')


class ComputerAgainstHumanGame():

    def __init__(self):
        self.is_playing = True
        self.min = 0
        self.max = 100

    def input_text(self):
        self.guess = int((self.min + self.max)/2)
        self.input_text1 = ("Is it your number {}?".format(self.guess))
        return self.input_text1

    def play (self, inp):
        if inp == '=':
            self.is_playing = False
        elif inp == '-':
            self.max = self.guess
        elif inp == '+':
            self.min = self.guess
        self.input_text()