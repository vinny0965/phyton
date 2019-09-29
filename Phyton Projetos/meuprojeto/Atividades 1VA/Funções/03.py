"""lista=[]
for i in range(3):
    x=int(input('digite um numero'))
    lista.append(x)
print("a soma dos elementos é {}".format(sum(lista)))
"""
def soma3(n1,n2,n3):
    numero=n1+n2+n3
    return numero
numero1 = str(input("Informe um argumento"))
numero2 = str(input("Informe outro argumento"))
terceiro = str(input("Informe o terceiro argumento"))
print("a soma dos três argumentos é",soma3(numero1,numero2,terceiro))