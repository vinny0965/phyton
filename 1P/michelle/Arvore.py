class No:
    def __init__(self, elemento):
        self.elemento = elemento
        self.filhoesq = None
        self.filhodir = None
        self.pai = None

    def __str__(self):
        return str(self.elemento)

class Arvore:
    def __init__(self):
        self.raiz = None
        self.__qtdFolhas = 0

    def add(self, elemento):
        no = No(elemento)
        perc = self.raiz

        if self.raiz is None:
            self.raiz = no

        else:
            while True:
                if no.elemento > perc.elemento:
                    if perc.filhodir is not None:
                        perc = perc.filhodir
                    else:
                        perc.dieita = no
                        break
                elif no.elemento < perc.elemento:
                    if perc.filhoesq is not None:
                        perc = perc.filhoesq
                    else:
                        perc.filhoesq = no
                        break
                else:
                    raise Exception("Elemento já adicionado a lista!")

        self.__qtdFolhas +=1

    def pesquisar(self, elemento, raiz):
        if not self.vazia():
            if (elemento == raiz.elemento()):
                return raiz
            elif elemento <= raiz.elemento() and raiz.filhoesq() != None:
                return self.pesquisar(elemento, raiz.filhoesq())
            elif raiz.filhodir() != None:
                return self.pesquisar(elemento, raiz.filhodir())
        return None

    def getTamanho(self):
        return self.__qtdFolhas

    def imprimirNo(self, no):
        if no is not None:
            self.imprimirNo(no.filhoesq)
            print(no)
            self.imprimirNo(no.filhodir)

    def imprimir(self):
        self.imprimir(self.raiz)

    def vazia(self):
        if self.raiz == None:
            return True
        return False

    def minimo(self, no=None):
        if no is None:
            no = self.raiz
        while no.filhoesq is not None:
            no = no.filhoesq
        return no

    def maximo(self, no=None):
        if no is None:
            no = self.raiz
        while no.filhodir is not None:
            no = no.filhodir
        return no

    def busca(self, elemento):
        if elemento > self.elemento:
            if self.elemento:
                return self.elemento.busca(elemento)
            else:
                return None
        elif elemento < self.elemento:
            if self.elemento:
                return self.elemento.busca(elemento)
            else:
                return None
        else:
            return self

    def sucessor(self, no):
        if not self.vazia():
            no = self.pesquisar(no, self.raiz)
            if no.filhodir() == None:
                return no.elemento()
            else:
                return self.minimo(no.filhodir())
        else:
            return None

    def predecessor(self, no):
        if not self.vazia():
            no = self.pesquisar(no, self.raiz)
            if no.filhoesq() == None:
                return no.elemento()
            else:
                return self.maximo(no.filhoesq())
        else:
            return None

    def balanco(self):
        prof_esq = 0
        if self.filhoesq:
            prof_esq = self.filhoesq.profundidade()
        prof_dir = 0
        if self.filhodir:
            prof_dir = self.filhodir.profundidade()
        return prof_esq - prof_dir

    def profundidade(self):
        prof_esq = 0
        if self.filhoesq:
            prof_esq = self.filhoesq.profundidade()
        prof_dir = 0
        if self.filhodir:
            prof_dir = self.filhodir.profundidade()
        return 1 + maximo(prof_esq, prof_dir)

    def rotacaoEsquerda(self):
        self.elemento, self.filhodir.elemento = self.filhodir.elemento, self.elemento
        old_esquerda = self.filhoesq
        self.filhoesq.filhodir
        self.filhoesq.filhoesq.filhodir(self.filhoesq.filhoesq, old_esquerda)

    def rotacaoDireita(self):
        self.elemento, self.filhoesq.elemento = self.filhoesq.elemento, self.elemento
        old_direita = self.filhodir
        self.filhodir.filhoesq
        self.filhodir.filhodir.filhoesq(self.filhodir.filhorei, old_direita)

    def rotacaoEsquerdaDireita(self):
        self.filhoesq.rotacaoEsquerda()
        self.rotacaoDireita()

    def rotacaoDireitaEsquerda(self):
        self.filhodir.rotacaoDireita()
        self.rotacaoEsquerda()

    def executaBalanco(self):
        bal = self.balanco()
        if bal > 1:
            if self.filhoesq.balanco() > 0:
                self.rotacaoDireita()
            else:
                self.rotacaoEsquerdaDireita()
        elif bal < -1:
            if self.filhodir.balanco() < 0:
                self.rotacaoEsquerda()
            else:
                self.rotacaoDireitaEsquerda()

    def altura(self, atual):
        if atual == None or atual.filhoesq == None and atual.filhodir == None:
            return 0
        else:
            if self.altura(atual.filhoesq) > self.altura(atual.filhodir):
                return 1 + self.altura(atual.filhoesq)
            else:
                return 1 + self.altura(atual.filhodir)

    def folhas(self, elemento):
        if elemento == None:
            return 0
        if elemento.filhoesq == None and elemento.filhodir == None:
            return 1
        return self.folhas(elemento.filhoesq) + self.folhas(elemento.filhodir)

    def contarNos(self, elemento):
        if elemento == None:
            return 0
        else:
            return 1 + self.contarNos(elemento.filhoesq) + self.contarNos(elemento.filhodir)

    def nivelArvore(self, no):
        if no is None:
            return 0
        else:
            if self.nivel(no, filhoesq) == None and self.nivel(no, filhodir) == None:
                return 1
            else:
                return self.nivel(no, filhoesq) + self.nivel(no, filhodir)

    def nivel(self):
        return self.nivelArvore(self, raiz)

    def remover(self, raiz, no):
        if not self.vazia():
            if self.raiz.elemento() == no:
                if (self.raiz.filhodir == None) and (self.raiz.filhodir == None):
                    pass
                elif (self.raiz.filhoesq == None) or (self.raiz.filhoesq == None):
                    pass
                elif (self.raiz.filhoesq != None) and (self.raiz.filhoesq != None):
                    pass
            else:
                pass
        else:
            print("Árvore Vazia!")

    def imprimeMenu(self):
        print('\n' + '\033[31m' + '=' * 30 + '\033[0;0m')
        print('\033[33m' + '(1)' + '\033[0;0m' + ' Inserir elemento')
        print('\033[33m' + '(2)' + '\033[0;0m' + ' Buscar elemento')
        print('\033[33m' + '(3)' + '\033[0;0m' + ' Remover elemento')
        print('\033[33m' + '(4)' + '\033[0;0m' + ' Listar nos')
        print('\033[33m' + '(5)' + '\033[0;0m' + ' Altura da arvore')
        print('\033[33m' + '(6)' + '\033[0;0m' + ' Niveis da arvore')
        print('\033[33m' + '(7)' + '\033[0;0m' + ' Soma de todos os nos')
        print('\033[33m' + '(8)' + '\033[0;0m' + ' Elementos de cada nivel')
        print('\033[33m' + '(9)' + '\033[0;0m' + ' Elemento maximo')
        print('\033[33m' + '(10)' + '\033[0;0m' + ' Elemento minimo')
        print('\033[33m' + '(11)' + '\033[0;0m' + ' Elemento predecessor')
        print('\033[33m' + '(12)' + '\033[0;0m' + ' Elemento Sucessor')
        print('\033[33m' + '(13)' + '\033[0;0m' + ' Total de elementos de um no')
        print('\033[33m' + '(14) ' + '\033[0;0m' + ' Balanceamento')
        print('\033[33m' + '(15) ' + '\033[0;0m' + ' Nivel do Elemento')
        print('\033[33m' + '(16) ' + '\033[0;0m' + ' Profundidade da arvore')
        print('\033[33m' + '(17) ' + '\033[0;0m' + ' Sair do programa')
        print('\033[31m' + '=' * 30 + '\033[0;0m' + '\n')

