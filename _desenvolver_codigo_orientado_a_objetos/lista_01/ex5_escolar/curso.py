class Curso:
    
    def __init__(self, materia="Matéria vazia"):
        self.materia = materia

    def mostrar_boletins(self):
        print(f"Curso de {self.materia}:")

    def adicionar_estudante(self, estudante):
        self.lista_curso = []
        self.lista_curso.append(estudante)

    def mostrar_notas(self):
        print(f"Curso de {self.materia}: ")
        for e in self.lista_curso:
            e.mostrar_boletins()
        media = sum(self.lista_curso)/len(self.lista_curso)
        print(f"A média das notas do aluno é de: {media}")
    

    