from Lista import Lista

# Método para criar um menu no console
def menu():
    print('''
    [1] - Inserir Inicio
    [2] - Inserir Fim
    [3] - Remover Inicio
    [4] - Remover Fim
    [5] - Listar
    [0] - Sair
    ''')

# Instancio a lista
lista = Lista()
dado = 0
opcao = -1

while opcao is not 0:

    # Chamada no menu
    menu()
    dado = int(input('Digite uma opção: '))

    # Verifica a opção desejada
    if dado is 1:
        dado = input('Digite um dado: ')
        lista.inserir_Inicio(dado)
    elif dado is 2:
        dado = input('Digite um dado: ')
        lista.inserir_Fim(dado)
    elif dado is 3:
        lista.remover_Primeiro()
    elif dado is 4:
        lista.remover_Ultimo()
    elif dado is 5:
        lista.listar()
    elif dado is 0:
        break
    else:
        print('Digite uma opção do menu!')
