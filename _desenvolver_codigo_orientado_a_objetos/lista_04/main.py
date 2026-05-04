from imports import *

def lista_4():
   print("-" * 20)
   while True:

        print("Lista de Exercícios 4\n")
        print("[1] - Exercício 1.")
        print("[2] - Exercício 2.")
        print("[3] - Exercício 3.")
        print("[4] - Exercício 4.")
        print("[0] - Sair")
        print("-" * 20)

        opcao = int(input("Escolha uma opção: "))

        match opcao:
            case 1:
                exercicio_01()
            case 2:
                exercicio_02()
            # case 3:
            #     exercicio_03()
            # case 4:
            #     exercicio_04()
            case 0:
                print("Encerrando script. Até mais...")
                break
            case _:
                print(f" A opção {opcao} é inválida. Tente novamente.")
                
if __name__ == "__main__":
    lista_4()

# Regra comum para todos os exercícios
# Toda interação com o usuário deve ser feita via menu interativo na função main() do 
# programa principal.
# O menu principal deve permitir que o usuário escolha qual exercício executar.
# Cada exercício está em um pacote próprio, com suas classes em módulos separados.
# Para rodar o exercício, o menu deve importar e executar o módulo chamado 
# executar_respectivo_exercicioX.py (onde X é o número do exercício), que terá a 
# lógica para rodar aquele exercício, incluindo a interação via input().

# Exercício 1
# Pacote: exercicio1
# Módulos: usuario.py, cliente.py, cliente_vip.py
# Desenvolva uma estrutura de classes que modele uma hierarquia simples de usuários em 
# um sistema. Essa hierarquia deve permitir que um cliente possa realizar login e efetuar 
# compras, com um comportamento adicional reservado apenas a clientes VIP. Sua 
# implementação deve demonstrar o uso de herança e reutilização de código entre as classes. 
# Os métodos devem exibir mensagens descritivas que evidenciem as ações executadas e a 
# classe que as realiza. No módulo de execução, o programa deve interagir com o usuário por 
# meio do terminal: coletar um nome via input, instanciar o tipo apropriado de usuário, e 
# demonstrar o funcionamento da hierarquia chamando os métodos relevantes em 
# sequência.

# Exercício 2
# Pacote: exercicio2
# Módulos: base_notificacao.py, pagamento.py, notificacao.py, 
# pagamento_com_notificacao.py
# Implemente um conjunto de classes relacionadas à funcionalidade de pagamentos e 
# notificações. O sistema deve ser organizado para permitir a execução encadeada de 
# métodos, explorando conceitos de herança múltipla, sobrescrita, e o uso do método 
# super() de forma controlada. A estrutura final deve permitir a criação de uma instância 
# que realize um pagamento e dispare notificações, respeitando a cadeia de herança e 
# garantindo que todas as versões relevantes do método sejam executadas na ordem correta.
# No módulo de execução, demonstre o comportamento esperado chamando os métodos da 
# instância criada. Inclua comentários no código explicando a sequência das mensagens 
# exibidas e como ela está relacionada à resolução de método

# Exercício 3 
# Pacote: exercicio3
# Módulos: produto.py, livro.py, eletronico.py, pessoa.py, registro.py, 
# funcionario.py
# Implemente um sistema que modele uma pequena estrutura de produtos e pessoas 
# envolvidas em um processo de registro. Este exercício explora conceitos de herança 
# hierárquica, herança múltipla e sobrescrita de métodos, além da organização modular. A 
# estrutura deve permitir: O uso de uma classe genérica de produto que pode ser 
# especializada em tipos distintos. A representação de um funcionário que herda de múltiplas 
# classes para compor seu comportamento. A criação de objetos e a chamada de métodos 
# para exibir informações e registrar ações. No módulo principal, o programa deve interagir 
# com o usuário, instanciar objetos com base nos dados fornecidos e demonstrar o 
# funcionamento da hierarquia definida. O comportamento esperado deve ser evidenciado 
# pela execução dos métodos, que devem imprimir mensagens representativas de suas 
# responsabilidades.

# Exercício 4 
# Pacote: exercicio4
# Módulos: pessoa.py, suporte.py, funcionario.py, tecnico.py,
# Implemente um sistema que explore o funcionamento da herança múltipla, com foco 
# especial na ordem de resolução de métodos. A estrutura deve ser composta por diferentes 
# classes que representam tipos de pessoas e funções desempenhadas dentro de uma 
# organização, cada uma com sua própria implementação de um método responsável por 
# identificá-las. A hierarquia deve permitir que, ao chamar um único método em uma 
# instância de uma das classes mais especializadas, sejam acionados comportamentos 
# definidos em diversas superclasses, seguindo a ordem de resolução determinada 
# automaticamente pela linguagem. Essa cadeia de chamadas deve ser construída com o uso 
# de chamadas à superclasse em cada sobrescrita do método envolvido. No módulo principal, 
# o programa deve criar uma instância da classe mais derivada e acionar o método de 
# identificação, permitindo que todas as etapas da hierarquia sejam percorridas 
# corretamente. O código também deve conter comentários explicando a ordem em que as 
# mensagens são exibidas, justificando a sequência com base no mecanismo de resolução de 
# herança utilizado pela linguagem