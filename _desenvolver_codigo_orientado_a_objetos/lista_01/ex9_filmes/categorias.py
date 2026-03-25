class Categoria:
    
    def __init__(self, nome="Categoria Geral"):
        self.nome = nome
        self.filmes = []

    def adicionar_filme(self, filme):
        self.filmes.append(filme)
        print(f"Filme '{filme.titulo}' adicionado à categoria '{self.nome}'!")

    def listar_filmes(self):
        if not self.filmes:
            print(f"Nenhum filme na categoria '{self.nome}'.")
            return
        
        print(f"Categoria: {self.nome}")
        print("-" * 20)
        for filme in self.filmes:
            filme.detalhes_filme()
            print("-" * 20)