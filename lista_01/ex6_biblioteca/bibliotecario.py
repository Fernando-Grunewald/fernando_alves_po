class Bibliotecario:

    def __init__(self, nome="Bibliotecário Vazio"):
        self.__nome = ""
        self.__livros_emprestados = []

        self.nome = nome

    @property
    def nome(self):
        """
        Getter para retornar o nome do bibliotecário
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
    def livros_emprestados(self):
        """
        Getter para retornar os livros emprestados
        """
        return self.__livros_emprestados

    def emprestar_livro(self, livro):
        """
        Método para emprestar um livro
        """
        sucesso = livro.emprestar(self.__nome)

        if sucesso:
            self.__livros_emprestados.append(livro)
            print("Livro emprestado com sucesso!")
        else:
            print("Livro não está disponível.")

    def devolver_livro(self, livro):
        """
        Método para devolver um livro
        """
        if livro in self.__livros_emprestados:
            livro.devolver()
            self.__livros_emprestados.remove(livro)
            print("Livro devolvido!")
        else:
            print("Você não está com esse livro.")

    def mostrar_info(self):
        """
        Método para mostrar informações do bibliotecário
        """
        print(f"\nBibliotecário: {self.__nome}")

        if len(self.__livros_emprestados) == 0:
            print("Nenhum livro emprestado.")
        else:
            print("Livros emprestados:")
            for livro in self.__livros_emprestados:
                print(f"- {livro.titulo}")