class Exercicio:

    def __init__(self, nome="Exercício vazio", repeticoes=0):
        self.nome = nome
        self.repeticoes = repeticoes

    def mostrar_exercicio(self):
        print(f"Exercício: {self.nome}, Repetições: {self.repeticoes}")