class Bibliotecario:

    def __init__(self, nome_bibliotecario="", dias=0, valor=0.0):
        self.nome_bibliotecario = nome_bibliotecario
        self.dias = dias
        self.valor = valor

    def mostrar_emprestimos(self):
        print(f"Alugante: {self.nome_bibliotecario} / Dias: {self.dias} / Valor: {self.valor}.")