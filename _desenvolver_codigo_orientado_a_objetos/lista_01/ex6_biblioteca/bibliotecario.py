class Bibliotecario:
    def __init__(self, nome):
        self.nome = nome
        self.livros_emprestados = []

    def emprestar_livro(self, livro):
        sucesso = livro.emprestar(self.nome)

        if sucesso:
            self.livros_emprestados.append(livro)
            print("Livro emprestado com sucesso!")
        else:
            print("Livro não está disponível.")

    def devolver_livro(self, livro):
        if livro in self.livros_emprestados:
            livro.devolver()
            self.livros_emprestados.remove(livro)
            print("Livro devolvido!")
        else:
            print("Você não está com esse livro.")

    def mostrar_info(self):
        print(f"\nBibliotecário: {self.nome}")

        if len(self.livros_emprestados) == 0:
            print("Nenhum livro emprestado.")
        else:
            print("Livros emprestados:")
            for livro in self.livros_emprestados:
                print(f"- {livro.titulo}")