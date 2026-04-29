class Usuario5:
    def __init__(self, nome, email):
        if not Usuario5.validar_email(email):
            print("Email inválido!")
        else:
            print("Email válido. Parabéns!")
        self.nome = nome
        self.email = email

    @staticmethod
    def validar_email(email):
        """Método estático pra validar o email"""
        return "@" in email and "." in email

#=============================================================================

def exercicio_05():
    nome = input("Digite seu nome de usuário: ")
    email = input("Digite seu email para validarmos: ")

    usuario = Usuario5(nome, email)

    usuario.validar_email(email) # Levantou erro, o que eu esperava, mas não sei como fazer o programa encerrar normalmente.

    print("-" * 15)

# Exercício 5 – Criar usuário com validação de email 
# Permitir que o usuário digite nome e email. O construtor (__init__) deve usar o método 
# estático validar_email() para validar o email e lançar erro se for inválido.