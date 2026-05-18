# Regra comum para todos os exercícios:
# Toda interação com o usuário deve ser feita via menu interativo na função main() do 
# programa principal.
# O menu principal deve permitir que o usuário escolha qual exercício executar.
# Cada exercício está em um pacote próprio, com suas classes em módulos 
# separados.
# Para rodar o exercício, o menu deve importar e executar o módulo chamado 
# executar_respectivo_exercicioX.py (onde X é o número do exercício), que terá a 
# lógica para rodar aquele exercício, incluindo a interação via input().

# Exercício 4
# Combine os conceitos anteriores: crie pelo menos 4 classes em hierarquia, com 
# métodos compartilhados e operadores redefinidos.
# Implemente a interação para criar e manipular objetos desses tipos via menu, usando 
# polimorfismo com funções, operadores e herança.

class Mago:
    def __init__(self, nome, raca, nivel):
        self.nome = nome
        self.raca = raca
        self.nivel = nivel
        
    @classmethod
    def criar_mago(cls):
        print("Vamos criar um mago!")
        try:
            nome = input("\nNome: ")
            raca = input("Raça do personagem: ")
            nivel = int(input("Digite o Nível:"))
            # while True:
            #     print("\n [ Escolha a especialzação dele!")
            #     print(" [ Mago Gélido - 1")
            #     print(" [ Mago Arcano - 2")
            #     print(" [ Mago Flamejante - 3")
            #     especializacao = int(input("\n Digite aqui: "))
                
            #     match especializacao:
            #         case 1:
            #             especializacao = "Mago Gélido"
            #             break
                        
            #         case 2:
            #             especializacao = "Mago Arcano"
            #             break
                        
            #         case 3:
            #             especializacao = "Mago Flamejante"
            #             break
                        
            #         case _:
            #             print("\n Você precisa digitar 1 , 2 OU 3!")
            # subclasse = especializacao
            return cls(nome, raca, nivel)
            
        except ValueError as erro:
            print(f"\n Erro: {erro}")
            return None
        
            
class MagoArcano(Mago):
    def __init__(self, nome, raca, nivel):
        super().__init__(nome, raca, nivel)
    
class LancaFeiticos(MagoArcano or MagoGélido):
    pass
    
    
    
        
    
        