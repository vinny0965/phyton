import bancodeDados
import menu
import util

def iniciar_sistema_boletos():
    while True:
        menu.menu_boleto()
        opcao = input('Digite a Opção:')
        if opcao== '0':
            print('Saindo do Sistema')
            break

        elif opcao == '1':
            util.imprimir_contratos()
            cod_contrato= input('Digite o Codigo do Contrato:')
            contrato= bancodeDados.buscar_contrato_por_codigo(cod_contrato)
            if contrato is not None:
                cod = input('Digite o Cógigo do Boleto:')
                boleto= bancodeDados.buscar_boleto_por_codigo(cod)
                if boleto == None:
                    valor_parcela=input('Digite o valor das Parcelas:')
                    situação = 'Aberta'
                    vencimento= input('Digite a data de vencimento:')

                    bancodeDados.adicionar_boleto(boleto)
                    print('Boleto Cadrastrado Com Sucesso!!')

                else:
                    print('Boleto já existente')
            else:
                print('opção inválida')
        if opcao == '3':
            util.imprimir_boletos()

        if opcao == '2':
            print('Buscar Por codigo')
            cod_boleto= input('Digite o codigo do boleto')
            boleto= bancodeDados.buscar_boleto_por_codigo(cod_boleto)
            if boleto != None:
                print(boleto)
            else:
                print('Boleto nao encontrado')



