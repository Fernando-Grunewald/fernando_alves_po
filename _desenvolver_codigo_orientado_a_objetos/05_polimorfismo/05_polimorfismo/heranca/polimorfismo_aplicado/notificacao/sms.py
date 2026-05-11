from base import Notificacao

class SMS(Notificacao):
    def enviar(self, mensagem):
        print(f"Enviando SMS para {self.destino}: {mensagem}")
