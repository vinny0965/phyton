import random
n1=str(input("Digite um Nome"))
n2=str(input("Digite Mais um"))
n3=str(input("Digite mais um"))
n4=str(input("Digite o ultimo"))
lista=[n1,n2,n3,n4]
sorteio=random.choice(lista)
print(sorteio)
