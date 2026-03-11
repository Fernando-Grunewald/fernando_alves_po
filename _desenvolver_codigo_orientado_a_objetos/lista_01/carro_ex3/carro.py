class Carro:

    def __init__(self, marca="Volkswagen", quilometragem=25000, placa="FR7D36"):

        self.marca = marca
        self.quilometragem = quilometragem
        self.placa = placa
    
    def atualizar_placa(self, nova_placa):
            
        self.placa = nova_placa
        print(f"A nova placa do seu {self.marca} é: ", nova_placa)
    
    def atualizar_quilometragem(self, nova_quilometragem):

        self.quilometragem += nova_quilometragem
        print(f"O seu carro {self.marca} andou um total de {self.quilometragem} quilomêtros!")

