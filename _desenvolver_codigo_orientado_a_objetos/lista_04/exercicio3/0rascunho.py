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

    @staticmethod
    def validacao_email(email):
        """Método Estático pra validar characteres em um email"""
        return "@" in email and "." in email


#==================================================================

class Pessoa:
    def __init__(self, nome, email):
        

#==================================================================

class Funcionario:
    pass

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
        print("Produto: ", self.nome)
        print("Código: ", self.codigo)
        print("Preço: R$ ", self.preco)
        print(f"Descrição: {self.descricao}.")

    @classmethod
    def produto_generico(cls):
        return cls("Produto Genérico", "0000", 9.99, "...") # nome - codigo - preco - descricao
        
#===================================================================

class Livro(Produto):
    def __init__(self, nome, codigo, preco, descricao, autor, categoria, paginas):
        super().__init__(nome, codigo, preco, descricao)
        self.autor = autor
        self.categoria = categoria
        self.paginas = paginas

    def detalhes(self):
        super().detalhes()
        print("Autor: ", self.autor)
        print("Categoria: ", self.categoria)
        print("Quantia de páginas: ", self.paginas)

    @classmethod
    def livro_generico(cls):
        return cls("Nome Genérico", "0000", 24.99, "Livro de Genérico para preencher", "Autor Genérico", "Genérico", 100) # nome, codigo, preco, descricao, autor, categoria, paginas

#===================================================================

class Eletronico(Produto):
    def __init__(self, nome, codigo, preco, marca, tipo):
        super().__init__(nome, codigo, preco)
        self.marca = marca
        self.tipo = tipo

    def detalhes(self):
        super().detalhes()
        print("Marca: ", self.marca)
        print("Tipo: ", self.tipo)

    @classmethod
    def eletronico_generico(cls):
        return cls("Nome Genérico", "0000", 129.99, "Marca Genérica", "Genérico")

#===================================================================

livro_teste = Livro("Harry Potter e o Cálice de Fogo", "0001", 79.99, "Livro sobre a história de um jovem bruxo", "J. K. Rowling", "Fantasia", 339)
livro_generico = Livro.livro_generico()

livro_teste.detalhes()
print("=" * 30)
livro_generico.detalhes()