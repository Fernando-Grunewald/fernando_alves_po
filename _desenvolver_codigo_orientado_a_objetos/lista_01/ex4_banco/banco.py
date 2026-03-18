class Banco:
    def depositar(self, conta, valor):
        if valor > 0:
            conta.saldo += valor
            print("Depósito realizado!")
        else:
            print("Valor inválido.")

    def sacar(self, conta, valor):
        if valor <= 0:
            print("Valor inválido.")
        elif valor > conta.saldo:
            print("Saldo insuficiente.")
        else:
            conta.saldo -= valor
            print("Saque realizado!")

    def mostrar_info(self, conta):
        print(f"\nTitular: {conta.titular}")
        print(f"Saldo: {conta.saldo}")