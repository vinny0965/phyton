def valorPagamento(vp, da):
    if da < 1:
        valor = vp
        print(valor)
        return valor
    else:
        valor = (vp + vp * 0.03 + 0.01 * da)
        print(valor)
        return valor


valor = []
vp = 0
da = 0
qp = 0
valortotal = 0

while True:
    qp += 1
    vp = float(input('Qual o valor da prestacao? '))
    da = int(input('Quantos dias esta em atraso? '))
    if vp == 0:
        break
    valor.append(valorPagamento(vp, da))

qp -= 1
for i in range(qp):
    valortotal += valor[i]

print('Relatorio do dia, foram pagas %d prestacoes no valor: ' % qp, valor)
print('Valor total de prestacoes pagas: ', valortotal)