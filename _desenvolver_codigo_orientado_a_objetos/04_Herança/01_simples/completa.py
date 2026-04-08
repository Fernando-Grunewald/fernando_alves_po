class Usuario: 
    def __init__(self, nome, idade): 
        self._nome = nome             
        self.idade = idade           
        self.nivel = 1               

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, valor):
        if valor > 0:
            self.__idade = valor
        else:
            print("Idade inválida")

    @property
    def nivel(self):
        return self._nivel

    @nivel.setter
    def nivel(self, valor):
        if valor > 0:
            self._nivel = valor
        else:
            print("Nível inválido") 

    def login(self): 
        print(f"{self._nome} fez login.") 

    @staticmethod 
    def saudacao(): 
        print("Bem-vindo ao sistema!") 

class Cliente(Usuario): 
    def __init__(self, nome, idade, saldo): 
        super().__init__(nome, idade) 
        self._saldo = saldo 

    def mostrar_saldo(self): 
        print(f"Saldo de {self._nome}: R$ {self._saldo:.2f}")

    def mostrar_dados(self):
        print(f"Nome: {self._nome}")
        print(f"Idade: {self.idade}")
        print(f"Nível: {self.nivel}")
        print(f"Saldo: R$ {self._saldo:.2f}")
       
    @classmethod
    def criar_padrao(cls):
        return cls("Padrão", 18, 2000.0)

cliente = Cliente("Alice", 30, 1500.0) 
cliente.login()              
cliente.mostrar_saldo() 
cliente.nivel = 3             
print(cliente.nivel)         
Cliente.saudacao()            

c2 = Cliente.criar_padrao()   
c2.login()


print("\n--- Cliente 1 ---")
cliente.mostrar_dados()

print("\n--- Cliente 2 (Padrão) ---")
c2.mostrar_dados()