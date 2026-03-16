class Livro:

    def __init__(self, nome_livro="Livro Sem Nome",):
        self.nome_livro = nome_livro
        self.lista_livros = []

    def adicionar_livro(self, bibliotecario):
        self.lista_livros.append(bibliotecario)

    def mostrar_livro(self):
        print(f"Livro: {self.nome_livro}")
        for e in self.lista_livros:
            e.emprestimo_registros()