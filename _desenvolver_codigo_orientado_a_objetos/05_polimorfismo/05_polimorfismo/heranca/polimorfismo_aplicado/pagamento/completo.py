class Pagamento:
    def __init__(self, valor):
        self.valor = valor

    def processar_pagamento(self):
        print(f"Processando pagamento genérico de R$ {self.valor}")

class CartaoCredito(Pagamento):
    def __init__(self, valor, numero_cartao):
        super().__init__(valor)
        self.numero_cartao = numero_cartao

    def processar_pagamento(self):
        print(f"Cartão {self.numero_cartao} processando R$ {self.valor}...")

class BoletoBancario(Pagamento):
    def __init__(self, valor, vencimento):
        super().__init__(valor)
        self.vencimento = vencimento

    def processar_pagamento(self):
        print(f"Boleto de R$ {self.valor} com vencimento em {self.vencimento}")

class Pix(Pagamento):
    def __init__(self, valor, chave_pix):
        super().__init__(valor)
        self.chave_pix = chave_pix

    def processar_pagamento(self):
        print(f"Transferência PIX de R$ {self.valor} para {self.chave_pix}")


pagamentos = [
    CartaoCredito(150.0, "1234-5678-9012-3456"),
    BoletoBancario(200.0, "15/08/2025"),
    Pix(50.0, "cliente@exemplo.com")
]

for p in pagamentos:
    p.processar_pagamento()