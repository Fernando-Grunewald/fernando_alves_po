class Cofre:
    def __init__(self):
        self.__segredo:int = "1234"

    def mostrar_segredo(self):
        return self.__segredo

def executar_privado():
    c = Cofre()
    print("Segredo via método:", c.mostrar_segredo())
    try:
        print("Tentativa acesso direto:", c.__segredo)  
    except AttributeError:
        print("Não é possível acessar __segredo diretamente.")

   
    print("Acesso via name mangling:", c._Cofre__segredo)

    c._Cofre__segredo=12345
    input("Pressione Enter para voltar ao menu...")

    