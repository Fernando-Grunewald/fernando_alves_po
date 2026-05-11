class Pato:
    def fazer_som(self):
        print("Quack!")

class Cachorro:
    def fazer_som(self):
        print("Au au!")

class Pessoa:
    def fazer_som(self):
        print("Olá!")

def fazer_animais_falarem(animal):
    animal.fazer_som()

for animal in [Pato(), Cachorro(), Pessoa()]:
    fazer_animais_falarem(animal)