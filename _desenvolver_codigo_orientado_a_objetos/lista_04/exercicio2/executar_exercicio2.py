from exercicio2.utils import *
import time
from exercicio2.pagamento_com_notificacao import carregamento

def exercicio_02():

    transacao = PagamentoComNotificacao.valor_padrao()

    while True:
                print("\n [ MENU ]")

                print("[1] Confirmar Pagamento.")
                print("[2] Enviar comprovante.")
                print("[3] Finalizar compra.")
                print("[0] Sair.")
                try:
                    opcao = int(input("\nEscolha uma opção: "))
                except ValueError:
                    print("Entrada inválida.")
                    continue
                
                match opcao:

                    case 1:
                        try:
                            quantia = float(input("Boa tarde. Digite o valor do pagamento: R$"))
                        except ValueError as e:
                            print("Erro = ", e, ". Valor de transação padrão atribuída!")
                            transacao.valor_padrao()
                        transacao = PagamentoComNotificacao(quantia)
                        transacao.pagamento_feito()
                        carregamento()
                        print("\n [ INFO ] \n Estado do pagamento: ", transacao.confirmado)
                        transacao.tipo_pagamento()
                        input("Pressione enter para sair.")
                    case 2:
                        if transacao == 0:
                            print("Você não possui nenhuma transação atual!")
                        else:
                            transacao.notificar()
                            carregamento()
                            print("\n [ INFO ] \n Estado a transação: ", transacao.enviado)
                            transacao.tipo_notificao()
                            input("Pressione enter para sair.")
                    case 3:
                        if transacao.enviado == True: 
                            if transacao._valor != 0:
                                transacao.processar()
                                transacao.limpar()
                                input("Pressione enter para sair.")

                        else:
                            print("Você não possui nenhuma transção confirmada atual!")
                            continue
                    
                    case 0:
                        print("Até mais usuário!")
                        break

                    case _:
                        print("Opção inválida.")







