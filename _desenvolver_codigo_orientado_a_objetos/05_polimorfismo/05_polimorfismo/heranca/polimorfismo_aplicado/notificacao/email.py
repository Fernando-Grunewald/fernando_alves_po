from base import Notificacao

class Email(Notificacao):
    def enviar(self, mensagem):
        print(f"Enviando e-mail para {self.destino}: {mensagem}")