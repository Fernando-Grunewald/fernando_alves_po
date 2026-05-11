class Notificacao:
    def __init__(self, destino):
        self.destino = destino

    def enviar(self, mensagem):
        print(f"Enviando notificação genérica para {self.destino}: {mensagem}")