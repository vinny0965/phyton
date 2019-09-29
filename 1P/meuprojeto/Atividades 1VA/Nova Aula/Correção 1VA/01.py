"""lista=[]
for i in range (10):
    x=int(input("insira um numero"))
    lista.append(x)
print(lista)
print("O maior elemento da lista é {}".format(max(lista)))
print("A soma dos elementos é {}".format(sum(lista)))
"""

"""lista=[1,2,4,3,2,1,23,3]
count=0
media=sum(lista)/8
print("a soma dos elementos é {}".format(sum(lista)))
print("O maior elemento é {}".format(max(lista)))
print("repetição do primeiro elemento é de {}".format(lista.count(lista[0])),"Vezes")
print("a meida é {}".format(media))
"""
usuario=int(input("Insira a Quantidade de Usuários"))
dicionario= {}
usuarioMaisvelho=0
maiorIdade= -1

for i in range(usuario):
    print(f"Informações do usuário #")
    nome=str(input("Insira Seu Nome"))
    idade=int(input("Insira sua idade"))
    cpf=int(input("Insira seu cpf"))
    tel=int(input("Insira seu telefone"))
    dicionario[cpf]=(nome,idade,cpf,tel)

    if idade > maiorIdade:
        maiorIdade=idade
        usuarioMaisvelho=cpf

lista=dicionario[usuarioMaisvelho]
