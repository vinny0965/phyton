print("teste de login")


from  tkinter import *

class Login:
    def __init__(self,master):
        self.master = master
        self.master.title("Invasion System")
        Label(self.master,text= "(((Sistema de Rede e Controle de Câmeras POLÍCIA FEDERAL/Perimetro/Região)))").grid(row=1,column=1,columnspan=2,pady=4)
        Label(self.master,text="Usuário:").grid(row=2,column=1,pady=4)
        self.usuario = Entry(self.master,width=10).grid(row=2,column=2)
        Label(self.master, text="Senha:").grid(row=3, column=1,pady=4)
        self.senha = Entry(self.master,width=10).grid(row=3, column=2)
        Button(self.master, text="login",width=8 ).grid(row=4,column=2,pady=4)
        Button(self.master, text = "Sair",width = 8).grid(row=4,column=2,pady=4)


root = Tk()
Login(root)
root.mainloop()


#def __init__(self, master=None):
    # -----------------------------------------
    # Criando widget inicial
    # -----------------------------------------
 #   self.widget1 = Frame(master)
  #  self.widget1.pack()
   # self.mensagem = Label(self.widget1, text="Primeiro widget")
    #self.mensagem["font"] = ("Verdana", "10", "italic", "bold")
   # self.mensagem.pack()
    # -----------------------------------------

    # funcao sair
   # """self.sair = Button(self.widget1)
   # self.sair["text"] = "Sair"
   # self.sair["font"] = ("Calibri", "10")
   # self.sair["width"] = 10
   # self.sair["command"]  = self.widget1.quit
  #  self.sair.pack()
 #   """

 #   self.sair = Button(self.widget1)
 #   self.sair["text"] = "Sair"
  #  self.sair["font"] = ("Calibri", "10")
   # self.sair["width"] = 10
    #self.sair.bind("<Button-1>", self.mudarTexto)
    #self.sair.pack()


#def mudarTexto(self, event):
#    if self.mensagem["Text"] == "Primeiro Widget":
 #       self.mensagem["Text"] = "O botão recebeu um clique!"
  #  else:
   #     self.mensagem["text"] = "Primeiro Widget"


