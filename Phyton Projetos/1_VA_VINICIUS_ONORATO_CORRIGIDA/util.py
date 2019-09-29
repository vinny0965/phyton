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
        print('Codigo do Contrato:', c[0])
        print('Nome do cliente', c[1][1])
        print('CPF do cliente',c[1][0])
        print('Valor total Contrato', c[2])
        print('Quantidade Parcelas', c[3])
        print('---------*----------')
        count +=1

def imprimir_boletos():
    print('Boletos>>>')
    count = 1
    boletos = bancodeDados.get_boletos()
    for c in boletos:
        print('Boleto:' , count)
        print('Codigo do Boleto:', c[0])
        print('Código do Contrato:', c[1][0])
        print('Valor Parcela:', c[2])
        print('Situação:', c[3])
        print('Vencimento:', c[4])
        print('---------*----------')
        count += 1


def imprimir_contratos_por_cpf():
    for cliente in bancodeDados.__clientes:
        print('CPF: {}'.format(cliente[0]))
        for contrato in bancodeDados.__contratos:
            if cliente[0] == contrato[1][0]:
                print(' Codigo:', contrato[0])
                print(' Valor total Contrato', contrato[2])
                print(' Quantidade Parcelas', contrato[3])
        print()


def imprimir_boletos_por_situacao():
    print('Situação Aberta')
    for boleto in bancodeDados.__boletos:
        if boleto[3] == 'Aberta':
            print(' Codigo do Boleto:', boleto[0])
            print(' Código do Contrato:', boleto[1][0])
            print(' Valor Parcela:', boleto[2])
            print(' Vencimento:', boleto[4])
        print()
    print()
    print('Situação Fechada')
    for boleto in bancodeDados.__boletos:
        if boleto[3] == 'Fechada':
            print(' Codigo do Boleto:', boleto[0])
            print(' Código do Contrato:', boleto[1][0])
            print(' Valor Parcela:', boleto[2])
            print(' Vencimento:', boleto[4])
        print()
    print()


def pagar_boleto():
    print('Situação Aberta')
    for boleto in bancodeDados.__boletos:
        if boleto[3] == 'Aberta':
            print(' Codigo do Boleto:', boleto[0])
            print(' Código do Contrato:', boleto[1][0])
            print(' Valor Parcela:', boleto[2])
            print(' Vencimento:', boleto[4])
        print()
    print()
    cod = str(input('Código do Boleto: '))
    boleto = bancodeDados.buscar_boleto_por_codigo(cod)
    if boleto is not None:
        if boleto[3] == 'Aberta':
            print('Boleto pago com sucesso')
            boleto[3] = 'Fechada'
            print()
        else:
            print('Boleto já foi pago')
            print()
    else:
        print('Código inválido')
        print()
