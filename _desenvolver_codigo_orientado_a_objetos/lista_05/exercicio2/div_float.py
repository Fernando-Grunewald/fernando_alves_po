class DivisaoFloat:
    
    # Divisão comum (retorna float)
    # resultado = 7 / 2 
    # print(resultado)  Saída: 3.5

    # Divisão inteira (retorna int)
    # resultado_inteiro = 7 // 2
    # print(resultado_inteiro)  Saída: 3

    def __init__(self, valor):
        self.valor = valor
        
    def __truediv__(self, outro_valor):
        return DivisaoFloat(self.valor / outro_valor.valor)
    
    def __str__(self): 
        return f"Divisão com Float: {self.valor}" # acho que isso aqui é pra exibir resultado em print.
