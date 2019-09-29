"""Crie um programa que leia um arquivo no seguinte formato
Nome1 idade1 curso1
Nome2 idade2 curso2
Nome3 idade3 curso3
Armazene os dados lidos em um dicionário e imprima
"""
dicionario={}
arq=open('nomer.txt','r')
for dicionario in arq:
    print(dicionario)