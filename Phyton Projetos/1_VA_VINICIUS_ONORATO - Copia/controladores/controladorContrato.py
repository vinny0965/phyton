import bancodeDados
import menu
import util

def iniciar_sistema_contrato():
    while True:
        menu.menu_contrato()
        opcao = input('Digite a Opcao:')

        if opcao == '0':
            print('Saindo do Sistema')
            break

        if opcao == '1':
            util.imprimir_clientes()
            cpf_cliente = input('Digite o Cpf do Cliente:')
            cliente= bancodeDados.buscar_por_cpf(cpf_cliente)
            if cliente is not None:
                cod = input('Digite o Código do Contrato:')
                contrato = bancodeDados.buscar_contrato_por_codigo(cod)
                if contrato == None:
                    valor_total=input('Digite o Valor Total do Contrato')
                    parcelas= input('Digite a quantidade de Parcelas')
                    contrato = [cod, valor_total, parcelas]

                    bancodeDados.adicionar_contrato(contrato)
                    print('Contrato Registrado Com Sucesso!!')

                else:
                    print('Contrato Já Existente!')
            else:
                print('contrato inválido')
        if opcao == '3':
            util.imprimir_contratos()

        if opcao== '2':
            print('Buscar Por Código>>>')
            cod = input('Digite o Código:')
            contrato = bancodeDados.buscar_contrato_por_codigo(cod)
            if contrato !=None:
                print(contrato)
            else:
                print('Contrato Não Encontrado')






