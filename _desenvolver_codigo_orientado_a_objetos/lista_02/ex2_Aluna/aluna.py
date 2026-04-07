# Exercício 2 
# Crie um objeto da classe Aluno. 
# Acesse diretamente o atributo nome. 
# Tente acessar diretamente _matricula e __senha_portal. 
# Use o método exibir_senha() para mostrar a senha corretamente. 
# Adicione um método get_matricula() e teste seu uso. 

class Aluna:
    def __init__(self, nome, matricula, senha_portal):
        self.nome = nome
        self._matricula = matricula
        self.__senha_portal = senha_portal

    @property
    def senha(self):
        """
        Método Getter para senha da classe Aluna
        """
        return self.__senha_portal
    
    @property
    def matricula(self):
        """
        Método Getter para a matrícula da Aluna
        """
    
    @senha.setter
    def senha(self, nova_senha):
        """
        Método Setter para modificar a senha da classe Aluno
        """
        return nova_senha
    
    @matricula.setter
    def matricula(self, nova_matricula: int):
        """
        Método Setter da matrícula pra validar e atualizar
        """
        if nova_matricula.isdigit() and nova_matricula >= 1:
            self._matricula = nova_matricula
            print(f"Matrícula atualizada: {self._matricula}")
        else:
            print("Erro: A matrícula deve ser maior que 1 e ser apenas composta por dígitos.")

    def exibir_senha(self):
        """
        Método para eu poder exibir a senha PRIVADA da Aluna
        """
        print(f"Senha: {aluna.__senha_portal} (Exibida com setter)")

aluna = Aluna("Fernanda", 293020, "PanquecasDeMirtilo")

print(f"Nome da Aluna: {aluna.nome}.")
print(f"Matrícula: {aluna._matricula}")
print("-" * 15)

try:

    print(f"Senha: {aluna.__senha_portal}")
    
except AttributeError:
    print("Não foi possível exibir forçadamente a senha estudantil. ERRO")
    print("-" * 15)

aluna.exibir_senha()


# def executar_protegido():

#     cofre = Cofre("1234")
#     print(f"Segredo inicial: {cofre.segredo}")

#     print("\n--- Tentando alterar o segredo ---")
#     cofre.segredo = "5678"
#     print(f"Novo segredo: {cofre.segredo}")

#     print("\n--- Testando validação ---")
  
#     cofre.segredo = "123"
#     print(f"Segredo atual após tentativa inválida: {cofre.segredo}")

    
#     cofre.segredo = "abc!"
#     print(f"Segredo atual após outra tentativa inválida: {cofre.segredo}")

    
#     cofre._segredo = "xyz"
#     print(f"Segredo alterado diretamente no '_segredo': {cofre.segredo}")
#     input("Pressione Enter para voltar ao menu...")