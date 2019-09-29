"""Faça um programa para imprimir:
 1
 2 2
 3 3 3
 .....
 n n n n n n ... n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro e
imprima até a n-ésima linha
."""
def degraus(n):
    cont=0
    for c in range(n):
        cont+=1
        txt=str(cont)
        print(f'{txt * cont}')

degraus(9)