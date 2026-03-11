class Curso:
    
    def __init__(self, materia="Maéria vazia", repeticoes=0):
        self.materia = materia
        self.repeticoes = repeticoes

    def mostrar_boletim(self):
        print(f"Curso de {self.nome}: Repetições: {self.repeticoes}")