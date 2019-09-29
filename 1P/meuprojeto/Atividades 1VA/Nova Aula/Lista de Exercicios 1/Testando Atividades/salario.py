salario=float(input("Informe seu salário"))
salario1=salario*0.10
salario2=salario*0.15
if salario>1.250:
    print("Obteve um aumento de 10% {}".format(salario+salario1))
else:
    print("Obteve um aumento de 15% {}".format(salario+salario2))