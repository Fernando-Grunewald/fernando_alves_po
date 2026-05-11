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


print("Opções disponíveis: expresso, latte, cappuccino")
escolha = input("Qual tipo de café você deseja? ").strip().lower()


if escolha == "expresso":
    cafe = CafeExpresso()
    fazer_cafe(cafe)
elif escolha == "latte":
    cafe = CafeLatte()
    fazer_cafe(cafe)
elif escolha == "cappuccino":
    cafe = CafeCappuccino()
    fazer_cafe(cafe)
else:
    print("Tipo de café não reconhecido.")