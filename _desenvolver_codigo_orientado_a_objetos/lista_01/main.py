from ex1_humano.humano import Pessoa
from ex2_gato_cachorro.cachorro import Cachorro
from ex2_gato_cachorro.gato import Gato
from ex3_carro.carro import Carro
from ex4_banco.banco import Banco
from ex4_banco.titular import Titular
from ex5_escolar.estudante import Estudante
from ex5_escolar.curso import Curso
from ex6_biblioteca.bibliotecario import Bibliotecario
from ex6_biblioteca.livro import Livro
from ex7_dep_func.departamento import Departamento
from ex7_dep_func.funcionario import Funcionario
from ex8_ecommerce.clientes import Cliente
from ex8_ecommerce.produtos import Produto
from ex9_filmes.categorias import Categoria
from ex9_filmes.filmes import Filme


# ADICIONAR ENCAPSULAMENTO!

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
        print(" [5] - Gerenciar estudantes.") # ARRUMAR E POLIR
        print(" [6] - Gerenciar livros.") # Ajeitar tudo
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
                        humano.humano_nome = input("Qual é seu nome? ")
                        humano.humano_idade = int(input("Qual é sua idade? "))
                        print("=" * 20)

                        if humano.humano_nome.isalpha() and (humano.humano_idade >=1, humano.humano_idade <= 100):
                            humano.apresentacao_pessoal()
                            break

                    except ValueError as e:
                        print(f"Entrada de dados inválida. Erro = ", e)

            case 2:
                while True:
                    try:
                        cachorrinho.dog_name = input("Digite um nome de cachorro: ")
                        cachorrinho.dog_race = input("Digite uma raça de cachorro: ")
                        gatinho.cat_name = input("Digite um nome de gato: ")
                        gatinho.cat_color = input("Digite uma cor de gato: ")
                        print("=" * 20)
                        continue

                    except ValueError as e:
                        print(f"Entrada de dados inválida. Erro = ", e)

                    finally:
                        cachorrinho.dog_bark()
                        gatinho.cat_meow()
                        break
            
            case 3:
                carro.atualizar_placa(nova_placa = input("Digite uma nova placa para seu carro: "))
                print("=" * 20)
                carro.atualizar_quilometragem(nova_quilometragem = int(input("Quantos KM seu carro andou hoje? ")))
                
            case 4:
                while True:
                    print("[MENU BANCÁRIO]")
                    print("1 - Depositar")
                    print("2 - Sacar")
                    print("3 - Ver conta")
                    print("0 - Sair")

                    opcao = input("Escolha: ")

                    match opcao:
                        case "1":
                            valor = float(input("Valor: "))
                            banco.depositar(banco, valor)

                        case "2":
                            valor = float(input("Valor: "))
                            banco.sacar(titular, valor)

                        case "3":
                            banco.mostrar_info(titular)

                        case "0":
                            break

                        case _:
                            print("Opção inválida.")

            case 5:

                while True:
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
                                    print(f"{i} - {est.nome}")

                                indice = int(input("Número: "))
                                nota = float(input("Nota: "))

                                curso.estudantes[indice].adicionar_nota(nota)
                                print("Nota adicionada!")

                            case "3":
                                curso.listar_estudantes()
                            
                            case 0:
                                print("Encerrando programa...")
                                break
            
                            case _:
                                print(f"A opção {opcao} é inválida!")

            case 6: 
                
                while True:
                    print("[MENU BIBLIOTECÁRIO]")
                    print("1 - Adicionar livro")
                    print("2 - Emprestar livro")
                    print("3 - Devolver livro")
                    print("4 - Listar livros")
                    print("5 - Ver bibliotecário")
                    print("0 - Sair")
                    livros = []
                    
                    opcao = input("Escolha: ")

                    match opcao:
                        case "1":
                            
                            livros = input("Título do livro: ")
                            livros = Livro(livro)
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
                            bibliotecario.devolver_livro(bibliotecario.livros_emprestados[indice])

                        case "4":
                            if len(livros) == 0:
                                print("Nenhum livro cadastrado.")
                            else:
                                for livro in livros:
                                    livro.mostrar_info()
                                    print("-" * 20)

                        case "5":
                            bibliotecario.mostrar_info()

            case 7:

                while True:
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

                        case "2":
                            nome = input("Digite o nome do funcionário: ")
                            
                            for func in departamento.funcionarios:
                                if func.nome == nome:
                                    func.editar_salario()
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

            case 8:

                produtos = []

                while True:
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

                            try:
                                preco = float(input("Preço: "))
                                estoque = int(input("Estoque inicial: "))
                            except:
                                print("Um dos valores é inválido!")
                                continue

                            novo = Produto(nome, preco, estoque)
                            produtos.append(novo)

                        case "2":
                            nome = input("Nome do produto: ")

                            for p in produtos:
                                if p.nome == nome:
                                    p.atualizar_estoque()
                                    break
                            else:
                                print("Produto não encontrado.")

                        case "3":
                            if not produtos:
                                print("Nenhum produto cadastrado.")
                            else:
                                for p in produtos:
                                    p.mostrar_produto()
                                    print("-" * 20)

                        case "4":
                            nome_cliente = input("Nome do cliente: ")
                            cliente = Cliente(nome_cliente)

                            nome_produto = input("Produto desejado: ")

                            for p in produtos:
                                if p.nome == nome_produto:
                                    cliente.comprar(p)
                                    break
                            else:
                                print("Produto não encontrado.")

                        case "0":
                            print("Encerrando...")
                            break

                        case _:
                            print("Opção inválida!")

            case 9:

                categorias = []

                while True:
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
                            nome_categoria = input("Categoria: ")

                            for cat in categorias:
                                if cat.nome == nome_categoria:

                                    titulo = input("Título: ")
                                    diretor = input("Diretor: ")

                                    try:
                                        ano = int(input("Ano: "))
                                    except:
                                        print("Ano inválido!")
                                        break
                                    
                                    filme = Filme(titulo, diretor, ano)
                                    cat.adicionar_filme(filme)
                                    break
                            else:
                                print("Categoria não encontrada.")

                        case "3":
                            if not categorias:
                                print("Nenhuma categoria cadastrada.")
                            else:
                                print("Categorias:")
                                for cat in categorias:
                                    print(f"- {cat.nome}")
                                print("-" * 20)

                        case "4":
                            nome_categoria = input("Categoria: ")

                            for cat in categorias:
                                if cat.nome == nome_categoria:
                                    cat.listar_filmes()
                                    break
                            else:
                                print("Categoria não encontrada.")

                        case "0":
                            print("Encerrando...")
                            break

                        case _:
                            print("Opção inválida!")

            # case 10:

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