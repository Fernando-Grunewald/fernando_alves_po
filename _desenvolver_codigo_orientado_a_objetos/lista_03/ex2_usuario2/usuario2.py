class Usuario2:
    def __init__(self, nome, email, senha, tipo):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.tipo = tipo

    def exibir_info(self):
        """Método de Instância pra exibir tudo"""
        print(f"Nome: {self.nome}")
        print(f"Email: {self.email}")
        print(f"Senha: {self.senha}")
        print(f"Tipo: {self.tipo}")

    @classmethod
    def criar_usuario_teste(cls): # Sempre tem que ter apenas cls do lado aqui aonde iria um self.
        """Método de classe pra criar um usuário de teste"""
        print("Usuário padrão criado!")
        return cls ("Usuário Temporário", "usuariotemp@gmail.com", "12345", "Teste")
    

#================================================

def exercicio_02():
    print("Gerando usuário padrão...")
    
    usuario_teste = Usuario2.criar_usuario_teste()
    print("-" * 15)
    usuario_teste.exibir_info()
    print("-" * 15)

# Exercício 2 – Criar um usuário de teste 
# Usar o método de classe criar_usuario_teste() para instanciar um usuário padrão e 
# exibir seus dados usando o método de instância exibir_info().