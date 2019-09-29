from datetime import datetime

import menu
from controladores import controladorBoletos , controladorCliente , controladorContrato

def iniciar_sistema():
    while True:
        menu.menu_principal()
        opcao=input('Digite a Opcao:')
        if opcao== '0':
            print('Saindo do Sistema')
            break
        elif opcao=='1':
            controladorCliente.iniciar_sistema_cliente()
        elif opcao=='2':
            print('222')
            controladorContrato.iniciar_sistema_contrato()
        elif opcao=='3':
            print('333')
            controladorBoletos.iniciar_sistema_boletos()
        else:
            print('OPCAO INVALIDA - TENTE NOVAMENTE')



iniciar_sistema()