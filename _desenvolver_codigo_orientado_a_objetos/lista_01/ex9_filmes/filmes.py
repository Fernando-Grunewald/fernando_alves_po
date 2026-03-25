class Filme:
    
    def __init__(self, titulo="Filme sem título", diretor="Desconhecido", ano=0):
        self.titulo = titulo
        self.diretor = diretor
        self.ano = ano

    def detalhes_filme(self):
        print(f"Título: {self.titulo}")
        print(f"Diretor: {self.diretor}")
        print(f"Ano: {self.ano}")