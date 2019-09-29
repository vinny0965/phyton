class No:

    def __init__(self, valor):
        self.dado = valor
        self.proximo = None
        self.anterior = None

    def setDado(self, valor):
        self.dado = valor

    def getDado(self):
        return self.dado

    def setProximo(self, no):
        self.proximo = no

    def getProximo(self):
        return self.proximo

    def setAnterior(self, no):
        self.anterior = no

    def getAnterior(self):
        return self.dado

class Lista:

    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def isEmpty(self):
        if self.inicio == self.fim == None:
            return True
        return False

    def addInicio(self, valor):
        novo = No(valor)

        if self.isEmpty():

            self.inicio = self.fim = novo
        else:
            novo.setProximo(self.inicio)
            self.inicio = novo
        self.tamanho += 1

    def addFim(self, valor):

        novo = No(valor)

        if self.isEmpty():
            self.addInicio(valor)

        else:
            self.fim.setProximo(novo)
            self.fim = novo
        self.tamanho += 1

    def print(self):
        aux = self.inicio
        ant = "["
        while aux is not None:
            print("dado: ", aux.getDado())
            ant += str(aux.dado) + ","
            aux = aux.getProximo()
            print(ant, "]")
