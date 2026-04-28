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
        print("[7] = Logoff.")
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
                        print(c.nome, c.email, "R$", c.saldo, sep=" ")
                else:
                    print("Nenhum cliente.")

                print("\n[ Clientes VIP ]")
                if clientes_vips:
                    for v in clientes_vips:
                        print(v.nome, v.email, "R$", v.saldo, sep=" ")
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
                    cliente.comprar_itens()

                else:
                    print("\nVocê não está logado!")
                    time.sleep(2)
                    print("Voltando para o menu principal...")
                    time.sleep(2)

            case 6:
                if cliente_atual != "" and cliente_atual in clientes_vips:
                    cliente_vip.acesso_exclusivo()
                    print("=" * 18)
                    print(f"Bem vindo(a) {nome}, o que deseja comprar hoje? ")
                    cliente_vip.comprar_itens_vip()
                    # valor = int(input("Digite quanto deseja gastar: R$"))
                    # print("=" * 18)
                    # cliente_vip.comprar_vip()
            
                else:
                    print("\nVocê não está logado ou não está na lista vip!")
                    time.sleep(2)
                    print("Voltando para o menu principal...")
                    time.sleep(2)

            case 7:
                print("Deslogando do sistema...")
                time.sleep(1) 
                print(f" \nVolte em breve {cliente_atual}!")
                cliente_atual = ""

            case 0:
                print("Encerrando script. Até mais...")
                break

            case _:
                print(f"A opção {opcao} é inválida. Tente novamente.")


if __name__ == "__main__":
    exercicio_01()






