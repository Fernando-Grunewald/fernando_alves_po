class Usuario: 
    def __init__(self, nome, senha): 
        self._nome = nome               
        self.senha = senha # Não precisa ter __ aqui, pode ter só no getter e setter.
 
    @property 
    def senha(self): 
        return self.__senha 
 
    @senha.setter 
    def senha(self, valor): 
        if len(valor) >= 6: 
            self.__senha = valor 
        else: 
            print("Senha deve ter ao menos 6 caracteres") 
 
    def login(self): 
        print(f"{self._nome} fez login.") 
 
    @classmethod 
    def usuario_padrao(cls): 
        return cls("usuario", "123456") 
 
    @staticmethod 
    def tipo_usuario(): 
        print("Tipo: Usuário comum") 
 
 
class Administrador(Usuario): 
    def __init__(self, nome, senha, nivel): 
        super().__init__(nome, senha) 
        self._nivel = nivel             
        self.__acessos = 0             
 
    @property 
    def acessos(self): 
        return self.__acessos 
 
    @acessos.setter 
    def acessos(self, valor): 
        if valor >= 0: 
            self.__acessos = valor 
        else: 
            print("Acessos inválidos") 

    def login(self): 
        print(f"{self._nome} tentando login como administrador...") 
        super().login() 
        self.__acessos += 1 
        print(f"Acessos administrativos: {self.__acessos}")
 
    @classmethod 
    def admin_padrao(cls): 
        return cls("admin", "admin123", 10) 
 
    @staticmethod 
    def tipo_usuario(): 
        print("Tipo: Administrador")
 
 

adm = Administrador("Carlos", "senhaSegura", 5) 
adm.login()
adm.acessos = 3 
print("Acessos atuais:", adm.acessos)
 
Administrador.tipo_usuario()    
Usuario.tipo_usuario()         
 
u = Usuario.usuario_padrao() 
u.login()