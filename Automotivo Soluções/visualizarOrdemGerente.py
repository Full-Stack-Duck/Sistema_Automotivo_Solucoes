from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import BOLD


class GerenciarOrdens():
   def __init__(self):

      self.janela = Tk()
      self.janela.title('Gerenciar Ordens de Serviço')
      self.janela.geometry('1600x900')
      self.janela.minsize(1600, 900)
      self.janela.maxsize(1600, 900)
      self.janela.config(bg="#484848")
      self.janela.state("zoomed")
      self.janela.iconbitmap('automotivo.ico')

   # ============= SEÇÕES ================ #
      self.containerInicial = Label(self.janela, bg="#484848", fg="white", text='Ordens de Serviço', font=(
         "Roboto", 25, BOLD))

      self.container = LabelFrame(self.janela, bg="#484848", fg="#e1e3db")
      self.rodape = Frame(self.janela, bg="#484848")

      self.containerInicial.pack(fill='x', expand='no', pady=40)
      self.container.pack(fill='x', expand='yes', ipadx=30, padx=30)
      self.rodape.pack(fill='both', expand='no', padx=20)

   # ------------------- TREEVIEW ------------------ #
      self.style = ttk.Style(master=self.janela)
      self.style.theme_use("clam")
      self.style.configure("mystyle.Treeview", font=("Roboto", 14))
      self.style.configure("mystyle.Treeview.Heading", font=("Roboto", 16))
      self.style.configure("Treeview", background="silver",
                     rowheight=25, fieldbackground="#E0FFFF",)
      self.style.configure("Heading", background="#4682B4", foreground="white")

      self.cabecalho = ('#', 'cliente', 'cpfCliente', 'mecanico', 'cpfMecanico',
                        'servico', 'valor')
      self.trv = ttk.Treeview(
         self.container, selectmode='browse', columns=self.cabecalho, show='headings')

      self.trv.column('#', width=30)
      self.trv.column('cliente', anchor='center', width=300)
      self.trv.column('cpfCliente', anchor='center', width=200)
      self.trv.column('mecanico', anchor='center', width=300)
      self.trv.column('cpfMecanico', anchor='center', width=200)
      self.trv.column('servico', anchor='center', width=200)
      self.trv.column('valor', anchor='center', width=200)

      self.trv.heading('#', text='#')
      self.trv.heading('cliente', text='Nome do Cliente')
      self.trv.heading('cpfCliente', text='CPF do Cliente')
      self.trv.heading('mecanico', text='Nome do Mecânico')
      self.trv.heading('cpfMecanico', text='CPF do Mecânico')
      self.trv.heading('servico', text='Serviço')
      self.trv.heading('valor', text='Valor')

      self.trv.bind('<Double 1>', self.pegar_linha)
      self.trv.pack(pady=20)

      self.popular()

      # ========= SEÇÃO RODAPÉ ======= #
      # ---------- BOTÃO ----------- #
      self.finalizarBtn = Button(self.container, text='Finalizar Ordem', font=("Roboto", 14, BOLD), width='20', height=2,
                              command=self.finalizar, bg="#566981", fg="#e1e3db", relief=RAISED)
      self.finalizarBtn.pack(side='left', pady=20, padx=165)
      self.finalizarBtn.bind("<Enter>", self.hoverIn1)
      self.finalizarBtn.bind("<Leave>", self.hoverOut)

      self.ativasBtn = Button(self.container, text='Ordens ativas', font=("Roboto", 14, BOLD), width='20', height=2,
                              command=self.ver_ativas, bg="#566981", fg="#e1e3db", relief=RAISED)
      self.ativasBtn.pack(side='left', pady=20, padx=100)
      self.ativasBtn.bind("<Enter>", self.hoverIn1)
      self.ativasBtn.bind("<Leave>", self.hoverOut)

      self.finalizadasBtn = Button(self.container, text='Ordens finalizadas', font=("Roboto", 14, BOLD), width='20', height=2,
                              command=self.ver_finalizadas, bg="#566981", fg="#e1e3db", relief=RAISED)
      self.finalizadasBtn.pack(side='left', pady=20, padx=150)
      self.finalizadasBtn.bind("<Enter>", self.hoverIn1)
      self.finalizadasBtn.bind("<Leave>", self.hoverOut)

      self.voltarBtn = Button(self.rodape, text='Voltar', font=("Roboto", 14, BOLD), width='20', height=2,
                              command=self.voltar_tela, bg="#cc0000", fg="#e1e3db", relief=RAISED)
      self.voltarBtn.pack(side='right', pady=40)
      self.voltarBtn.bind("<Enter>", self.hoverIn3)
      self.voltarBtn.bind("<Leave>", self.hoverOut2)

      mainloop()

   # ============= FUNÇÕES ============== #
   def pegar_linha(self, identificador):

      return

   def popular(self):
      # self.trv.delete(*self.trv.get_children())
      # staff = TabFunc()
      # for i in staff.populate():
      #     self.trv.insert('', 'end', values=i)
      return

   def finalizar(self):
      return

   def ver_finalizadas(self):
      return

   def ver_ativas(self):
      return

   def voltar_tela(self):
      self.janela.destroy()
      return

   def hoverIn1(self, event):  # verde
      event.widget.config(bg="#3CB371", fg="white", relief=GROOVE)

   def hoverIn3(self, event):  # vermelho
      event.widget.config(bg="#8B0000", fg="white", relief=GROOVE)

   def hoverOut(self, event):
      event.widget.config(bg="#566981", fg="#e1e3db", relief=RAISED)

   def hoverOut2(self, event):
      event.widget.config(bg="#cc0000", fg="#e1e3db", relief=RAISED)


minhaTela = GerenciarOrdens()
