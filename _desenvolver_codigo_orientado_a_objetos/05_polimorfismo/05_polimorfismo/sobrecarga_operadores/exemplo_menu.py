class Soma:
    def __init__(self, valor):
        self.valor = valor

    def __add__(self, outro):
        return Soma(self.valor + outro.valor)

    def __str__(self):
        return f"Soma: {self.valor}"

class Concatena:
    def __init__(self, texto):
        self.texto = texto

    def __add__(self, outro):
        return Concatena(self.texto + outro.texto)

    def __str__(self):
        return f"Concatenação: '{self.texto}'"

def menu():
    print("Operadores")
    print("1 - Somar números")
    print("2 - Concatenar textos")
    print("0 - Sair")

def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            print("Saindo...")
            break
        elif opcao == "1":
            try:
                n1 = float(input("Digite o primeiro número: "))
                n2 = float(input("Digite o segundo número: "))
                soma1 = Soma(n1)
                soma2 = Soma(n2)
                resultado = soma1 + soma2  
                print(resultado)
            except ValueError:
                print("Digite números válidos!")
        elif opcao == "2":
            t1 = input("Digite o primeiro texto: ")
            t2 = input("Digite o segundo texto: ")
            c1 = Concatena(t1)
            c2 = Concatena(t2)
            resultado = c1 + c2 
            print(resultado)
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()