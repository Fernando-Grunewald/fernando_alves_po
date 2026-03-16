class Cachorro:

    def __init__(self, dog_name="Apolo", dog_race="pastor alemão"):

        self.dog_name = dog_name
        self.dog_race = dog_race

    def dog_bark(self):
        print(f" — Aquele {self.dog_race} chamado {self.dog_name} não para de latir!")
        print("\n Au Au Au!" * 3)