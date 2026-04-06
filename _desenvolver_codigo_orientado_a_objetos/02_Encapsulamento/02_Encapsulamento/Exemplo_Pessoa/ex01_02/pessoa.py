class Pessoa:
    def __init__(self, nome: str, cpf: str, idade: int):
        self.nome = nome
        cpf_limpo = cpf.replace(".", "").replace("-", "")
        if not cpf_limpo.isdigit() or len(cpf_limpo) != 11:
            raise ValueError("CPF deve conter 11 dígitos numéricos.")
        self.__cpf = cpf_limpo

        if not (0 <= idade <= 120):
            raise ValueError("Idade deve estar entre 0 e 120.")
        self.__idade = idade

    @property
    def cpf(self):
        return self.__cpf

    @property
    def idade(self):
        return self.__idade

    def apresentar(self):
        return f"{self.nome}, {self.idade} anos | CPF: {self.cpf}"
    



def main_pessoa():
    
    def validar_nome(nome):
        if not nome.strip():
            raise ValueError("O nome não pode estar vazio.")
        if nome.isdigit():
            raise ValueError("O nome não pode ser apenas números.")
        return nome.strip()
    

   
    nome = input("Digite o nome: ")
    cpf = input("Digite o CPF: ")
    idade = int(input("Digite a idade: "))

    try:
        nome_valido = validar_nome(nome)
       
        pessoa = Pessoa(nome_valido, cpf, idade)

        print("\nPessoa criada com sucesso!")
        print(pessoa.apresentar())

    except ValueError as e:
        print(f"Erro ao criar a pessoa: {e}")


if __name__=="__main__":
    main_pessoa()