class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __add__(self, outro):
        return self.preco + outro.preco

p1 = Produto("Camisa", 50)
p2 = Produto("Calça", 80)
print(p1 + p2)