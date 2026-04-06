class Cliente:

    def __init__(self, nome="Cliente Vazio"):
        self.__nome = ""

        self.nome = nome

    @property
    def nome(self):
        """
        Getter para retornar o nome do cliente
        """
        return self.__nome

    @nome.setter
    def nome(self, valor):
        """
        Setter para validar o nome
        """
        if not valor.replace(" ", "").isalpha():
            raise ValueError("Nome inválido!")
        self.__nome = valor

    def comprar(self, produto, quantidade):
        """
        Método para realizar compra
        """
        produto.reduzir_estoque(quantidade)
        total = produto.preco * quantidade

        print("Compra realizada!")
        print(f"Cliente: {self.__nome}")
        print(f"Produto: {produto.nome}")
        print(f"Quantidade: {quantidade}")
        print(f"Total: R${total:.2f}")