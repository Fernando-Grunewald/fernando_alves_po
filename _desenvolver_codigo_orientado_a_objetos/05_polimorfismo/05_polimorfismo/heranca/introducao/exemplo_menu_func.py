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

def menu_cafe():
    tipos_de_cafe = {
        "expresso": CafeExpresso,
        "latte": CafeLatte,
        "cappuccino": CafeCappuccino
    }
    while True:
        opcoes = ", ".join(tipos_de_cafe.keys())
        escolha = input(f"\nQual tipo de café você deseja {opcoes}? Digite 'sair' para encerrar: ").strip().lower()

        match escolha:
            case "sair":
                print("Obrigado! Volte sempre.")
                break
            case _ if escolha in tipos_de_cafe:
                cafe = tipos_de_cafe[escolha]()
                cafe.preparar()
            case _:
                print("Tipo de café não reconhecido. Tente novamente.")

menu_cafe()