class Livro:
    def __init__(self, titulo="Título Vazio"):
        self.titulo = titulo
        self.disponivel = True
        self.historico = []  # pessoas que já pegaram

    def emprestar(self, nome_usuario):
        if self.disponivel:
            self.disponivel = False
            self.historico.append(nome_usuario)
            return True
        return False

    def devolver(self):
        self.disponivel = True

    def mostrar_info(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        print(f"Livro: {self.titulo}")
        print(f"Status: {status}")
        print(f"Histórico: {self.historico}")