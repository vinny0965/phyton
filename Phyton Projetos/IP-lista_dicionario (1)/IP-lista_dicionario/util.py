from datetime import datetime

import BD


def imprimir_cursos():
    print('CURSOS')
    count = 1
    cursos = BD.get_cursos()
    for c in cursos:
        print('CURSO: ', count)
        print('Código: ', c.get('cod'))
        print('Nome: ', c.get('nome'))
        print('SIGLA: ', c.get('sigla'))
        print('STATUS: ', c.get('status'))
        print('-----------')
        count += 1


def imprimir_disciplinas():
    print('DISCIPLINAS>>>')
    count = 1
    disciplinas = BD.get_disciplinas()
    for c in disciplinas:
        print('Disciplina: ', count)
        print('Código: ', c.get('cod'))
        print('Nome: ', c.get('nome'))
        print('Período: ', c.get('periodo'))
        curso = BD.buscar_curso_por_codigo('cod')
        print('CURSO: ', c.get('curso'))
        print('-----------')
        count += 1


def get_semestre_atual():
    data = datetime.now()
    if data.month < 6:
        mes = 1
    else:
        mes = 2
    semestre_atual = str(data.year) + '.' + str(mes)
    return semestre_atual
