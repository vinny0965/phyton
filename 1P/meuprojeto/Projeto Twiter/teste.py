from datetime import datetime
now = datetime.now()
x = str(now.day)+ ' '+str(now.month)+ ' '+str(now.year)


def cadastro(data):
    dicio = dict()
    for i in data.readlines():
        nome, apelido, idade = i.split(' ')
        dicio[nome] = apelido, idade
    return dicio

def readstart(usuario, filename):
    postagens = list()
    userpost = dict()
    with open('{}.txt'.format(filename),'r') as arquivo:
        for i in arquivo.readlines():
            postagens.append(i)
    arquivo.close()
    userpost[usuario] = postagens
    return userpost

def exibedados(nome, starts):
    if nome in starts:
        return starts[nome]
    else:
        return "Usuario não registrado"
        
def writepost(nome, postagem):
   
    with open('{}.txt'.format(nome),'a') as postuser:
        for post in postagem:
            now = datetime.now()
            x = str(now.day)+ ' '+str(now.month)+ ' '+str(now.year)+ ' '+nome+ ' '+post+'\n'
            postuser.write(x)            
    postuser.close()
    return "Sucesso "
        

def main():
    tudo = list()
    contador = 0
    with open('usuario.txt','r') as inicio:
        starts = cadastro(inicio)
        print("Cadastro realizado.")
        print('\n')
        while True:
            print("1 -> postagem de usuario")
            print("2 -> dado de usuario")
            print("3 -> mostrar postagem de usuario")
            print("4 -> criar um novo post")
            print("5 -> finalizar e sair")
            action = input(">>>> ")
            while action not in "12345":
                print("Erro, digite novamente")
                action = input(">>>> ")
            if action == '2':
                quantpost = int(input("Quantos usuarios à ler a postagem? "))
                fin = list()
                for i in range(1,quantpost+1):    
                    whatsuser = input("Digite o nome do %d usuario: " %i)
                    filename = input("Digite o nome do arquivo a ser lido: ")
                    resultado = readstart(whatsuser,filename)
                    fin.append(resultado)
                print(fin)                

            elif action == '3':
                nome = input("digite seunome: ")
                dadosexibe = exibedados(nome,starts)
                print(dadosexibe)

            elif action == '4':
                thepostst = list()
                nomeusuario = input("digite o nome do usuario: ")
                quantidadepost = int(input("quantas postagem deseja realizar? "))
                for i in range(quantidadepost):
                    postagematual = [input("Digite sua postagem: ")]
                    thepostst.append(postagematual)
                    contador +=1
                    tudo.append([x, postagematual])
                for x in thepostst:
                    resultpost = writepost(nomeusuario,x)
                    print(resultpost)
                            









main()
