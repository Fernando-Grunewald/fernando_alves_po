class Usuario: 
    def login(self): 
        print("Usuário logado.") 
 
class Administrador(Usuario): 
    def login(self): 
        print("Verificando permissões...") 
        super().login() 
 
adm = Administrador()
adm.login() 
