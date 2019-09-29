produto=float(input("Qual o valor do produto?"))
print("----Escolha a forma de pagamento------")
print(" A vista no dinheiro",(1))
print("A vista no cartão",(2))
print("A vista parcelar em 2x",(3))
print("A vista parcelar em 3x +",(4))
opcao=int(input(""))
if opcao ==1:
    result=produto-((produto/100)*10)
    print("O valor total é {}".format(result))
elif opcao==2:
    result=produto-((produto/100)*5)
    print("O valor total é {}".format(result))
elif opcao==3:
    result=produto
    print(produto)
elif opcao==4:
    result=produto+((produto/100)*20)
    print("O valor total é {}".format(result))
else:
    print("Opção Inválida")


