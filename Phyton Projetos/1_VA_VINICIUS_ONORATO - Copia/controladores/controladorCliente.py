import menu
import bancodeDados
import util

def iniciar_sistema_cliente():
    while True:
        menu.menu_paciente()
        opcao = input('Digite a Opção:')
        if opcao == '0':
            print('Saindo do Sistema')
            break
        elif opcao == '1':
            print('Cadrastrar Cliente>>>')
            cod = input(' Digite o CPF do Cliente')
            cliente = bancodeDados.buscar_por_cpf(cod)
            if cliente ==None:
                nome = input('Digite o Nome do Cliente:')
                sexo = input('Digite o Sexo do Cliente:')
                telefone = input('Digite o Telefone do Cliente:')
                status= True
                clientee= [cod , nome , sexo , telefone]
                bancodeDados.adicionar_cliente(clientee)
                print(' Cliente Cadrastrado Com Sucesso!!!')
            else:
                print('CPF já Cadastrado!!!')

        elif opcao == '3':
            util.imprimir_clientes()
        elif opcao == '2':
            print('Buscar Por CPF>>>')
            cod = input("Digite o CPF:")
            cliente = bancodeDados.buscar_por_cpf(cod)
            if cliente!=None:
                print(cliente)
            else:
                print('Curso Não Encontrado')

        else:
            print('Opção Invalida - Tente Outra Vez!')