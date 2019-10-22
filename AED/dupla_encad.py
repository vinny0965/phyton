class No(object):

    def __init__(self, valor):
        self.valor = (valor)
        self.anterior = None
        self.proximo = None


class ListaEncadeada(object):

    def __init__(self, *args):
        self.inicio = None
        self.fim = None
        self.tamanho = 0
        for item in args:
            self.adicionar(item)

    def __len__(self):
        return self.tamanho

    def __str__(self):

        aponta = self.inicio
        iniciar = False

        estilolista = "["

        while aponta:

            if type(aponta.valor) == str:
                temp = f"'{aponta.valor}'"

            else:
                temp = str(aponta.valor)

            if iniciar == False:
                estilolista += temp
                iniciar = True

            else:
                estilolista += "," + temp
            aponta = aponta.proximo
        return estilolista + "]"

    def __getitem__(self, indice):
        aponta = self.percorrer_indice(indice)
        return aponta.valor

    def __setitem__(self, indice, valor):
        aponta = self.percorrer_indice(indice)
        aponta.valor = valor

    def adicionar(self, valor):

        no = No(valor)

        if not self.inicio:

            self.inicio = no
            self.fim = self.inicio



        else:
            self.fim.proximo = no
            no.anterior = self.fim
            self.fim = no
        self.tamanho += 1

    def buscar_indice(self, indice):
        meio = self.tamanho // 2
        maximo = self.tamanho - 1
        if self.inicio and indice >= 0 and indice <= maximo:
            if indice >= meio:
                aponta = self.fim
                for item in range(maximo, indice, -1):
                    aponta = aponta.anterior
            else:
                aponta = self.inicio
                for item in range(indice):
                    aponta = aponta.proximo

            return aponta
        raise IndexError("Índice fora de alcance")

    def inserir(self, indice, valor):
        no = No(valor)
        if indice >= self.tamanho and indice >= 0:
            self.adicionar(valor)
        else:
            if indice == 0:
                no.proximo = self.inicio
                self.inicio.anterior = no
                self.inicio = no
            else:
                aponta = self.buscar_indice(indice)
                no.proximo = aponta
                no.anterior = aponta.anterior
                aponta.anterior.proximo = no
                aponta.anterior = no
            self.tamanho += 1

    def remover(self, indice):
        if indice == 0:
            self.inicio = self.inicio.proximo
            self.inicio.anterior = None

        elif indice == self.tamanho - 1:
            self.fim = self.fim.anterior
            self.fim.proximo = None
        else:
            aponta = self.buscar_indice(indice)
            aponta.anterior.proximo = aponta.proximo
            aponta.proximo.anterior = aponta.anterior
        self.tamanho -= 1

lista = ListaEncadeada()
#lista.inserir()
#print(lista)
#print(len(lista))
