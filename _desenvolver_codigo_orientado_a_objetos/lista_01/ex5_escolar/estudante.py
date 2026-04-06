class Estudante:

    def __init__(self, nome="Nome Vazio", idade=1, matricula="000"):
        self.__nome = ""
        self.__idade = 0
        self.__matricula = ""
        self.__notas = []

        self.nome = nome
        self.idade = idade
        self.matricula = matricula

    @property
    def nome(self):
        """
        Getter para retornar o nome do estudante
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
    def idade(self):
        """
        Getter para retornar a idade
        """
        return self.__idade

    @idade.setter
    def idade(self, valor):
        """
        Setter para validar a idade
        """
        if valor <= 0:
            raise ValueError("Idade inválida!")
        self.__idade = valor

    @property
    def matricula(self):
        """
        Getter para retornar a matrícula
        """
        return self.__matricula

    @matricula.setter
    def matricula(self, valor):
        """
        Setter para validar a matrícula
        """
        if len(valor) < 3:
            raise ValueError("Matrícula inválida!")
        self.__matricula = valor

    @property
    def notas(self):
        """
        Getter para retornar as notas
        """
        return self.__notas

    def adicionar_nota(self, nota):
        """
        Método para adicionar nota
        """
        if nota < 0 or nota > 10:
            raise ValueError("Nota inválida! (0 a 10)")
        self.__notas.append(nota)

    def calcular_media(self):
        """
        Método para calcular a média
        """
        if len(self.__notas) == 0:
            return 0
        return sum(self.__notas) / len(self.__notas)

    def mostrar_dados(self):
        """
        Método para mostrar os dados do estudante
        """
        print(f"Nome: {self.__nome}")
        print(f"Idade: {self.__idade}")
        print(f"Matrícula: {self.__matricula}")
        print(f"Notas: {self.__notas}")
        print(f"Média: {self.calcular_media():.2f}")
    
    
