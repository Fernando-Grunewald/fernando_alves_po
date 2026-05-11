from email import Email
from sms import SMS
from push import PushNotification

def menu_notificacoes():
    while True:
        print(" Notificações ")
        print("1 - Enviar E-mail")
        print("2 - Enviar SMS")
        print("3 - Enviar Push Notification")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            destino = input("Digite o e-mail do destinatário: ")
            mensagem = input("Digite a mensagem: ")
            Email(destino).enviar(mensagem)

        elif opcao == "2":
            destino = input("Digite o número de telefone: ")
            mensagem = input("Digite a mensagem: ")
            SMS(destino).enviar(mensagem)

        elif opcao == "3":
            destino = input("Digite o nome de usuário do app: ")
            mensagem = input("Digite a mensagem: ")
            PushNotification(destino).enviar(mensagem)

        elif opcao == "4":
            print("Encerrando o sistema de notificações.")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_notificacoes()