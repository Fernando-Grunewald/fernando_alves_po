class Pessoa:
    def __init__(self, nome):
        self._nome = nome
        self.__id = 0

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, valor):
        if valor >= 0:
            self.__id = valor
        else:
            print("ID inválido")

    def identificar(self):
        print(f"Pessoa: {self._nome}")

    @classmethod
    def pessoa_padrao(cls):
        return cls("Pessoa Genérica")

    @staticmethod
    def especie():
        print("Espécie: Humano")



class Suporte:
    def __init__(self):
        self._setor = "Suporte Técnico"
        self.__nivel = 1

    @property
    def nivel(self):
        return self.__nivel

    @nivel.setter
    def nivel(self, valor):
        if valor > 0:
            self.__nivel = valor
        else:
            print("Nível inválido")

    def identificar(self):
        print("Equipe de Suporte")


    @classmethod
    def suporte_padrao(cls):
        return cls()

    @staticmethod
    def tipo_equipe():
        print("Equipe: Técnica")



class Funcionario(Pessoa):
    def __init__(self, nome):
        super().__init__(nome)
        self._cargo = "Funcionário"
        self.__salario = 0

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, valor):
        if valor >= 0:
            self.__salario = valor
        else:
            print("Salário inválido")

    def identificar(self):
        print("Funcionário")
        super().identificar()

    @classmethod
    def funcionario_padrao(cls):
        return cls("Funcionário Genérico")

    @staticmethod
    def setor():
        print("Setor: Administrativo")



class Tecnico(Suporte, Funcionario):
    def __init__(self, nome):
        Funcionario.__init__(self, nome)
        Suporte.__init__(self)
        self._especialidade = "TI"
        self.__certificacao = False

    @property
    def certificacao(self):
        return self.__certificacao

    @certificacao.setter
    def certificacao(self, valor):
        if isinstance(valor, bool):
            self.__certificacao = valor
        else:
            print("Certificação inválida")

    def identificar(self):
        print("Técnico")
        super().identificar()  

    @classmethod
    def tecnico_padrao(cls):
        return cls("Técnico Genérico")

    @staticmethod
    def nivel_tecnico():
        print("Nível: Júnior")


tec = Tecnico("Joana")
tec.identificar()

tec.salario = 3500
print("Salário:", tec.salario)

Tecnico.nivel_tecnico()
Funcionario.setor()
Suporte.tipo_equipe()
Pessoa.especie()