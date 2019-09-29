"""Crie um programa que leia uma matriz 3x3 do usuário e guarde os valores em uma
arquivo, na forma de matriz:
"""
arq=open("matriz.txt","w")
matriz=[]
matriz.append([[1,2,3],[2,3,4],[3,4,5]])
arq.writelines(matriz)
arq.close