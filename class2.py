from math import *

class Esfera:
    def __init__(self, cor, radio):
        self.cor   = cor
        self.radio = radio

    def volume(self):
        vol = (4 / 3) * pi * (self.radio * 3)

        return vol
    
    def area(self):
        ar = 4 * pi * (self.radio ** 2)

        return ar
    
bola1 = Esfera("vermelha", 8)
bola2 = Esfera("azul", 9)

print(f'O volume da bola 1 é {bola1.volume()} cm^3')
print(f'A área superficial da bola 1 é {bola1.area()} cm^3')

print(bola1.volume())
print(Esfera.volume(bola1))