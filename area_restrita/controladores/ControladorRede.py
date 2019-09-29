import Banco_de_Dados
import menu

def iniciar_sistema_rede():
    while True:
        menu.principal()
        select = input("Digite a opção:")
        if select == '0':
            print("Saindo do Sistema com Segurança")


