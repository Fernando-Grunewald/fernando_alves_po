class Categoria:

    def __init__(self, nome="Categoria Geral"):
        self.__nome = ""
        self.__filmes = []

        self.nome = nome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        if not valor.strip():
            raise ValueError("Nome da categoria inválido!")
        self.__nome = valor

    @property
    def filmes(self):
        return self.__filmes

    def adicionar_filme(self, filme):
        self.__filmes.append(filme)
        print(f"Filme '{filme.titulo}' adicionado à categoria '{self.__nome}'!")

    def listar_filmes(self):
        if not self.__filmes:
            print(f"Nenhum filme na categoria '{self.__nome}'.")
            return
        
        print(f"Categoria: {self.__nome}")
        print("-" * 20)
        for filme in self.__filmes:
            filme.detalhes_filme()
            print("-" * 20)