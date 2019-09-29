class No:
    def __init__(self, elemento):
        self.dado = elemento
        self.proximo = None
        self.anterior = None

    def __str__(self):
        return str(self.elemento)

class ListaDuplamente:
    def __init__(self, tipo=None):
        self.__tamanho = 0
        self.inicio = None
        self.fim = None
        self.__tipo = tipo

    def __str__(self):
        valor = '['
        if self.inicio is not None:
            perc = self.inicio
            valor += str(perc.elemento)

            while perc.proximo is not None:
                perc = perc.proximo
                valor += ','
                valor += str(perc.elemento)
        valor += "]"
        return valor

    def add(self, novoElemento):
        if self.__tipo != None:
            if type(novoElemento) != self.__tipo:
                raise TypeError('Tipo Inválido')

        no = No(novoElemento)

        if self.fim is None:
            self.inicio = no
            self.fim = no
        else:
            self.fim.proximo = no
            self.fim = no
        self.__tamanho += 1







