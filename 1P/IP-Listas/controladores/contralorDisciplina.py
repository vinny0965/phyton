import BD
import menu
import util


def iniciar_sistema_disciplina():
    while True:
        menu.disciplina()
        op = input('DIGITE A OPÇÃO: ')

        if op == '0':
            print('SAINDO DO MENU DISCIPLINA')
            break

        if op == '1':
            util.imprimir_cursos()
            cod_curso = input('DIGITE O COD DO CURSO: ')
            curso = BD.buscar_curso_por_codigo(cod_curso)
            if curso is not None:
                cod = input('Digite o código da disciplina: ')
                disciplina = BD.buscar_disciplina_por_codigo(cod)
                if disciplina == None:
                    nome = input('Digite o nome da Disciplina: ')
                    periodo = input('Digite o período da Disciplina: ')
                    disciplina = [cod, nome, periodo, cod_curso]

                    BD.adicionar_disciplina(disciplina)
                    print('DISCIPLINA ADICIONADA COM SUCESSO')

                else:
                    print('Disciplina já existente')
            else:
                print('CURSO INVÁLIDO')
        if op == '2':
            util.imprimir_disciplinas()

        if op == '3':
            print('Buscar por Código>>>')
            cod = input('DIGITE O CÓDIGO: ')
            disciplina = BD.buscar_disciplina_por_codigo(cod)
            if disciplina != None:
                print(disciplina)
            else:
                print('Disciplina não encontrada')
