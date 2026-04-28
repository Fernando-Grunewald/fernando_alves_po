from exercicio1.usuario import Usuario

class Cliente(Usuario):
    def __init__(self, nome, email, senha, cpf, saldo):
        """Hierarquia simples. Cliente faz parte da classe usuário, recebendo atributos dele e seus métodos."""
        super().__init__(nome, email, senha, cpf) # Em uma hierarquia simples, o super serve para defubur o que a classe recebe especificamente de atributos de outra.
        self.saldo = saldo
        self.clientes = []

    @classmethod
    def criar(cls):
        """Método de classe pra criar um cliente"""
        nome = input("\nNome: ")
        email = input("Email: ")
        senha = input("Senha: ")
        cpf = input("CPF: ")
        saldo = float(input("Saldo inicial: "))
        return cls(nome, email, senha, cpf, saldo)

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)
        print(f"Cliente '{cliente.nome}' foi adicionado à lista de clientes!")

    def exibir_detalhes(self):
        if len(self.clientes) != 0 :
            for self.cliente in self.clientes:
                print(f"Nome: {self.nome}. ")
                print(f"Email: {self.email}.")
                print(f"Senha: {self.senha}.")
                print(f"Cpf: {self.cpf}.")
                
        else:
            print("Não existem clientes!")

    def listar_clientes(self):
        if not self.clientes:
            print(f"Não foi possível encontrar o cliente '{self.__nome}'.")
            return
        print("=" * 20)
        print(f"Clientes Normais.")
        print("-" * 20)
        for cliente in self.clientes:
            cliente.exibir_detalhes()
            print("-" * 20)

    def comprar_itens(self): # Posso tentar fazer isso no cliente vip com super. mas vai ficar confuso ;_;
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

    # def comprar(self, valor):
    #     if self.saldo >= valor:
    #         self.saldo -= valor
    #         print(f"[Cliente {self.nome}] comprou R${valor:.2f}. Saldo restante: R${self.saldo:.2f}.")
    #     else:
    #         print(f"[Cliente {self.nome}] não tem saldo suficiente.")

    


 
    
