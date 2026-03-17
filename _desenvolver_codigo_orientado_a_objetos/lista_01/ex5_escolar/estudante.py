class Estudante:

    def __init__(self, nome_aluno="Para registrar", idade=0, matricula="0000000", nota=0):
        self.nome_aluno = nome_aluno
        self.idade = idade
        self.matricula = matricula
        self.nota = nota
        self.lista_curso = []

    def adicionar_estudante(self, estudante):
        self.lista_curso.append(estudante)

    def mostrar_notas(self):
        print(f"Curso de {self.materia}: ")
        for e in self.lista_curso:
            e.mostrar_boletins()
        media = sum(self.lista_curso)/len(self.lista_curso)
        print(f"A média das notas do aluno é de: {media}")
    

    
    
