"""Crie um algoritmo que lê um conjunto de nomes de um arquivo ‘nomes.txt’. Esse
algoritmo deverá separar os nomes que iniciam com vogal e escrever em um novo
arquivo ‘vogal.txt’, enquanto que os nomes que iniciam com consoante devem ser
escritos no arquivo ‘consoante.txt
"""
listaVogais=[]
listaConsoantes=[]
arq=open('nomes.txt','r')
arqVogais=open("listaVogais.txt","w")
arqConsoante=open("listaConsoantes.txt","w")

texto = arq.read().split()

for nome in texto:
    if nome[0] in "aeiouAEIOU":
        arqVogais.write(nome+'\n')
    else:
        arqConsoante.write(nome+'\n')
arq.close()
arqVogais.close()
arqConsoante.close()

