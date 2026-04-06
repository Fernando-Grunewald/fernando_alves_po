class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome          
        self._idade = idade       
        self.__cpf = "000.000.000-00"  

    def exibir_cpf(self):
        print(f"CPF privado: {self.__cpf}")

def executar_base():
    print("\n público, protegido e privado \n")
    p = Pessoa("João", 30)
    print(f"Nome público: {p.nome}")         
    print(f"Idade protegida: {p._idade}")   
    try:
        print(f"CPF privado: {p.__cpf}")   
    except AttributeError:
        print("Não é possível acessar __cpf diretamente.")
    
    p.exibir_cpf()  

    input("Pressione Enter para voltar ao menu...")