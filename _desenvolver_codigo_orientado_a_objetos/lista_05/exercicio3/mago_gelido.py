from exercicio3.mago import Mago

class Mago_Gélido(Mago):
    def __init__(self, classe):
        Mago.__init__(self, classe)
        
    def habilidade_principal(self):
        print(f" [ Seta de Gelo ] -> O {self.classe} carrega uma seta de gelo e a dispara contra o alvo causando dano e breve lentidão, invocando 1 sincelo de gelo.")

    def habilidade_secundaria(self):
        print(f" [ Lança de Gelo ] -> Até 5 sincelos do {self.classe} são atirados contra um inimigo de uma vez só junto de uma lança de gelo que causa crítico a inimigos congelados.")
    
    def habilidade_terciaria(self):
        print(f" [ Nova de Gelo ] -> O {self.classe} emite uma onda de gelo envolta de si que congela todos os inimigos próximos.")