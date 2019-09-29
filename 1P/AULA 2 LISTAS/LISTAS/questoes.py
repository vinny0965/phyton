
#Adicione n elementos na lista

def questao1():
    lista=[]
    n=int(input('quantos numeros'))
    for i in range(n):
        n1=int(input('insira os numeros'))
        lista.append(n1)
    print(lista)

questao1()

def questao2():
    lista=[]
    while True:
        n=int(input('Insira os numeros'))
        lista.append(n)
        if n==0:
            break
    print(lista)
questao2()

def questao3():
    lista=[]
    while True:
        n=int(input('Insira os numeros'))
        if n==0:
            break
        if n %2==0:
            lista.append(n)
    print('numeros pares',lista)
questao3()

def questao4():
    lista=[]
    while True:
        n=int(input('insira os numeros'))
        if n==0:
            break
        if n %2==0:
            lista.append(n)
    print('A soma dos números pares{}'.format(lista),'é = {}'.format(sum(lista)))
questao4()

def questao5():
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
    print('Numeros Pares',listaPar,'soma dos Numeros = ',sum(listaPar))
    print('numeros Impares',listaImpar,'soma dos Numeros = ',sum(listaImpar))
questao5()