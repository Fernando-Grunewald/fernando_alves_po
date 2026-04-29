class Titular:
    
    def __init__(self, titular="Fernando", saldo=0):
        self.__titular = None
        self.__saldo = None

        self.titular = titular
        self.saldo = saldo

    @property
    def titular(self):
        """
        Getter para retornar o nome do titular
        """
        return self.__titular

    @titular.setter
    def titular(self, valor):
        """
        Setter para validar o nome do titular
        """
        if not valor.replace(" ", "").isalpha():
            raise ValueError("Nome do titular inválido!")
        self.__titular = valor

    @property
    def saldo(self):
        """
        Getter para retornar o saldo
        """
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        """
        Setter para validar o saldo
        """
        if valor < 0:
            raise ValueError("Saldo não pode ser negativo!")
        self.__saldo = valor