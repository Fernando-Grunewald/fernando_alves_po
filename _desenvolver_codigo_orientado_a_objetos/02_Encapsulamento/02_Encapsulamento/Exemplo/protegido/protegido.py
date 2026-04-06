class Cofre:
    def __init__(self, segredo_inicial):
        self._segredo = segredo_inicial 

    @property
    def segredo(self):
  
        return self._segredo

    @segredo.setter
    def segredo(self, novo_segredo: str):
        if len(novo_segredo) >= 4 and novo_segredo.isalnum():
            self._segredo = novo_segredo
            print(f"Segredo atualizado para: {self._segredo}")
        else:
            print("Erro: O segredo deve ter pelo menos 4 caracteres e ser alfanumérico.")

def executar_protegido():

    cofre = Cofre("1234")
    print(f"Segredo inicial: {cofre.segredo}")

    print("\n--- Tentando alterar o segredo ---")
    cofre.segredo = "5678"
    print(f"Novo segredo: {cofre.segredo}")

    print("\n--- Testando validação ---")
  
    cofre.segredo = "123"
    print(f"Segredo atual após tentativa inválida: {cofre.segredo}")

    
    cofre.segredo = "abc!"
    print(f"Segredo atual após outra tentativa inválida: {cofre.segredo}")

    
    cofre._segredo = "xyz"
    print(f"Segredo alterado diretamente no '_segredo': {cofre.segredo}")
    input("Pressione Enter para voltar ao menu...")

