from Arvore import Arvore

arvore = Arvore()
print('\033[33m' + '\tArvore Binaria' + '\033[0;0m')

raiz = None

while True:
    arvore.imprimeMenu()
    select = int(input('\033[31m' + 'Opcao: ' + '\033[0;0m' ))

    if select == 1: # Add elemento
        print('\n Insira elemento na arvore!')
        raiz = arvore.add(arvore(input('Elemento: ')))

    elif select == 2: #Buscar elemento
        print('\nBuscar elemento!')
        elemento = input('\033[33m' + 'Digite elemento: ' + '\033[0;0m')
        print('-' * 30)
        print('\n {}\n'. format(arvore.busca(raiz, elemento)))
        print('-' * 30)

    elif select == 3: #Remover elemento
      print('\nRemover elemento: ')
      elemento = input()
      arvore.remover(raiz, elemento)

    elif select == 4: # Listar nos
        pass

    elif select == 5: # Altura da arvore
        print('\nAltura da arvore: {}'.format(arvore.altura(raiz)))

    elif select == 6: # Niveis da arvore
        print('\nNivel da arvore: {}'.format(arvore.nivel(raiz)))

    elif select == 7: # Soma de todos os nos
        pass

    elif select == 8: # Elemento de cada nível
        pass

    elif select == 9: # Elemento maximo
        print('\nElemento maximo: {}'.format(arvore.maximo()))

    elif select == 10: # Elemento minimo
        print('\nElemento minimo: {}'.format(arvore.minimo()))

    elif select == 11: # Elemento predecessor
        print('\nElemento predecessor: {}'.format(arvore.predecessor()))

    elif select == 12: # Elemento sucessor
        print('\nElemento sucessor: {}'.format(arvore.sucessor()))

    elif select == 13: # Total de elementos de um no
        pass

    elif select == 14: # Balanceamento
        print('\nBalanceamento: {}'.format(arvore.executaBalanco()))

    elif select == 15: # Retornar nivel do elemento
      pass

    elif select == 16: #Profundidade
        print('\nProfundidade: {}'.format(arvore.profundidade()))

    elif select == 17:
        print('\n\033[33m' + '\tPrograma Finalizado!' + '\033[0;0m\n')




