# Exercício 5 
# Crie a classe Funcionario com: 
# Atributo público nome 
# Atributo protegido _cargo Atributo 
# privado __salario Adicione os 
# métodos: 
# mostrar_detalhes() — imprime todos os dados. get_salario() 
# — retorna o salário. set_salario(valor) — só aceita valores 
# numéricos positivos. 

class Funcionario:
    def __init__(self, nome="Sem nome", cargo="Nenhum", salario_func="1"):
        self.nome = nome
        self._cargo = cargo
        self.__salario_func = salario_func

    @property
    def salario(self):
        """Método do Getter pra pegar o salário"""
        return self.__salario_func
    
    @salario.setter
    def salario(self, novo_salario: int):
        """Método Setter para aceitar apenas positivos."""
        if novo_salario >= 1:
            self.__salario_func = novo_salario
            print(f"Salário de {self.nome} alterado com sucesso para R${novo_salario} reais.")
        else:
            print("O salário não pode ser negativo ou igual a zero.")

    def mostrar_detalhes(self):
        """Método pra exibir todos os dados do funcionário."""
        print("(DADOS DO FUNCIONÁRIO)")
        print("Nome: ", self.nome)
        print("Cargo: ", self._cargo)
        print("Salário: R$", self.salario)
        

def exercicio_5():
    print("-" * 13)
    print("[Exercício 5]")
    print("-" * 13)
    func1 = Funcionario()
    nome_f = input("Digite o nome do funcionário: ")
    cargo_f = input("Digite o cargo dele na empresa: ")
    print("-" * 15)
    func1.nome = nome_f
    func1._cargo = cargo_f
    
    while True:
        print("-" * 13)
        print("[Exercício 5]")
        print("-" * 13)
        print("1 = Mostrar detalhes do funcionário.")
        print("2 = Editar valor do salário.")
        print("0 = Sair.")
        print("-" * 15)
        escolha = int(input("Escolha uma opção: "))
        print("-" * 15)

        match escolha:
            case 1:
                func1.mostrar_detalhes()
                input("Precione enter para voltar...")
            case 2:
                try:
                    func1.salario = int(input(f"Digite um novo salário: "))
                except ValueError as e:
                    print("Não foi possível editar o salário, tente novamente...")
            case 0:
                print("Até mais...")

            case _:
                print(f"{escolha} não é uma opção válida! Tente de novo.")







