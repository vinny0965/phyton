import menu
import BD
import util

def iniciar_sistema_curso():
    while True:
        menu.curso()
        op = input('DIGITE A OPÇÃO: ')
        if op == '0':
            print('SAINDO DO CURSO')
            break
        elif op=='1':
            print('CADASTRAR CURSO>>>')
            cod = input('Digite o código do Curso: ')
            curso = BD.buscar_curso_por_codigo(cod)
            if curso == None:
                nome = input('Digite o nome do Curso: ')
                sigla= input('Digite a sigla do Curso: ')
                status = True
                cursoo =[cod, nome, sigla, status]
                BD.adicionar_curso(cursoo)
                print('CURSO ADICIONADO COM SUCESSO!!!')
            else:
                print('Código já utilizado')

        elif op =='2':
            util.imprimir_cursos()
        elif op=='3':
            print('Buscar por Código>>>')
            cod = input('DIGITE O CÓDIGO: ')
            curso = BD.buscar_curso_por_codigo(cod)
            if curso!=None:
                print(curso)
            else:
                print('CURSO NÃO ENCONTRADO')

        else:
            print('OPÇÃO INVÁLIDA - TENTE NOVAMENTE')




