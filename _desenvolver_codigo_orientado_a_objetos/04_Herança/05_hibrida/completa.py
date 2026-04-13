class Pessoa: 
    def __init__(self, nome, idade): 
        self._nome = nome               
        self.__idade = idade            
 
    @property 
    def idade(self): 
        return self.__idade 
 
    @idade.setter 
    def idade(self, valor): 
        if valor >= 0: 
            self.__idade = valor 
        else: 
            print("Idade inválida") 
 
    def apresentar(self): 
        print(f"Pessoa: {self._nome}, {self.__idade} anos") 
 
    @classmethod 
    def pessoa_padrao(cls): 
        return cls("Pessoa Genérica", 0) 
 
    @staticmethod 
    def especie(): 
        print("Espécie: Humano") 
 
 
class Registro: 
    def __init__(self): 
        self._registro_ativo = False      
        self.__ultimo_acesso = None       
 
    @property 
    def ultimo_acesso(self): 
        return self.__ultimo_acesso 
 
    @ultimo_acesso.setter 
    def ultimo_acesso(self, valor): 
        self.__ultimo_acesso = valor 
 
    def registrar(self): 
        self._registro_ativo = True 
        print("Registro ativado") 
 
    @classmethod 
    def registro_padrao(cls): 
        return cls() 
 
    @staticmethod 
    def tipo_registro(): 
        print("Tipo: Padrão") 
 
 
class Funcionario(Pessoa, Registro): 
    def __init__(self, nome, idade, cargo): 
        Pessoa.__init__(self, nome, idade) 
        Registro.__init__(self) # Self apenas para pegar os métodos.
        self._cargo = cargo               
        self.__salario = 0               
 
    @property 
    def salario(self): 
        return self.__salario 
 
    @salario.setter 
    def salario(self, valor): 
        if valor >= 0: 
            self.__salario = valor 
        else: 
            print("Salário inválido") 
 
    def trabalhar(self): 
        print(f"{self._nome} está trabalhando como {self._cargo}") 
 
    @classmethod 
    def funcionario_padrao(cls): 
        return cls("Funcionário Genérico", 18, "Cargo Genérico") 
 
    @staticmethod 
    def turno(): 
        print("Turno: Diurno") 
 
 

f = Funcionario("Carlos", 35, "Analista") 
f.apresentar()          
f.registrar()          
f.trabalhar() 
f.salario = 4500 
print("Salário:", f.salario) 
Funcionario.turno()      
print("Espécie:", end=" ") 
Funcionario.especie()   
print("Tipo de registro:", end=" ") 
Funcionario.tipo_registro() 
 
