class Usuario4:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    @classmethod
    def criar_usuario_fixo(cls):
        """Método pra criar usuário fixo"""
        print("Usuário criado!")
        return cls ("UsuárioTeste", "usuariotest@outlook.com")
    
    def enviar_email_boas_vindas(self):
        print(f"[ Boas vindas, {self.nome}! ]")


#========================================================================

def exercicio_04():
    usuario_fixo = Usuario4.criar_usuario_fixo()

    usuario_fixo.enviar_email_boas_vindas()


# Exercício 4 – Enviar email de boas-vindas 
# Criar um usuário com nome e email fixos e chamar o método de instância 
# enviar_email_boas_vindas() para simular o envio de uma mensagem.