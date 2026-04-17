from imports_utils import *

class Cliente(Usuario):
    def __init__(self, nome, email, senha, cpf, saldo):
        """Hierarquia simples. Cliente faz parte da classe usuário, recebendo atributos dele e seus métodos."""
        super().__init__(nome, email, senha, cpf) # Em uma hierarquia simples, o super serve para defubur o que a classe recebe especificamente de atributos de outra.
        self._saldo = saldo


# Preciso fazer um menu de itens e botar o preço = o valor.

    def comprar(self, valor):
        """Método pra subtrair o saldo"""
        if self.saldo >= valor:
            self.saldo -= valor 
            print("[Cliente", self.nome,"] - comprou R${valor:.2f}. Seu saldo restante é R${self.saldo:.2f}", sep=" ")
        else:
            print("[Cliente", self.nome,"] - não tem saldo suficiente.")



 
    
