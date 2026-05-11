from exercicio1.usuario import Usuario

class Cliente(Usuario):
    def __init__(self, nome, email, senha, cpf, saldo):
        """Hierarquia simples. Cliente faz parte da classe usuário, recebendo atributos dele e seus métodos."""
        super().__init__(nome, email, senha, cpf) # Em uma hierarquia simples, o super serve para definir o que a classe recebe especificamente de atributos de outra.
        self.saldo = saldo
        self.clientes = []
    
    @classmethod
    def criar(cls):
        """Método de classe pra criar um cliente"""
        try:
            nome = input("\nNome: ")
            email = input("Email: ")
            senha = input("Senha: ")
            cpf = input("CPF: ")
            saldo = float(input("Saldo inicial: "))
            return cls(nome, email, senha, cpf, saldo)

        except ValueError as erro:
            print(f"\nErro: {erro}")
            return None

    def registro_sucesso():
        """Método de Instância"""
        print("Cliente registrado com sucesso.")

    def comprar_itens(self):
        """Método para comprar itens dos clientes"""
        valor = 0
        carrinho = []

        while True:
            print("CARRINHO ATUAL =", carrinho)

            print("\n[ ITENS ]")
            print("[1] Pulseira Pista Full - R$65")
            print("[2] Drink Doce - R$32")

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

                case 0:
                    break

                case _:
                    print("Opção inválida.")

            if not carrinho:
                print("Nenhum item selecionado.")
                return
            print("\nResumo da compra:")
            print("\nItens:", carrinho)

            if self.saldo >= valor:
                self.saldo -= valor
                print(f"[Cliente] {self.nome} comprou com sucesso!")
                print(f"Saldo restante: R${self.saldo:.2f}")
                print("=" * 18)
            else:
                print(f"[Cliente] {self.nome} não tem saldo suficiente.")
                print("=" * 18)

    


 
    
