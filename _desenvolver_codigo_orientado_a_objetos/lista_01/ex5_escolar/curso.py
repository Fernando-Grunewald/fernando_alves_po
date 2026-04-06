class Curso:

    def __init__(self, nome="Técnico em Desenvolvimento de Sistemas"):
        self.__nome = ""
        self.__estudantes = []

        self.nome = nome

    @property
    def nome(self):
        """
        Getter para retornar o nome do curso
        """
        return self.__nome

    @nome.setter
    def nome(self, valor):
        """
        Setter para validar o nome do curso
        """
        if not valor.strip():
            raise ValueError("Nome do curso inválido!")
        self.__nome = valor

    @property
    def estudantes(self):
        """
        Getter para retornar a lista de estudantes
        """
        return self.__estudantes

    def adicionar_estudante(self, estudante):
        """
        Método para adicionar estudante ao curso
        """
        self.__estudantes.append(estudante)

    def listar_estudantes(self):
        """
        Método para listar estudantes
        """
        print(f"\nCurso: {self.__nome}")
        print("=" * 20)

        for estudante in self.__estudantes:
            estudante.mostrar_dados()
            print("-" * 20)