class Estudante:
    def __init__(self, nome="Nome Vazio", idade="Idade Vazia", matricula="Matricula Vazia"):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula
        self.notas = []

    def adicionar_nota(self, nota):
        self.notas.append(nota)

    def calcular_media(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Notas: {self.notas}")
        print(f"Média: {self.calcular_media():.2f}")

    
    
