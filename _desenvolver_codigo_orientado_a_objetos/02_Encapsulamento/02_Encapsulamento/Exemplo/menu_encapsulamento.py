from utils import *


def  menu_encapsulamento_introducao():
    while True:
        print("### Menu Encapsulamento ###\n")
        print("1 - Introdução")
        print("2 - Protegido")
        print("3 - Privado")
        print("2 - getter e setter")
        print("5 - Completo")
        print("0 - Sair")

        opcao = int(input("Escolha uma opção: "))
        match opcao:
             case 1:
                  executar_base()
             case 2:
                   executar_protegido()  
             case 3:
                 executar_privado()
             case 4:
                  executar_getter_setter()
             case 5: 
                 executar_completo()
             case 0:
                print("Encerrando programa")
                break
             case _:
                print("Opção inválida. Tente novamente.")
                
if __name__=="__main__":
    menu_encapsulamento_introducao()
