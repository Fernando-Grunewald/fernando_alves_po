class Funcionario:
    
    def __init__(self, nome="Nome Vazio", cpf="Cpf Vazio", telefone="Telefone Vazui", salario=0):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.salario = salario

    def editar_salario(self):
        try:
            self.salario = float(input(f"Digite o novo salário de {self.nome}: R$ "))
        except:
            print("Valor inválido! Não foi possível editar o salário.")

    def atributos_funcionario(self):
        print(f"Funcionário: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Telefone: {self.telefone}")
        print(f"Salário: R${self.salario:.2f}")


                                

        
        

