from datetime import datetime

import menu

def iniciar_sistema():
    while True:
        menu.menu_principal()
        op = input('Digite a opçã0')
        if op == "0":
            print("Saindo do Sistema")
            break
        elif op == "1":
            print("Acessando todas as Câmeras")
