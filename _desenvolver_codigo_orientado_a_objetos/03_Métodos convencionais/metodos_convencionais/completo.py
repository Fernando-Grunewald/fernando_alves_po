class Usuario:
    def __init__(self, nome, email, senha):
        if not Usuario.validar_email(email):  
            raise ValueError("Email inválido.")
        self.nome = nome
        self.email = email
        self._senha = senha

   
    def verificar_senha(self, senha_digitada):
        return self._senha == senha_digitada

   
    def exibir_boas_vindas(self):
        print(f"\nBem-vindo(a), {self.nome}!")

   
    @classmethod
    def criar_usuario_teste(cls):
        print("\nUsuário de teste criado com sucesso.")
        return cls("Usuário Teste", "teste@email.com", "123456")


    @staticmethod
    def validar_email(email):
        return "@" in email and "." in email


usuarios_registrados = []


def cadastrar_usuario():
    nome = input("Nome: ")
    email = input("Email: ")
    senha = input("Senha: ")

    
    for usuario in usuarios_registrados:
        if usuario.email == email:
            print("Erro: Email já cadastrado.")
            return

    try:
        novo_usuario = Usuario(nome, email, senha)
        usuarios_registrados.append(novo_usuario)
        print("Usuário cadastrado com sucesso!")
    except ValueError as ve:
        print(f"Erro ao cadastrar: {ve}")


def login():
    print("\n Login ")
    email = input("Email: ")
    senha = input("Senha: ")

    for usuario in usuarios_registrados:
        if usuario.email == email:
            if usuario.verificar_senha(senha):  
                print("Login bem-sucedido!")
                usuario.exibir_boas_vindas()    
                return
            else:
                print("Senha incorreta.")
                return
    print("Usuário não encontrado.")


def adicionar_usuario_teste():
    
    usuario_teste = Usuario.criar_usuario_teste()  
    usuarios_registrados.append(usuario_teste)


def executar_menu_completo():
    while True:
        print("\n Menu Principal ")
        print("1 - Cadastrar Novo Usuário")
        print("2 - Fazer Login")
        print("3 - Adicionar Usuário de Teste")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            login()
        elif opcao == "3":
            adicionar_usuario_teste()
        elif opcao == "0":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")



if __name__ == "__main__":
    executar_menu_completo()