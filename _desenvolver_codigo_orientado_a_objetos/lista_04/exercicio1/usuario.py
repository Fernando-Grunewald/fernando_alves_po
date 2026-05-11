class Usuario:
    def __init__(self, nome, email, senha, cpf):
        if not Usuario.validar_email(email):
            raise ValueError("Email inválido!")
        if not Usuario.validar_cpf(cpf):
            raise ValueError("CPF inválido!")
        self.nome = nome
        self.email = email
        self.__senha = senha
        self.__cpf = cpf
        self.usuarios = []
 
    @staticmethod
    def validar_email(email):
        """Método estático pra validar o email geral"""
        return "@" in email and "." in email
    
    @staticmethod
    def validar_cpf(cpf):
        """Método estático para validar o cpf geral"""
        return len(cpf) == 11

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

        
    
    