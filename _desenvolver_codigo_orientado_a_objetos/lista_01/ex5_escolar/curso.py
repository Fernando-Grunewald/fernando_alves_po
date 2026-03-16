class Curso:
    
    def __init__(self, materia="Matéria vazia", nota=0):
        self.materia = materia
        self.nota = nota

    def mostrar_boletim(self):
        print(f"Curso de {self.materia} - {self.nota}")