class Cafe:
    def preparar(self):
        print("Preparando um café genérico")

class CafeExpresso(Cafe):
    def preparar(self):
        print("Preparando um café expresso")

class CafeLatte(Cafe):
    def preparar(self):
        print("Preparando um café latte com leite vaporizado")

class CafeCappuccino(Cafe):
    def preparar(self):
        print("Preparando um cappuccino com espuma de leite")


cafe = CafeLatte()
cafe.preparar()