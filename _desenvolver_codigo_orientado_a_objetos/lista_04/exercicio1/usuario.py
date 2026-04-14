class Usuario:
    def __init__(self, nome, email, senha, cpf):
        self.nome = nome
        self._email = email
        self.__senha = senha
        self.__cpf = cpf
        
    @property
    def senha(self):
        return self.__senha
    
    @senha.setter
    


        
    
    