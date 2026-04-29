class Banco:

    def depositar(self, conta, valor):
        """
        Método para depositar dinheiro na conta
        """
        if valor <= 0:
            raise ValueError("Valor inválido para depósito!")

        conta.saldo = conta.saldo + valor
        print("Depósito realizado!")

    def sacar(self, conta, valor):
        """
        Método para sacar dinheiro da conta
        """
        if valor <= 0:
            raise ValueError("Valor inválido!")

        if valor > conta.saldo:
            raise ValueError("Saldo insuficiente!")

        conta.saldo = conta.saldo - valor
        print("Saque realizado!")

    def mostrar_info(self, conta):
        """
        Método para mostrar informações da conta
        """
        print(f"\nTitular: {conta.titular}")
        print(f"Saldo: {conta.saldo}")