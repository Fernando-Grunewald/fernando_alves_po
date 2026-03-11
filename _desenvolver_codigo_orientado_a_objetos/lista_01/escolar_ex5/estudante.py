class Estudante:

    def __init__(self, nome_aluno="Para registrar", idade=0, matricula="0000000"):
        self.nome_aluno = nome_aluno
        self.lista_notas = []

    def adicionar_notas(self, nota):
        self.lista_notas.append(nota)

    def mostrar_notas(self):
        print(f"Boletim de {self.nome_aluno}:")
        for i in self.lista_notas:
            i.mostrar_boletim()
        media = sum(self.lista_notas)/len(self.lista_notas)
        print(f"A média das notas do aluno é de: {media}")
    
