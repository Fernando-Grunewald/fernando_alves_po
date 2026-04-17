# Exercício 6 
# Crie a classe Cofre com: 
# Atributo privado __segredo 
# Atributo protegido _historico, uma lista com os segredos antigos Adicione os 
# métodos: 
# alterar_segredo(novo) — altera o segredo apenas se diferente do atual, e salva o 
# antigo no histórico. mostrar_historico() — imprime todos os segredos antigos 
# armazenados na lista.

class Cofre:
    def __init__(self, segredo):
        self.__segredo = segredo
        self._historico = []

    @property
    def alterar_segredo(self):
        """Método do Getter pra obter o segredo"""
        return self.__segredo

    @alterar_segredo.setter
    def alterar_segredo(self, novo_segredo: str):
        """Método do Setter pra podermos alterar a variável do segredo e adicionar ao histórico"""
        if novo_segredo == self.__segredo:
            print("O segredo não foi alterado, pois são iguais.")
        else:
            self._historico.append(self.__segredo)
            self.__segredo = novo_segredo
            print("Segredo alterado com sucesso!")
            print("O antigo foi enviado para o histórico...")
    
    def mostrar_historico(self):
        print("Histórico de segredos: ",self._historico)

#===========================================================================================

def exercicio_6():

    segredo_inicial = Cofre("Eu roubo o wifi do vizinho.")

    while True:
        print("-" * 13)
        print("[Exercício 6]")
        print("-" * 13)
        print("1 = Alterar um segredo.")
        print("2 = Exibir histórico de segredos.")
        print("0 = Sair.")
        print("-" * 15)
        escolha = int(input("Escolha uma opção: "))
        print("-" * 15)

        match escolha:
            case 1:
                print("Você escolheu substituir o segredo atual...")
                segredo_inicial.alterar_segredo = input("Digite um segredo novo: ")
            
            case 2:
                segredo_inicial.mostrar_historico()

            case 0:
                print("Até mais...")
                break
            
            case _:
                print("Opção inválida, tente novamente...")