class Curso:
    def __init__(self, nome="Técnico em Desenvolvimento de Sistemas"):
        self.nome = nome
        self.estudantes = []

    def adicionar_estudante(self, estudante):
        self.estudantes.append(estudante)

    def listar_estudantes(self):
        print(f"\nCurso: {self.nome}")
        print("=" *20)
        for estudante in self.estudantes:
            estudante.mostrar_dados()
            print("-" * 20)
    