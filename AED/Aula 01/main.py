class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        no.anterior = self.fim
    self.tamanho+=1

class ListaEncadeada:
    def __init__(self):
        self.inicio = None
        self.tamanho= 0
    def __str__(self):
        return ''
    def __len__(self):
        return self.tamanho
    def add(self, valor):
        pass
    def inserir(self, pos, valor):
        if pos> self.tamanho or self.tamanho==0:
            self.add(valor)
        else:
            no = No (valor)
            if pos ==0:
                self.inicio.anterior = no
                no.proximo = self.inicio
                self.inicio = no
            else:
                codValor = int(self.tamanho/2)
                if pos>codValor:
                    pass
                #direita para a esquerda
                else:
                    pass
        pass


lista = ListaEncadeada()
lista.add(10)
lista.add(50)
lista.add(100)
lista.add(200)
lista.add(500)
print(lista)
print(len(lista))
lista.inserir(2, 100)







