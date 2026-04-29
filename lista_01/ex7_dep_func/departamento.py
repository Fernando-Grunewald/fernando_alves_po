class Departamento:

    def __init__(self, nome="Departamento de Funcionários"):
        self.__nome = ""
        self.__funcionarios = []

        self.nome = nome

    @property
    def nome(self):
        """
        Getter para retornar o nome do departamento
        """
        return self.__nome

    @nome.setter
    def nome(self, valor):
        """
        Setter para validar o nome do departamento
        """
        if not valor.strip():
            raise ValueError("Nome inválido!")
        self.__nome = valor

    @property
    def funcionarios(self):
        """
        Getter para retornar a lista de funcionários
        """
        return self.__funcionarios

    def adicionar_funcionario(self, funcionario):
        """
        Método para adicionar funcionário
        """
        self.__funcionarios.append(funcionario)

    def listar_funcionarios(self):
        """
        Método para listar funcionários
        """
        if not self.__funcionarios:
            print("Nenhum funcionário cadastrado.")
            return
        
        for funcionario in self.__funcionarios:
            funcionario.atributos_funcionario()
            print("-" * 20)