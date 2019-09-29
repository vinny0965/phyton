viagem=float(input("Insira uma distância:"))
if viagem <=200:
    print("O Valor da Sua viagem foi R$ {}".format(viagem*0.50))
else:
    print("O Valor da Sua Viagem foi R$ {}".format(viagem*0.45))