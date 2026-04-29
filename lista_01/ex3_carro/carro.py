class Carro:

    def __init__(self, marca="Volkswagen", quilometragem=25000, placa="FR7D36"):
        self.__marca = None
        self.__quilometragem = None
        self.__placa = None

        self.marca = marca
        self.quilometragem = quilometragem
        self.placa = placa

    @property
    def marca(self):
        """
        Método Getter para retornar a marca do carro
        """
        return self.__marca

    @marca.setter
    def marca(self, valor):
        """
        Método Setter para validar a marca do carro
        """
        if not valor.replace(" ", "").isalpha():
            raise ValueError("Marca inválida!")
        self.__marca = valor

    @property
    def quilometragem(self):
        """
        Método Getter para retornar a quilometragem do carro
        """
        return self.__quilometragem

    @quilometragem.setter
    def quilometragem(self, valor):
        """
        Método Setter para validar a quilometragem
        """
        if valor < 0:
            raise ValueError("Quilometragem não pode ser negativa!")
        self.__quilometragem = valor

    @property
    def placa(self):
        """
        Método Getter para retornar a placa do carro
        """
        return self.__placa

    @placa.setter
    def placa(self, valor):
        """
        Método Setter para validar a placa do carro
        """
        if len(valor) < 6:
            raise ValueError("Placa inválida!")
        self.__placa = valor.upper()

    def atualizar_placa(self, nova_placa):
        """
        Método para atualizar a placa do carro
        """
        self.placa = nova_placa
        print(f"A nova placa do seu {self.__marca} é: {self.__placa}")

    def atualizar_quilometragem(self, nova_quilometragem):
        """
        Método para somar a quilometragem do carro
        """
        if nova_quilometragem < 0:
            raise ValueError("Valor inválido de quilometragem!")
        
        self.__quilometragem += nova_quilometragem
        print(f"O seu carro {self.__marca} andou um total de {self.__quilometragem} quilômetros!")