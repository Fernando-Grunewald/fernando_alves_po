class Pato:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        print(f"{self.nome} diz: Quack!")
class Cachorro:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        print(f"{self.nome} diz: Au au!")

class Gato:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        print(f"{self.nome} diz: Miau!")



def fazer_animais_falarem(animal):
    animal.falar()

def menu_animais():
    tipos_animais = {
        "cachorro": Cachorro,
        "gato": Gato,
        "pato": Pato
    }

    while True:
        escolha = input("\nEscolha um animal (cachorro, gato, pato) ou 'sair' para encerrar: ").strip().lower()

        match escolha:
            case "sair":
                print("Até logo!")
                break
            case animal_nome if animal_nome in tipos_animais:
                nome = input("Digite o nome do animal: ")
                animal = tipos_animais[animal_nome](nome)
                fazer_animais_falarem(animal)
            case _:
                print("Animal não reconhecido. Tente novamente.")

menu_animais()