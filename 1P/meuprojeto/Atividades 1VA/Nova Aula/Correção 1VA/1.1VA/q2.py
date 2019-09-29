
saldoConta=500.00
quantidadeMeses=int(input("Digite a quantidade de meses"))

for i in range(quantidadeMeses):
    rendiemento=saldoConta * 0.012
    saldoConta+=rendiemento

print("saldo Conta", saldoConta)