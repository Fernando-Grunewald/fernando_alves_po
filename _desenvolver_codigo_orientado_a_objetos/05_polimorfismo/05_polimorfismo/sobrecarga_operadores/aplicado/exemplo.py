class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.nome}: R$ {self.preco:.2f}"

class DescontoFixo:
    def __init__(self, valor):
        self.valor = valor

    def __sub__(self, produto):
     
        preco_final = max(produto.preco - self.valor, 0)
        return Produto(produto.nome, preco_final)

class DescontoPorcentagem:
    def __init__(self, percentual):
        self.percentual = percentual

    def __sub__(self, produto):
        desconto = produto.preco * (self.percentual / 100)
        preco_final = max(produto.preco - desconto, 0)
        return Produto(produto.nome, preco_final)

def menu():
    print("Sistema de Descontos")
    print("1 - Desconto fixo")
    print("2 - Desconto percentual")
    print("0 - Sair")

def main():
    produto = Produto("Notebook", 3000.00)
    print(f"Produto base: {produto}")

    while True:
        menu()
        opcao = input("Escolha o tipo de desconto: ")

        if opcao == "0":
            print("Encerrando sistema.")
            break

        if opcao == "1":
            try:
                valor = float(input("Digite o valor do desconto fixo: R$ "))
                desconto = DescontoFixo(valor)
                produto_com_desconto = desconto - produto 
                print(f"Preço com desconto: {produto_com_desconto}")
            except ValueError:
                print("Valor inválido.")
        elif opcao == "2":
            try:
                percentual = float(input("Digite o percentual de desconto: "))
                desconto = DescontoPorcentagem(percentual)
                produto_com_desconto = desconto - produto  
                print(f"Preço com desconto: {produto_com_desconto}")
            except ValueError:
                print("Percentual inválido.")
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()