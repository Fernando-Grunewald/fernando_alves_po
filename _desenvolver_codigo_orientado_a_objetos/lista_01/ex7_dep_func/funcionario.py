class Funcionario:
    
    def __init__(self, nome="Nome Vazio", cpf="Cpf Vazio", telefone="Telefone Vazio", salario=0):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.salario = salario

    def inserir_funcionario(self, novo_func, nome, cpf, telefone, salario):
        self.novo_func = novo_func
        nome = input("Digite o nome do funcionário: ")
        cpf = input("Digite o cpf do funcionário: ")
        telefone = input("Digite o telefone do funcionário: ")
        salario = 0
        self.novo_func = Funcionario(nome, cpf, telefone, salario)

    def editar_salario(self, salario):
        self.salario = int(input(f"Digite o Salário de {self.nome}:"))
        self.novo_func = Funcionario(self.nome, self.cpf, self.telefone, salario)

    def atributos_funcionario(self):
        print(f"Funcionário {self.nome}:")
        print(f"Cpf = [{self.cpf}]")
        print(f"Telefone = [{self.salario}]")
        print(f"Salário = [R${self.salario}]")



                                

        
        

