from tkinter import *


class Gerente:
    def __init__(self):
        self.janela = Tk()
        self.janela.title('Gerência')
        self.titleStyles = ('Arial', 14)
        self.textStyles = ('Roboto', 14)
        self.imgStyles = ('Roboto', 15)
        self.janela.minsize(1200, 650)
        self.janela.maxsize(1200, 650)
        # self.janela.state("zoomed")
        self.janela.configure(bg="#363636")
        self.janela.iconbitmap('automotivo.ico')

        self.img = PhotoImage(master=self.janela, file="tela-gerente.png")
        self.img1 = self.img.subsample(1, 1)

        self.localIMG = Label(master=self.janela, image=self.img1)
        self.localIMG.pack(fill='both', anchor='nw')

        self.botaoGerenciar = Button(self.janela, command=self.gerenciarFuncionarios,
                                     font=self.textStyles, text='Gerenciar\nFuncionários', width=20, height=3, bg='#4682B4', fg="white")
        self.botaoGerenciar.bind("<Enter>", self.hoverIn)
        self.botaoGerenciar.bind("<Leave>", self.hoverOut)
        self.botaoGerenciar.place(x=810, y=145)

        self.botaoOrdem = Button(self.janela, command=self.verOrdem,
                                 font=self.textStyles, text='Ordens de Serviços', width=20, height=3, bg='#4682B4', fg="white")
        self.botaoOrdem.bind("<Enter>", self.hoverIn)
        self.botaoOrdem.bind("<Leave>", self.hoverOut)
        self.botaoOrdem.place(x=810, y=250)

        self.botaoCliente = Button(self.janela, command=self.verCliente,
                                   font=self.textStyles, text='Cliente', width=20, height=3, bg='#4682B4', fg="white")
        self.botaoCliente.bind("<Enter>", self.hoverIn)
        self.botaoCliente.bind("<Leave>", self.hoverOut)
        self.botaoCliente.place(x=810, y=360)

        self.botaoSair = Button(self.janela, command=self.sair,
                                font=self.textStyles, text='Sair', width=15, height=2, bg='#4682B4', fg="white")
        self.botaoSair.bind("<Enter>", self.hoverIn2)
        self.botaoSair.bind("<Leave>", self.hoverOut)
        self.botaoSair.place(x=837, y=500)

        self.titulo = Label(self.janela, bg='#363636',
                            fg='white', font=self.titleStyles, text='GERÊNCIA')
        self.titulo.pack(padx=0, pady=10)

        mainloop()

    def gerenciarFuncionarios(self):
        from cadastrarFuncionario import ver_cadastrar_func
        return

    def verOrdem(self):
        from GerOrdensGerente import ver_Ordens
        return

    def verCliente(self):
        from gerenciarCliente import tela_gerenciar_clientes
        return

    def sair(self):
        self.janela.destroy()
        from Tela_Login import Tela_de_Login
        return

    def hoverIn(self, event):
        event.widget.config(bg="#1E90FF", fg="white")

    def hoverIn2(self, event):
        event.widget.config(bg="#FF0000", fg="white")

    def hoverOut(self, event):
        event.widget.config(bg="#4682B4", fg="white")

    # def startGer(self):
    #    minhaTela = Gerente()
    #    return minhaTela.janela.mainloop()


minhaTela = Gerente()
