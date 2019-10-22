from No import No


class Lista(object):

    # Construtor
    def __init__(self):
        self.__inicio = None
        self.__ultimo = None

    # Métodos acessores
    def set_Inicio(self, inicio):
        self.__inicio = inicio

    def get_Inicio(self):
        return self.__inicio

    def set_Ultimo(self, ultimo):
        self.__ultimo = ultimo

    def get_Ultimo(self):
        return self.__ultimo

    # Método para adicionar no inicio da lista

    def inserir_Inicio(self, dado):
        # É instanciado um novo No
        novo_no = No()
        # São setados os valores desse No
        novo_no.set_Dado(dado)
        novo_no.set_Proximo(self.get_Inicio())
        # A lista recebe como novo elemento inicial o novo No
        self.set_Inicio(novo_no)
        # Verifica se o ultimo elemento da lista é None(null), se for, cadastrar o novo No como sendo o ultimo
        if self.get_Ultimo() is None:
            self.set_Ultimo(novo_no)

        print('O novo elemento cujo dado é ({}), foi adicionado com sucesso!'.format(dado))

    # Método para adicionar no final da lista

    def inserir_Fim(self, dado):
        # É instanciado um novo No
        novo_no = No()
        # São setados os valores desse No
        novo_no.set_Dado(dado)
        novo_no.set_Proximo(None)
        # Verifica se o ultimo não é None(null)
        if self.get_Ultimo() is not None:
            # O antigo elemento que era o ultimo recebe como valor 'proximo' o novo elemento
            # que será adicionado ao final da lista
            self.get_Ultimo().set_Proximo(novo_no)

        # A lista recebe como ultimo valor o novo elemento cadastrado
        self.set_Ultimo(novo_no)

        # Verifica se o 'inicio' da lista é None(Null)
        if self.get_Inicio() is None:
            # Cadastra o novo elemento como sendo o novo 'inicio'
            self.set_Inicio(novo_no)

        print('O elemento cujo dado é ({}) foi adicionado com sucesso!'.format(dado))

    # Método para remover do inicio da lista
    def remover_Primeiro(self):

        # Verifica se o elemento inicial da lista é diferente de None(Null)
        if self.get_Inicio() is not None:
            # Coloca o elemento inicial em uma variável temporária
            temp = self.get_Inicio()
            # Verifica se o proximo elemento não é None(Null)
            if temp.get_Proximo() is not None:
                # O novo elemento inicial da lista é o elemento 'proximo'
                self.set_Inicio(temp.get_Proximo())
                temp = None
                print('O primeiro elemento da lista foi removido com sucesso!')
            else:
                self.set_Inicio(None)
                self.set_Ultimo(None)
                temp = None
                print('A lista está vazia com a remoção do primeiro elemento!')

        else:
            print('A lista está vazia!')

    # Método para remover no final da lista

    def remover_Ultimo(self):

        #  Verifica se o elemento icial da lista é diferente de None(Null)
        if self.get_Inicio() is not None:
            # Cria-se uma variavel temporária, atual e anterior
            temp = self.get_Inicio()
            atual = self.get_Inicio()
            anterior = None

            # Percorre-se a lista até chegar no ultimo elemento
            while atual.get_Proximo() is not None:

                anterior = atual
                atual = atual.get_Proximo()

            # Verifica se tanto a variavel atual quanto a variavel anterior não são nulas
            if atual is not None and anterior is not None:

                anterior.set_Proximo(None)

            # Cadastra o elemento anterior ao 'ultimo' elemento como sendo o novo 'ultimo'
            self.set_Ultimo(anterior)

            # Verifica se o ultimo elemento é None(Null)
            if self.get_Ultimo() is None:
                # O inicio da lista também é cadastrado como None, logo a lista está vazia
                self.set_Inicio(None)
                print('A lista está vazia com a remoção do ultimo elemento!')

            temp = None
            atual = None
            anterior = None

            print('O ultimo elemento foi removido com sucesso!')
        else:
            print('A lista está vazia!')

    # Método para listar os elementos da lista

    def listar(self):

        # Cria-se uma variavel atual, cont e elementos
        atual = self.get_Inicio()
        cont = 0
        elementos = ""

        # Verifica se o elemento atual não é None(Null)
        if atual is not None:

            # Percorre a lista até 'atual' ser None
            while atual is not None:
                # Soma a variavel 'cont'
                cont += 1
                # Variável 'elementos' recebe o conteudo da lista
                elementos += str(cont) + " - " + atual.get_Dado() + "\n"
                # Ao final, a var. 'atual' recebe seu proximo valor
                atual = atual.get_Proximo()

            # Imprime a lista
            print('Lista simplesmente encadeada: \n' + elementos)

        else:
            print('A lista está vazia!')


lista = Lista()
print(lista)
