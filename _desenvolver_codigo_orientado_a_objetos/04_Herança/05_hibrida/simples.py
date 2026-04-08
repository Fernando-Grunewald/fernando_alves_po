class Pessoa: 
    def __init__(self, nome): 
        self.nome = nome 
 
class Registro: 
    def registrar(self): 
        print("Registrando no sistema.") 
 
class Funcionario(Pessoa, Registro): 
    def trabalhar(self): 
        print(f"{self.nome} está trabalhando.") 
 
f = Funcionario("Carlos") 
f.registrar()   
f.trabalhar()  