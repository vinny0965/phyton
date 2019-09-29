from datetime import datetime

import bancodeDados

def imprimir_clientes():
    print('Clientes')
    count = 1
    clientes = bancodeDados.get_clientes()
    for c in clientes:
        print('Cliente:', count)
        print('CPF:', c[0])
        print('Nome:', c[1])
        print('Sexo:', c[2])
        print('Telefone:', c[3])
        print('-------*--------')
        count +=1

def imprimir_contratos():
    print('Contratos>>>')
    count = 1
    contratos = bancodeDados.get_contratos()
    for c in contratos:
        print('Contrato:' , count)
        print('Codigo:', c[0])
        print('Valor total Contrato', c[1])
        print('Quantidade Parcelas', c[2])
        print('---------*----------')
        count +=1

def imprimir_boletos():
    print('Boletos>>>')
    count = 1
    boletos = bancodeDados.get_boletos()
    for c in boletos:
        print('Boleto:' , count)
        print('Codigo:', c[0])
        print('Valor Parcela', c[1])
        print('Situação', c[2])
        print('Vencimento', c[3])
        print('---------*----------')
        count +=1
