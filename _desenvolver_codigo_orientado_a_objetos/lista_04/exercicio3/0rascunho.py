# Exercício 3 
# Pacote: exercicio3
# Módulos: produto.py, livro.py, eletronico.py, pessoa.py, registro.py, 
# funcionario.py
# Implemente um sistema que modele uma pequena estrutura de produtos e pessoas 
# envolvidas em um processo de registro. Este exercício explora conceitos de herança 
# hierárquica, herança múltipla e sobrescrita de métodos, além da organização modular. A 
# estrutura deve permitir: O uso de uma classe genérica de produto que pode ser 
# especializada em tipos distintos. A representação de um funcionário que herda de múltiplas 
# classes para compor seu comportamento. A criação de objetos e a chamada de métodos 
# para exibir informações e registrar ações. No módulo principal, o programa deve interagir 
# com o usuário, instanciar objetos com base nos dados fornecidos e demonstrar o 
# funcionamento da hierarquia definida. O comportamento esperado deve ser evidenciado 
# pela execução dos métodos, que devem imprimir mensagens representativas de suas 
# responsabilidades.

# -> Pessoa e Funcionário devem herdar a classe registro

# -> Livro e Eletronico devem herdar a classe produto

# -> Herança Hierárquica e Herança Múltipla

#==================================================================

class Registro:
    def __init__(self, nome, cpf, email):
        if not Registro.validar_cpf(cpf):
            print("Cpf inválido!")
        else:
            print("Cpf válido e cadastrado.")
        if not Registro.validacao_email(email):
            print("Este email é inválido!")
        else:
            print("Email válido para cadastro!")
        self.nome = nome
        self.cpf = cpf
        self.email = email

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, definir_cpf):
        if len(definir_cpf) == 11:
            self.__cpf = definir_cpf
        else:
            print("Inválido = O cpf deve possuir 11 caracteres numéricas.")

    @property
    def email(self):
        """Método Getter para podermos retornar o email privado"""
        return self.__email
    
    @email.setter
    def email(self, novo_email):
        """Método Setter pra poder alterar e manipular o email"""
        if novo_email != "":
            self.__email = novo_email
        else:
            print("O email não pode ser vazio!")
            
    def exibir_info(self):
        print("Nome: ", self.nome)
        print("Cpf: ", self.cpf)
        print("Email: ", self.email)
        
    def boas_vindas(self):
        print(f"Bem vindo(a) ao sistema {self.nome}!")

    @staticmethod
    def validacao_email(email):
        """Método Estático pra validar characteres em um email"""
        return "@" in email and "." in email
    
    @staticmethod
    def validar_cpf(cpf):
        """Método Estático pra validar cpf"""
        return len(cpf) != 11
    
    @classmethod # Método de classe pra registrar alguém
    def registrar(cls):
        nome = input("\nNome: ")
        cpf = input("CPF: ")
        email = input("Email: ")
        return cls(nome, email, cpf)

#==================================================================

class Pessoa(Registro):
    def __init__(self, nome, cpf, email, saldo):
        super().__init__(nome, cpf, email)
        self.saldo = saldo
        
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, novo_saldo: float):
        if novo_saldo >= 0:
            self.__saldo = novo_saldo
        else:
            print("O cliente não pode possuir um saldo negativo!")
            
    def exibir_info(self):
        super().exibir_info()
        print("Saldo: R$ ", self.saldo)
        
    def boas_vindas():
        super().boas_vindas()
        print("-Usuário logado como cliente-")

    def comprar(self):
        print("\n [ MERCADO LITERÁRIO ]")

#==================================================================

class Funcionario(Registro):
    def __init__(self, nome, email, num_contrat):
        super().__init__(nome, email)
        self.num_contrat = num_contrat
        
    def boas_vindas():
        super().boas_vindas()
        print("-Usuário logado como funcionário-")

    @classmethod
    def registrar(cls):
        return super().registrar()

#===================================================================

class Produto:
    def __init__(self, nome, codigo, preco, descricao):
        self.nome = nome
        self.codigo = codigo
        self.preco = preco
        self.descricao = descricao

    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, ajustar_preco: float):
        if ajustar_preco <= 0:
            print("Não podemos vender nenhum produto de graça! O preço não pode ser menor que zero.")
        else:
            self.__preco = ajustar_preco

    def detalhes(self): # Esse método será sobreescrito pelas classes que herdarem ele.
        print("| Nome do Produto: ", self.nome, " | Código: ", self.codigo)
        print("| Preço: [ R$ ", self.preco," ] ")
        print(f"| Descrição: {self.descricao}.")

    @classmethod
    def produto_generico(cls):
        return cls("Jornal", "0001", 1.75, "Um conjunto de reportagens, artigos e jogos contidos em papéis datados.") # nome - codigo - preco - descricao
        
#===================================================================

class Livro(Produto):
    def __init__(self, nome, codigo, preco, descricao, autor, categoria, paginas):
        super().__init__(nome, codigo, preco, descricao)
        self.autor = autor
        self.categoria = categoria
        self.paginas = paginas

    def detalhes(self):
        print(" [ L I V R O ] ")
        super().detalhes()
        print("| Autor: ", self.autor, "| Categoria: ", self.categoria, "| Quantia de páginas: ", self.paginas)

    def listar_livros(self, lista):
        print("[ LIVROS ]")
        for i, livro in enumerate(lista):
            print(f"{i} - {livro.nome}")
            print("-" * 20)

    @classmethod
    def livro_generico(cls):
        return cls("Harry Potter e A Pedra Filosofal", "0005", 24.99, "Livro de Fantasia e Aventura", "J. K. Rowling", "Juvenil", 384) # nome, codigo, preco, descricao, autor, categoria, paginas

#===================================================================

class Eletronico(Produto):
    def __init__(self, nome, codigo, preco, descricao, marca, tipo):
        super().__init__(nome, codigo, preco, descricao)
        self.marca = marca
        self.tipo = tipo
        self.eletronicos = []

    def detalhes(self):
        print(" [ E L E T R Ô N I C O ] ")
        super().detalhes()
        print("| Marca: ", self.marca, " | Tipo: ", self.tipo)

    @classmethod
    def ebook_generico(cls):
        return cls("Apple-Book", "1005", 659.99, "E-book para leitura de eReaders digitais.", "Apple", "E-book")

#===================================================================

print(" = " * 30)

livros = []

l1 = Livro("Harry Potter", 1, 50, "Magia", "J.K.", "Fantasia", 300)
l2 = Livro("Senhor dos Anéis", 2, 80, "Aventura", "Tolkien", "Fantasia", 500)

livros.append(l1)
livros.append(l2)

l1.listar_livros(livros)
l2.listar_livros(livros)


def listar(self):
    for i, livro in enumerate(self.livros):
        print(f"{i} - {livro.nome}")

def exercicio_03():

    lista_clientes = []
    lista_funcionarios = []
    pessoa_atual = ""

    
    while True:

        print("\n [ Exercício 3 ] ")
        print("\n [1] = Login")
        print("\n [2] = Cadastrar")
        print("\n [0] Encerrar")

        try:
            opcao = int(input("\n Escolha uma opção: "))
            
        except ValueError:
            print("Não foi possível escolher a opção - ", opcao)
            continue

        match opcao:
            case 1:
                nome = input("Digite o nome de usuário: ")
                email = input("Digite seu email para entrar: ")
                for i in lista_clientes + lista_funcionarios:
                    if i.nome == nome and i.email == email:
                        print("Login realizado.")
                        pessoa_atual = nome
                        break
                else:
                    print("Usuário e(ou) senha não encontrados.")

                

            case 2:
                cadastro = Registro.registrar()

                print(cadastro)
            
            case 0:
                print("Até mais!")
                break

exercicio_03()
        
        
