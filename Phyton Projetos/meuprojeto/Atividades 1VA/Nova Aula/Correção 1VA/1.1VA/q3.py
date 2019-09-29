quantidadeNumero=10
listaNumeros= []

for i in range(quantidadeNumero):
    numero=int(input("Insira um Numero"))
    listaNumeros.append(numero)

qdadePositivo = 0
qdadeItemC = 0
qdadeItemd = 0

for numero in listaNumeros:
    #item a e item b
    if numero > 0:
        qdadePositivo += 1
        somaPositivo += numero

    if numero > 50 and numero < 100:
        qdadeItemC +=1

    if numero < 50:
        qdadeItemD +=1
        if numero > 