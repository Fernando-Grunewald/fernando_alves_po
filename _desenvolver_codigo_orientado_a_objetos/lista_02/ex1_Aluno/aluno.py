# Exercício 1 
# Crie a classe Aluno com: 
# Atributo público nome 
# Atributo protegido _matricula Atributo 
# privado __senha_portal Adicione: 
# Um método exibir_senha() que imprime a senha.

class Aluno:
    def __init__(self, nome, matricula, senha_portal):
        self.nome = nome
        self._matricula = matricula
        self.__senha_portal = senha_portal


    @property
    def senha(self):
        """
        Método Getter para senha da classe Aluno
        """
        return self.__senha_portal
    
    @senha.setter
    def senha(self, nova_senha):
        """
        Método Setter para modificar a senha da classe Aluno
        """
        return nova_senha
    
    def exibir_senha(self):
        """
        Método para eu poder exibir a senha PRIVADA do Aluno
        """
        print(f"Senha do aluno: {aluno.__senha_portal}")

aluno = Aluno("Félix", 11000066, "Fe1521")

print(f"Aluno: {aluno.nome} \nMatrícula: {aluno._matricula}")
aluno.exibir_senha()


