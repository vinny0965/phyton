valor_casa=float(input("Qual o Valor da casa?"))
salario=float(input("Qual seu salário?"))
prestacao=float(input("Em quantos anos quer pagar?"))
emprestimo=valor_casa*0.30
condicao=valor_casa+emprestimo
if condicao>salario:
    print("Empréstimo Negado")
else:
    print("Sucesso!")