class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def enviar_email_boas_vindas(self):
        print(f"Enviando email para {self.email}...")
        print(f"Olá {self.nome}, seja bem-vindo à plataforma!")

def executar_metodo_instancia():
    usuario = Usuario("Maria", "maria@email.com")
    usuario.enviar_email_boas_vindas()

    input("\nPressione Enter para voltar ao menu...")

executar_metodo_instancia()