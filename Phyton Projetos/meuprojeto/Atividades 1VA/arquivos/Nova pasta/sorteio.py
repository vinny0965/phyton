import random
arq=open("arquivo3.txt","r")
novoarquivo=open("arquivonovo.txt","w")

escolhido=arq.read().split()
novoEscolhido=random.choice(escolhido)
novoarquivo.write(novoEscolhido)
arq.close()
novoarquivo.close()