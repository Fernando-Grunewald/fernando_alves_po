class Produto:
    
    def __init__(self, nome="Produto Vazio", preco=0, estoque=0):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def atualizar_estoque(self):
        try:
            quantidade = int(input(f"Adicionar quantidade ao estoque de {self.nome}: "))
            self.estoque += quantidade
            print("Estoque atualizado!")
        except:
            print("Não foi possível atualizar o estoque!")

    def reduzir_estoque(self, quantidade):
        if quantidade <= self.estoque:
            self.estoque -= quantidade
            return True
        else:
            print("Estoque insuficiente!")
            return False

    def mostrar_produto(self):
        print(f"Nome do Produto: {self.nome}")
        print(f"Preço: R${self.preco:.2f}")
        print(f"Estoque: {self.estoque}")

