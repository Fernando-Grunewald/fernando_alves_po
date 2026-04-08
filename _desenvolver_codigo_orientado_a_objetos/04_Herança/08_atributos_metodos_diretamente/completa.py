class Animal: 
    def __init__(self, especie): 
        self._especie = especie         
        self.__idade = 0               
 
    @property 
    def idade(self): 
        return self.__idade 
 
    @idade.setter 
    def idade(self, valor): 
        if valor >= 0: 
            self.__idade = valor 
        else: 
            print("Idade inválida") 
 
    def emitir_som(self): 
        print(f"O {self._especie} faz um som.") 
 
    @classmethod 
    def animal_padrao(cls): 
        return cls("Animal Genérico") 
 
    @staticmethod 
    def reino(): 
        print("Reino: Animalia") 
 
 
class Cachorro(Animal): 
    def __init__(self, nome): 
        super().__init__("Canis lupus familiaris") 
        self._nome = nome               
        self.__raça = "SRD"            
 
    @property 
    def raça(self): 
        return self.__raça 
 
    @raça.setter 
    def raça(self, valor): 
        if isinstance(valor, str): 
            self.__raça = valor 
        else: 
            print("Raça inválida") 
 
    def emitir_som(self): 
        print(f"{self._nome} late: Au Au!") 
 
    @classmethod 
    def cachorro_padrao(cls): 
        return cls("Totó") 
 
    @staticmethod 
    def especie_cachorro(): 
        print("Espécie: Canino doméstico") 
 

a = Animal.animal_padrao() 
a.emitir_som() 
a.idade = 5 
print("Idade do animal:", a.idade) 
Animal.reino() 
 
c = Cachorro("Rex") 
c.emitir_som() 
c.raça = "Labrador" 
print("Raça do cachorro:", c.raça) 
Cachorro.especie_cachorro() 