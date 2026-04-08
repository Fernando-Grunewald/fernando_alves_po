class Veiculo: 
    def mover(self): 
        print("Movendo...") 
 
class Terrestre(Veiculo): 
    def rodar(self): 
        print("Rodando nas ruas.") 
 
class Carro(Terrestre): 
    def acelerar(self): 
        print("Acelerando o carro!") 
 
c = Carro() 
c.mover()     
c.rodar()      
c.acelerar()    
 