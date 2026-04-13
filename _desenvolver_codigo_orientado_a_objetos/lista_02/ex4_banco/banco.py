# Exercício 4 
# Crie a classe ContaBancaria com: 
# Atributo privado __saldo, iniciado em 0. 
# Adicione os métodos: 
# get_saldo() — retorna o saldo atual. depositar(valor) — só 
# permite depósito se valor > 0. sacar(valor) — só permite saque 
# se houver saldo suficiente. 
# Teste a classe com vários depósitos e saques válidos e inválidos.

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    @property
    def saldo(self):
        """Método Getter pra obter o saldo"""
        return self.__saldo
    
    @saldo.setter
    def saldo(self, novo_deposito: int):
        """Método Setter pra depositar o saldo (acho)"""
        if novo_deposito >= 1:
            self.__saldo += novo_deposito
            print("Depósito realizado com sucesso!")
        else:
            print("O depósito precisa ser positivo e um número inteiro.")

    def sacar(self, saque: int):
        """Método para poder sacar o dinheir se a variável for maior que 1"""
        if saque >= 1 and saque <= self.saldo and self.saldo >= 1:
            self.__saldo -= saque
            print(f"Saque de {saque} realizado com sucesso.")
        else:
            print("Não há saldo suficiente para o saque.")
            
    def exibir_saldo(self):
        """Método para eu poder exibir o saldo"""
        print("Saldo atual: R$", self.__saldo)
        
#=============================================================================

def exercicio_4():
    conta1 = ContaBancaria("Fernando", 0)

    while True:
        print("-" * 13)
        print("[Exercício 4]")
        print("-" * 13)
        print("1 = Adicionar depósito.")
        print("2 = Realizar saque.")
        print("3 = Exibir informações")
        print("0 = Sair.")
        print("-" * 15)
        escolha = int(input("Escolha uma opção: "))
        print("-" * 15)

        match escolha:
            case 1:
                deposito = int(input("Digite o valor do depósito: R$"))
                conta1.saldo = deposito
                
            case 2:
                sacar = int(input("Quanto deseja sacar hoje? R$"))
                conta1.sacar(sacar)
                
            case 3:
                print("Titular do cartão: ", conta1.titular)
                conta1.exibir_saldo()
            
            case 0:
                print("Até mais...")
                break
            
            case _:
                print("Opção inválida, tente novamente...")



                    
                    
                
    
    

        



