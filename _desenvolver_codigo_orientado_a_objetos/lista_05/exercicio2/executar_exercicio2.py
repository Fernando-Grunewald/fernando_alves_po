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
    
    def __add__(self, outro_valor):
        