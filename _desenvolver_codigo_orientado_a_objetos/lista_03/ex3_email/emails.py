class Usuario3:
    def __init__(self, nome, email):
        if not Usuario3.validar_emails(email):
            print("Email inválido!")
        self.nome = nome
        self.email = email

    @staticmethod
    def validar_emails(email):
        return "@" in email and "." in email
    
    









# class Usuario:
#     def __init__(self, nome, email):
#         if not Usuario.validar_email(email):
#             raise ValueError("Email inválido.")
#         self.nome = nome
#         self.email = email

#     @staticmethod
#     def validar_email(email):
#         return "@" in email and "." in email

# def executar_metodo_estatico():
  
#     print("Validando emails...\n")
#     emails = ["joao@email.com", "usuario-sem-arroba.com", "teste@gmail"]
    
#     for e in emails:
#         valido = Usuario.validar_email(e)
#         print(f"{e}: {'Válido' if valido else 'Inválido'}")

#     input("\nPressione Enter para voltar ao menu...")

#===============================================================

# Exercício 3 – Validar uma lista de emails 
# Validar uma lista de emails, imprimindo se cada um é válido ou não, utilizando o 
# método estático validar_email().