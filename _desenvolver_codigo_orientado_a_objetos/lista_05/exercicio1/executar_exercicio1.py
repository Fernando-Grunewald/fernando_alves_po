# Regra comum para todos os exercícios:
# Toda interação com o usuário deve ser feita via menu interativo na função main() do 
# programa principal.
# O menu principal deve permitir que o usuário escolha qual exercício executar.
# Cada exercício está em um pacote próprio, com suas classes em módulos 
# separados.
# Para rodar o exercício, o menu deve importar e executar o módulo chamado 
# executar_respectivo_exercicioX.py (onde X é o número do exercício), que terá a 
# lógica para rodar aquele exercício, incluindo a interação via input().

# Exercício 1
# Crie pelo menos 4 classes diferentes, cada uma com pelo menos 2 métodos.
# Os métodos devem ter nomes iguais entre as classes, mas implementações 
# distintas.
# Crie uma função que receba qualquer objeto e chame esses métodos, sem depender 
# da classe.

"""
Exercício 1 que cria 4 classes diferentes, cada uma com 2 métodos de nome igual entre as classes, porém suas implementações são distintas.
Por fim, ele cria uma função que pode receber qualquer um desses objetos e chama os métodos deles.
O exercício me deu liberdade criativa para criar classes de acordo com as diferentes raças de slime do jogo Slime Rancher.

Autor: Fernando Alves Grunevald. :3
Data: 12/05/2026
"""

from exercicio1.utils import *

def slime_info(slime):
    slime.caracteristica()
    slime.dieta()

def slimepedia():
    slimes_tipos = {
        "Rosa": Rosa,
        "Caçador": Cacador,
        "Mosaico": Mosaico,
        "Soneca": Soneca}
    
    while True:
        """A variável de opção irá pegar apenas os MÉTODOS do objeto que vamos escrever. O segundo input abaixo de slime_nome será responsável por nomear o objeto"""
        opcao = input("\n Escolha um tipo de slime! Digite aqui: ").capitalize().strip()

        match opcao:
            case "Encerrar":
                print("Encerrando programa.")
                break

            case slime_nome if slime_nome in slimes_tipos:
                nome = input("Digite o tipo de um slime: ")
                slime = slimes_tipos[slime_nome](nome)
                slime_info(slime)

            case _:
                print("Slime não cadastrado.")

if __name__ == "__main__":
    slimepedia()