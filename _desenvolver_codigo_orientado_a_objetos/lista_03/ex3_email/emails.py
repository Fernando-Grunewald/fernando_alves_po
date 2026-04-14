class Usuario3:
    def __init__(self, nome, email):
        if not Usuario3.validar_email(email):
            raise ValueError("Email inválido!")
        self.nome = nome
        self.email = email

    @staticmethod
    def validar_email(email):
        return "@" in email and "." in email
    
#===============================================================
    
def exercicio_03():
    lista_emails = []
    quant_emails = int(input("Quantos emails deseja validar hoje? "))
    print("-" * 15)
    for i in range(quant_emails):
        email = input(f"Digite o {i+1}º email para validação: ")
        lista_emails.append(email)

    print("-" * 15)
    print("Lista de emails: ",lista_emails)
    print("-" * 15)
    contador = 1
    for e in lista_emails:
        validar = Usuario3.validar_email(e)
        print(f"{contador}º Email: {e} = {'Válido' if validar else 'Inválido'}")
        contador += 1
    print("-" * 15)

# Exercício 3 – Validar uma lista de emails 
# Validar uma lista de emails, imprimindo se cada um é válido ou não, utilizando o 
# método estático validar_email().