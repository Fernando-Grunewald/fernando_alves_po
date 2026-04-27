from exercicio1.cliente import Cliente

class ClienteVip(Cliente):
    def __init__(self, nome, email, senha, cpf, saldo, desconto):
        super().__init__(nome, email, senha, cpf, saldo)
        self.desconto = desconto
        self.clientes_vips = []

    # @classmethod
    # def criar(cls):
    #     print("[Criando Cliente VIP]")
    #     return super().criar()

    @classmethod
    def criar_vip(cls):
        """Método de classe pra criar um cliente vip"""
        nome = input("\nNome: ")
        email = input("Email: ")
        senha = input("Senha: ")
        cpf = input("CPF: ")
        saldo = float(input("Saldo inicial: "))
        desconto = int(input(("Digite seu valor de desconto (até 50%): "))) / 100
        return cls(nome, email, senha, cpf, saldo, desconto)

    def comprar_vip(self, valor):
        """Método para aplicar desconto as compras"""
        valor_descontado = valor * self.desconto
        valor_final = valor - valor_descontado

        if self.saldo >= valor_final:
            self.saldo -= valor_final
            print(f"[Cliente Vip] {self.nome} comprou com desconto de 10%!")
            print(f"Valor: R${valor_final:.2f} / Saldo restante: R${self.saldo:.2f}")
        else:
            print(f"[Cliente Vip] {self.nome} não tem saldo suficiente.")

    def acesso_exclusivo(self):
        print(f"[Cliente Vip] {self.nome} acessou conteúdo exclusivo VIP.")

    def adicionar_cliente_vip(self, cliente_vip):
        self.clientes_vips.append(cliente_vip)
        print(f"'{cliente_vip.nome}' foi adicionado à lista de clientes vips! Seja bem vindo...")