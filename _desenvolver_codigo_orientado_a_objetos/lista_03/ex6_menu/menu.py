class Usuario6:
    def __init__(self, nome, email, senha):
        if not Usuario6.validar_email(email):
            print("Email inválido!")
        else:
            print("Email válido. Parabéns!")
        self.nome = nome
        self.email = email
        self.senha = senha

    @classmethod
    def criar_usuario_teste(cls):
        print("Usuário criado!")
        return cls("UsuarioTeste", "usuariotest@gmail.com", "12345")

    @staticmethod
    def validar_email(email):
        return "@" in email and "." in email
    
#=============================================================================

def menu_interativo():
    usuarios = []

    while True:
        print("\n[MENU INTERATIVO]")
        print("[1] = Criar usuário de teste")
        print("[2] = Validar email")
        print("[3] = Criar usuário validando email")
        print("[0] = Sair")
        print("-" * 15)

        escolha = int(input("Escolha uma opção: "))
        
        print("-" * 15)

        match escolha:
            case 1:
                usuario_teste = Usuario6.criar_usuario_teste()
                usuarios.append(usuario_teste)
            case 2:
                email = input("Digite um email para validar: ")
                valido = Usuario6.validar_email(email)
                print(f"{email}: {'Válido' if valido else 'Inválido'}")
            case 3:
                nome = input("Nome: ")
                email = input("Email: ")
                senha = input("Senha: ")
                usuario = Usuario6(nome, email, senha)
                usuarios.append(usuario)
            case 4:
                print(usuarios)
            case 0:
                print("\nAté mais...")
                print("-" * 15)
                break

            case _:
                print("Opção inválida.")


# Exercício 6 – Criar menu interativo 
# Criar um menu com opções para:
# 1. Criar um usuário de teste usando método de classe
# 2. Validar um email informado usando método estático
# 3. Criar usuário com validação de email usando método estático no construtor
# 4. Sair
# Cada opção deve chamar o método adequado de acordo com sua natureza.