# Regra comum para todos os exercícios:
# Toda interação com o usuário deve ser feita via menu interativo na função main() do 
# programa principal.
# O menu principal deve permitir que o usuário escolha qual exercício executar.
# Cada exercício está em um pacote próprio, com suas classes em módulos 
# separados.
# Para rodar o exercício, o menu deve importar e executar o módulo chamado 
# executar_respectivo_exercicioX.py (onde X é o número do exercício), que terá a 
# lógica para rodar aquele exercício, incluindo a interação via input().

# Exercício 2
# Crie pelo menos 4 classes que redefinem o mesmo operador por exemplo, + ou -, 
# cada uma com um comportamento diferente.
# Cada classe deve ter ao menos 2 métodos (podem ser auxiliares ou relacionados).
# Crie exemplos para mostrar as diferenças de comportamento conforme o objeto 
# usado.

from exercicio2.utils import *

def divisao_e_multiplicacao():
    input("\n Olá usuário, gostaria de praticar operações matemáticas? (excluindo soma e subtração)")

    while True:
        print("\n [ Operações disponíveis ]")
        print("1 - Executar uma divisão simples.")
        print("2 - Executar uma divisão inteira.")
        print("3 - Executar uma multiplicação.")
        print("4 - Executar uma potência.")
        print("0 - Sair")

        try:
            opcao = int(input("\n Escolha uma operação: "))
            entrada1 = float(input("Digite o primeiro número: "))
            entrada2 = float(input("Digite o segundo número: "))

        except ValueError:
            print("Escolha uma opção válida! ")
            continue

        match opcao:

            case 1:
                numero1 = DivisaoFloat(entrada1)
                numero2 = DivisaoFloat(entrada2)
                dividido = numero1 / numero2
                input(dividido)

            case 2:
                numero1 = DivisaoInt(entrada1)
                numero2 = DivisaoInt(entrada2)
                divididao = numero1 // numero2
                input(divididao)

            case 3:
                numero1 = Multiplicacao(entrada1)
                numero2 = Multiplicacao(entrada2)
                multiplicado = numero1 * numero2
                input(multiplicado)

            case 4:
                numero1 = Potencia(entrada1)
                numero2 = Potencia(entrada2)
                potencia = numero1 ** numero2
                input(potencia)

            case 0:
                print("Até logo...")
                break

if __name__ == "__main__":
    divisao_e_multiplicacao()

# Operadores Aritméticos (Binários)
# __add__(self, other): Adição (+)
# __sub__(self, other): Subtração (-)
# __mul__(self, other): Multiplicação (*)
# __truediv__(self, other): Divisão (/)
# __floordiv__(self, other): Divisão inteira (//)
# __mod__(self, other): Módulo/Resto (%)
# __pow__(self, other): Potenciação (**) 

# FACOM | Faculdade de Computação
#  +4
# Operadores de Comparação
# __eq__(self, other): Igualdade (==)
# __ne__(self, other): Diferente (!=)
# __lt__(self, other): Menor que (<)
# __le__(self, other): Menor ou igual (<=)
# __gt__(self, other): Maior que (>)
# __ge__(self, other): Maior ou igual (>=) 

#=====================================================

# class Ponto:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     # Sobrecarga do operador +
#     def __add__(self, outro):
#         return Ponto(self.x + outro.x, self.y + outro.y)

#     def __repr__(self):
#         return f"({self.x}, {self.y})"

# p1 = Ponto(1, 2)
# p2 = Ponto(3, 4)
# print(p1 + p2)  # Resultado: (4, 6)