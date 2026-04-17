from imports_utils import *

class ClienteVip(Cliente):
    def __init__(self, nome, email, senha, cpf, saldo, desconto):
        super().__init__(nome, email, senha, cpf, saldo)
        self.desconto = desconto

    def comprar(self, valor):
        """Método para aplicar desconto as compras"""
        desconto = valor * 0.10
        valor_final = valor - desconto

        if self.saldo >= valor_final:
            self.saldo -= valor_final
            print(f"[Cliente Vip] {self.nome} comprou com desconto de 10%!")
            print(f"Valor: R${valor_final:.2f} / Saldo restante: R${self.saldo:.2f}")
        else:
            print(f"[Cliente Vip] {self.nome} não tem saldo suficiente.")

    def acesso_exclusivo(self):
        print(f"[Cliente Vip] {self.nome} acessou conteúdo exclusivo VIP.")