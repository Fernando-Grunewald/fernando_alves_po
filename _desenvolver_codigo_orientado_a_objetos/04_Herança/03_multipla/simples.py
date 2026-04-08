class Pagamento: 
    def pagar(self): 
        print("Pagamento realizado.") 
 
class Notificacao: 
    def notificar(self): 
        print("Enviando notificação.") 
 
class PagamentoComNotificacao(Pagamento, Notificacao): 
    pass 
 
transacao = PagamentoComNotificacao() 
transacao.pagar()       
transacao.notificar()  
 