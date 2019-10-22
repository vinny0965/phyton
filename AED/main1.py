from AED import dupla_encad

def menu():
    print('''
        [1] - Inserir Inicio
        [2] - Inserir Fim
        [3] - Remover Inicio
        [4] - Remover Fim
        [5] - Listar
        [0] - Sair
        ''')

lista = dupla_encad.ListaEncadeada()
lista = dupla_encad.ListaEncadeada()
dado = 0
opcao = -1

while opcao is not 0:

    # Chamada no menu
    menu()
    dado = int(input('Digite uma opção: '))
    # Verifica a opção desejada
    if dado is 1:
        dado = input('Digite um dado: ')
        lista.adicionar(dado)

    if dado is 2:
        indice = input('Digite a posição que quer adicionar:')
        lista.inserir(indice,valor)
    if dado is 4:
        print(lista)




