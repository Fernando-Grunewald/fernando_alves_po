class Estudante:

    def __init__(self, nome_aluno="Para registrar", idade=0, matricula="0000000"):
        self.nome_aluno = nome_aluno
        self.idade = idade
        self.matricula = matricula
        self.lista_notas = []

    def adicionar_estudante(self, estudante):
        self.lista_notas.append(estudante)

    def mostrar_notas(self):
        print(f"Curso de {self.curso}:")
        for e in self.lista_notas:
            e.mostrar_boletim()
        media = sum(self.lista_notas)/len(self.lista_notas)
        print(f"A média das notas do aluno é de: {media}")
    
