""""". Crie um programa que leia um arquivo com uma lista de nomes de um arquivo e só
deixe os nomes que iniciam com vogal no mesmo arquivo.
Nome1
Nome2
Nome3 etc
"""
dados=[]
arq=[]
dados=open('nomes4.txt','r')
arq=open('nomes4.txt','W')
for nome in dados:
    if nome[0] in 'aeiouAEIOU':
        arq.write(nome+'\n')

dados.close()
arq.close()