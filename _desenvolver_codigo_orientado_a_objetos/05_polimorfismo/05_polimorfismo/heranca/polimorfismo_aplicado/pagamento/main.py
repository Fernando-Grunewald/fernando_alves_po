from cartao import CartaoCredito
from boleto import BoletoBancario
from pix import Pix

def menu_pagamentos():
    while True:
        print(" Pagamentos ")
        print("1 - Cartão de Crédito")
        print("2 - Boleto Bancário")
        print("3 - PIX")
        print("4 - Sair")
        escolha = input("Escolha uma opção: ").strip()

        if escolha == "1":
            valor = float(input("Digite o valor do pagamento: "))
            numero = input("Digite o número do cartão: ")
            pagamento = CartaoCredito(valor, numero)
            pagamento.processar_pagamento()

        elif escolha == "2":
            valor = float(input("Digite o valor do boleto: "))
            vencimento = input("Digite a data de vencimento (dd/mm/aaaa): ")
            pagamento = BoletoBancario(valor, vencimento)
            pagamento.processar_pagamento()

        elif escolha == "3":
            valor = float(input("Digite o valor da transferência PIX: "))
            chave = input("Digite a chave PIX: ")
            pagamento = Pix(valor, chave)
            pagamento.processar_pagamento()

        elif escolha == "4":
            print("Encerrando o sistema de pagamentos.")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_pagamentos()