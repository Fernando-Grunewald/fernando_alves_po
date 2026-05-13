class Mago:
    def __init__(self, classe):
        self.classe = classe

    def habilidade_principal(self):
        print(f" [ Seta de Gelo ] -> O {self.classe} carrega uma seta de gelo e a dispara contra o alvo causando dano e breve lentidão.")
        
    def habilidade_secundaria(self):
        print(f" [ Explosão de Fogo ] -> O {self.classe} prepara uma explosão concentrada de fogo no alvo que causa dano.")
    
    def habilidade_terciaria(self):
        print(f" [ Invisibilidade ] -> Em alguns segundos, o {self.classe} se torna invisível por 15 segundos até atacar alguém.")