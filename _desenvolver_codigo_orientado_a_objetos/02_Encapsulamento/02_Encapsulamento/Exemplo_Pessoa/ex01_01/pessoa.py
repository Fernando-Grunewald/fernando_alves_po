class Pessoa:
    def __init__(self, nome, cpf, idade):
        self.nome = nome        
        self.cpf = cpf         
        self.idade = idade       

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, valor: str):
        cpf_limpo = valor.replace(".", "").replace("-", "")
        if not cpf_limpo.isdigit() or len(cpf_limpo) != 11:
            raise ValueError("CPF deve conter 11 dígitos numéricos.")
        self.__cpf = cpf_limpo


    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, valor: int):
        if not (0 <= valor <= 120):
            raise ValueError("Idade deve estar entre 0 e 120.")
        self.__idade = valor


    def apresentar(self):
        idade_texto = str(self.idade) + " anos"
        cpf_texto = self.cpf
        return f"{self.nome}, {idade_texto} | CPF: {cpf_texto}"