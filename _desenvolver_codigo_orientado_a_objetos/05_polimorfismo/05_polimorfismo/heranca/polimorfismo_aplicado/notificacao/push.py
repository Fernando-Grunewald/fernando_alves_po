from base import Notificacao

class PushNotification(Notificacao):
    def enviar(self, mensagem):
        print(f"Enviando push notification para {self.destino}: {mensagem}")