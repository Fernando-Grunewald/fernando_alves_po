class Potencia:
    def __init__(self, valor):
        self.valor = valor

    def __pow__(self, outro_valor):
        return Potencia(self.valor ** outro_valor.valor)
    
    def __str__(self):
        return f"Potência: {self.valor}"