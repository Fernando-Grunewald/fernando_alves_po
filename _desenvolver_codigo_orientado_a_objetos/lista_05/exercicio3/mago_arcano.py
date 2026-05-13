from exercicio3.mago import Mago

class Mago_Arcano(Mago):
    def __init__(self, classe):
        Mago.__init__(self, classe)
    
    def habilidade_principal(self):
        print(f" [ Impacto Arcano ] -> Casta brevemente um glifo sobre o inimigo que causa dano. Esse glifo concede ao {self.classe} uma Carga Arcana, causa mais dano e consome mais dano conforme o número delas e têm chance de conceder Abstração.")

    def habilidade_secundaria(self):
        print(f" [ Salva Arcana ] -> O {self.classe} libera dois projéteis rodopiantes que atacam um inimigo, causando mais dano conforme as Cargas Arcanas. Ter Abstração faz com que a Salva Arcana gere 4 Cargas Arcanas")

    def habilidade_terciaria(self):
        print(f" [ Invisibilidade Maior ] -> Instantâneamente, o {self.classe} se torna invisível por 45 segundos até atacar alguém.")