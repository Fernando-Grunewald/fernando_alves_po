class Departamento:
    
    def __init__(self, nome="Departamento de Funcionários"):
        self.nome = nome
        self.funcionarios = []

    # def adicionar_funcionario(self, funcionario):
    #     self.funcionarios.append(funcionario)

    def listar_funcionarios(self):
        for funcionario in self.funcionarios:
            funcionario.atributos_funcionario()
            print("-" * 20)