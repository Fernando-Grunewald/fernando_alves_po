class Usuario: 
    def __init__(self, nome): 
        self.nome = nome 
 
    def login(self): 
        print(f"{self.nome} fez login.") 
 
class Cliente(Usuario): 
    pass 
 
cliente = Cliente("Alice") 
cliente.login()  