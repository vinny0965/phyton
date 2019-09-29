class No:
    def __init__(self, elemento):
        self.dado = elemento
        self.proximo = None

    def setDado(self, elemento):
        self.dado = elemento
    def getDado(self):
        return self.dado
    def setProximo(self, no):
        self.proximo = no
    def getProximo(self):
        return self.proximo


class ListaDuplamente:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def vazia(self):
        if self.inicio == self.fim == None:
            return True
        return False

    def addIncio(self, elemento):
        novo = No(elemento)
        if self.vazia():
            self.inicio = self.fim = novo
        else:
            novo.setProximo(self.inicio)
            self.inicio = novo

    def addFim(self, elemento):
        novo = No(elemento)
        if self.vazia():
            self.inicio = self.fim = novo
        else:
            self.fim.setProximo(novo)
            self.fim = novo

    def imprimirLista(self):
        a = self.inicio
        b = "["
        while a is not None:
            print("Dado: ", a.getDado())
            b += str(a.dado) + ","
            a = a.getProximo()
            print(b, "]")



