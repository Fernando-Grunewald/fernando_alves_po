from imports_utils import *

def exercicio_01():
   print("-" * 20)
   while True:

        print("Exercício 1 \n")
        print("[0] - Sair")
        print("-" * 20)

        opcao = int(input("Escolha uma opção: "))
        print("-" * 20)

        match opcao:
        
            case 0:
                print("Encerrando script. Até mais...")
                break
            case _:
                print(f" A opção {opcao} é inválida. Tente novamente.")
                
if __name__ == "__main__":
    exercicio_01()