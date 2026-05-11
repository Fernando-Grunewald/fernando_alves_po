from base import Pagamento

class Pix(Pagamento):
    def __init__(self, valor, chave_pix):
        super().__init__(valor)
        self.chave_pix = chave_pix

    def processar_pagamento(self):
        print(f"Transferência PIX de R$ {self.valor} para {self.chave_pix}")