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

class Divisao:
    def __init__(self, valor):
        self.valor = valor
        
    def __truediv__(self, outro_valor):
        return Divisao(self.valor + outro_valor.valor)
    
    def __str__(self): # acho que isso aqui é pra exibir resultado em print.
        return f"Divisão: {self.valor}"
        
class Multiplicacao:
    def __init__(self):
        pass


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