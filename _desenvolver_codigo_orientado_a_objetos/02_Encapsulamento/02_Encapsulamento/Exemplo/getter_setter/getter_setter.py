class Produto:
    def __init__(self,nome, preco):
        self.nome = nome
        self.__preco = preco

    @property
    def preco(self):
        """Getter para o atributo preco."""
        return self.__preco

    @preco.setter
    def preco(self, novo_preco):
        """Setter para o atributo preco com validação."""
        if novo_preco >= 0:
            self.__preco = novo_preco
        else:
            print("Preço não pode ser negativo!")

def executar_getter_setter():
    print("\n--- getter_setter.py: Encapsulamento com @property ---\n")
    produto = Produto("Caneta",2.50)
    print(f"Preço atual: R$ {produto.preco:.2f}") 
    produto.preco = 3.00 
    print(f"Novo preço: R$ {produto.preco:.2f}")
    produto.preco = -1 
    input("Pressione Enter para voltar ao menu...")