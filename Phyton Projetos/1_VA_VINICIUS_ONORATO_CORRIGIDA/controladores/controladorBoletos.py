import bancodeDados
import menu
import util


def iniciar_sistema_boletos():
    while True:
        menu.menu_boleto()
        opcao = input('Digite a Opção:')
        if opcao == '0':
            print('Saindo do Sistema')
            break

        elif opcao == '1':
            util.imprimir_contratos()
            cod_contrato= input('Digite o Codigo do Contrato:')
            contrato= bancodeDados.buscar_contrato_por_codigo(cod_contrato)
            if contrato is not None:
                cod = input('Digite o Cógigo do Boleto:')
                boleto= bancodeDados.buscar_boleto_por_codigo(cod)
                if boleto is None:
                    valor_parcela=input('Digite o valor das Parcelas:')
                    print('Menu Situação')
                    print('1.Aberta')
                    print('2.Fechada')
                    situacao = str(input('Digite a opção: ').strip())
                    while True:
                        if situacao == '1':
                            situacao = 'Aberta'
                            break
                        if situacao == '2':
                            situacao = 'Fechada'
                            break
                        situacao = str(input('Digite a opção: ').strip())


                    vencimento= input('Digite a data de vencimento:')
                    boleto = [cod, contrato, valor_parcela, situacao, vencimento]
                    bancodeDados.adicionar_boleto(boleto)
                    print('Boleto Cadrastrado Com Sucesso!!')

                else:
                    print('Boleto já existente')
            else:
                print('opção inválida')

        if opcao == '2':
            print('Buscar Por codigo')
            cod= input('Digite o codigo do boleto')
            boleto= bancodeDados.buscar_boleto_por_codigo(cod)
            if boleto != None:
                print(boleto)
            else:
                print('Boleto nao encontrado')

        if opcao == '3':
            util.imprimir_boletos()

        if opcao == '4':
            print('Listar Boletos por situacão')
            util.imprimir_boletos_por_situacao()

        if opcao == '5':
            print('Pagar Boleto')
            util.pagar_boleto()
            print()

