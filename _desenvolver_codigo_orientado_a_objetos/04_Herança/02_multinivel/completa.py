class Veiculo:
    def __init__(self, marca):
        self._marca = marca
        self.__ligado = False

    @property
    def ligado(self):
        return self.__ligado

    @ligado.setter
    def ligado(self, valor):
        if isinstance(valor, bool):
            self.__ligado = valor
        else:
            print("Valor inválido para ligado")

    def ligar(self):
        self.__ligado = True
        print(f"{self._marca} está ligado.")

    @classmethod
    def fabrica_padrao(cls):
        return cls("VeiculoX")

    @staticmethod
    def tipo_veiculo():
        print("Tipo: Genérico")


class Terrestre(Veiculo):
    def __init__(self, marca, rodas):
        super().__init__(marca)
        self._rodas = rodas

    def rodar(self):
        print(f"{self._marca} rodando com {self._rodas} rodas.")


class Carro(Terrestre):
    def __init__(self, marca, rodas, modelo):
        super().__init__(marca, rodas)
        self._modelo = modelo

    def acelerar(self):
        print(f"{self._marca} {self._modelo} acelerando!")

    @classmethod
    def fabrica_padrao(cls):
        return cls("Toyota", 4, "Corolla")


carro = Carro("Toyota", 4, "Corolla")
carro.ligar()
carro.rodar()
carro.acelerar()
carro.ligado = True

Carro.tipo_veiculo()

novo = Carro.fabrica_padrao()
novo.ligar()