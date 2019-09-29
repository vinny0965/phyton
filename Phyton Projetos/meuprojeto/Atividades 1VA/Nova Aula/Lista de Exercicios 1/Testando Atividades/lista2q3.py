n1=float(input("Insira uma nota"))
n2=float(input("Insira outra nota"))
n3=float(input("Insira outra nota"))
n4=float(input("Insira outra nota"))
s=(n1+n2+n3+n4)/4
if s<5.0:
    print("Reprovado")
elif s>=5.0 and s<7.0:
    print("Recuperacao")
else:
    print("aprovado")
