class Pagamento: 
    def __init__(self, valor): 
        self._valor = valor             
        self.__confirmado = False       
 
    @property 
    def confirmado(self): 
        return self.__confirmado 
 
    @confirmado.setter 
    def confirmado(self, status): 
        if isinstance(status, bool): 
            self.__confirmado = status 
        else: 
            print("Valor inválido para confirmação") 
 
    def pagar(self): 
        self.__confirmado = True 
        print(f"Pagamento de R$ {self._valor:.2f} realizado.") 
 
    @classmethod 
    def transacao_padrao(cls): 
        return cls(100.00) 
 
    @staticmethod 
    def tipo_pagamento(): 
        print("Tipo: Cartão de crédito") 
 
 
class Notificacao: 
    def __init__(self): 
        self._canal = "email"            
        self.__enviado = False           
 
    @property 
    def enviado(self): 
        return self.__enviado 
 
    @enviado.setter 
    def enviado(self, valor): 
        if isinstance(valor, bool): 
            self.__enviado = valor 
        else: 
            print("Valor inválido para enviado") 
 
    def notificar(self): 
        self.__enviado = True 
        print(f"Notificação enviada por {self._canal}.") 
 
    @classmethod 
    def canal_padrao(cls): 
        return cls() 
 
    @staticmethod 
    def tipo_notificacao(): 
        print("Tipo: Instantânea") 
 
 
class PagamentoComNotificacao(Pagamento, Notificacao): 
    def __init__(self, valor): 
        Pagamento.__init__(self, valor) 
        Notificacao.__init__(self) 
 
    def processar(self): 
        self.pagar() 
        self.notificar() 
 
 

transacao = PagamentoComNotificacao(250.00) 
transacao.processar()              
print("Confirmado?", transacao.confirmado) 
print("Enviado?", transacao.enviado) 
 
transacao.confirmado = True         
transacao.enviado = True 
 
PagamentoComNotificacao.tipo_pagamento()     
PagamentoComNotificacao.tipo_notificacao()  
 
nova = PagamentoComNotificacao.transacao_padrao() 
nova.processar()