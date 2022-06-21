from tkinter import *
from tkinter import messagebox


class Recepcao:
   def __init__(self):
      self.janela = Tk()
      self.janela.title('Recepção')
      self.titleStyles = ('Arial', 14)
      self.textStyles = ('Roboto', 13)
      self.janela.maxsize(1200, 600)
      self.janela.minsize(1200, 600)
      self.janela.configure(bg='#363636')
      self.janela.minsize(width=1200,height=600)
      self.janela.iconbitmap('automotivo.ico')
      
      self.LoginCanvas = Canvas(master=self.janela, width = 600, height=370)
      self.LoginCanvas.pack(expand=1,fill=BOTH)
      
      self.Back = PhotoImage(master=self.janela, file="recepcao.png")
      self.LoginCanvas.create_image(0,0,image=self.Back, anchor=NW)
      
      self.hoverColor1 = '#008000'
      self.hoverColor2 = '#1E90FF'
      self.hoverColor3 = '#FF0000'

      self.botaoCadastrar = Button(self.janela,text="Cadastrar\nCliente",font=('Roboto', 15),width=15,height=3,pady=5,bg="#4682B4",fg="white",relief=RAISED,command=self.cadastrarCliente)
      self.LoginCanvas.create_window(900,200,window=self.botaoCadastrar)
      self.botaoCadastrar.bind("<Enter>", self.hoverIn1)
      self.botaoCadastrar.bind("<Leave>", self.hoverOut)
      

      self.botaoOrcamento = Button(self.janela,text="Ver\nOrçamento",font=('Roboto', 15),width=15,height=3,pady=1,bg="#4682B4",fg="white",relief=RAISED,command=self.verOrcamento)
      self.LoginCanvas.create_window(900,330,window=self.botaoOrcamento)
      self.botaoOrcamento.bind("<Enter>", self.hoverIn2)
      self.botaoOrcamento.bind("<Leave>", self.hoverOut)
      

      self.botaoSair = Button(self.janela,text="SAIR",font=('Roboto', 15),width=7,bg="#4682B4",fg="white",pady=5,relief=RAISED,command=self.saiu)
      self.LoginCanvas.create_window(900,500,window=self.botaoSair)
      self.botaoSair.bind("<Enter>", self.hoverIn3)
      self.botaoSair.bind("<Leave>", self.hoverOut)
      

      self.titulo = Label(self.janela,bg='#363636',fg='white', font=self.titleStyles, text='RECEPÇÃO')
      self.titulo.pack(padx=0, pady=10)

            
      
      mainloop()

   def cadastrarCliente(self):
      from cadastrarCliente import tela_ver_cadastrar_clientes
      return

   def hoverIn1(self, event):
      event.widget.configure(bg=self.hoverColor1, fg="white",relief=GROOVE)
   def hoverIn2(self, event):
      event.widget.configure(bg=self.hoverColor2, fg="white",relief=GROOVE)
   def hoverIn3(self, event):
      event.widget.configure(bg=self.hoverColor3, fg="white",relief=GROOVE)
   def hoverOut(self, event):
      event.widget.configure(bg='#4682B4',relief=RAISED)
   def hoverOut2(self, event):
      event.widget.configure(relief=RAISED)

   def saiu(self):
      self.janela.destroy()
      from Tela_Login import Tela_de_Login
      return

   def verOrcamento(self):
      from VerOrcamentoRecep import ver_Orcamento
      return
         
   

minhaTela = Recepcao()
