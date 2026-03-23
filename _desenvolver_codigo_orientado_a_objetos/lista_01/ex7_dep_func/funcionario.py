class Funcionario:
    
    def __init__(self, nome, cpf, telefone, salario):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.salario = salario

    def inserir_funcionario(self, novo_func, nome, cpf, telefone, salario):
        self.novo_func = novo_func
        self.nome = input("Digite o nome do funcionário: ")
        self.cpf = input("Digite o cpf do funcionário: ")
        self.telefone = input("Digite o telefone do funcionário: ")
        salario = 0
        novo_func = Funcionario(nome, cpf, telefone, salario)

    def adicionar_salario(self, salario):
        self.salario = input(f"Digite o Salário de {self.nome}:")
        self.novo_func = Funcionario(self.nome, self.cpf, self.telefone, salario)
    
    



        
        

