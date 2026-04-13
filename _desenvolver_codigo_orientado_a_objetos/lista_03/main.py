from utils import *
from imports import *

def lista_3():
   print("-" * 15)
   while True:

        print("Lista de Exercícios 3\n")
        print("[1] - Exercício 1.")
        print("[2] - Exercício 2.")
        print("[3] - Exercício 3.")
        print("[4] - Exercício 4.")
        print("[5] - Exercício 5.")
        print("[6] - Exercício 6.")
        print("[0] - Sair")
        print("-" * 15)

        opcao = int(input("Escolha uma opção: "))
        print("-" * 15)

        match opcao:
            case 1:
                exercicio_01()
            case 2:
                exercicio_02()
            case 0:
                print("Encerrando script. Até mais...")
                break
            case _:
                print(f" A opção {opcao} é inválida. Tente novamente.")
                
if __name__ == "__main__":
    lista_3()

# Todos os exercícios devem estar organizados em pacotes e módulos. O arquivo 
# principal main.py deve apresentar um menu de opções que chama os exercícios 
# por meio de seus respectivos módulos.

# Exercício 1 – Criar e exibir um usuário 
# Criar um objeto da classe Usuario com nome e email inseridos pelo usuário e exibir 
# as informações usando o método de instância exibir_info().

# Exercício 2 – Criar um usuário de teste 
# Usar o método de classe criar_usuario_teste() para instanciar um usuário padrão e 
# exibir seus dados usando o método de instância exibir_info().

# Exercício 3 – Validar uma lista de emails 
# Validar uma lista de emails, imprimindo se cada um é válido ou não, utilizando o 
# método estático validar_email().

# Exercício 4 – Enviar email de boas-vindas 
# Criar um usuário com nome e email fixos e chamar o método de instância 
# enviar_email_boas_vindas() para simular o envio de uma mensagem.

# Exercício 5 – Criar usuário com validação de email 
# Permitir que o usuário digite nome e email. O construtor (__init__) deve usar o método 
# estático validar_email() para validar o email e lançar erro se for inválido.

# Exercício 6 – Criar menu interativo 
# Criar um menu com opções para:
# 1. Criar um usuário de teste usando método de classe
# 2. Validar um email informado usando método estático
# 3. Criar usuário com validação de email usando método estático no construtor
# 4. Sair
# Cada opção deve chamar o método adequado de acordo com sua natureza.