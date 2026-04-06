class Pessoa:
    def __init__(self, nome):
        self.nome = nome       
        self.__cpf   
        self.__idade   


    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, valor):
        cpf_limpo = valor.replace(".", "").replace("-", "")
        if not cpf_limpo.isdigit() or len(cpf_limpo) != 11:
            raise ValueError("CPF deve conter 11 dígitos numéricos.")
        self.__cpf = cpf_limpo


    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, valor):
        if not (0 <= valor <= 120):
            raise ValueError("Idade deve estar entre 0 e 120.")
        self.__idade = valor

    def apresentar_compression(self):
        idade_texto = f"{self.idade} anos" if self.idade is not None else "idade não definida"
        cpf_texto = self.cpf if self.cpf is not None else "CPF não definido"
        return f"{self.nome}, {idade_texto} | CPF: {cpf_texto}"
    
    def apresentar(self):
        if self.idade is not None:
            idade_texto = str(self.idade) + " anos"
        else:
            idade_texto = "idade não definida"

        if self.cpf is not None:
            cpf_texto = self.cpf
        else:
            cpf_texto = "CPF não definido"

        return self.nome + ", " + idade_texto + " | CPF: " + cpf_texto