class Pagamento:
    def __init__(self, valor):
        self.valor = valor

    def processar_pagamento(self):
        print(f"Processando pagamento genérico de R$ {self.valor}")