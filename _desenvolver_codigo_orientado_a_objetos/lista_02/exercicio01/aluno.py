# Crie a classe Aluno com: 
# Atributo público nome 
# Atributo protegido _matricula Atributo 
# privado __senha_portal Adicione: 
# Um método exibir_senha() que imprime a senha.

class Aluno:
    def __init__(self, nome, matricula, senha):
        self.nome = nome
        self._matricula = matricula
        self.__senha = senha


    @property
    def senha(self):
        """
        Método Getter para senha da classe Aluno
        """
        return self.__senha
    
    @senha.setter
    def senha(self, nova_senha):
        """
        Método Setter para modificar a senha da classe Aluno
        """

aluno = Aluno("gabriel", 1, "senha")