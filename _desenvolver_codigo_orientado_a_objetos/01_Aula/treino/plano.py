class PlanoTreino:

    def __init__(self, nome_plano="Plano vazio"):
        self.nome_plano = nome_plano
        self.lista_exercicios = []

    def adicionar_exercicio(self, exercicio):
        self.lista_exercicios.append(exercicio)

    def mostrar_plano(self):
        print(f"Plano de treino: {self.nome_plano}")
        for e in self.lista_exercicios:
            e.mostrar_exercicio()