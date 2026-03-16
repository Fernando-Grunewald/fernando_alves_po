from usuario.cliente import Usuario
from treino.exercicio import Exercicio
from treino.plano import PlanoTreino
def main():

    usuario_atual = Usuario()
    plano_atual = PlanoTreino()

    while True:

        print("\n Menu Academia")
        print("1 - Criar/editar usuário")
        print("2 - Criar/editar plano de treino")
        print("3 - Adicionar exercício ao plano")
        print("4 - Mostrar plano de treino")
        print("0 - Sair")

        opcao = int(input("Escolha uma opção: "))

        match opcao:

            case 1:
                usuario_atual.nome = input("Nome do usuário: ")
                usuario_atual.idade = int(input("Idade do usuário: "))
                usuario_atual.apresentar()

            case 2:
                plano_atual.nome_plano = input("Nome do plano de treino: ")
                print("Plano criado/editado com sucesso!")

            case 3:
                nome_exercicio = input("Nome do exercício: ")
                repeticoes = int(input("Número de repetições: "))
                novo_exercicio = Exercicio(nome_exercicio, repeticoes)
                plano_atual.adicionar_exercicio(novo_exercicio)
                print("Exercício adicionado ao plano!")

            case 4:
                plano_atual.mostrar_plano()

            case 0:
                print("Encerrando programa")
                break

            case _:
                print("Opção inválida!")


if __name__ == "__main__":
    main()