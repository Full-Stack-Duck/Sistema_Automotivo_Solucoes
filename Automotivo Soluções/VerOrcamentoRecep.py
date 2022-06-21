from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD
import TabOrc as orc


class ver_Orcamento():
    def __init__(self):

        self.janelaVerOrc = Tk()
        self.janelaVerOrc.title('Ver Orçamentos')
        self.janelaVerOrc.geometry('1600x900')
        self.janelaVerOrc.config(bg='#484848')
        self.janelaVerOrc.state('zoomed')
        self.janelaVerOrc.iconbitmap('automotivo.ico')

    # ==========|  SEÇÕES  | =========== #
        self.frameTop = Frame(self.janelaVerOrc, bg='#484848')
        self.frameMid = Frame(self.janelaVerOrc, bg='#484848')
        # self.frameBot = Frame(self.janelaVerOrc, bg='#484848')

        self.frameTop.pack(pady=(20, 0))
        self.frameMid.pack()
        # self.frameBot.pack()

        self.wrapper_trv = LabelFrame(
            self.frameMid, text='  Orçamentos Cadastrados  ', bg='#484848', fg='white', font=('Roboto', 10, BOLD))
        self.wrapper_aprov = LabelFrame(
            self.frameMid, text=' Gerar Ordem de Serviço ', bg='#484848', fg='white', font=('Roboto', 10, BOLD))
        self.wrapper_filtrar = LabelFrame(
            self.frameMid, text=' Pesquisar ', bg='#484848', fg='white', font=('Roboto', 10, BOLD))
        self.frameRodape = Frame(self.janelaVerOrc, bg='#484848')

        self.wrapper_trv.pack(fill='both', expand='yes', padx=20, pady=10)
        self.wrapper_aprov.pack(fill='both', expand='yes', padx=20, pady=10)
        self.wrapper_filtrar.pack(fill='both', expand='yes', padx=20, pady=10)
        self.frameRodape.pack(fill='both', expand='yes', padx=20, pady=10)

    # =========|  TOP  |========= #
        self.titulo = Label(self.frameTop, text='Orçamentos',
                            bg='#484848', fg='white', font=('Roboto', 20, BOLD))
        self.titulo.pack(padx=20, pady=10)

    # ========| MIDDLE  |======== #
    # =======| TREEVIEW  |======== #
        self.cabecalho = ('#', 'cliente', 'carro', 'cpf_cliente',
                          'mecanico', 'cpf_mec', 'valor', 'descricao')
        self.trv = ttk.Treeview(
            self.wrapper_trv, selectmode='browse', columns=self.cabecalho, show='headings')

        self.trv.column('#', width=10)
        self.trv.column('cliente', width=150)
        self.trv.column('carro', width=150)
        self.trv.column('cpf_cliente', width=150)
        self.trv.column('mecanico', width=150)
        self.trv.column('cpf_mec', width=150)
        self.trv.column('valor', width=150)
        self.trv.column('descricao', width=400)

        self.trv.heading('#', text='#')
        self.trv.heading('cliente', text='Cliente')
        self.trv.heading('carro', text='Carro')
        self.trv.heading('cpf_cliente', text='CPF Cliente')
        self.trv.heading('mecanico', text='Mecânico')
        self.trv.heading('cpf_mec', text='CPF Mec')
        self.trv.heading('valor', text='Valor')
        self.trv.heading('descricao', text='Descrição do Serviço')

        self.trv.bind('<Double 1>', self.pegar_linhaBind)
        self.trv.pack(pady=10)

        self.popular()

    # =========|  GERAR ORDEM DE SERVIÇO  |======== #
        self.btn_Aprovar = Button(
            self.wrapper_aprov, text='Aprovar', command=self.cadastrar, bg='#484848', fg='white')
        self.btn_Excluir = Button(
            self.wrapper_aprov, text='Excluir', command=self.excluir, bg='#484848', fg='white')

        self.btn_Aprovar.pack(side='left', padx=(30, 0), pady=10, ipadx=20)
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

        self.btn_Aprovar.bind("<Enter>", self.hoverIn1)
        self.btn_Aprovar.bind("<Leave>", self.hoverOut)
        self.btn_Excluir.bind("<Enter>", self.hoverIn3)
        self.btn_Excluir.bind("<Leave>", self.hoverOut)
        self.btn_voltar.bind("<Enter>", self.hoverIn3)
        self.btn_voltar.bind("<Leave>", self.hoverOut)
        self.btn_procurar.bind("<Enter>", self.hoverIn2)
        self.btn_procurar.bind("<Leave>", self.hoverOut)
        self.btn_mostrar.bind("<Enter>", self.hoverIn2)
        self.btn_mostrar.bind("<Leave>", self.hoverOut)

        self.varDeArmaz = ''
        mainloop()


# ===========|  FUNÇÕES  |============ #

    def pegar_linhaBind(self, event):
        return self.pegar_linha()

    def pegar_linha(self):
        for item in self.trv.selection():
            self.id = self.trv.item(item, 'values')
        ident = self.id
        self.varDeArmaz = ident
        print(self.varDeArmaz)

    def popular(self):
        self.trv.delete(*self.trv.get_children())
        for i in orc.populate():
            self.trv.insert('', 'end', values=i)

    def cadastrar(self):
        return self.aprovar()

    def aprovar(self):
        tupla = self.varDeArmaz
        listinha = []
        for i in tupla:
            listinha.append(i)
        cliente = str(listinha[1])
        cpf_cliente = str(listinha[2])
        carro = str(listinha[3])
        mecanico = str(listinha[4])
        cpf_mec = str(listinha[5])
        valor = str(listinha[6])
        descricao = str(listinha[7])
        status = str(listinha[8])
        orc.inserir_ord(cliente, cpf_cliente, carro,
                        mecanico, cpf_mec, valor, descricao, status)
        self.excluir()
        self.varDeArmaz = ''

    def excluir(self):
        tupla = self.varDeArmaz
        pickingID = []
        for m in tupla:
            pickingID.append(m)
        idorc = pickingID[0]
        orc.delete_aprov(idorc)
        self.popular()

    # def status(self):
    #     state = 'Pendente'
    #     tupla = self.varDeArmaz
    #     lista1 = []
    #     for j in tupla:
    #         lista1.append(j)
    #     idordem = lista1[0]
    #     orc.update_status(state, idordem)

    def procurar(self):
        chave = self.entBusca.get()
        self.trv.delete(*self.trv.get_children())
        for i in orc.filtrar(chave):
            self.trv.insert('', END, values=i)

    def voltar(self):
        self.janelaVerOrc.destroy()
        return
    
    def hoverIn1(self, event):  # verde
       event.widget.config(bg="#3CB371", fg="white", relief=GROOVE)

    def hoverIn3(self, event):  # vermelho
       event.widget.config(bg="#8B0000", fg="white", relief=GROOVE)

    def hoverOut(self, event):
       event.widget.config(bg='#484848', fg="#e1e3db", relief=RAISED)
    def hoverIn2(self, event):
       event.widget.config(bg='#00BFFF', fg="black", relief=GROOVE)


app = ver_Orcamento()
