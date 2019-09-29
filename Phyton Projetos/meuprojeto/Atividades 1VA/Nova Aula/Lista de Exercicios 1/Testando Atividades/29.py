velocidade=float(input("Informe a Velocidade do Carro:"))
multa=7
if velocidade >80:
    print("Você foi multado danado", "Sua Multa é R${:.2f}:".format((velocidade-80)*multa))
else:
    print("Pode ir Safadão")