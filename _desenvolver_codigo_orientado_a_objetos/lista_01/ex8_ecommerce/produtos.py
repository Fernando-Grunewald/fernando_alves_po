class Produto:

    def __init__(self, nome="Produto Vazio", preco=0.0, estoque=0):
        self.__nome = ""
        self.__preco = 0.0
        self.__estoque = 0

        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    @property
    def nome(self):
        """
        Getter para retornar o nome do produto
        """
        return self.__nome

    @nome.setter
    def nome(self, valor):
        """
        Setter para validar o nome
        """
        if not valor.strip():
            raise ValueError("Nome inválido!")
        self.__nome = valor

    @property
    def preco(self):
        """
        Getter para retornar o preço
        """
        return self.__preco

    @preco.setter
    def preco(self, valor):
        """
        Setter para validar o preço
        """
        if valor < 0:
            raise ValueError("Preço inválido!")
        self.__preco = valor

    @property
    def estoque(self):
        """
        Getter para retornar o estoque
        """
        return self.__estoque

    @estoque.setter
    def estoque(self, valor):
        """
        Setter para validar o estoque
        """
        if valor < 0:
            raise ValueError("Estoque inválido!")
        self.__estoque = valor

    def adicionar_estoque(self, quantidade):
        """
        Método para adicionar ao estoque
        """
        if quantidade <= 0:
            raise ValueError("Quantidade inválida!")
        self.__estoque += quantidade
        print("Estoque atualizado!")

    def reduzir_estoque(self, quantidade):
        """
        Método para reduzir estoque
        """
        if quantidade <= 0:
            raise ValueError("Quantidade inválida!")

        if quantidade > self.__estoque:
            raise ValueError("Estoque insuficiente!")

        self.__estoque -= quantidade
