class Usuario:
    def __init__(self, nome, email, senha, cpf):
        self.nome = nome
        self._email = email
        self.__senha = senha
        self.__cpf = cpf
        self.usuarios = []

    @property
    def senha(self):
        """Método getter pra obter a senha"""
        return self.__senha
    
    @senha.setter
    def senha(self, nova_senha):
        """Método de setter pra alterar a senha"""
        self.__senha = nova_senha
    
    @property
    def cpf(self):
        """Método de getter pra obter o cpf"""
        return self.__cpf
    
    @cpf.setter
    def cpf(self, novo_cpf):
        """Método de setter pra alterar o cpf"""
        self.__cpf = novo_cpf

    def login(self):
        """Método de instância pra exibir""" # Não sei se é exatamente isso um método de instância.
        print("\n [Usuário =", self.nome, "] - Realizou login no sistema - ", sep=" ")

    # @classmethod
    # def criar_usuario_teste(cls):
    #     print("Criando um usuário de teste.")
    #     return cls("Usuário Temporário", "teste@email.com", "temporario1234", "222.222.222.22")

    # def cadastrar_usuario(self):
    #     nome = input("Nome: ")
    #     email = input("Email: ")
    #     senha = input("Senha: ")
    #     cpf = input("CPF: ")
    #     saldo = float(input("Saldo inicial: "))

    #     print("[1] Cliente comum")
    #     print("[2] Cliente VIP")

    #     self.usuarios.append(usuario)
    #     print("Usuário cadastrado com sucesso!")

    #     tipo = int(input("Escolha: "))

    #     if tipo == 1:
    #         usuario = Cliente(nome, email, senha, cpf, saldo)
    #     elif tipo == 2:
    #         usuario = ClienteVip(nome, email, senha, cpf, saldo)
    #     else:
    #         print("Tipo inválido.")
    #         return

    # def detalhes_usuarios(self):
    #     print(f"Nome: {self.nome}")
    #     print(f"Email: {self._email}")
    #     print(f"Senha: {self.senha}")
    #     print(f"Cpf: {self.cpf}")
        
    def login(self):
        nome = input("Digite seu nome: ")
        for u in self.usuarios:
            if u == nome:
                print("Login realizado com sucesso!")
                return u
        print("Usuário não encontrado.")
        return None

        
    
    