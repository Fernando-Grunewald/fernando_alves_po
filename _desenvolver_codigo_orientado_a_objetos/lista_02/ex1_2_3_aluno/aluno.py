# Exercício 1 
# Crie a classe Aluno com: 
# Atributo público nome 
# Atributo protegido _matricula Atributo 
# privado __senha_portal Adicione: 
# Um método exibir_senha() que imprime a senha.

# Exercício 2 
# Crie um objeto da classe Aluno. 
# Acesse diretamente o atributo nome. 
# Tente acessar diretamente _matricula e __senha_portal. 
# Use o método exibir_senha() para mostrar a senha corretamente. 
# Adicione um método get_matricula() e teste seu uso. 

# Exercício 3 
# Modifique a classe Aluno: 
# Crie o método get_senha() para retornar a senha. 
# Crie o método set_senha(nova_senha) que: 
# Só permite alterar a senha se ela tiver pelo menos 6 caracteres. 
# Caso contrário, exiba uma mensagem de erro. 

class Aluno:
    def __init__(self, nome, matricula, senha_portal):
        self.nome = nome
        self._matricula = matricula
        self.__senha_portal = senha_portal


    @property
    def senha(self):
        """Método Getter para senha da classe Aluno"""
        return self.__senha_portal
    
    @property
    def matricula(self):
        """Método Getter para a matrícula do Aluno"""
        return self._matricula
    
    @senha.setter
    def senha(self, nova_senha: str):
        """Método Setter para modificar a senha da classe Aluno"""
        if len(nova_senha) >= 6:
            self.__senha_portal = nova_senha
        else:
            print("A senha nova precisa ter ao menos 6 caracteres.")
            
    
    @matricula.setter
    def matricula(self, nova_matricula: int):
        """Método Setter da matrícula pra validar e atualizar"""
        if nova_matricula.isdigit() and nova_matricula >= 1:
            self._matricula = nova_matricula
            print(f"Matrícula atualizada: {self._matricula}")
        else:
            print("Erro: A matrícula deve ser maior que 1 e ser apenas composta por dígitos.")
    
    def exibir_senha(self):
        """Método para eu poder exibir a senha PRIVADA do Aluno"""
        print(f"Senha do aluno: {self.__senha_portal}")


    def get_senha(self): # ISSO É MALING NÃO FAZER (Compromete o usuário)
        """Método para em maling para retornar senha abruptamente com sucesso."""
        return self.__senha_portal


def exercicio_1():
    
    aluno = Aluno("Félix", 11000066, "Fe1521")

    print("=" * 15)
    print("[Exercício 1]")
    print(f"Aluno: {aluno.nome} \nMatrícula: {aluno._matricula}")
    aluno.exibir_senha()
    print("=" * 15)


# =============================================================

def exercicio_2():
    aluno = Aluno("Félix", 11000066, "Fe1521")

    print("[Exercício 2]")

    print(f"Nome do Aluno: {aluno.nome}.")
    print(f"Matrícula: {aluno._matricula}")
    print("-" * 15)

    try:

        print(f"Senha: {aluno.__senha_portal}")
        
    except AttributeError:
        print("ERRO = Não foi possível exibir forçadamente a senha estudantil.")
        print("-" * 15)

    aluno.exibir_senha()
    print("(Método de exibição com getter)")

    print("=" * 15)

# =============================================================

def exercicio_3():
    aluno = Aluno("Félix", 11000066, "PaoDeForma")

    print("[Exercício 3]")

    print("Senha Original:", aluno.senha)
    # print("Senha Original:", aluno.get_senha()) Isso também é uma forma de chegar ao resultado com uma função, mas é irresponsável!

    aluno.senha = input("Digite uma nova senha com 6 caracteres: ")

    print("Senha Final: ", aluno.senha)
    print("=" * 15)
