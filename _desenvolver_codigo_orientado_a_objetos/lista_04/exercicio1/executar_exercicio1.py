from exercicio1.utils import *
import time


def exercicio_01():
    print("-" * 20)

    clientes = []
    clientes_vips = []

    cliente_atual = ""
    
    while True:
        print("\n Exercício 1")
        print("\n[1] = Login.")
        print("[2] = Exibir lista de clientes.")
        print("[3] = Criar Cliente VIP.")
        print("[4] = Criar Cliente.")
        print("[5] = Compras")
        print("[6] = Compras Vip.")
        print("[0] Sair")

        opcao = int(input("\n Escolha: "))

        match opcao:
            case 1:
                nome = input("Digite o nome de usuário: ")
                senha = input("Digite a senha: ")
                for i in clientes + clientes_vips:
                    if i.nome == nome and i.senha == senha:
                        print("Login realizado com sucesso.")
                        i.login_inst()
                        cliente_atual = nome
                        break
                else:
                    print("Usuário e(ou) senha não encontrados.")

            case 2:
                print("\n[ Clientes Normais ]")
                if clientes:
                    for c in clientes:
                        print(c.nome, c.email, c.saldo, sep=" - ")
                else:
                    print("Nenhum cliente.")

                print("\n[ Clientes VIP ]")
                if clientes_vips:
                    for v in clientes_vips:
                        print(v.nome, "-", v.email)
                else:
                    print("Nenhum cliente VIP.")

            case 3:
                cliente_vip = ClienteVip.criar_vip()
                clientes_vips.append(cliente_vip)
                print("Cliente VIP registrado com sucesso.")

            case 4:
                cliente = Cliente.criar()
                clientes.append(cliente)
                print("Cliente registrado com sucesso.")

            case 5:
                if cliente_atual != "":
                    print(f"Bem vindo(a) {nome}, o que deseja comprar hoje? ")
                    valor = int(input("Digite quanto deseja gastar: R$"))
                    cliente.comprar(valor)

                else:
                    print("\nVocê não está logado!")
                    time.sleep(2)
                    print("Voltando para o menu principal...")
                    time.sleep(3)

            case 0:
                print("Encerrando script. Até mais...")
                break

            case _:
                print(f"A opção {opcao} é inválida. Tente novamente.")


if __name__ == "__main__":
    exercicio_01()






