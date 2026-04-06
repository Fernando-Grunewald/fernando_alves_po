class Cachorro:

    def __init__(self, nome="Apolo", raca="pastor alemão"):
        self.__nome = None
        self.__raca = None
        self.nome = nome
        self.raca = raca

    @property
    def nome(self):
        """
        Método Getter para retornar o nome do cachorro
        """
        return self.__nome

    @nome.setter
    def nome(self, valor):
        """
        Método Setter para validar o nome do cachorro
        """
        if not valor.replace(" ", "").isalpha():
            raise ValueError("Nome inválido para o cachorro!")
        self.__nome = valor

    @property
    def raca(self):
        """
        Método Getter para retornar a raça do cachorro
        """
        return self.__raca

    @raca.setter
    def raca(self, valor):
        """
        Método Setter para validar a raça do cachorro
        """
        if not valor.replace(" ", "").isalpha():
            raise ValueError("Raça inválida!")
        self.__raca = valor

    def latir(self):
        print(f" — Aquele {self.__raca} chamado {self.__nome} não para de latir!")
        print("\n Au Au Au!" * 3)