class Produto:
    def __init__(self, nome="Produto Genérico"):
        self.nome = nome
        self.categoria = "Geral"

    def descricao(self):
        print(f"{self.nome} está disponível na categoria '{self.categoria}'.")

class Camiseta(Produto):
    def __init__(self, nome="Camiseta", tamanho="M", cor="Branca"):
        super().__init__(nome)
        self.tamanho = tamanho
        self.cor = cor
        self.categoria = "Vestuário"

    def descricao(self):
        print(f"{self.nome} ({self.cor}, tamanho {self.tamanho}) está disponível na categoria '{self.categoria}'.")

item = Camiseta(tamanho="G", cor="Azul")
print(item.categoria)
item.descricao()