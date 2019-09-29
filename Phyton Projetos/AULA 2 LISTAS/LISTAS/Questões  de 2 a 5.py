
#Adicione n elementos na lista

def q1():
    lista=[]
    n=int(input('insira a quantidade de Elementos:'))
    for i in range(n):
        n1=int(input('Insira os Elementos:'))
        lista.append(n1)
    print(lista)

q1()
# 2 questão - Adicionar na lista elementos, parar quando for digitado o numero ZERO
def q2():
    lista=[]
    while True:
        n=int(input('Insira os elementos:'))
        lista.append(n)
        if n==0:
            break
    print(lista)
q2()
#3 questão - Adicionar Somente numeros pares, quando digitar o ZERO, aí o programa imprime a lista.
def q3():
    lista=[]
    while True:
        n=int(input('Insira os Elementos:'))
        if n==0:
            break
        if n %2==0:
            lista.append(n)
    print('numeros pares',lista)
q3()
#4 questão - Adicionar Somente numeros pares, quando digitar o ZERO, aí o programa imprime a lista, no final imprimir o somatorio da lista
def q4():
    lista=[]
    while True:
        n=int(input('insira os elementos:'))
        if n==0:
            break
        if n %2==0:
            lista.append(n)
    print('A soma dos números pares{}'.format(lista),'é {}'.format(sum(lista)))
q4()
# 5 questão - Adicionar numeros a lista, mostrar o somatório dos pares e o somatório dos impares.
def q5():
    listaPar=[]
    listaImpar=[]
    while True:
        n=int(input('insira elementos'))
        if n==0:
            break
        if n %2==0:
            listaPar.append(n)
        if n %2 ==1:
            listaImpar.append(n)
    print('Lista de Números Pares',listaPar,'soma = ',sum(listaPar))
    print('lista de Numeros Impares',listaImpar,'soma = ',sum(listaImpar))
q5()