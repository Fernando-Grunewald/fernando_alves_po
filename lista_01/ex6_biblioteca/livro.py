class Livro:

    def __init__(self, titulo="Título Vazio"):
        self.__titulo = ""
        self.__disponivel = True
        self.__historico = []

        self.titulo = titulo

    @property
    def titulo(self):
        """
        Getter para retornar o título do livro
        """
        return self.__titulo

    @titulo.setter
    def titulo(self, valor):
        """
        Setter para validar o título
        """
        if not valor.strip():
            raise ValueError("Título inválido!")
        self.__titulo = valor

    @property
    def disponivel(self):
        """
        Getter para verificar se o livro está disponível
        """
        return self.__disponivel

    def emprestar(self, nome_usuario):
        """
        Método para emprestar livro
        """
        if self.__disponivel:
            self.__disponivel = False
            self.__historico.append(nome_usuario)
            return True
        return False

    def devolver(self):
        """
        Método para devolver livro
        """
        self.__disponivel = True

    def mostrar_info(self):
        """
        Método para mostrar informações do livro
        """
        status = "Disponível" if self.__disponivel else "Emprestado"
        print(f"Livro: {self.__titulo}")
        print(f"Status: {status}")
        print(f"Histórico: {self.__historico}")