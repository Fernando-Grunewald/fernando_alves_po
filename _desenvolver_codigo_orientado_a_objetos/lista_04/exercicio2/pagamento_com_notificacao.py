from exercicio2.pagamento import Pagamento
from exercicio2.notificacao import Notificacao
import time

class PagamentoComNotificacao(Pagamento, Notificacao): # Herando duas classes
    def __init__(self, valor):
        Pagamento.__init__(self, valor)
        Notificacao.__init__(self)

    def processar(self):
        """Método que une dois métodos herdados por Pagamento e Notificação"""
        self.pagamento_feito()
        self.tipo_pagamento()
        self.notificar()
        self.tipo_notificao()

    def limpar(self):
        """Método para a notificação quebrar ao ser finalizada"""
        self._valor = 0
        self.confirmado = False
        self.enviado = False

def carregamento():
    """Função para imersão no código"""
    print("\n Processando... Aguarde!")
    t = 0
    for t in range(3):
        t += 1
        time.sleep(1)
        print(f"\n {t}... \n")