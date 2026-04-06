class Gato:

    def __init__(self, nome="Nix", cor="preta"):
        self.__nome = None
        self.__cor = None
        self.nome = nome
        self.cor = cor

    @property
    def nome(self):
        """
        Método Getter para retornar o nome do gato
        """
        return self.__nome

    @nome.setter
    def nome(self, valor):
        """
        Método Setter para validar o nome do gato
        """
        if not valor.replace(" ", "").isalpha():
            raise ValueError("Nome inválido para o gato!")
        self.__nome = valor

    @property
    def cor(self):
        """
        Método Getter para retornar a cor do gato
        """
        return self.__cor

    @cor.setter
    def cor(self, valor):
        """
        Método Setter para validar a cor do gato
        """
        if not valor.replace(" ", "").isalpha():
            raise ValueError("Cor inválida!")
        self.__cor = valor

    def miar(self):
        print(f" — Aquela gatinha {self.__cor} chamada {self.__nome} está miando sem parar!")
        print("\n Miau Miau Miau Miau!" * 3)