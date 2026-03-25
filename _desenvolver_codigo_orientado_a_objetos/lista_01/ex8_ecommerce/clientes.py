class Cliente:
    
    def __init__(self, nome="Cliente Vazio"):
        self.nome = nome

    def comprar(self, produto):
        try:
            quantidade = int(input(f"{self.nome}, quantos '{produto.nome}' deseja comprar? "))

            if produto.reduzir_estoque(quantidade):
                total = produto.preco * quantidade
                print(f"Compra realizada!")
                print(f"Total: R${total:.2f}")
        except:
            print("Valor inválido!")