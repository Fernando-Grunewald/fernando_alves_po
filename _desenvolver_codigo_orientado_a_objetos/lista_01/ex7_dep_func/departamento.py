class Departamento:
    
    def __init__(self, nome="Departamento de Funcionários"):
        self.nome = nome
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)