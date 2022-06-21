from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import BOLD
import TabOrd as ordem


class ver_Ordens():
    def __init__(self):

        self.janelaVerOrd = Tk()
        self.janelaVerOrd.title('Gerenciar Ordem')
        self.janelaVerOrd.geometry('1600x900')
        self.janelaVerOrd.config(bg='#484848')
        self.janelaVerOrd.state('zoomed')
        self.janelaVerOrd.iconbitmap('automotivo.ico')

    # ==========|  SEÇÕES  | =========== #
        self.frameTop = Frame(self.janelaVerOrd, bg='#484848')
        self.frameMid = Frame(self.janelaVerOrd, bg='#484848')
        # self.frameBot = Frame(self.janelaVerOrc, bg='#484848')

        self.frameTop.pack(pady=(20, 0))
        self.frameMid.pack()
        # self.frameBot.pack()

        self.wrapper_trv = LabelFrame(
            self.frameMid, text='  Ordens Cadastradas  ', bg='#484848', fg='white', font=('Roboto', 10, BOLD))
        self.wrapper_aprov = LabelFrame(
            self.frameMid, text=' Gerenciar ', bg='#484848', fg='white', font=('Roboto', 10, BOLD))
        self.wrapper_filtrar = LabelFrame(
            self.frameMid, text=' Pesquisar ', bg='#484848', fg='white', font=('Roboto', 10, BOLD))
        self.frameRodape = Frame(self.janelaVerOrd, bg='#484848')

        self.wrapper_trv.pack(fill='both', expand='yes', padx=20, pady=10)
        self.wrapper_aprov.pack(fill='both', expand='yes', padx=20, pady=10)
        self.wrapper_filtrar.pack(fill='both', expand='yes', padx=20, pady=10)
        self.frameRodape.pack(fill='both', expand='yes', padx=20, pady=10)

    # =========|  TOP  |========= #
        self.titulo = Label(self.frameTop, text='Ordens de Serviços',
                            bg='#484848', fg='white', font=('Roboto', 20, BOLD))
        self.titulo.pack(padx=20, pady=10)

    # ========| MIDDLE  |======== #
    # =======| TREEVIEW  |======== #
        self.cabecalho = ('#', 'cliente', 'carro', 'cpf_cliente',
                          'mecanico', 'cpf_mec', 'valor', 'descricao', 'status')
        self.trv = ttk.Treeview(
            self.wrapper_trv, selectmode='browse', columns=self.cabecalho, show='headings')

        self.trv.column('#', width=10)
        self.trv.column('cliente', width=150, anchor='center')
        self.trv.column('carro', width=150, anchor='center')
        self.trv.column('cpf_cliente', width=150, anchor='center')
        self.trv.column('mecanico', width=150, anchor='center')
        self.trv.column('cpf_mec', width=150, anchor='center')
        self.trv.column('valor', width=150, anchor='center')
        self.trv.column('descricao', width=300)
        self.trv.column('status', width=100, anchor='center')

        self.trv.heading('#', text='#')
        self.trv.heading('cliente', text='Cliente')
        self.trv.heading('carro', text='Carro')
        self.trv.heading('cpf_cliente', text='CPF Cliente')
        self.trv.heading('mecanico', text='Mecânico')
        self.trv.heading('cpf_mec', text='CPF Mec')
        self.trv.heading('valor', text='Valor R$')
        self.trv.heading('descricao', text='Descrição do Serviço')
        self.trv.heading('status', text='Status')

        self.trv.bind('<Double 1>', self.pegar_linhaBind)
        self.trv.pack(pady=10)

        self.popular()

    # =========|  GERAR ORDEM DE SERVIÇO  |======== #
        self.btn_Concluir = Button(
            self.wrapper_aprov, text='Concluir', command=self.concluir, bg='#484848', fg='white')
        self.btn_Excluir = Button(
            self.wrapper_aprov, text='Excluir', command=self.excluir, bg='#484848', fg='white')

        self.btn_Concluir.pack(side='left', padx=(30, 0), pady=10, ipadx=20)
        self.btn_Excluir.pack(side='left', padx=30, pady=10, ipadx=20)

    # =========|  CAMPO DE BUSCA  |======== #
        self.lblChave = Label(self.wrapper_filtrar,
                              text='Palavra-chave', bg='#484848', fg='white')
        self.lblChave.pack(side='left', padx=6, pady=10)

        self.entBusca = Entry(self.wrapper_filtrar, textvariable='filtro')
        self.entBusca.pack(side='left', padx=6, pady=10, ipadx=15)

        self.btn_procurar = Button(
            self.wrapper_filtrar, text='Procurar', command=self.procurar, bg='#484848', fg='white')
        self.btn_mostrar = Button(
            self.wrapper_filtrar, text='Mostrar Todos', command=self.popular, bg='#484848', fg='white')

        self.btn_procurar.pack(side='left', padx=6, pady=10, ipadx=20)
        self.btn_mostrar.pack(side='left', padx=6, pady=10, ipadx=20)

    # ===========| BOTTOM  |=========== #
    # ===========| VOLTAR  |=========== #
        self.btn_voltar = Button(
            self.frameRodape, text='Voltar', command=self.voltar, bg='#484848', fg='white')

        self.btn_voltar.pack(side='right', padx=6, pady=10, ipadx=30)

        self.varDeArmaz = ''

        self.btn_voltar.bind("<Enter>", self.hoverIn3)
        self.btn_voltar.bind("<Leave>", self.hoverOut)
        self.btn_Excluir.bind("<Enter>", self.hoverIn3)
        self.btn_Excluir.bind("<Leave>", self.hoverOut)
        self.btn_Concluir.bind("<Enter>", self.hoverIn1)
        self.btn_Concluir.bind("<Leave>", self.hoverOut)
        
        mainloop()
        

# ===========|  FUNÇÕES  |============ #


    def pegar_linhaBind(self, event):
        return self.pegar_linha()

    def pegar_linha(self):
        for item in self.trv.selection():
            self.id = self.trv.item(item, 'values')
        ident = self.id
        self.varDeArmaz = ident

    def popular(self):
        self.trv.delete(*self.trv.get_children())
        for i in ordem.populate(self):
            self.trv.insert('', 'end', values=i)

    def status(self):
        state = 'Finalizada'
        tupla = self.varDeArmaz
        lista1 = []
        for i in tupla:
            lista1.append(i)
        idordem = lista1[0]
        ordem.update(state, idordem)
        self.popular()
        self.varDeArmaz = ''

    def concluir(self):
        return self.status()

    def excluir(self):
        tupla = self.varDeArmaz
        pickingID = []
        for i in tupla:
            pickingID.append(i)
        idordem = pickingID[0]
        ordem.delete(idordem)
        self.popular()
        self.varDeArmaz = ''

    def procurar(self):
        chave = self.entBusca.get()
        self.trv.delete(*self.trv.get_children())
        for i in ordem.filtrar(chave):
            self.trv.insert('', END, values=i)

    def voltar(self):
        self.janelaVerOrd.destroy()
        return

    def hoverIn1(self, event):  # verde
       event.widget.config(bg="#3CB371", fg="white", relief=GROOVE)

    def hoverIn3(self, event):  # vermelho
       event.widget.config(bg="#8B0000", fg="white", relief=GROOVE)

    def hoverOut(self, event):
       event.widget.config(bg='#484848', fg="#e1e3db", relief=RAISED)

   


app = ver_Ordens()
