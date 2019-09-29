x = input("Digite alguma coisa:")

contador=0

for i in x:
    if i.islower():
        contador+=1
print(contador)