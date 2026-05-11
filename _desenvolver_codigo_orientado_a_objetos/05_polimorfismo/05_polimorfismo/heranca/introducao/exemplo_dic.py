
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


def fazer_cafe(tipo_cafe):
    tipo_cafe.preparar()


tipos_de_cafe = {
    "expresso": CafeExpresso,
    "latte": CafeLatte,
    "cappuccino": CafeCappuccino
}


opcoes = ", ".join(tipos_de_cafe.keys())


escolha = input(f"Qual tipo de café você deseja {opcoes}? ").strip().lower()


if escolha in tipos_de_cafe:
    cafe = tipos_de_cafe[escolha]()  
    fazer_cafe(cafe)  
else:
    print("Tipo de café não reconhecido.")