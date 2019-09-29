#Q8

#23
lista = [1,2,3,55,66,77,88,-1,-2,-3]
#lista = [-1, -2, -3, -4, -5]

"""
#Retornar o maior elemento
maior = lista[0]
for numero in lista :
    if (numero > maior) :
        maior = numero
print (f"Maior número:{maior}")

#Forma alternativa de resolução
#print (max(lista))



#Retornar a soma
soma = 0
for numero in lista :
    soma += numero
print (f"Soma:{soma}")

#Forma alternativa de resolução
#print (sum(lista))

"""
"""
#Número de ocorrências do primeiro elemento da lista

count = 0
for numero in lista :
    if (lista[0] == numero):
        count += 1
print (f"Quantidade de ocorrências do primeiro elemento:{count}")
#Forma alternativa de resolução
#print(lista.count(lista[0]))



#Média dos elementos

media = 0
for numero in lista:
    media += numero
media = media/len(lista)
print (f"Média dos números:{media}")

#Soma dos elementos negativos

somaNegativos = 0
for numero in lista:
    if (numero < 0) :
        somaNegativos += numero
print (f"Soma elementos negativos:{somaNegativos}")

#Qual o valor mais próximo da média
proximo = lista[0]
diferenca = media
for numero in lista:
    subtracao = media - numero
    if (subtracao < 0):
        subtracao = subtracao * -1
    print (media, numero, subtracao, diferenca)
    
    if (subtracao < diferenca):
        diferenca = subtracao
        proximo = numero
print (f"Valor mais próximo:{proximo}")

"""

#Q9

quantidade = int(input("Digite a quantidade de usuários"))
dicionario = {}
usuarioMaisVelho = 0
maiorIdade = -1

for i in range(quantidade):
    print (f"Informações usuário #{i}")
    nome = input("Digite o nome:")
    idade = int(input("Digite o idade:"))
    cpf = int(input("Digite o cpf (apenas os números):"))
    telefone = input("Digite o número de telefone:")
    dicionario[cpf] = [nome, idade, cpf, telefone]

    if idade > maiorIdade :
        maiorIdade = idade
        usuarioMaisVelho = cpf

lista = dicionario[usuarioMaisVelho]
print ("Nome do usuário mais velho:" + lista[0])
print ("Idade do usuário mais velho:" + lista[1])
print ("Cpf do usuário mais velho:" + lista[2])
print ("telefone do usuário mais velho:" + lista[3])
















        

















        
    
