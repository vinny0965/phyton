#==================================================================
#       Bibliotecas Importadas
#==================================================================
import time, os, loading_scene, random
from datetime import datetime
#-----------------------------------------------------------------#

loading_scene.loading()

#==================================================================
# Configurações
#==================================================================
SEPARADOR = ";"
SAVING = "%s%s%s%s%s%s%s\n"
USER_ARCHIVE = "usuario.txt"
MAIN_MENU = """
==================================================================
        Menu Principal
==================================================================

████████╗██╗    ██╗███████╗███████╗████████╗██╗███╗   ██╗ ██████╗ 
╚══██╔══╝██║    ██║██╔════╝██╔════╝╚══██╔══╝██║████╗  ██║██╔════╝ 
   ██║   ██║ █╗ ██║█████╗  █████╗     ██║   ██║██╔██╗ ██║██║  ███╗
   ██║   ██║███╗██║██╔══╝  ██╔══╝     ██║   ██║██║╚██╗██║██║   ██║
   ██║   ╚███╔███╔╝███████╗███████╗   ██║   ██║██║ ╚████║╚██████╔╝
   ╚═╝    ╚══╝╚══╝ ╚══════╝╚══════╝   ╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝
        A rede social que mais cresce na UFRPE
__________________________________________________________________

╔═══════════════════════════════════════════════════════☻
║ 1 - Login       ► O que seus amigos estão aprontando? ║
║                                                       ║
║ 2 - Sign In     ► Cadastre-se já!                     ║
║                                                       ║
║ 3  - Exit       ► A gente se vê...                    ║
╚═══════════════════════════════════════════════════════╝
tweeting alpha 1.0              Usuários Ativos: %s 
__________________________________________________________________
"""
INFO = """
==================================================================
        Informações do Usuário
==================================================================
Nome do usuário:        %s
Apelido:                %s
Idade:                  %s
Senha:                  %s
__________________________________________________________________
Pressione ENTER para continuar
__________________________________________________________________
"""
USER_MENU = """
____________________________________________________________________

████████╗██╗    ██╗███████╗███████╗████████╗██╗███╗   ██╗ ██████╗ 
╚══██╔══╝██║    ██║██╔════╝██╔════╝╚══██╔══╝██║████╗  ██║██╔════╝ 
   ██║   ██║ █╗ ██║█████╗  █████╗     ██║   ██║██╔██╗ ██║██║  ███╗
   ██║   ██║███╗██║██╔══╝  ██╔══╝     ██║   ██║██║╚██╗██║██║   ██║
   ██║   ╚███╔███╔╝███████╗███████╗   ██║   ██║██║ ╚████║╚██████╔╝
   ╚═╝    ╚══╝╚══╝ ╚══════╝╚══════╝   ╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝ 
--------------------------------------------------------------------
 Menu do Usuário 			conta: {}
--------------------------------------------------------------------
	_____________________ 	______________________
	1 - Postar Tweet    	4 - Mudar Senha         
	2 - Acessar Postagens 	5 - Deletar Conta
        3 - Central de Amigos   6 - Meus Dados
	_____________________   _______________________
	

tweeting alpha 1.0			7 - Log Out
____________________________________________________________________
"""
#=================================================================
#       Configurações de Sign In:
#=================================================================
USER_NAME_SIZE = 5
PASSWORD_SIZE = (6,12) # (mínimo,máximo)
#=================================================================
#       Configurações da Mensagem
#=================================================================
TAMANHO_MENSAGEM = 140
DATA = "%02d/%02d/%02d, às %02d:%02d"
GUI = """
====================================================================
        %s - %s         [tweeting alpha 1.0]
====================================================================
"%s"
____________________________________________________________________
"""
TWEET_SHAME = """
____________________________________________________________________
                POSTS - Servidor: %s
--------------------------------------------------------------------
%s

        Pressione ENTER para voltar.
_____________________________________________________________________

"""
USER_LIST = """
_____________________________________________________________________
        Lista de usuários
---------------------------------------------------------------------
%s


_____________________________________________________________________
"""
class Screen(object):
        def imprime(self,text,arg="="):
                self.text = text
                print(arg*50+"\n%s\n"%text+arg*50)
        def update(self,delay=1):
                self.delay = delay
                time.sleep(delay)
                os.system('cls')     
class Modify(object):
        global screen, total_users
        screen = Screen()
        total_users = 0
        def load(self,archive_name):
                global total_users
                screen.update()
                not_found = "Arquivo \"%s\" não encontrado, Novo\narquivo criado!"%archive_name
                found = "Arquivo \"%s\" carregado com sucesso!"%archive_name
                self.archive_name = archive_name
                try:
                        file = open(archive_name,"r")
                        archive = file.readlines()
                        total_users = len(archive)
                        file.close()
                        screen.imprime(found)
                        screen.update()
                        return archive
                except:
                        file = open(archive_name,"w")
                        file.close()
                        screen.imprime(not_found)
                        screen.update()
                        return False   
        def save(self,archive_name,archive,arg = "a"):
                screen.update()
                self.load(archive_name)
                self.archive_name = archive_name
                self.archive = archive
                self.load(archive_name)
                file = open(archive_name,arg)
                file.write(archive)
                file.close()
                screen.imprime("Dados salvos com sucesso!")
        def check_space_bar(self,var):
                if " " in var:
                        screen.imprime("Espaços não serão tolerados!")
                        return True
                if "\ç".replace("ç","") in var:
                        screen.imprime('"\\" não será tolerado!')
                        return True
                if SEPARADOR in var:
                        screen.imprime('"%s" não será tolerado!'%SEPARADOR)
                        return True
                if var == "":
                        screen.imprime("Voltando...","-")
                        return True
                return False
        def delete(self,user_name):
                while True:
                        screen.update()
                        screen.imprime("Tem certeza que deseja apagar a conta?")
                        screen.imprime("S - sim\nN - não","-")
                        choice = input()
                        if choice.upper() == "S":
                                #deletando
                                screen.update()
                                screen.imprime("Deletando conta...")
                                file = open(USER_ARCHIVE,"r")
                                file_II = open("..//tweeting//usuários//%s"%user_name+".txt","w")
                                reading = file.readlines()
                                file.close()
                                file_II.close()
                                temp, x = "",SEPARADOR
                                for line in reading:
                                        line = line.replace("\n","")
                                        line = line.split(SEPARADOR)
                                        if not line[0] == user_name:
                                                temp += SAVING%(line[0],x,line[1],x,line[2],x,line[3])
                                self.save(USER_ARCHIVE,temp,"w")
                                screen.update()
                                screen.imprime("Conta eliminada com sucesso")
                                Application()
                        if choice.upper() == "N":
                                screen.imprime("Voltando...","-")
                                return   
        def change_key(self,user_name):
                global user_info
                while True:
                        screen.update()
                        screen.imprime("Tela de alteração de senha")
                        screen.imprime("Nota: deixe o texto em branco para voltar ao menu\nanterior","-")
                        file = open(USER_ARCHIVE,"r")
                        reading = file.readlines()
                        old_key = input("Senha antiga: ")
                        temp = ""
                        x, y = SEPARADOR,PASSWORD_SIZE
                        end = False
                        if old_key == "":
                                screen.imprime("Voltando","-")
                                In_App()
                        for line in reading:
                                line = line.replace("\n","")
                                line = line.split(x)
                                if not line[0] == user_name:
                                        temp += SAVING%(line[0],x,line[1],x,line[2],x,line[3])
                                elif line[0] == user_name and old_key == line[3]:
                                        print("Ok")
                                        screen.imprime("A nova senha deve conter entre %s e %s caracteres!"%(y[0],y[1]),"-")
                                        new_password = input("Nova senha: ")
                                        a = self.check_space_bar(new_password)
                                        if a == True:
                                                self.change_key(nome)
                                        if len(new_password) < y[0] or len(new_password) < y[0]:
                                                screen.imprime("Senha demasiadamente longa ou curta!")
                                                self.change_key(nome)
                                        else:
                                                print("Ok")
                                                line[3] = new_password
                                                temp += SAVING%(line[0],x,line[1],x,line[2],x,line[3])
                                                end = True
                        if end == True:
                                self.save(USER_ARCHIVE,temp,"w")
                                user_info[3] = new_password
                                screen.imprime("Senha alterada com sucesso!","-")
                                In_App()
class In_App(Modify):
        def __init__(self):
                while True:
                        screen.update()
                        print(USER_MENU.format(nome))
                        choice = input()
                        if choice == "1":
                                self.tweeting(nome)
                        if choice == "2":
                                self.check_tweets()
                        if choice == "3":
                                self.friend_central(nome)
                        if choice == "4":
                                self.change_key(nome)
                        if choice == "5":
                                self.delete(nome)
                        if choice == "6":
                                screen.update()
                                self.load(USER_ARCHIVE)
                                input(INFO%(user_info[0],user_info[1],user_info[2],user_info[3]))
                        if choice == "7":
                                Application()
        def tweeting(self,nome):
                screen.update()
                screen.imprime("Área dos posts - As mensagens devem ter no máximo\n%s caracteres"%TAMANHO_MENSAGEM)
                screen.imprime("Nota: deixe o texto em branco para voltar ao menu","-")
                message = input()
                if message == "":
                        screen.imprime("Voltando...","-")
                        In_App()
                self.check_dir("..//tweeting//usuários")
                self.check_dir("..//tweeting//geral")
                file = open("..//tweeting//usuários//%s"%nome+".txt","a")
                x = datetime.now()
                data = DATA%(x.day,x.month,x.year,x.hour,x.minute)
                file.write(GUI%(nome,data,message))
                file.close()
                file = open("..//tweeting//geral//servidor_geral.txt","a")
                data = DATA%(x.day,x.month,x.year,x.hour,x.minute)
                file.write(GUI%(nome,data,message))
                file.close()
        def check_tweets(self):
                while True:
                        screen.update()
                        screen.imprime("Qual servidor deseja acessar?")
                        screen.imprime("1 - Usuário\n2 - Servidor Geral\n3 - Voltar")
                        choice = input()
                        screen.update()
                        if choice == "1":
                                a = self.list_users()
                                print(a)
                                screen.imprime("Nota: deixe o texto em branco para voltar ao menu\nanterior","-")
                                user = input("Digite o usuário a ser acessado: ")
                                if user == "":
                                        screen.imprime("Voltando...","-")
                                        self.check_tweets()
                                screen.update()
                                try:
                                        file = open("..//tweeting//usuários//%s"%user+".txt","r")
                                except:
                                        screen.update()
                                        screen.imprime("Usuário não disponível ou ainda não fez nenhuma\npostagem")
                                        In_App()
                                reading = file.readlines()
                                tweets = ""
                                for line in reading:
                                        tweets += line
                                input(TWEET_SHAME%(user,tweets))
                        if choice == "2":
                                screen.update()
                                file = open("..//tweeting//geral//servidor_geral.txt","r")
                                reading = file.readlines()
                                tweets = ""
                                for line in reading:
                                        tweets += line
                                input(TWEET_SHAME%("Tweeting: Servidor Geral",tweets))
                        if choice == "3":
                                In_App()
        def check_dir(self,dir_):
                if not os.path.exists(dir_):
                        os.mkdir(dir_)
                        return True
                else:
                        return False
        def list_users(self):
                file = open(USER_ARCHIVE,"r")
                reading = file.readlines()
                user_list, x = "", SEPARADOR
                for line in reading:
                        line = line.replace("\n","")
                        line = line.split(x)
                        user_list += line[0] + "\n"
                        lista = USER_LIST%user_list
                return lista
        def friend_central(self,user):
                # EM ANDAMENTO - OBS: Ainda não pude polir essa parte
                while True:
                        screen.update()
                        screen.imprime("Central de Amigos")
                        screen.imprime("1 - Seguir\n2 - Deixar de seguir\n3 - Meus ídolos\n4 - Meus fans\n5 - Voltar","-")
                        choice = input()
                        if choice == "1":
                                self.load("..//tweeting//usuários//%s"%user+"_following.txt")
                                screen.update()
                                screen.imprime("Seguir usuário")
                                screen.imprime("Nota: deixe o texto em branco para voltar ao menu\nanterior","-")
                                a = self.list_users()
                                print(a)
                                friend = input("Digite o nome do usuário: ")
                                if friend == "":
                                        screen.imprime("Voltando...","-")
                                        self.friend_central(nome)
                                a = self.check_user(USER_ARCHIVE)
                                b = self.check_user("..//tweeting//usuários//%s"%user+"_following.txt")
                                if friend.replace(" ","") in a and friend.replace(" ","") != user and not friend.replace(" ","") in b:
                                        following_friend = friend + "\n"
                                        self.save("..//tweeting//usuários//%s"%user+"_following.txt",following_friend,"a")
                                        screen.imprime("Amigo adicionado com sucesso!")
                                        self.friend_central(nome)
                                elif friend.replace(" ","") == user:
                                        screen.imprime("Você não pode seguir a si próprio!","-")
                                elif friend.replace(" ","") in b:
                                        screen.imprime("Você atualmente já segue esse usuário!")
                                else:
                                        screen.imprime("Usuário indisponível!","-")
                        if choice == "2":
                                self.load("..//tweeting//usuários//%s"%user+"_following.txt")
                                screen.imprime("Controle de amigos")
                                screen.imprime("Nota: deixe o texto em branco para voltar ao menu\nanterior","-")
                                a = self.check_user("..//tweeting//usuários//%s"%user+"_following.txt")
                                new = ""
                                for item in a:
                                        print(item)
                                        remove_friend = input("Digite o nome do usuário a remover: ").replace(" ","")
                                if remove_friend in a:
                                        for item in a:
                                                if remove_friend != item:
                                                        new += remove_friend + "\n"
                                        self.save("..//tweeting//usuários//%s"%user+"_following.txt",new,"w")
                                        self.save("..//tweeting//usuários//%s"%remove_friend+"_followers.txt",user+'\n',"a")
                                        screen.imprime("Usuário removido com sucesso!","-")
                                        self.friend_central(nome)
                                else:
                                        screen.imprime("Usuário não encontrado!")
                                        self.friend_central(nome)
                                        
                        if choice == "3":
                                self.load("..//tweeting//usuários//%s"%user+"_following.txt")
                                screen.update()
                                screen.imprime("Menu - Meus Ídolos: Lista de usuários que\nsigo atualmente")
                                a = self.check_user("..//tweeting//usuários//%s"%user+"_following.txt")
                                screen.imprime("Total de ídolos: %s"%len(a),"_")
                                idols = ""
                                for item in a:
                                        idols += item + "\n"
                                print(idols)
                                screen.imprime("Pressione ENTER para voltar ao menu anterior")
                                input()
                                self.friend_central(nome)
                        if choice == "4":
                                pass
                        if choice == "5":
                                In_App()
        def check_user(self,archive):
                file = open(archive,"r")
                reading = file.readlines()
                users = []
                for line in reading:
                        line = line.replace("\n","")
                        line = line.split(SEPARADOR)
                        users.append(line[0])
                return users
class Login_Scene(Modify):
        def __init__(self):
                global nome
                screen.imprime("Tela de login - Fornece  o acesso dos usuários\nao servidor")              
                nome = input("Usuário: ")
                screen.imprime("R - recuperação de senha")
                senha = input("Senha: ")
                if senha.upper() == "R":
                       self.recover(nome)
                if total_users <= 0:
                        screen.imprime("Nenhum usuário encontrado!")
                        screen.update()
                        Application()
                self.load_info()
                self.load_user(nome,senha)
        def load_user(self,nome,senha):
                self.load("..//tweeting//usuários//%s"%nome+".txt")
                file = open(USER_ARCHIVE,"r")
                reading = file.readlines()
                for line in reading:
                        line = line.replace("\n","")
                        line = line.split(SEPARADOR)
                        if line[0] == nome and line[3] == senha:
                                screen.imprime("Acesso concebido!!")
                                time.sleep(1)
                                In_App()               
                screen.imprime("Nome do usuário ou senha incorreta!")
                Application()
        def load_info(self):
                file = open(USER_ARCHIVE,"r")
                global user_info
                user_info = []
                reading = file.readlines()
                for line in reading:
                        line = line.replace("\n","")
                        line = line.split(SEPARADOR)
                        if line[0] == nome:
                                user_info = line
        def recover(self,nome):
                file = open(USER_ARCHIVE,"r")
                reading = file.readlines()
                file.close()
                apelido = input("Digite o apelido do usuário: ")
                new = ""
                for line in reading:
                        line = line.replace("\n","")
                        line = line.split(SEPARADOR)
                        end = False
                        x = SEPARADOR
                        if line[0] == nome and apelido == line[1]:
                                senha = str(random.randint(0,999999))
                                line[3] = senha
                                new += SAVING%(line[0],x,line[1],x,line[2],x,line[3])
                                end = True
                        elif line[0] != nome:
                                new += SAVING%(line[0],x,line[1],x,line[2],x,line[3])
                if end == True:
                        self.save(USER_ARCHIVE,new,"w")
                        screen.imprime("Sua nova senha é: %s"%senha,"=")
                        screen.imprime("Pressione ENTER para voltar")
                        input()
                        Application()
                if end == False:
                        screen.imprime("Não foi posível realizar alterações!")
                        Login_Scene()
class Signin_Scene(Modify):
        def display_menu(self):
                screen.imprime("Tela de Sign in - Novos usuários podem se\n cadastrados")
                screen.imprime("Nota: deixe o texto em branco para voltar ao menu","-")
        def __init__(self):
                while True:
                        screen.update(1)
                        self.display_menu()
                        screen.imprime("O nome do usuário deve conter pelo menos %s\ncaracteres"%USER_NAME_SIZE,"-")
                        nome = input("Digite um nome para o usuário: ")
                        i = self.search_in_archive(nome)
                        if len(nome) < USER_NAME_SIZE:
                                screen.imprime("Nome demasiadamente curto!","-")
                                i = True
                        space_bar_check = self.check_space_bar(nome)
                        if i == False and space_bar_check == False or i == None and space_bar_check == False:
                                print("OK")
                                break
                while True:
                        screen.update(1)
                        self.display_menu()
                        #apelido
                        apelido = input("Digite um apelido para o usuário: ")
                        space_bar_check = self.check_space_bar(apelido)
                        if space_bar_check == False:
                                print("Ok")
                                break
                while True:
                        screen.update(1)
                        self.display_menu()
                        screen.imprime("A idade deve ser um número inteiro!","-")
                        #idade
                        try:
                                idade = int(input("Digite a idade do usuário: "))
                                print("Ok")
                                break
                        except:
                                screen.imprime("Formato não suportado!","-")
                while True:
                        screen.update(1)
                        self.display_menu()
                        x = PASSWORD_SIZE
                        screen.imprime("A senha deve conter entre %s e %s caracteres!"%(x[0],x[1]),"-")
                        #senha
                        senha = input("Digite uma senha para o usuário: ")
                        i = self.check_space_bar(senha)
                        if i == False and x[0] <= len(senha) <= x[1]:
                                print("Ok")
                                break
                        elif len(senha) < x[0]:
                                screen.imprime("Senha muito curta!")
                        elif len(senha) > x[1]:
                                screen.imprime("Senha demasiadamente longa!")
                screen.update()
                x = SEPARADOR
                saving = SAVING%(nome,x,apelido,x,idade,x,senha)
                self.save(USER_ARCHIVE,saving)
                time.sleep(1)
                screen.imprime("Novo usuário adicionado com sucesso!")
                screen.update()
                input(INFO%(nome,apelido,idade,senha))
                Application()
        def search_in_archive(self,nome):
                file = open(USER_ARCHIVE,"r")
                reading = file.readlines()
                for line in reading:
                        line.replace("\n","")
                        line = line.split(SEPARADOR)
                        if line[0] == nome:
                                screen.imprime("Usuário indisponível no momento! '-'","-")
                                return True
                return False
class Application(Modify):
        def __init__(self):
                while True:
                        self.load(USER_ARCHIVE)
                        screen.update(0.5)
                        print(MAIN_MENU%total_users)
                        choice = input()
                        if choice == "1":
                                screen.update(0.2)
                                Login_Scene()
                        if choice == "2":
                                #screen.update(0.2)
                                screen.imprime("Loading...","-")
                                Signin_Scene()
                        if choice == "3":
                                exit()
Application()
