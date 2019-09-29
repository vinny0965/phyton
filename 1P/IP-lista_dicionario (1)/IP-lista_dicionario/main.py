from datetime import datetime

import menu
from controladores import controladorCurso, contralorDisciplina


def iniciar_sistema():
    while True:
        menu.principal()
        op = input('DIGITE A OPÇÃO: ')
        if op == '0':
            print('SAINDO DO SISTEMA')
            break
        elif op == '1':
            controladorCurso.iniciar_sistema_curso()
        elif op == '2':
            print('2222')
            contralorDisciplina.iniciar_sistema_disciplina()
        elif op == '3':
            print('333')
            # controladorCurso.iniciar_sistema_curso()
        elif op == '4':
            print('4444')
            # controladorCurso.iniciar_sistema_curso()

        else:
            print('OPÇÃO INVÁLIDA - TENTE NOVAMENTE')


iniciar_sistema()


