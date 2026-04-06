class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def exibir_info(self):
        print(f"Nome: {self.nome}, Email: {self.email}")

    @classmethod
    def criar_usuario_teste(cls):
        print("Criando um usuário de teste usando o método de classe...")
        return cls("Usuário Teste", "teste@email.com")


def executar_metodo_classe():
    print("\nExemplo comum: gerar usuários padrão para testes, admins, convidados, etc.\n")

  
    usuario_teste = Usuario.criar_usuario_teste()
    
    print("\nExibindo os dados do usuário criado:")
    usuario_teste.exibir_info()

    input("\nPressione Enter para voltar ao menu...")