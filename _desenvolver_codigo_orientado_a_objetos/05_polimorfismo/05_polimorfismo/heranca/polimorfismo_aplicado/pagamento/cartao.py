from base import Pagamento

class CartaoCredito(Pagamento):
    def __init__(self, valor, numero_cartao):
        super().__init__(valor)
        self.numero_cartao = numero_cartao

    def processar_pagamento(self):
        print(f"Cartão {self.numero_cartao} processando R$ {self.valor}...")