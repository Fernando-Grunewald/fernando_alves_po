class Produto: 
    def __init__(self, nome, preco): 
        self._nome = nome             
        self.__preco = preco          
 
    @property 
    def preco(self): 
        return self.__preco 
 
    @preco.setter 
    def preco(self, valor): 
        if valor >= 0: 
            self.__preco = valor 
        else: 
            print("Preço não pode ser negativo") 
 
    def exibir_info(self): 
        print(f"Produto: {self._nome}, Preço: R$ {self.__preco:.2f}") 
 
    @classmethod 
    def produto_padrao(cls): 
        return cls("Produto Genérico", 0.0) 
 
    @staticmethod 
    def categoria(): 
        print("Categoria: Geral") 
 
 
class Livro(Produto): 
    def __init__(self, nome, preco, autor): 
        super().__init__(nome, preco) 
        self._autor = autor           
        self.__paginas = 0            
 
    @property 
    def paginas(self): 
        return self.__paginas 
 
    @paginas.setter 
    def paginas(self, n): 
        if n > 0: 
            self.__paginas = n 
        else: 
            print("Número de páginas inválido") 
 
    def exibir_info(self): 
        super().exibir_info() 
        print(f"Autor: {self._autor}, Páginas: {self.__paginas}") 
 
    @classmethod 
    def livro_padrao(cls): 
        return cls("Livro Genérico", 10.0, "Autor Desconhecido") 
 
    @staticmethod 
    def tipo_livro(): 
        print("Tipo: Livro Impressão") 
 
 
class Eletronico(Produto): 
    def __init__(self, nome, preco, marca): 
        super().__init__(nome, preco) 
        self._marca = marca            
        self.__garantia = 12           
 
    @property 
    def garantia(self): 
        return self.__garantia 
 
    @garantia.setter 
    def garantia(self, meses): 
        if meses >= 0: 
            self.__garantia = meses 
        else: 
            print("Garantia inválida") 
 
    def exibir_info(self): 
        super().exibir_info() 
        print(f"Marca: {self._marca}, Garantia: {self.__garantia} meses") 
 
    @classmethod 
    def eletronico_padrao(cls): 
        return cls("Eletrônico Genérico", 100.0, "MarcaX") 
 
    @staticmethod 
    def tipo_eletronico(): 
        print("Tipo: Produto Eletrônico") 
 
 
# Testes 
l = Livro("Python 101", 59.90, "João") 
l.paginas = 350 
l.exibir_info() 
print("Preço:", l.preco) 
l.preco = 70.0 
print("Preço atualizado:", l.preco) 
Livro.tipo_livro() 
livro_pad = Livro.livro_padrao() 
livro_pad.exibir_info() 
 
e = Eletronico("Fone Bluetooth", 120.00, "Sony") 
e.garantia = 24 
e.exibir_info() 
Eletronico.tipo_eletronico() 
eletronico_pad = Eletronico.eletronico_padrao() 
eletronico_pad.exibir_info() 
 