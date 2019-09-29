class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        #self.anterior = None

    def __str__(self):
        return str(self.valor)


class ListaEncadeada:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def __str__(self):
        if self.tamanho == 0:
            return '[]'
        valor = '['
        perc = self.inicio
        while perc.proximo != None:
            valor += str(perc.valor) + ','
            perc = perc.proximo
        valor += str(perc.valor) + ']'
        return valor

    def __len__(self):
        return self.tamanho

    def add(self, valor):
        no = No(valor)

        if self.inicio == None:
            self.inicio = no
            self.fim = no
        else:
            self.fim.proximo = no
            self.fim = no
        self.tamanho+=1
        pass


    def inserir(self, pos, valor):
       no = No(valor)

       cont = 1
       perc = self.inicio

       if self.inicio == None:
           self.inicio = no
           self.fim = no

       elif pos <=0:
           no.proximo = self.inicio
           self.inicio = no

       elif pos > self.tamanho:
           raise("Posição Inválida")



       else:
          while cont != pos:
            perc = perc.proximo
            cont += 1
          no.proximo = perc.proximo
          perc.proximo = no

       self.tamanho += 1


    def buscarIndex(self, index):
        pass
    def buscarValor(self, valor):
        pass
    def countPorValor(self, valor):
        pass
    def deletarIndex(self, index):
        pass
    def deletarValor(self, valor):
        pass
    def editarIndex(self, index):
        pass
    def editarValor(self, valor):
        pass


lista = ListaEncadeada()
# lista.add(10)
# lista.add(50)
# lista.add(60)
# lista.add(70)
lista.inserir(-2,80)
lista.inserir(-2,50)
lista.inserir(0,67)
lista.inserir(4,78)
#lista.inserir(0, 30)
#lista.inserir(1, 5)
#print(len(lista))
print(lista)
#print(lista.buscar(5))
