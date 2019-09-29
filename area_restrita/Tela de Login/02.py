from tkinter import *

class Login:
    def __init__(self, master=None):
        # -----------------------------------------
        # Criando widget inicial
        # -----------------------------------------
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.mensagem = Label(self.widget1, text="Primeiro Widget")
        self.mensagem["font"] = ("Verdana", "10", "italic", "bold")
        self.mensagem.pack()
        # -----------------------------------------

        # funcao sair
        """self.sair = Button(self.widget1)
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Calibri", "10")
        self.sair["width"] = 10
        self.sair["command"]  = self.widget1.quit
        self.sair.pack()
        """

        self.sair = Button(self.widget1)
        self.sair["text"] = "Clique Aqui"
        self.sair["font"] = ("Calibri", "10")
        self.sair["width"] = 10
        self.sair["command"] = self.mudarTexto
        self.sair.pack()

    def mudarTexto(self):
        if self.mensagem["text"] == "Primeiro Widget":
            self.mensagem["text"] = "O botão recebeu um clique!"
        else:
            self.mensagem["text"] = "Primeiro Widget"









root = Tk()
Login(root)
root.mainloop()







"""self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text="Primeiro widget")
        self.msg["font"] = ("Verdana", "10", "italic", "bold")
        self.msg.pack ()

"""