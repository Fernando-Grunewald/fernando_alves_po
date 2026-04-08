class Produto: 
    def exibir_info(self): 
        print("Produto genérico") 
 
class Livro(Produto): 
    def exibir_info(self): 
        print("Livro: Python para Iniciantes") 
 
class Eletronico(Produto): 
    def exibir_info(self): 
        print("Eletrônico: Fone Bluetooth") 
 
p1 = Livro() 
p2 = Eletronico() 
p1.exibir_info()  
p2.exibir_info()  
