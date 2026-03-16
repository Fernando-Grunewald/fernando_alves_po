class Pessoa:

    def __init__(self, humano_nome="Fernando", humano_idade=20):

        self.humano_nome = humano_nome
        self.humano_idade = humano_idade

    def apresentacao_pessoal(self):
        print(f"Seu nome é {self.humano_nome}, e sua idade é {self.humano_idade}.")


