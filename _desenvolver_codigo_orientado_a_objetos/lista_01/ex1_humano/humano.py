class Pessoa:

    def __init__(self, nome="Fernando", idade=60):
        self.__nome = None
        self.__idade = None
        self.nome = nome
        self.idade = idade

    @property
    
    def nome(self):
        """
        Método Getter para retornar o nome da classe Pessoa
        """
        return self.__nome

    @nome.setter
    def nome(self, valor):
        """
        Método do Setter para validar o nome com letras
        """
        if not valor.replace(" ", "").isalpha():
            raise ValueError("Nome inválido! Use apenas letras.")
        self.__nome = valor

    @property
    def idade(self):
        """
        Método Getter para retornar a idade da classe Pessoa
        """
        return self.__idade

    @idade.setter
    def idade(self, valor):
        """
        Método Setter para validar uma idade normal
        """
        if not (1 <= valor <= 100):
            raise ValueError("Idade deve ser entre 1 e 100.")
        self.__idade = valor

    def apresentacao_pessoal(self):
        print(f"Seu nome é {self.__nome}, e sua idade é {self.__idade}.")