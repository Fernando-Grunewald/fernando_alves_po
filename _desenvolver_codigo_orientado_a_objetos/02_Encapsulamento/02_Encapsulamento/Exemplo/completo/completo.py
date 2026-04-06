class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome             
        self._idade = idade          
        self.__cpf = "000.000.000-00"  

    @property
    def idade(self):
        """Getter para idade."""
        return self._idade

    @idade.setter
    def idade(self, nova_idade):
        """Setter com validação para idade."""
        if isinstance(nova_idade, int) and nova_idade >= 0:
            self._idade = nova_idade
        else:
            raise ValueError("Idade deve ser um número inteiro positivo.")

    @property
    def cpf(self):
        """Getter para o CPF."""
        return self.__cpf

    @cpf.setter
    def cpf(self, novo_cpf):
        """Setter controlado para alterar o CPF."""
        if isinstance(novo_cpf, str) and len(novo_cpf.strip()) > 0:
            self.__cpf = novo_cpf.strip()
        else:
            raise ValueError("CPF inválido.")

    def exibir_cpf(self):
        """Método que exibe o CPF de forma segura."""
        print(f"CPF (acesso via método): {self.__cpf}")


def executar_completo():
    print("\n--- Encapsulamento público, protegido e privado ---\n")

    print("Criando objeto Pessoa com nome='João' e idade=30...")
    p = Pessoa("João", 30)

    print("\n) Acessando atributo PÚBLICO diretamente:")
    print(f"Nome: {p.nome}")

    print("\n) Acessando atributo PROTEGIDO via getter:")
    print(f"Idade: {p.idade}")

    print("\n) Atualizando idade via setter (encapsulamento + validação):")
    p.idade = 35
    print(f"Idade atualizada: {p.idade}")

    print("\n) Acessando atributo PRIVADO de forma segura via @property:")
    print(f"CPF: {p.cpf}")

    print("\n) Atualizando CPF com setter seguro:")
    p.cpf = "111.222.333-44"
    print(f"Novo CPF: {p.cpf}")

    print("\n) Exibindo CPF via método da classe:")
    p.exibir_cpf()

    input("Pressione Enter para voltar ao menu...")


