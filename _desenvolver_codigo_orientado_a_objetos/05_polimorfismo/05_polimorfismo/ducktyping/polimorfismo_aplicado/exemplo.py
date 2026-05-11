class LogConsole:
    def escrever(self, mensagem):
        print(f"[Console] {mensagem}")

class LogArquivo:
    def __init__(self, caminho):
        self.caminho = caminho

    def escrever(self, mensagem):
        print(f"Simulando gravação de '{mensagem}' em {self.caminho}")

class LogRemoto:
    def escrever(self, mensagem):
        print(f"Enviando: {mensagem}")

def registrar_log(logger, mensagem):
    logger.escrever(mensagem)

def menu():
    print("Sistema de Logs")
    print("1 - Log no Console")
    print("2 - Log em Arquivo")
    print("3 - Log em Servidor Remoto")
    print("0 - Sair")

def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            print("Saindo do sistema de logs.")
            break

        if opcao == "1":
            logger = LogConsole()
        elif opcao == "2":
            logger = LogArquivo("log.txt")
        elif opcao == "3":
            logger = LogRemoto()
        else:
            print("Opção inválida. Tente novamente.")
            continue

        mensagem = input("Digite a mensagem do log: ")
        registrar_log(logger, mensagem)

if __name__ == "__main__":
    main()