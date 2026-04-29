class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.pedidos = []

    def adicionar_pedidos(self, pedido):
        self.pedidos.append(pedido)
        print("Deu tudo certo.")

    def exibir_pedidos(self):
        if len(self.pedidos) != 0 :
            for pedido in self.pedidos:
                print(f"Cliente: {self.nome}")
                print(f"ID: {pedido.id}")
                print(f"Nome: {pedido.nome}")
                print(f"Quantidade: {pedido.quantidade}")
        else:
            print("Não existem pedidos registrados")
    @property
    def cpf(self):
        """
        Esse é o método Getter para o cpf da classe Cliente
        """
        return self.__cpf
    
    @cpf.setter
    def cpf(self, novo_cpf):
        """
        Esse é o método Setter para cpf da classe Cliente
        """
        cpf_limpo = novo_cpf.replace(".","").replace("-", "")
        if not cpf_limpo.isdigit() or len(cpf_limpo)!= 11:
            raise ValueError("Erro: o cpf deve ter 11 digitos númericos")
        else:
            self.__cpf = cpf_limpo


