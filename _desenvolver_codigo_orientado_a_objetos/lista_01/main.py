from utils import *


def main():

    humano = Pessoa()
    cachorrinho = Cachorro()
    gatinho = Gato()
    carro = Carro()
    banco = Banco()
    titular = Titular()
    aluno = Estudante()
    curso = Curso()
    bibliotecario = Bibliotecario()
    livro = Livro()
    departamento = Departamento()
    produtos = Produto()
    categoria = Categoria()


    while True:
        print("\n", "=" * 20)
        print("Lista de exercícios 1:")
        print("\n [1] - Classe que representa uma pessoa.")
        print(" [2] - Módulo de gato e cachorro.")
        print(" [3] - Atualizar seu carro.")
        print(" [4] - Sistema Bancário.")
        print(" [5] - Gerenciar estudantes.")
        print(" [6] - Gerenciar livros.")
        print(" [7] - Departamento de Funcionários.")
        print(" [8] - Mercado Online.")
        print(" [9] - Filmes e Categorias.")
        print(" [10] - Clientes e Pedidos.")
        print( "=" * 20)
        exercicio_escolhido = int(input(" Escolha um exercício (1-10): "))
        print("=" * 20)

        match exercicio_escolhido:

                        
            case 1:
                while True:
                    try:
                        nome = input("Qual é seu nome? ")
                        idade = int(input("Qual é sua idade? "))
                        print("=" * 20)

                        humano.nome = nome
                        humano.idade = idade

                        humano.apresentacao_pessoal()
                        break

                    except ValueError as e:
                        print("Erro:", e)

            case 2:
                while True:
                    try:
                        cachorrinho.nome = input("Digite um nome de cachorro: ")
                        cachorrinho.raca = input("Digite uma raça de cachorro: ")

                        gatinho.nome = input("Digite um nome de gato: ")
                        gatinho.cor = input("Digite uma cor de gato: ")

                        print("=" * 20)

                        cachorrinho.latir()
                        gatinho.miar()

                        break

                    except ValueError as e:
                        print("Entrada de dados inválida. Erro =", e)
            
            case 3:
                while True:
                    try:
                        carro.atualizar_placa(
                            nova_placa=input("Digite uma nova placa para seu carro: ")
                        )

                        print("=" * 20)

                        carro.atualizar_quilometragem(
                            nova_quilometragem=int(input("Quantos KM seu carro andou hoje? "))
                        )

                        break

                    except ValueError as e:
                        print("Entrada inválida:", e)
                
            case 4:
                while True:
                    try:
                        print("[MENU BANCÁRIO]")
                        print("1 - Depositar")
                        print("2 - Sacar")
                        print("3 - Ver conta")
                        print("0 - Sair")

                        opcao = input("Escolha: ")

                        match opcao:
                            case "1":
                                valor = float(input("Valor: "))
                                banco.depositar(titular, valor)

                            case "2":
                                valor = float(input("Valor: "))
                                banco.sacar(titular, valor)

                            case "3":
                                banco.mostrar_info(titular)

                            case "0":
                                break

                            case _:
                                print("Opção inválida.")

                    except ValueError as e:
                        print("Erro:", e)

            case 5:
                while True:
                    try:
                        print("\n [MENU ESCOLAR]")
                        print("1 - Adicionar estudante")
                        print("2 - Adicionar nota")
                        print("3 - Listar estudantes")
                        print("0 - Sair")

                        opcao = input("Escolha: ")

                        match opcao:
                            case "1":
                                nome = input("Nome: ")
                                idade = int(input("Idade: "))
                                matricula = input("Matrícula: ")

                                aluno = Estudante(nome, idade, matricula)
                                curso.adicionar_estudante(aluno)

                                print("Estudante adicionado!")

                            case "2":
                                if len(curso.estudantes) == 0:
                                    print("Nenhum estudante cadastrado.")
                                    continue

                                print("\nEscolha o estudante:")
                                for i, est in enumerate(curso.estudantes):
                                    print(f"{i+1} - {est.nome}")

                                indice = int(input("Número: "))
                                nota = float(input("Nota: "))

                                curso.estudantes[indice-1].adicionar_nota(nota)
                                print("Nota adicionada!")

                            case "3":
                                curso.listar_estudantes()

                            case "0":
                                print("Encerrando programa...")
                                break

                            case _:
                                print(f"A opção {opcao} é inválida!")

                    except ValueError as e:
                        print("Erro:", e)
                    except IndexError:
                        print("Índice inválido!")

            case 6:
                
                nome_bibliotecario = input("Digite o nome do bibliotecário: ")
                bibliotecario = Bibliotecario(nome_bibliotecario)

                livros = []

                while True:
                    try:
                        print("\n[MENU BIBLIOTECÁRIO]")
                        print("1 - Adicionar livro")
                        print("2 - Emprestar livro")
                        print("3 - Devolver livro")
                        print("4 - Listar livros")
                        print("5 - Ver bibliotecário")
                        print("6 - Trocar bibliotecário")
                        print("0 - Sair")

                        opcao = input("Escolha: ")

                        match opcao:
                            case "1":
                                titulo = input("Título do livro: ")
                                livro = Livro(titulo)
                                livros.append(livro)
                                print("Livro adicionado!")

                            case "2":
                                if len(livros) == 0:
                                    print("Nenhum livro cadastrado.")
                                    continue

                                for i, livro in enumerate(livros):
                                    print(f"{i} - {livro.titulo}")

                                indice = int(input("Escolha o livro: "))
                                bibliotecario.emprestar_livro(livros[indice])

                            case "3":
                                if len(bibliotecario.livros_emprestados) == 0:
                                    print("Nenhum livro para devolver.")
                                    continue

                                for i, livro in enumerate(bibliotecario.livros_emprestados):
                                    print(f"{i} - {livro.titulo}")

                                indice = int(input("Escolha o livro: "))
                                bibliotecario.devolver_livro(
                                    bibliotecario.livros_emprestados[indice]
                                )

                            case "4":
                                if len(livros) == 0:
                                    print("Nenhum livro cadastrado.")
                                else:
                                    for livro in livros:
                                        livro.mostrar_info()
                                        print("-" * 20)

                            case "5":
                                bibliotecario.mostrar_info()

                            case "6":
                                novo_nome = input("Novo nome do bibliotecário: ")
                                bibliotecario.nome = novo_nome
                                print("Bibliotecário atualizado!")

                            case "0":
                                print("Saindo...")
                                break

                            case _:
                                print("Opção inválida.")

                    except ValueError as e:
                        print("Erro:", e)
                    except IndexError:
                        print("Índice inválido!")

            case 7:
                while True:
                    try:
                        print("[MENU FUNCIONÁRIOS]")
                        print("1 - Adicionar funcionário")
                        print("2 - Editar salário")
                        print("3 - Listar funcionários")
                        print("0 - Sair")
                        print("-" * 20)

                        opcao = input("Escolha: ")

                        match opcao:
                            case "1":
                                nome = input("Nome: ")
                                cpf = input("CPF: ")
                                telefone = input("Telefone: ")

                                novo = Funcionario(nome, cpf, telefone)
                                departamento.adicionar_funcionario(novo)

                                print("Funcionário adicionado!")

                            case "2":
                                if len(departamento.funcionarios) == 0:
                                    print("Nenhum funcionário cadastrado.")
                                    continue

                                nome = input("Digite o nome do funcionário: ")

                                for func in departamento.funcionarios:
                                    if func.nome == nome:
                                        novo_salario = float(input("Novo salário: "))
                                        func.editar_salario(novo_salario)
                                        break
                                else:
                                    print("Funcionário não encontrado.")

                            case "3":
                                departamento.listar_funcionarios()

                            case "0":
                                print("Encerrando...")
                                break

                            case _:
                                print("Opção inválida!")

                    except ValueError as e:
                        print("Erro:", e)

            case 8:
                produtos = []

                while True:
                    try:
                        print("[MENU PRODUTOS]")
                        print("1 - Cadastrar produto")
                        print("2 - Atualizar estoque")
                        print("3 - Mostrar produtos")
                        print("4 - Comprar produto")
                        print("0 - Sair")
                        print("-" * 20)

                        opcao = input("Escolha: ")

                        match opcao:

                            case "1":
                                nome = input("Nome do produto: ")
                                preco = float(input("Preço: "))
                                estoque = int(input("Estoque inicial: "))

                                novo = Produto(nome, preco, estoque)
                                produtos.append(novo)

                                print("Produto cadastrado!")

                            case "2":
                                if not produtos:
                                    print("Nenhum produto cadastrado.")
                                    continue

                                for i, p in enumerate(produtos):
                                    print(f"{i} - {p.nome}")

                                indice = int(input("Escolha o produto: "))
                                quantidade = int(input("Quantidade a adicionar: "))

                                produtos[indice].adicionar_estoque(quantidade)

                            case "3":
                                if not produtos:
                                    print("Nenhum produto cadastrado.")
                                else:
                                    for p in produtos:
                                        print(f"Nome: {p.nome}")
                                        print(f"Preço: R${p.preco:.2f}")
                                        print(f"Estoque: {p.estoque}")
                                        print("-" * 20)

                            case "4":
                                if not produtos:
                                    print("Nenhum produto cadastrado.")
                                    continue

                                nome_cliente = input("Nome do cliente: ")
                                cliente = Cliente(nome_cliente)

                                for i, p in enumerate(produtos):
                                    print(f"{i} - {p.nome}")

                                indice = int(input("Escolha o produto: "))
                                quantidade = int(input("Quantidade: "))

                                cliente.comprar(produtos[indice], quantidade)

                            case "0":
                                print("Encerrando...")
                                break

                            case _:
                                print("Opção inválida!")

                    except ValueError as e:
                        print("Erro:", e)
                    except IndexError:
                        print("Índice inválido!")

            case 9:

                categorias = []

                while True:
                    try:
                        print("[MENU CINÉFILO]")
                        print("1 - Criar categoria")
                        print("2 - Adicionar filme em categoria")
                        print("3 - Listar categorias")
                        print("4 - Listar filmes de uma categoria")
                        print("0 - Sair")
                        print("-" * 20)

                        opcao = input("Escolha: ")
                        print("-" * 20)

                        match opcao:

                            case "1":
                                nome = input("Nome da categoria: ")
                                nova = Categoria(nome)
                                categorias.append(nova)
                                print("Categoria criada!")

                            case "2":
                                if not categorias:
                                    print("Nenhuma categoria cadastrada.")
                                    continue

                                for i, cat in enumerate(categorias):
                                    print(f"{i} - {cat.nome}")

                                indice = int(input("Escolha a categoria: "))

                                titulo = input("Título: ")
                                diretor = input("Diretor: ")
                                ano = int(input("Ano: "))

                                filme = Filme(titulo, diretor, ano)
                                categorias[indice].adicionar_filme(filme)

                            case "3":
                                if not categorias:
                                    print("Nenhuma categoria cadastrada.")
                                else:
                                    print("Categorias:")
                                    for i, cat in enumerate(categorias):
                                        print(f"{i} - {cat.nome}")
                                    print("-" * 20)

                            case "4":
                                if not categorias:
                                    print("Nenhuma categoria cadastrada.")
                                    continue

                                for i, cat in enumerate(categorias):
                                    print(f"{i} - {cat.nome}")

                                indice = int(input("Escolha a categoria: "))
                                categorias[indice].listar_filmes()

                            case "0":
                                print("Encerrando...")
                                break

                            case _:
                                print("Opção inválida!")

                    except ValueError as e:
                        print("Erro:", e)
                    except IndexError:
                        print("Índice inválido!")

            case 10:
                while True:
                    print("[MENU PEDIDOS]")
                    print("1 - Inserir cliente")
                    print("2 - Criar pedido")
                    print("3 - Adicionar pedido a cliente")
                    print("4 - Exibir pedidos")
                    print("0 - Sair")
                    print("-" * 20)

                    opcao = input("Escolha: ")
                    print("-" * 20)

                    match opcao:

                        case "1":
                            nome = input("Nome do cliente: ")
                            cpf = input("Digite o cpf: ")

                            cliente = Cliente(nome, cpf)
                            print("Cliente registrado com sucesso")

                        case "2":
                            i = 1
                            id = i
                            nome = input("Digite o produto que deseja: ")
                            quantidade = int(input(f"Quantos {nome} você deseja encomendar? "))

                            pedido = Pedidos(id, nome, quantidade)

                            print("Pedido criado com sucesso!")
                            i += 1


                        case "3":
                            cliente.adicionar_pedidos(pedido)
                            print("Pedido adicionado para o cliente!")

                        case "4":
                            cliente.exibir_pedidos()

                        case "5": # testes
                            cliente = Cliente("fernando","03702309063")

                            pedido = Pedidos(1, "Gatorade", 2)

                            cliente.adicionar_pedidos(pedido)
                            

                        case "0":
                            print("Encerrando...")
                            break

                        case _:
                            print("Opção inválida!")



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