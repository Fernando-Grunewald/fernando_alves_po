from metodo_instancia import executar_metodo_instancia
from metodo_estatico import executar_metodo_estatico
from metodo_classe import executar_metodo_classe
from completo import executar_menu_completo
def menu_metodos_convencionais():
    while True:
        print("1 - Método de Instância")
        print("2 - Método Estático (@staticmethod)")
        print("3 - Método de Classe (@classmethod)")
        print("4 - Completo")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            executar_metodo_instancia()
        elif opcao == '2':
            executar_metodo_estatico()
        elif opcao == '3':
            executar_metodo_classe()
        elif opcao == '4':
            executar_menu_completo()
        elif opcao == '0':
            break
        else:
            print("Opção inválida.")



if __name__=="__main__":
    menu_metodos_convencionais()