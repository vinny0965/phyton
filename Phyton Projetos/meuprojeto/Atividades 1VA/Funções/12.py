from random import randint
k = 0

def craps():
    k = randint(2,13)
    if k == 7 or k == 11:
        print('Você é o mestre!! Ganhou!!', k)
    elif k == 2 or k == 3 or k == 12:
        print('Craps!!! Você perdeu!', k)
    elif k in range(4,6) or k in range(8,10):
        print('Esse é o seu numero vamos jogar!! Numero:', k)
        print('Digite D para jogar o dado: ')
        z = 0
        while k != z:
            print('Digite D para jogar o dado:')
            s = input()
            if s == 'D':
                z = randint(2,13)
                print('Seu numero foi: ', z)
                if z == 7:
                    print('Voce Perdeu!!!')
                    break
        if  z != 7:
            print('Voce Ganhou!!!')
craps()