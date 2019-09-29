"""Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
"""
Notas = [ int(input("Informe a nota "+str(x) ) )
for x in range(4) ]
print("Notas", Notas)
print("média das Notas", sum(Notas)/4)