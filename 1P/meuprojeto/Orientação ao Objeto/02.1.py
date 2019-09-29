class Biblioteca:
    nome=None
    livros=None
    def __init__(self,nome,livros):
        self.nome=nome
        self.livros=livros
    def ImprimirBiblioteca(self):
        print(self.nome,self.livros)
bibli1=Biblioteca('Vinicius',114)
bibli2=Biblioteca('Matheus',123)

bibli1.ImprimirBiblioteca()
bibli2.ImprimirBiblioteca()