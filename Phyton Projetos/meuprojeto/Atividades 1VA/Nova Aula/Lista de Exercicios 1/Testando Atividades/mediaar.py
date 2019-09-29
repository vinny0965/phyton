contador=0
y=resto=0
for i in range(4):
    n=int(input("Informe Um numero"))
    if n>0:
       resto=n%2
       if resto==0:
       contador +=1
       y+=n
print("Media",int(y/contador))
