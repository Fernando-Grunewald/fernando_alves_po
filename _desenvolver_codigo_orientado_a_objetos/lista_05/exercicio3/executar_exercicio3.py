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

"""
Exercício 3 que usa hierarquia de classes para criar uma classe que passa seus 3 métodos para 3 outras subclasses. Cada uma das 4 classes sobreescreve seus métodos de mesmo nome com descrições diferentes.
O programa executa de forma automatica a criação dos 4 objetos para evidenciar dentro de um laço for que os métodos são alterados para cada objeto de acordo com sua classe respectiva.
O exercício me deu liberdade criativa para criar classes de acordo com a classe e as subclasses de magos em Wolrd of Warcraft.

Autor: Fernando Alves Grunevald
Data: 13/05/2026    
"""

from exercicio3.utils import *

def magos_wow():
    subclasses_magos = [
        Mago("Mago"),
        Mago_Gélido("Mago Gélido"),
        Mago_Flamejante("Mago de Fogo"),
        Mago_Arcano("Mago Arcano")]
    
    print("=" * 30)
    
    for mago in subclasses_magos:
        print(f"\n [ Classe - {mago.classe}] ")
        mago.habilidade_principal()
        mago.habilidade_secundaria()
        mago.habilidade_terciaria()
        print("\n ")
        print("=" * 200)
        
if __name__ == "__main__":
    magos_wow()
    
    


    
    