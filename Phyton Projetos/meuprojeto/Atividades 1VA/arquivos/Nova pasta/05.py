"""Crie um programa que leia dois arquivos e crie um terceiro com um merge do
conteúdo dos dois.
"""
arquivo1=[]
arquivo2=[]
arq1=open("arquivo1.txt","r")
arq2=open("arquivo2.txt","r")
arq3=open("arquivo3.txt","w")

texto=arq1.read().split()

for nome in texto:
    arq3.write(nome+'\n')
texto1=arq2.read().split()

for nome in texto1:
    arq3.write(nome+'\n')
arq3.close()
arq1.close()
arq2.close()