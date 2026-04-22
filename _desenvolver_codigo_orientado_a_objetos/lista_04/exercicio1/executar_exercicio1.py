from exercicio1.utils import *


def exercicio_01():
    print("-" * 20)
    # usuarios = []

    # def exibir_usuarios(usuarios):
    #     if not usuarios:
    #         print("Nenhum usuário cadastrado.")
    #         return
    #     print("\n--- Usuários cadastrados ---")
    #     for u in usuarios:
    #         print(u)
    
    while True:
        print("Exercício 1\n")
        print("\n[1] Login")
        print("[2] ")
        print("[3] = Criar Cliente VIP")
        print("[4] = Criar Cliente.")
        print("[0] Sair")

        opcao = int(input("\n Escolha: "))

        match opcao:
            case 1:
                pass

            case 2:
                pass

            case 3: # Criar o cliente VIP
                nome = input("Nome do cliente: ")
                email = input("Email: ")
                senha = input("Digite a senha")
                cpf = input("Digite o cpf: ")
                saldo = float(input("Inclua seu saldo inicial: R$"))
                desconto = int(input(("Digite seu valor de desconto (até 50%): "))) / 100

                cliente = Cliente(nome, email, cpf, senha, saldo, desconto)
                print("Cliente VIP registrado com sucesso! Bem-vindo(a)...")

            case 4: # Criar o cliente normal
                nome = input("Nome do cliente: ")
                email = input("Email: ")
                senha = input("Digite a senha")
                cpf = input("Digite o cpf: ")
                saldo = float(input("Inclua seu saldo inicial: R$"))

                cliente = Cliente(nome, email, cpf, senha, saldo)
                print("Cliente registrado com sucesso.")

            case 0:
                print("Encerrando script. Até mais...")
                break

            case _:
                print(f"A opção {opcao} é inválida. Tente novamente.")


if __name__ == "__main__":
    exercicio_01()