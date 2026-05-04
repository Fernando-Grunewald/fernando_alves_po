import time
from datetime import date, datetime # Isso aqui pra importar data

class Pagamento:
    def __init__(self, valor):
        self._valor = valor
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
        time.sleep(1.5)
        print(f"Um pagamento de R${self._valor} foi processado às", datetime.now(), ".")

    @classmethod
    def valor_padrao(cls):
        """Método de classe para deixar um valor fixo"""
        print(f"\n Valor de transação padrão atribuído. R$35.99")
        return cls(35.99)
        
    @staticmethod
    def tipo_pagamento(): # Não vai nada dentro das aspas em método estático
        """Método estático para especificar o método padrão de pagamento"""
        print("Pagamento feito por Pix!")