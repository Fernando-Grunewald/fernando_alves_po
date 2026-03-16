class Usuario:

    def __init__(self, nome="Sem nome", idade=0):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, eu sou {self.nome} e tenho {self.idade} anos.")