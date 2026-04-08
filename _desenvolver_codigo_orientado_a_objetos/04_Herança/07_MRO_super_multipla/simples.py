class Pessoa: 
    def identificar(self): 
        print("Pessoa") 
 
class Suporte: 
    def identificar(self): 
        print("Equipe de Suporte") 
        super().identificar() 
 
class Funcionario(Pessoa): 
    def identificar(self): 
        print("Funcionário") 
        super().identificar() 
 
class Tecnico(Suporte, Funcionario): 
    def identificar(self): 
        print("Técnico") 
        super().identificar() 
 
tec = Tecnico() 
tec.identificar()