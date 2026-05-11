from base import Pagamento

class BoletoBancario(Pagamento):
    def __init__(self, valor, vencimento):
        super().__init__(valor)
        self.vencimento = vencimento

    def processar_pagamento(self):
        print(f"Boleto de R$ {self.valor} com vencimento em {self.vencimento}")