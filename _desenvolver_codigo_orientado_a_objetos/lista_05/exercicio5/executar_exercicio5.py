# Regra comum para todos os exercícios:
# Toda interação com o usuário deve ser feita via menu interativo na função main() do 
# programa principal.
# O menu principal deve permitir que o usuário escolha qual exercício executar.
# Cada exercício está em um pacote próprio, com suas classes em módulos 
# separados.
# Para rodar o exercício, o menu deve importar e executar o módulo chamado 
# executar_respectivo_exercicioX.py (onde X é o número do exercício), que terá a 
# lógica para rodar aquele exercício, incluindo a interação via input().

# Exercício 5
# Projete um sistema com pelo menos 4 classes diferentes, cada uma com pelo menos 
# 2 métodos, que possam ser usadas de forma intercambiável graças ao polimorfismo 
# O sistema deve ter uma interface genérica para processar os objetos, independente 
# da classe concreta.

class Personagem:

class Geo:
    def __init__(self, visao, nome, arma, vida, ataque, defesa, habilidade_elemental, explosao_elemental):
        self.visao = visao
        self.nome = nome
        self.arma = arma
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.habilidade_elemental = habilidade_elemental
        self.explosao_elemental = explosao_elemental
    
    @classmethod
    def criar_personagem_geo(cls):
        print("Vamos criar um personagem do elemento geo!")
        try:
            visao = "Geo"
            nome = input("\n Nome do personagem: ")
            arma = input("Tipo de Arma: ")
            vida = int(input("Máximo de pontos de vida: "))
            ataque = int(input("Ataque base do personagem: "))
            defesa = int(input("Defesa do personagem: "))
            habilidade_elemental = input("Nome da habilidade elemental: ")
            explosao_elemental = input("Nome da explosão elemental: ")
            return cls(visao, nome, arma, vida, ataque, defesa, habilidade_elemental, explosao_elemental)
        
        except ValueError as erro:
            print(f"\n Erro: {erro}")
            return None
        
    def habilidade_q(self):
        print(f"A explosão elemental de {self.nome} é {self.explosao_elemental}")
        
    def habilidade_e(self):
        print(f"A habilidade elemental de {self.nome} é {self.habilidade_elemental}")