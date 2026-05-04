class Notificacao:
    def __init__(self):
        self._canal = "email"
        self.enviado = False

    @property
    def enviado(self):
        """Método Getter para fazer o atributo virar privado"""
        return self.__enviado
    
    @enviado.setter
    def enviado(self, valor):
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
        print("Tipo de mensagem: Instantânea")