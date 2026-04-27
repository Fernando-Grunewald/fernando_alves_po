class Usuario:
    def __init__(self, nome, email, senha, cpf):
        self.nome = nome
        self.email = email
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

    def login_inst(self):
        """Método de instância pra exibir""" # Não sei se é exatamente isso um método de instância.
        print("\n [Usuário =", self.nome, "] - Realizou login no sistema - ", sep=" ")
        
    # def login(self):
    #     nome = input("Digite seu nome: ")
    #     for u in self.usuarios:
    #         if u == nome:
    #             print("Login realizado com sucesso!")
    #             return u
    #     print("Usuário não encontrado.")
    #     return None

        
    
    