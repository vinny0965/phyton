#==================================================
#        Lista Encadeada: Intensivo Python
#==================================================
# Objetos necessários
#    * No
#    * Lista_Encadeada


# Estrutura do Nó
class No(object):
    
    # No:
    #   ANTERIOR | VALOR |  PROXIMO
    #
    
    def __init__(self, valor):
        self.valor = valor     # Item no (nó)
        self.anterior = None   # Ponteiro pro no anterior
        self.proximo = None    # Ponteiro pro no posterior

# Estrutura da lista;
class Lista_Encadeada(object):
    
    def __init__(self, *args):
        self.cabeca = None
        self.rabo = None
        self.tamanho = 0
        for item in args:
            self.adicionar(item)
        
        
#Função para adicionar itens;        
    def adicionar(self, valor):
        
        novo_item = No(valor)
       
        # Se não houver item na cabeca, o primeiro será adicionado;
        
        if not self.cabeca:
            """
            c/r -> a.V.p
        
            """
            self.cabeca = novo_item
            self.rabo = self.cabeca
        
        # Já há um ou mais itens na lista;
       
        else:
            self.rabo.proximo = novo_item
            novo_item.anterior = self.rabo
            self.rabo = novo_item
        self.tamanho += 1


# Função para percorrer a lista e retornar o Nó desejado; 
    def percorrer_indice(self, indice):
        centro = self.tamanho // 2
        maximo = self.tamanho - 1
        if self.cabeca and indice >= 0 and indice <= maximo:
            if indice >= centro:
                ponteiro = self.rabo
                for item in range(maximo,indice,-1):
                    ponteiro = ponteiro.anterior
            else:
                ponteiro = self.cabeca
                for item in range(indice):
                    ponteiro = ponteiro.proximo
            
            return ponteiro
        raise IndexError("Índice fora de alcance")
          
    
    def inserir(self, indice, valor):
        novo_valor = No(valor)
        if indice >= self.tamanho and indice >= 0:
            self.adicionar(valor)
        else:
            if indice == 0:
                novo_valor.proximo = self.cabeca
                self.cabeca.anterior = novo_valor
                self.cabeca = novo_valor
            else: 
                ponteiro = self.percorrer_indice(indice)          
                novo_valor.proximo = ponteiro
                novo_valor.anterior = ponteiro.anterior
                ponteiro.anterior.proximo = novo_valor
                ponteiro.anterior = novo_valor
            self.tamanho += 1

    def remover(self, indice):
        if indice == 0:
            self.cabeca = self.cabeca.proximo
            self.cabeca.anterior = None
            
        elif indice == self.tamanho -1:
            self.rabo = self.rabo.anterior
            self.rabo.proximo = None
        else:
            ponteiro = self.percorrer_indice(indice)
            ponteiro.anterior.proximo = ponteiro.proximo 
            ponteiro.proximo.anterior = ponteiro.anterior            
        self.tamanho -= 1       
       
 # Função para retornar a imagem da lista com o comando 'print';          
   
    def __str__(self):
    
        ponteiro = self.cabeca
        primeiro = False
        
        imagem = "["
        
        while ponteiro:
            
            if type(ponteiro.valor) == str:
                temp = f"'{ponteiro.valor}'"    
            
            else:
                temp = str(ponteiro.valor)
            
            if primeiro == False:    
                imagem += temp
                primeiro = True
            
            else:
                imagem += "," + temp
            ponteiro = ponteiro.proximo
        return imagem + "]"

# Função para retornar o tamanho da lista com o comando 'len';   
    def __len__(self):
        return self.tamanho

     
# Função para informar o valor do item de acordo com o indice desajado com o comando (lista[0] - retorna valor na posição 0);  
    def __getitem__(self, indice):
        ponteiro = self.percorrer_indice(indice)
        return ponteiro.valor

# Função para modificar item da lista de acordo com o indice, exemplo: lista[0] = 'hello world';          
    def __setitem__(self, indice, valor):
        ponteiro = self.percorrer_indice(indice)
        ponteiro.valor = valor
        

#==============================================================================================================================
#======================================================== seção de testes =====================================================

lista = Lista_Encadeada(1,2,3,4)
lista.remover(2)
print(lista)
print(len(lista))

'''

def __len__(self):
        return self.tamanho
    def add(self, valor):          feito
    
    def __str__:                   feito
    
    def __getitem__:               feito

    def inserir(self, pos, valor): feito
 
    def buscarIndex(self, index):  feito
       
    def buscarValor(self, valor):  
     
    def countPorValor(self, valor):
       
    def deletarIndex(self, index): feito
       
    def deletarValor(self, valor):
       
    ( __setitem__) def editarIndex(self, index):  feito
       
    def editarValor(self, valor):
     
'''
