nota1=float(input("Insira sua nota:"))
nota2=float(input("Insira sua nota:"))
s=(nota1+nota2)/2
if s<5.0:
    print("Reprovado")
elif s>=5.0 and s<=6.9:
    print("Recuperação")
else:
    print("Aprovado")