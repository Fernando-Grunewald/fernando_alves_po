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
        if novo_deposito >= 1 and novo_deposito is int:
            self.__saldo += novo_deposito
            print("Depósito realizado com sucesso!")
        else:
            print("O depósito precisa ser positivo e um número inteiro.")

    @saldo.setter 
    def saldo(self, saque: int):
        """Método Setter"""

    def sacar(self, saque: int):
        if saque >= 1 and self.saldo >= 1:
            print("")
        

    

        



