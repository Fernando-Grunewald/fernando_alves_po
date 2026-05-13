# Regra comum para todos os exercícios:
# Toda interação com o usuário deve ser feita via menu interativo na função main() do 
# programa principal.
# O menu principal deve permitir que o usuário escolha qual exercício executar.
# Cada exercício está em um pacote próprio, com suas classes em módulos 
# separados.
# Para rodar o exercício, o menu deve importar e executar o módulo chamado 
# executar_respectivo_exercicioX.py (onde X é o número do exercício), que terá a 
# lógica para rodar aquele exercício, incluindo a interação via input().

# Exercício 3
# Crie uma hierarquia com uma classe base e pelo menos 3 subclasses total de 4 
# classes.
# Cada classe deve ter pelo menos 2 métodos, e as subclasses devem sobrescrever 
# algum método da base com implementações próprias.
# Crie objetos das subclasses e execute os métodos para evidenciar o polimorfismo.

class Mago:
    def __init__(self, classe):
        self.classe = classe

    def habilidade_principal(self):
        print(f" [ Seta de Gelo ] = O {self.classe} carrega uma seta de gelo e a dispara contra o alvo causando dano e breve lentidão.")
        
    def habilidade_secundaria(self):
        print(f" [ Explosão de Fogo ] = O {self.classe} prepara uma explosão concentrada de fogo no alvo que causa dano.")
    
    def habilidade_terciaria(self):
        print(f" [ Invisibilidade ] = Em alguns segundos, o {self.classe} se torna invisível por 15 segundos até atacar alguém.")

class Mago_Gélido(Mago):
    def __init__(self, classe):
        Mago.__init__(self, classe)
        
    def habilidade_principal(self):
        return super().habilidade_principal(print(f" Adicionalmente, por ser um {self.classe}, usar Seta de Gelo invoca 1 sincelo de gelo."))

    def habilidade_secundaria(self):
        print(f" [ Lança de Gelo ] = Até 5 sincelos do {self.classe} são atirados contra um inimigo de uma vez só junto de uma lança de gelo que causa crítico a inimigos congelados.")
    
    def habilidade_terciaria(self):
        print(f" [ Nova de Gelo ] = O {self.classe} emite uma onda de gelo envolta de si que congela todos os inimigos próximos.")

class Mago_Flamejante(Mago):
    def __init__(self, classe):
        Mago.__init__(self, classe)

    def habilidade_principal(self):
        print(f" [ Bola de Fogo ] = Carrega uma bola de fogo que a lança contra o alvo. Diminuindo a recarga de Combustão para o {self.classe} se causar acerto crítico.")
    
    def habilidade_secundaria(self):
        return super().habilidade_secundaria(print(f" [ Adicionalmente, por ser um {self.classe} a Explosão de Fogo ganha uma chance de acerto crítico quase garantida."))
    
    def habilidade_terciaria(self):
        print(f" [ Combustão ] = O {self.classe} entre em um estado de combustão por 10 segundos, a Explosão de Fogo é instantânea e não têm mais recarga.")

class Mago_Arcano(Mago):
    def __init__(self, classe):
        Mago.__init__(self, classe)
    
    def habilidade_principal(self):
        print(f" [ Impacto Arcano ] = Casta brevemente um glifo sobre o inimigo que causa dano. Esse glifo concede ao {self.classe} uma Carga Arcana, causa mais dano e consome mais dano conforme o número delas e têm chance de conceder Abstração.")

    def habilidade_secundaria(self):
        print(f" [ Salva Arcana ] = O {self.classe} libera dois projéteis rodopiantes que atacam um inimigo, causando mais dano conforme as Cargas Arcanas. Ter Abstração faz com que a Salva Arcana gere 4 Cargas Arcanas")

    def habilidade_terciaria(self):
        return super().habilidade_terciaria(print(f" [ Adicionalmente, por ser um {self.classe} a Invisibildiade se transforma em Invisibilidade Maior, sendo instantânea e durando 45 segundos."))