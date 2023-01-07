#import das bibliotecas
from tkinter import *
from tkinter import messagebox

class app():
    # Criador da Janela

    jan = Tk()
    jan.title("DP System - Acess")
    jan.geometry("600x300")
    jan.configure(background="black")
    jan.resizable(width=False,height=False)

    # Inserindo Imgs

    logo = PhotoImage(file="img/logo.jpg")

    # Basicamente o separador da janela

    LeftFrame = Frame(jan, width=200, height=300,bg="Blue",relief="raise")
    LeftFrame.pack(side=LEFT)

    RightFrame= Frame(jan, width=395, height=300,bg="Blue",relief="raise")
    RightFrame.pack(side=RIGHT)

    LogoLabel = Label(LeftFrame, image=logo, bg="Blue")

    # Chamada de funções
    jan.mainloop()
app()