class Gato:

    def __init__(self, cat_name="Nix", cat_color="preta"):
        
        self.cat_name = cat_name
        self.cat_color = cat_color
    
    def cat_meow(self):
        print(f" — Aquela gatinha {self.cat_color} chamada {self.cat_name} está miando sem parar!")
        print("\n Miau Miau Miau Miau!" * 3)
