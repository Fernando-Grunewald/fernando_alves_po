import time
from datetime import date, datetime # Isso aqui pra importar data

class Pagamento:
    def __init__(self, valor):
        self.valor = valor
        self.confirmado = False # Privado. False por que o pagamento não está "confirmado", e uma confirmação é facilmente assosciada a um boleano
    
    @property
    def confirmado(self):
        """Método de Getter pra poder manipular o atributo (isso transforma o atributo em privado)"""
        return self.__confirmado
    
    @confirmado.setter # Ter um getter e setter o sistema já entende ele como privado
    def confirmado(self, status):
        """Método Setter pra garantir que o confirmado seja um boleano de False ou True"""
        if isinstance(status, bool): # isinstance para verificar se o atributo de confirmado é um boleano (bool né, igual str, int, float)
            self.__confirmado = status
        else:
            print("Valor inválido para uma confirmação")

    def pagamento_feito(self):
        """Método de para exibir que o pagamento foi confirmado"""
        self.__confirmado = True
        time.sleep(1)
        print(f"Um pagamento de R${self._valor} foi processado as ", datetime.today(),  ".")

    @classmethod
    def valor_padrao(cls):
        """Método de classe para deixar um valor fixo"""
        return cls(67.67)
    
    @staticmethod
    def tipo_pagamento(): # Não vai nada dentro das aspas em método estático
        print("Tipo: Pix.")

#===================================================================================== separar tudo nos modulos dps 
    
class Notificacao:
    def __init__(self):
        self.canal = "email"
        self.enviado = False

    @property
    def enviado(self):
        """Método Getter para fazer o atributo virar privado"""
        return self.__enviado
    
    @enviado.setter
    def eviado(self, valor):
        """Método de Setter de novo para garantir um boleano"""
        if isinstance(valor, bool):
            self.__enviado = valor
        else:
            print("Valor inválido enviado")

    def notificar(self):
        """Método para dizer por qual meio a notificação veio"""
        self.__enviado = True
        print(f"Notificação por {self._canal} enviada.")

    @classmethod # não entendi praq issu aqui
    def canal_padrao(cls):
        return cls()
    
    @staticmethod
    def tipo_notificao():
        """Método estático para mostrar a natureza da notificação"""
        print("Tipo: Instantânea")

#=====================================================================================

class PagamentoComNotificacao(Pagamento, Notificacao): # Herando duas classes
    def __init__(self, valor):
        Pagamento.__init__(self, valor)
        Notificacao.__init__(self)

    def processar(self):
        self.pagamento_feito()
        self.notificar()

#======================================================================================

def exercicio_02():
    while True:
                print("[ MENU ]")

                print("[1] Confirmar Pagamento.")
                print("[2] Enviar comprovante.")
                print("[0] Finalizar compra")
               
                try:
                    opcao = int(input("\nEscolha uma opção: "))
                except ValueError:
                    print("Entrada inválida.")
                    continue
                
                match opcao:

                    case 1:
                        pass

                    case 2:
                        pass

                    case 0:
                        break

                    case _:
                        print("Opção inválida.")


quantia = PagamentoComNotificacao(65.00)
quantia.processar()






