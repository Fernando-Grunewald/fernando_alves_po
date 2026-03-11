from humano_ex1.humano import Pessoa
from gato_cachorro_ex2.cachorro import Cachorro
from gato_cachorro_ex2.gato import Gato
from carro_ex3.carro import Carro

def main():

    humano = Pessoa()
    cachorrinho = Cachorro()
    gatinho = Gato()
    carro = Carro()

    while True:
        print("\n", "=" * 20)
        print("Lista de exercícios 1:")
        print("\n 1 - Classe que representa uma pessoa.")
        print(" 2 - Módulo de gato e cachorro.")
        print(" 3 - Atualizar seu carro.")
        print(" 5 - Gerenciar estudantes.")
        print("\n", "=" * 20)
        exercicio_escolhido = int(input("\n Escolha um exercício (1-10): "))
        print("=" * 20)

        match exercicio_escolhido:

            case 1:
                humano.humano_nome = input("Qual é seu nome? ")
                humano.humano_idade = int(input("Qual é sua idade? "))
                print("=" * 20)
                humano.apresentacao_pessoal()

            case 2:
                cachorrinho.dog_bark()

                gatinho.cat_meow()
            
            case 3:
                carro.atualizar_placa(nova_placa = input("Digite uma nova placa para seu carro: "))
                print("=" * 20)
                carro.atualizar_quilometragem(nova_quilometragem = int(input("Quantos KM seu carro andou hoje? ")))

            case 5:

                while True:

                    print("1 - Adicionar estudante. ")
                    print("2 - Exibir boletins. ")
                    print("0 - Sair")
                    opcao = int(input("Escolha: "))

                    match opcao: 

                        case 1:
                            print()
                        
                        case 2:
                            print
                        
                        case 0:
                            print("Encerrando programa...")
                            break
        
                        case _:
                            print(f"A opção {opcao} é inválida!")


            case 0:
                print("Encerrando programa...")
                break
        
            case _:
                print(f"A opção {exercicio_escolhido} é inválida!")

if __name__ == "__main__":
    main()

# Exercício 1 
# Crie um módulo com uma classe que represente uma pessoa.
# Implemente um método que mostre uma apresentação pessoal com nome e idade.

# Exercício 2 
# Crie um pacote contendo dois módulos: um com uma classe que represente um cachorro 
# e outro com uma classe que represente um gato.
# Cada classe deve possuir dois atributos e um método específico que emite um som.

# Exercício 3 
# Crie uma classe que represente um carro com três atributos.
# Implemente dois métodos para atualizar dois desses atributos.

# Exercício 4 
# Crie um pacote com dois módulos.
# Implemente uma classe que represente uma conta bancária com saldo e titular.
# Implemente métodos para realizar operações financeiras.

# Exercício 5 
# Implemente um pacote com duas classes: uma representando um estudante com 
# informações básicas e uma lista de notas, e outra representando um curso.
# Inclua métodos para cálculo de média e para cadastrar estudantes no curso.

# Exercício 6 
# Crie duas classes em módulos separados dentro de um pacote.
# Implemente uma classe que represente um livro e outra que represente um bibliotecário.
# Inclua métodos para exibir informações e registrar empréstimos.

# Exercício 7 
# Implemente duas classes que representem um funcionário e um departamento.
# Adicione atributos e métodos que permitam organizar os funcionários e modificar dados 
# salariais.

# Exercício 8 
# Desenvolva um pacote com dois módulos: um para produtos e outro para clientes.
# Crie métodos para atualizar estoque e simular a compra de produtos.

# Exercício 9 
# Implemente uma classe para filmes e uma para categorias, organizadas em módulos 
# diferentes.
# Adicione métodos para exibir detalhes do filme e adicionar filmes a uma categoria.

# Exercício 10 
# Implemente duas classes, uma para clientes e outra para pedidos, organizadas em dois 
# módulos.
# Crie métodos para registrar pedidos e atualizar o status de um pedido