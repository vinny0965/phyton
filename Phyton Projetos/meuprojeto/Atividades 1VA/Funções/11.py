def hora(h, m):
    b = h / 12
    if b <= 1:
        hh = str(h)
        print('Sua hora: '+ hh + ':', end='')
    elif b > 1 and b < 2:
        hhh = str(h - 12)
        print('Sua hora: '+ hhh + ':', end='')
    else:
        print('Formato de hora invalido')
    if b <= 1 and m <= 60:
        print(m, 'a.m')
    elif b > 1 and m <= 60:
        print(m, 'p.m')
    else:
        print('Formato de minutos invalidos')

while True:
    print('digite 666 para sair')
    h = int(input('Informe a hora:'))
    if h == 666:
        break
    m = int(input('Informe os minutos: '))
    hora(h, m)