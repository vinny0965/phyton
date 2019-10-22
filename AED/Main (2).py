from AED import dupla_encad
# Método para criar um menu no console
def menu():
    print('''
    [1] - Inserir Algum dado
    [2] - Inserir Posição Específica
    [3] - Remover dado
    [4] - Buscar dado
    [5] - Imprimir lista
    [6] - Imprimir tamanho da lista
    [0] - Sair
    ''')

# Instancio a lista
lista = lista()
dado = 0
opcao = -1

while opcao is not 0:

    # Chamada no menu
    menu()
    dado = int(input('Digite uma opção: '))

    # Verifica a opção desejada
    if dado is 1:
        dado = input('Digite um dado: ')
        lista.inserir(dado)

    elif dado is 0:
        break
    else:
        print('Digite uma opção do menu!')
