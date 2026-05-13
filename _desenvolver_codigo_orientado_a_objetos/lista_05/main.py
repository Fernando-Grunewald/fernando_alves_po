from imports import *

def lista_5():
   print("-" * 20)
   while True:

        print("\n Lista de Exercícios 4\n")
        print("[1] - Exercício 1.")
        print("[2] - Exercício 2.")
        print("[3] - Exercício 3.")
        print("[4] - Exercício 4.")
        print("[5] - Exercício 5.")
        print("[0] - Sair")
        print("-" * 20)

        opcao = int(input("Escolha uma opção: "))

        match opcao:
            case 1:
                slimepedia()
            case 2:
                exercicio_02()
            # case 3:
            #     exercicio_03()
            # case 4:
            #     exercicio_04()
            case 0:
                print("Encerrando script. Até mais...")
                break
            case _:
                print(f" A opção {opcao} é inválida. Tente novamente.")
                
if __name__ == "__main__":
    lista_5()
    
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

# Exercício 2
# Crie pelo menos 4 classes que redefinem o mesmo operador por exemplo, + ou -, 
# cada uma com um comportamento diferente.
# Cada classe deve ter ao menos 2 métodos (podem ser auxiliares ou relacionados).
# Crie exemplos para mostrar as diferenças de comportamento conforme o objeto 
# usado.

# Exercício 3
# Crie uma hierarquia com uma classe base e pelo menos 3 subclasses total de 4 
# classes.
# Cada classe deve ter pelo menos 2 métodos, e as subclasses devem sobrescrever 
# algum método da base com implementações próprias.
# Crie objetos das subclasses e execute os métodos para evidenciar o polimorfismo.

# Exercício 4
# Combine os conceitos anteriores: crie pelo menos 4 classes em hierarquia, com 
# métodos compartilhados e operadores redefinidos.
# Implemente a interação para criar e manipular objetos desses tipos via menu, usando 
# polimorfismo com funções, operadores e herança.

# Exercício 5
# Projete um sistema com pelo menos 4 classes diferentes, cada uma com pelo menos 
# 2 métodos, que possam ser usadas de forma intercambiável graças ao polimorfismo 
# O sistema deve ter uma interface genérica para processar os objetos, independente 
# da classe concreta.