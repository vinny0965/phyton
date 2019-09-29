class Biblioteca:
    pessoa=None
    livro=None
    def __init__(self,pessoa,livro):
        self.pessoa=pessoa
        self.livro=livro
    def ImprimirBiblioteca(self):
        print(self.pessoa,self.livro)
bibli1=Biblioteca('vinicius',12)
bibli2=Biblioteca('jamisson',13)

bibli1.ImprimirBiblioteca()
bibli2.ImprimirBiblioteca()