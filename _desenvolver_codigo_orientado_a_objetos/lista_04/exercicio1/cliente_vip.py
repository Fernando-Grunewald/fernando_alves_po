from exercicio1.cliente import Cliente

class ClienteVip(Cliente):
    def __init__(self, nome, email, senha, cpf, saldo, desconto=0.20):
        super().__init__(nome, email, senha, cpf, saldo)
        self.desconto = desconto
        self.clientes_vips = []

    # @classmethod
    # def criar_vip(cls):
    #     """Método de classe pra criar um cliente vip"""
    #     nome = input("\nNome: ")
    #     email = input("Email: ")
    #     senha = input("Senha: ")
    #     cpf = input("CPF: ")
    #     saldo = float(input("Saldo inicial: "))
    #     return cls(nome, email, senha, cpf, saldo)

    @classmethod
    def criar_vip(cls):
        """Método de classe com hierarquia para aproveitar a criação de cliente"""
        print("[Criando Cliente VIP]")
        cliente_base = super().criar()

        return cls(
            cliente_base.nome,
            cliente_base.email,
            cliente_base.senha,
            cliente_base.cpf,
            cliente_base.saldo,)

    def acesso_exclusivo(self):
        """Método de Instância"""
        print(f"[Cliente Vip] {self.nome} acessou conteúdo exclusivo VIP. Suas compras terão {self.desconto} de desconto")

    def adicionar_cliente_vip(self, cliente_vip):
        """Método para adicionar clientes à lista vip"""
        self.clientes_vips.append(cliente_vip)
        print(f"'{cliente_vip.nome}' foi adicionado à lista de clientes vips! Seja bem vindo...")

    def comprar_itens_vip(self):
        """Método para comprar itens dos clientes vips adicionando eles ao carrinho, junto das suas regalias com opções extras e os descontos"""
        valor = 0
        carrinho = []

        while True:
            print("CARRINHO ATUAL =", carrinho)

            print("\n[ ITENS ]")
            print("[1] Pulseira Pista Full - R$65")
            print("[2] Drink Doce - R$32")

            print("\n[ ITENS EXCLUSIVOS VIP ] (desconto ainda aplicado)")
            print("[3] Colar Pista Premium - R$120")
            print("[4] Passe de Acesso à cobertura - R$220")
            print("[5] Vale 4 Drinks - R$80")

            print("[0] Finalizar compra")

            try:
                opcao = int(input("\nQual deseja comprar? "))
            except ValueError:
                print("Entrada inválida.")
                continue
            
            match opcao:

                case 1:
                    valor += 65
                    carrinho.append("Pulseira Pista Full")

                case 2:
                    valor += 32
                    carrinho.append("Drink Doce")

                case 3:
                    valor += 120
                    carrinho.append("Colar Pista Premium")

                case 4:
                    valor += 220
                    carrinho.append("Passe de Acesso à cobertura")

                case 5:
                    valor += 80
                    carrinho.append("Vale 4 Drinks")

                case 0:
                    break

                case _:
                    print("Opção inválida.")

            if not carrinho:
                print("Nenhum item selecionado.")
                return
            print("\nResumo da compra:")
            print("\nItens:", carrinho)
            print(f"Total sem desconto V-I-P: R${valor:.2f}")

            valor_descontado = valor * self.desconto
            valor_final = valor - valor_descontado

            print(f"Desconto aplicado: R${valor_descontado:.2f}")
            print(f"Total com desconto: R${valor_final:.2f}")

            if self.saldo >= valor_final:
                self.saldo -= valor_final
                print(f"[Cliente VIP] {self.nome} comprou com sucesso!")
                print(f"Saldo restante: R${self.saldo:.2f}")
                print("=" * 18)
            else:
                print(f"[Cliente VIP] {self.nome} não tem saldo suficiente.")
                print("=" * 18)

