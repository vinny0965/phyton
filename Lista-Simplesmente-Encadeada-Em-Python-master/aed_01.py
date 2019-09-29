class No:
    def __init__(self,valor):
        self.valor = valor
        self.proximo = None


    def __str__(self):
        return str(self.valor)

class Listaencadeada:
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
        print(self.tamanho)
        cont = 0
        perc = self.inicio
        if index < 0 or index > self.tamanho:
            raise("Posição Inválida")
        else:
            while cont != index:
                perc = perc.proximo
                cont += 1
            print(perc)



lista = Listaencadeada()
lista.add(20)
lista.add(30)
lista.inserir(1,13)
lista.inserir(2,12)
lista.buscarIndex(3)
print(lista)

