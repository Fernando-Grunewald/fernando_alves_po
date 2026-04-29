class Funcionario:

    def __init__(self, nome="Nome Vazio", cpf="00000000000", telefone="000000000", salario=0):
        self.__nome = ""
        self.__cpf = ""
        self.__telefone = ""
        self.__salario = 0.0

        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.salario = salario

    @property
    def nome(self):
        """
        Getter para retornar o nome do funcionário
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

    @property
    def cpf(self):
        """
        Getter para retornar o CPF
        """
        return self.__cpf

    @cpf.setter
    def cpf(self, valor):
        """
        Setter para validar o CPF (apenas números)
        """
        if not valor.isdigit() or len(valor) != 11:
            raise ValueError("CPF inválido! Deve ter 11 números.")
        self.__cpf = valor

    @property
    def telefone(self):
        """
        Getter para retornar o telefone
        """
        return self.__telefone

    @telefone.setter
    def telefone(self, valor):
        """
        Setter para validar o telefone
        """
        if not valor.isdigit():
            raise ValueError("Telefone inválido!")
        self.__telefone = valor

    @property
    def salario(self):
        """
        Getter para retornar o salário
        """
        return self.__salario

    @salario.setter
    def salario(self, valor):
        """
        Setter para validar o salário
        """
        if valor < 0:
            raise ValueError("Salário não pode ser negativo!")
        self.__salario = valor

    def editar_salario(self, novo_salario):
        """
        Método para atualizar o salário
        """
        self.salario = novo_salario
        print(f"Salário de {self.__nome} atualizado para R${self.__salario:.2f}")

    def atributos_funcionario(self):
        """
        Método para mostrar os dados do funcionário
        """
        print(f"Funcionário: {self.__nome}")
        print(f"CPF: {self.__cpf}")
        print(f"Telefone: {self.__telefone}")
        print(f"Salário: R${self.__salario:.2f}")
        
        

