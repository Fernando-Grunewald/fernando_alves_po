class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def exibir_info(self):
        """Método de Instância"""
        print(f"Nome: {self.nome}")
        print(f"Email: {self.email}")

#==============================================

def exercicio_01():

    nome = input("Digite o nome de usuário: ")
    email = input("Digite o email: ")
    print("-" * 15)
    usuario = Usuario(nome, email)

    usuario.exibir_info()
    print("-" * 15)
    

# Exercício 1 – Criar e exibir um usuário 
# Criar um objeto da classe Usuario com nome e email inseridos pelo usuário e exibir 
# as informações usando o método de instância exibir_info().

