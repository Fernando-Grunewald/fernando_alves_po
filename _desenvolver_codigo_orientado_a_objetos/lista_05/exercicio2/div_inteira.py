class DivisaoInt:
    def __init__(self, valor):
        self.valor = valor

    def __floordiv__(self, outro_valor):
        return DivisaoInt(self.valor // outro_valor.valor)

    def __str__(self):
        return f"Divisão Inteira: {self.valor}"
