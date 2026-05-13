from exercicio3.mago import Mago

class Mago_Flamejante(Mago):
    def __init__(self, classe):
        Mago.__init__(self, classe)

    def habilidade_principal(self):
        print(f" [ Bola de Fogo ] -> Carrega uma bola de fogo que a lança contra o alvo. Diminuindo a recarga de Combustão para o {self.classe} se causar acerto crítico.")
    
    def habilidade_secundaria(self):
        print(f" [ Explosão de Fogo ] -> O {self.classe} prepara uma explosão concentrada de fogo no alvo que causa dano. Adicionalmente, a Explosão de Fogo ganha uma chance de acerto crítico quase garantida.")
    
    def habilidade_terciaria(self):
        print(f" [ Combustão ] -> O {self.classe} entre em um estado de combustão por 10 segundos, a Explosão de Fogo é instantânea e não têm mais recarga.")