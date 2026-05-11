class Notificacao:
    def __init__(self, destino):
        self.destino = destino

    def enviar(self, mensagem):
        print(f"Enviando notificação genérica para {self.destino}: {mensagem}")

class Email(Notificacao):
    def enviar(self, mensagem):
        print(f"Enviando e-mail para {self.destino}: {mensagem}")

class SMS(Notificacao):
    def enviar(self, mensagem):
        print(f"Enviando SMS para {self.destino}: {mensagem}")

class PushNotification(Notificacao):
    def enviar(self, mensagem):
        print(f"Enviando push notification para {self.destino}: {mensagem}")


notificacoes = [
    Email("usuario@exemplo.com"),
    SMS("+5511999999999"),
    PushNotification("UsuárioApp123")
]

for n in notificacoes:
    n.enviar("Seu pedido foi enviado!")