class Multiplicacao:
    def __init__(self, valor):
        self.valor = valor
    
    def __mul__(self, outro_valor):
        return Multiplicacao(self.valor * outro_valor.valor)
    
    def __str__(self):
        return f"Multiplicação: {self.valor}"