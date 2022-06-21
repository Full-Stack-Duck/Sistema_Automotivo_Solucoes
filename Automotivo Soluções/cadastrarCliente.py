from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from TabClien import Clientes


class tela_ver_cadastrar_clientes():
    def __init__(self):

        self.janelaCad_Cliente = Tk()

        self.janelaCad_Cliente.title('Cadastro de clientes')
        self.janelaCad_Cliente.geometry('1280x1040')
        self.janelaCad_Cliente.config(bg="#484848")
        self.janelaCad_Cliente.state('zoomed')
        self.janelaCad_Cliente.iconbitmap('automotivo.ico')

# ============= SEÇÕES ================ #
        self.wrapper1 = LabelFrame(
            self.janelaCad_Cliente, text='Clientes Cadastrados', font=("Roboto", 14, 'bold'), bg="#484848", fg="#e1e3db")
        self.wrapper2 = LabelFrame(
            self.janelaCad_Cliente, text='Procurar Cliente', font=("Roboto", 14, 'bold'), bg="#484848", fg="#e1e3db")
        self.wrapper3 = LabelFrame(
            self.janelaCad_Cliente, text='Dados do Cliente', font=("Roboto", 14, 'bold'), bg="#484848", fg="#e1e3db")
        self.rodape = Frame(self.janelaCad_Cliente, bg="#484848")

        self.wrapper1.pack(fill='both', expand='no', padx=20, pady=(20, 0))
        self.wrapper2.pack(fill='both', expand='no', padx=20, pady=(30, 0))
        self.wrapper3.pack(fill='both', expand='no', padx=20, pady=30)
        self.rodape.pack(fill='both', expand='no', padx=20, pady=(0, 20))

# ============ SEÇÃO CLIENTES CADASTRADOS =============== #
# ------------------- TREEVIEW ------------------ #
        self.style = ttk.Style(master=self.janelaCad_Cliente)
        self.style.theme_use("clam")
        self.style.configure("mystyle.Treeview", font=("Roboto", 14))
        self.style.configure("mystyle.Treeview.Heading", font=("Roboto", 16))
        self.style.configure("Heading", background="#4682B4", foreground="black")

        self.cabecalho = ('#', 'nome', 'cpf', 'carro',
                          'telefone', 'email', 'endereco')
        self.trv = ttk.Treeview(
            self.wrapper1, selectmode='browse', columns=self.cabecalho, show='headings')

        self.trv.column('#', width=20)
        self.trv.column('nome', width=150, anchor='center')
        self.trv.column('cpf', width=150)
        self.trv.column('carro', width=150)
        self.trv.column('telefone', width=150)
        self.trv.column('endereco', width=320)

        self.trv.heading('#', text='#')
        self.trv.heading('nome', text='Nome')
        self.trv.heading('cpf', text='CPF')
        self.trv.heading('carro', text='Carro/Placa')
        self.trv.heading('telefone', text='Telefone')
        self.trv.heading('email', text='E-mail')
        self.trv.heading('endereco', text='Endereço')

        self.trv.bind('<Double 1>', self.pegar_linha)
        self.trv.pack(pady=10)

        self.popular()

# ============= SEÇÃO PROCURAR =========== #
# ---------- LABELS & ENTRYS ----------- #
        self.lbl1 = Label(self.wrapper2, text='Palavra-Chave',
                          bg="#484848", fg="#e1e3db")
        self.lbl1.pack(side='left', padx=10, pady=10)

        self.busca = Entry(self.wrapper2)
        self.busca.pack(side='left', padx=6, pady=10, ipadx=15)


# ------------- BOTÃO ------------- #
        self.procurarBtn = Button(
            self.wrapper2, text='Procurar', command=self.procurar, bg="#484848", fg="#e1e3db")
        self.procurarBtn.pack(side='left', padx=6, pady=10, ipadx=20)

        self.limparBtn = Button(self.wrapper2, text=(
            'Limpar'), command=self.limpar, bg="#484848", fg="#e1e3db", relief=RAISED)
        self.limparBtn.pack(side='left', padx=6, pady=10, ipadx=20)

        self.mostrarBtn = Button(
            self.wrapper2, padx=30, text='Mostrar Todos', command=self.popular, bg="#484848", fg="#e1e3db", relief=RAISED)
        self.mostrarBtn.pack(side='left', pady=10)

# ========= SEÇÃO DADOS DO CLIENTE ======= #
# ---------- LABELS & ENTRYS ----------- #
        self.lbl2 = Label(self.wrapper3, text='Nome',
                          bg="#484848", fg="#e1e3db")
        self.lbl2.grid(row=0, column=0, padx=5, pady=3)
        self.ent2 = Entry(self.wrapper3)
        self.ent2.grid(row=0, column=1, padx=5, pady=3)

        self.lbl3 = Label(self.wrapper3, text='CPF',
                          bg="#484848", fg="#e1e3db")
        self.lbl3.grid(row=1, column=0, padx=5, pady=3)
        self.ent3 = Entry(self.wrapper3)
        self.ent3.grid(row=1, column=1, padx=5, pady=3)

        self.lbl4 = Label(self.wrapper3, text='Carro/Placa',
                          bg="#484848", fg="#e1e3db")
        self.lbl4.grid(row=2, column=0, padx=5, pady=3)
        self.ent4 = Entry(self.wrapper3)
        self.ent4.grid(row=2, column=1, padx=5, pady=3)

        self.lbl5 = Label(self.wrapper3, text='Telefone',
                          bg="#484848", fg="#e1e3db")
        self.lbl5.grid(row=3, column=0, padx=5, pady=3)
        self.ent5 = Entry(self.wrapper3)
        self.ent5.grid(row=3, column=1, padx=5, pady=3)

        self.lbl6 = Label(self.wrapper3, text='E-mail',
                          bg="#484848", fg="#e1e3db")
        self.lbl6.grid(row=0, column=2, padx=5, pady=3)
        self.ent6 = Entry(self.wrapper3)
        self.ent6.grid(row=0, column=3, padx=5, pady=3, ipadx=40)

        self.lbl7 = Label(self.wrapper3, text='Endereço',
                          bg="#484848", fg="#e1e3db")
        self.lbl7.grid(row=1, column=2, padx=5, pady=3)
        self.ent7 = Entry(self.wrapper3)
        self.ent7.grid(row=1, column=3, padx=5, pady=3, ipadx=40)

        self.lbl8 = Label(self.wrapper3, text='ID Cliente',
                          bg="#484848", fg="#e1e3db")
        self.lbl8.grid(row=2, column=2, padx=5, pady=3)
        self.ent8 = Entry(self.wrapper3)
        self.ent8.grid(row=2, column=3, padx=5, pady=3, sticky='W')

# ------------ BOTÕES -------------- #
        self.addBtn = Button(self.wrapper3, text='Adicionar', bg="#484848", relief=RAISED, fg="#e1e3db",
                             command=self.inserir_cliente)
        self.alterarBtn = Button(
            self.wrapper3, text='Alterar', command=self.alterar_cliente, relief=RAISED, bg="#484848", fg="#e1e3db")
        self.excluirBtn = Button(
            self.wrapper3, text='Excluir', command=self.excluir_cliente, relief=RAISED, bg="#484848", fg="#e1e3db")

        self.addBtn.grid(row=4, column=0, padx=5, pady=15, ipadx=25)
        self.alterarBtn.grid(row=4, column=1, padx=2, pady=15, ipadx=20)
        self.excluirBtn.grid(row=4, column=2, padx=2, pady=15, ipadx=25)

        self.alterarBtn.bind("<Enter>", self.hoverIn3)
        self.alterarBtn.bind("<Leave>", self.hoverOut)
        self.excluirBtn.bind("<Enter>", self.hoverIn2)
        self.excluirBtn.bind("<Leave>", self.hoverOut)
        self.addBtn.bind("<Enter>", self.hoverIn)
        self.addBtn.bind("<Leave>", self.hoverOut)

# ========= SEÇÃO RODAPÉ ======= #
# ---------- BOTÃO ----------- #
        self.voltarBtn = Button(
            self.rodape, text='Voltar', width='20', command=self.voltar_tela, relief=RAISED, bg="#484848", fg="#e1e3db")
        self.voltarBtn.pack(side='right')

        mainloop()

# ============= FUNÇÕES ============== #
    def pegar_linha(self, identificador):
        customer = Clientes()
        self.normal()
        self.limpar_caixas()
        for item in self.trv.selection():
            self.id = self.trv.item(item, 'values')
        identificador = self.id[0]

        customer.identificar_linha(identificador)
        self.ent8.insert(INSERT, customer.idcliente)
        self.ent2.insert(INSERT, customer.nome)
        self.ent3.insert(INSERT, customer.cpf)
        self.ent4.insert(INSERT, customer.carro)
        self.ent5.insert(INSERT, customer.telefone)
        self.ent6.insert(INSERT, customer.email)
        self.ent7.insert(INSERT, customer.endereco)
        self.leitura_apenas()

    def limpar_caixas(self):
        self.normal()
        self.ent2.delete(0, END)
        self.ent3.delete(0, END)
        self.ent4.delete(0, END)
        self.ent5.delete(0, END)
        self.ent6.delete(0, END)
        self.ent7.delete(0, END)
        self.ent8.delete(0, END)

    def procurar(self):
        self.trv.delete(*self.trv.get_children())
        customer = Clientes()
        nome = self.busca.get()

        for i in customer.filtrar_cliente(nome):
            self.trv.insert('', 'end', values=i)

    def limpar(self):
        self.normal()
        self.busca.delete(0, END)
        self.ent2.delete(0, END)
        self.ent3.delete(0, END)
        self.ent4.delete(0, END)
        self.ent5.delete(0, END)
        self.ent6.delete(0, END)
        self.ent7.delete(0, END)
        self.ent8.delete(0, END)

    def inserir_cliente(self):
        customer = Clientes()
        customer.nome = self.ent2.get()
        customer.cpf = self.ent3.get()
        customer.carro = self.ent4.get()
        customer.telefone = self.ent5.get()
        customer.email = self.ent6.get()
        customer.endereco = self.ent7.get()
        customer.add_cliente()
        self.popular()
        self.limpar_caixas()

    def alterar_cliente(self):
        customer = Clientes()
        customer.nome = self.ent2.get()
        customer.cpf = self.ent3.get()
        customer.carro = self.ent4.get()
        customer.telefone = self.ent5.get()
        customer.email = self.ent6.get()
        customer.endereco = self.ent7.get()
        customer.idcliente = self.ent8.get()
        customer.atualizar_cliente()
        self.popular()
        self.limpar_caixas()

    def excluir_cliente(self):
        customer = Clientes()
        customer.idcliente = self.ent8.get()
        customer.deletar_cliente()
        self.popular()
        self.limpar_caixas()

    def voltar_tela(self):
        self.janelaCad_Cliente.destroy()
        # from telaRecepcao import Tela_de_Recepcao
        return

    def popular(self):
        self.trv.delete(*self.trv.get_children())
        costumer = Clientes()
        for i in costumer.populate():
            self.trv.insert('', 'end', values=i)

    def leitura_apenas(self):
        self.ent8.configure(state='disabled')

    def normal(self):
        self.ent8.configure(state='normal')

    def hoverIn(self, event):
        event.widget.config(bg="#1E90FF", fg="white", relief=GROOVE)

    def hoverIn2(self, event):
        event.widget.config(bg="#FF0000", fg="white", relief=GROOVE)

    def hoverIn3(self, event):
        event.widget.config(bg="#FFD700", fg="black", relief=GROOVE)

    def hoverOut(self, event):
        event.widget.config(bg="#484848", fg="white", relief=RAISED)


minhaTela = tela_ver_cadastrar_clientes()
