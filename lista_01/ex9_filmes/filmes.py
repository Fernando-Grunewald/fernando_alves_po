class Filme:

    def __init__(self, titulo="Filme sem título", diretor="Desconhecido", ano=0):
        self.__titulo = ""
        self.__diretor = ""
        self.__ano = 0

        self.titulo = titulo
        self.diretor = diretor
        self.ano = ano

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, valor):
        if not valor.strip():
            raise ValueError("Título inválido!")
        self.__titulo = valor

    @property
    def diretor(self):
        return self.__diretor

    @diretor.setter
    def diretor(self, valor):
        if not valor.replace(" ", "").isalpha():
            raise ValueError("Diretor inválido!")
        self.__diretor = valor

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, valor):
        if valor < 1800 or valor > 2100:
            raise ValueError("Ano inválido!")
        self.__ano = valor

    def detalhes_filme(self):
        print(f"Título: {self.__titulo}")
        print(f"Diretor: {self.__diretor}")
        print(f"Ano: {self.__ano}")