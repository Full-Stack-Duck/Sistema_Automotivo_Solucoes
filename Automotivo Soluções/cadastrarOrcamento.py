from tkinter import *
import tkinter as tk
from tkinter import ttk
import TabOrc as orc


class cadastrar_orcamento():
    def __init__(self):

        self.janelaCad_Orc = Tk()
        self.janelaCad_Orc.state('zoomed')
        self.janelaCad_Orc.title('Automativo Soluções')
        self.janelaCad_Orc.geometry('1200x600')
        self.janelaCad_Orc.configure(bg="#484848")
        #self.janelaCad_Orc.minsize(1200, 650)
        #self.janelaCad_Orc.maxsize(1200, 650)

# ===========|  SEÇÕES & FRAMES  |============== #
        self.frameTop = Frame(self.janelaCad_Orc, bg="#484848")
        self.frameMid = Frame(self.janelaCad_Orc, bg="#484848")

        self.secaoCliente = LabelFrame(
            self.frameTop, text=' Dados do Cliente ', bg="#484848", fg="white")
        self.secaoCadastro = LabelFrame(
            self.frameTop, text=' Cadastrar Orçamento ', bg="#484848", fg="white")
        self.secaoPesqCliente = LabelFrame(
            self.secaoCliente, text=' Pesquisar Cliente ', bg="#484848", fg="white")
        self.secaoOrcamento = LabelFrame(
            self.janelaCad_Orc, text=' Orçamentos cadastrados ', bg="#484848", fg="white")
        self.secaoPesqOrca = LabelFrame(
            self.secaoOrcamento, text=' Pesquisar Orçamento ', bg="#484848", fg="white")

        self.sub1 = Frame(self.secaoCadastro, bg="#484848")
        self.sub2 = Frame(self.secaoCadastro, bg="#484848")
        self.sub3 = Frame(self.sub2, bg="#484848")

        self.rodape = Frame(self.janelaCad_Orc, bg="#484848")

        self.frameTop.pack()
        self.frameMid.pack()

        self.secaoCliente.pack(side='left', expand='yes',
                               padx=10, pady=10, anchor='w')
        self.secaoCadastro.pack(side='left', fill='both',
                                expand='yes', padx=10, pady=10)
        self.secaoPesqCliente.pack(fill='both', expand='yes', padx=10, pady=10)
        self.secaoOrcamento.pack(fill='both', expand='yes')
        self.secaoPesqOrca.pack(
            fill='both', side='bottom', expand='no', padx=10, pady=10)

        self.sub1.pack(side='left')
        self.sub2.pack(side='left')
        self.sub3.grid(row=2, rowspan=5, column=0,
                       columnspan=3, padx=10)

        self.rodape.pack(fill='both', expand='yes', padx=20)


### ============|   SEÇÃO CLIENTE  |============== ###
# ==============| TREEVIEW CLIENTE |================ #
        self.header1 = ('#', 'nome', 'carro', 'cpf')

        self.trvClient = ttk.Treeview(
            self.secaoCliente, selectmode='browse', columns=self.header1, show='headings')

        self.trvClient.column('#', width=30, anchor='center')
        self.trvClient.column('nome', anchor='center')
        self.trvClient.column('carro', anchor='center')
        self.trvClient.column('cpf', anchor='center')

        self.trvClient.heading('#', text='#')
        self.trvClient.heading('nome', text='Nome')
        self.trvClient.heading('carro', text='Carro')
        self.trvClient.heading('cpf', text='CPF')

        self.trvClient.bind('<Double 1>', self.pegar_linha1)
        self.trvClient.pack(fill='both')

        self.listarClientes()
# ============|  CAMPO PESQUISAR CLIENTE  |========== #
        self.pesqClient = Label(self.secaoPesqCliente,
                                text='Pesquisa-cliente:', bg="#484848", fg="white")
        self.keyClient = Entry(self.secaoPesqCliente,
                               textvariable='txtPesquisaCliente', bg="#484848", fg="white")

        self.pesqClient.pack(side='left', padx=10, pady=6)
        self.keyClient.pack(side='left', padx=10, pady=6)

# ===============| BOTÕES |================= #
        self.btnPesqClient = Button(
            self.secaoPesqCliente, text='Pesquisar', bg="#484848", fg="white", command=self.pesquisar_cliente)
        self.btnMostrarCliente = Button(
            self.secaoPesqCliente, text='Mostrar Clientes', bg="#484848", fg="white", command=self.listarClientes)

        self.btnPesqClient.pack(side='left', padx=10, pady=6, ipadx=40)
        self.btnMostrarCliente.pack(side='left', padx=10, pady=6, ipadx=40)


### =========| SEÇÃO CADASTRO |=========== ###
# ============| CAMPOS DE DADO (SUB-1) |=============#
        self.lblCliente = Label(
            self.sub1, text='Cliente:', bg="#484848", fg="white")
        self.lblCarro = Label(self.sub1, text='Carro:',
                              bg="#484848", fg="white")
        self.lblCPF_Client = Label(
            self.sub1, text='CPF Cliente:', bg="#484848", fg="white")
        self.lblMecanico = Label(
            self.sub1, text='Mecânico:', bg="#484848", fg="white")
        self.lblCPF_Mec = Label(
            self.sub1, text='CPF Mec.:', bg="#484848", fg="white")

        self.lblCliente.grid_columnconfigure(0, minsize=10)
        self.lblCliente.grid(row=0, column=0, padx=1, pady=6, sticky='e')
        self.lblCarro.grid(row=1, column=0, padx=1, pady=6, sticky='e')
        self.lblCPF_Client.grid(row=2, column=0, padx=1, pady=6, sticky='e')
        self.lblMecanico.grid(row=3, column=0, padx=1, pady=6, sticky='e')
        self.lblCPF_Mec.grid(row=4, column=0, padx=1, pady=6, sticky='e')

        self.entNomeClient = Entry(
            self.sub1, textvariable='txtCliente', state='readonly')
        self.entClient_CPF = Entry(
            self.sub1, textvariable='txtCPF_cliente', state='readonly')
        self.entCarro = Entry(
            self.sub1, textvariable='txtCarro', state='readonly')
        self.entNomeMec = Entry(
            self.sub1, textvariable='txtNomeMecanico')
        self.entMEC_CPF = Entry(
            self.sub1, textvariable='txtCPF_mec')

# ===================================================================================
# ===================================================================================
# ===================================================================================


# ===================================================================================
# ===================================================================================
# ===================================================================================

        #self.entNomeMec.insert(INSERT, 'KELVIN ')
        #self.entMEC_CPF.insert(INSERT, '34567891234')

        # self.entNomeMec.configure(state='readonly')
        # self.entMEC_CPF.configure(state='readonly')

        self.entNomeClient.grid(row=0, column=1, padx=1, pady=6)
        self.entClient_CPF.grid(row=1, column=1, padx=1, pady=6)
        self.entCarro.grid(row=2, column=1, padx=1, pady=6)
        self.entNomeMec.grid(row=3, column=1, padx=1, pady=6)
        self.entMEC_CPF.grid(row=4, column=1, padx=1, pady=6)
# ==================================| (SUB-2) |=============================================== #
        txtServico = StringVar()
        txtValor = StringVar()

        self.lblServico = Label(
            self.sub2, text='Serviço/Peça', bg="#484848", fg="white")
        self.lblValor = Label(self.sub2, text='Valor(R$)',
                              bg="#484848", fg="white")

        self.entServico = Entry(self.sub2, textvariable=txtServico)
        self.entValor = Entry(self.sub2, textvariable=txtValor)

        self.lblServico.grid(row=0, column=0, padx=10, pady=3)
        self.lblValor.grid(row=0, column=1, padx=10, pady=3)

        self.entServico.grid(row=1, column=0, padx=10, pady=3)
        self.entValor.grid(row=1, column=1, padx=10, pady=3)

        self.entValor.bind('<Return>', self.adicionar)

# ===============| BOTÕES |================== #
        self.btnAlterar = Button(
            self.sub1, text='Alterar', command=self.alterar, bg="#484848", fg="white")
        self.btnLimpar = Button(
            self.sub1, text='Limpar', command=self.limpar_Cadastro_Cliente, bg="#484848", fg="white")
        self.btnCadastrar = Button(
            self.sub1, text='Cadastrar', command=self.cadastrar_orc, bg="#484848", fg="white")

        self.btnAlterar.grid(column=0, columnspan=2, padx=10, pady=6, ipadx=40)
        self.btnLimpar.grid(column=0, columnspan=2, padx=10, pady=6, ipadx=40)
        self.btnCadastrar.grid(column=0, columnspan=2,
                               padx=10, pady=6, ipadx=35)

        self.btnAlterar.bind("<Enter>", self.hoverIn3)
        self.btnAlterar.bind("<Leave>", self.hoverOut)
        self.btnLimpar.bind("<Enter>", self.hoverIn2)
        self.btnLimpar.bind("<Leave>", self.hoverOut)
        self.btnCadastrar.bind("<Enter>", self.hoverIn)
        self.btnCadastrar.bind("<Leave>", self.hoverOut)

        self.btnAdd = Button(self.sub2, text='Adicionar',
                             command=self.adicionar_serv, bg="#484848", fg="white")
        self.btnAdd.grid(row=1, column=2, padx=5, pady=6, ipadx=20)

# ==============| TREEVIEW CADASTRO (SUB-3) |================= #
        self.header2 = ('#', 'item', 'valor')

        self.trvCadastro = ttk.Treeview(
            self.sub3, selectmode='browse', columns=self.header2, show='headings')

        self.trvCadastro.column('#', width=30, anchor='center')
        self.trvCadastro.column('item', anchor='w')
        self.trvCadastro.column('valor', anchor='center')

        self.trvCadastro.heading('#', text='#')
        self.trvCadastro.heading('item', text='Item')
        self.trvCadastro.heading('valor', text='Valor')

        self.trvCadastro.bind('<Double 1>', self.pegar_linha2)
        self.trvCadastro.grid()

        self.total = 0
        self.valorTotal = Label(
            self.sub3, text=f'Valor Total: R${self.total:.2f}', bg="#484848", fg="white")
        self.valorTotal.grid(sticky='se')

### =================|  SEÇÃO ORCAMENTOS CADASTRADOS  |================== ###
# ========================| TREEVIEW ORCAMENTOS |========================== #
        self.header3 = ('#', 'nome', 'carro', 'valor', 'descricao')

        self.trv_Orcam = ttk.Treeview(
            self.secaoOrcamento, selectmode='browse', columns=self.header3, show='headings', height=6)

        self.trv_Orcam.column('#', width=10, anchor='center')
        self.trv_Orcam.column('nome', anchor='center')
        self.trv_Orcam.column('carro', anchor='center')
        self.trv_Orcam.column('valor', anchor='center')

        self.trv_Orcam.heading('#', text='#')
        self.trv_Orcam.heading('nome', text='Nome')
        self.trv_Orcam.heading('carro', text='Carro')
        self.trv_Orcam.heading('valor', text='Valor')
        self.trv_Orcam.heading('descricao', text='Descrição do Serviço')

        self.trv_Orcam.bind('<Double 1>', self.pegar_linha3)
        self.trv_Orcam.pack(fill='both')

        self.listarOrcamentos()

### ==============|  SEÇÃO PESQUISAR ORCAMENTO  |=========== ###
        self.pesqOrc = Label(self.secaoPesqOrca,
                             text='Palavra-chave', bg="#484848", fg="white")
        self.pesqOrc.pack(side='left', padx=10, pady=6)

        self.keyOrcam = Entry(self.secaoPesqOrca,
                              textvariable='txtPesquisaOrcamento')
        self.keyOrcam.pack(side='left', padx=10, pady=6)

# =========== BOTÕES ================= #
        self.btnPesqOrcam = Button(
            self.secaoPesqOrca, text='Pesquisar Orçamento', command=self.pesquisarORCAMENTO, bg="#484848", fg="white")
        self.btnMostrarOrcam = Button(
            self.secaoPesqOrca, text='Mostrar Todos', command=self.listarOrcamentos, bg="#484848", fg="white")

        self.btnPesqOrcam.pack(side='left', padx=10, pady=6, ipadx=40)
        self.btnMostrarOrcam.pack(side='left', padx=10, pady=6, ipadx=40)
        self.valoresDaSoma = []


### =============| SEÇÃO RODAPÉ |================== ###
# ==================| BOTÃO |==================  #
        self.btnVoltar = Button(
            self.rodape, text='Voltar', command=self.voltar, bg="#484848", fg="white")
        self.btnVoltar.pack(side='right', padx=10, pady=10, ipadx=40)

        self.lista_de_cadORCAMENTO = []
        self.contador = 0
        mainloop()

#====================================================|  FUNÇÕES  |=======================================================#

    # =====| GERAIS |===== #

    def treeviewDelete(self, local):
        return local.delete(*local.get_children())

    def voltar(self):
        self.janelaCad_Orc.destroy()
        return

    def entNormal(self):
        self.entNomeClient.configure(state='normal')
        self.entClient_CPF.configure(state='normal')
        self.entCarro.configure(state='normal')
        self.entNomeMec.configure(state='normal')
        self.entMEC_CPF.configure(state='normal')

    def entLeitura(self):
        self.entNomeClient.configure(state='readonly')
        self.entClient_CPF.configure(state='readonly')
        self.entCarro.configure(state='readonly')
        # self.entNomeMec.configure(state='readonly')
        # self.entMEC_CPF.configure(state='readonly')

    def limpar_tudo(self):
        self.entNormal()
        self.entNomeClient.delete(0, END)
        self.entClient_CPF.delete(0, END)
        self.entCarro.delete(0, END)
        self.entServico.delete(0, END)
        self.entValor.delete(0, END)
        self.total = 0
        self.valorTotal["text"] = f'Valor Total: R${self.total:.2f}'
        self.contador = 0
        self.valoresDaSoma = []
        self.lista_de_cadORCAMENTO = []
        self.entLeitura()

    def soma_valor(self):
        valor = 0
        selected = self.lista_de_cadORCAMENTO
        for i in selected:
            valor = i[2]
        self.valoresDaSoma.append(valor)
        total = sum(self.valoresDaSoma)
        self.total = total
        self.valorTotal["text"] = f'Valor Total: R${self.total:.2f}'

    # =====| CLIENTES |===== #

    def view_Client(self, local):
        self.treeviewDelete(local)
        linhas = orc.viewClientes()
        for i in linhas:
            local.insert('', END, values=i)

    def listarClientes(self):
        return self.view_Client(self.trvClient)

    def pesquisar_cliente(self):
        chave = self.keyClient.get()
        result = orc.searchCliente(chave)
        self.treeviewDelete(self.trvClient)
        selection = []
        selection.append((result[0][0], result[0][1],
                         result[0][3], result[0][4]))
        for i in selection:
            self.trvClient.insert('', END, values=i)

    def identificar_linha1(self, trvLocal):
        listaItem = []
        self.entNormal()
        self.limpar_Cadastro_Cliente()
        self.entNormal()
        for item in trvLocal.selection():
            identif = trvLocal.item(item, 'values')
            listaItem.append(identif)

        self.entNomeClient.insert(INSERT, listaItem[0][1])
        self.entClient_CPF.insert(INSERT, listaItem[0][2])
        self.entCarro.insert(INSERT, listaItem[0][3])
        self.entLeitura()

    def pegar_linha1(self, event):
        return self.identificar_linha1(self.trvClient)

    # ======| CADASTRO |=====#

    def view_cadORCAMENTO(self, local):
        self.treeviewDelete(local)
        linhas = self.lista_de_cadORCAMENTO
        for i in linhas:
            local.insert('', END, values=i)
        self.tupToStr(self.lista_de_cadORCAMENTO)

    def listarCadOrcamento(self):
        return self.view_cadORCAMENTO(self.trvCadastro)

    def limpar_Cadastro_Cliente(self):
        self.treeviewDelete(self.trvCadastro)
        self.entNormal()
        self.entNomeClient.delete(0, END)
        self.entClient_CPF.delete(0, END)
        self.entCarro.delete(0, END)
        self.entLeitura()

    def limpar_Servicos(self):
        self.entServico.delete(0, END)
        self.entValor.delete(0, END)

    def adicionar(self, event):
        self.adicionar_serv()

    def adicionar_serv(self):
        self.contador += 1
        self.appendListCadOrc(self.contador)
        self.listarCadOrcamento()
        self.limpar_Servicos()
        self.soma_valor()
        self.entServico.focus()

    def appendListCadOrc(self, contador):
        servico = str(self.entServico.get())
        valor = int(self.entValor.get())
        return self.lista_de_cadORCAMENTO.append((contador, servico, valor))

    def filtroDeImpurezas(self, string):
        characters = "(',)"
        for x in range(len(characters)):
            string = string.replace(characters[x], "")
        return string

    def adicionar_Orc(self, trvLocal):
        self.tupla = []
        for item in trvLocal.selection():
            self.identificador = trvLocal.item(item, 'values')
            self.tupla.append((self.identificador))

        self.idCadOrc = self.filtroDeImpurezas(self.tupla[0][0])
        self.entServico.insert(
            INSERT, self.filtroDeImpurezas(self.tupla[0][1]))
        self.entValor.insert(INSERT, self.filtroDeImpurezas(self.tupla[0][2]))
        self.entServico.focus()

    def pegar_linha2(self, event):
        self.limpar_Servicos()
        return self.adicionar_Orc(self.trvCadastro)

    def alterar_Serv(self, trvLocal):
        listValue = []
        selecao = trvLocal.selection()
        for item in selecao:
            identificador = trvLocal.item(item, 'values')
            listValue.append(identificador)
        trvLocal.item(selecao, values=(
            listValue[0][0], self.entServico.get(), self.entValor.get()))
        return

    def alterar(self):
        return self.alterar_Serv(self.trvCadastro)

    def cadastrar_orc(self):
        self.entNormal()
        status = 'Pendente'
        cliente = self.entNomeClient.get()
        cpf_client = self.entClient_CPF.get()
        carro = self.entCarro.get()
        nome_mec = self.entNomeMec.get()
        cpf_mec = self.entMEC_CPF.get()
        descricao = self.filtroDeImpurezas(
            self.tupToStr(self.lista_de_cadORCAMENTO))
        valor = self.total
        valores = orc.inserir_orc(
            cliente, carro, cpf_client, nome_mec, cpf_mec, valor, descricao, status)
        print(valores)
        self.view_Orcamento(self.trv_Orcam)
        self.limpar_tudo()
        self.entLeitura()

    def tupToStr(self, tupla):
        lista = []
        for i in tupla:
            lista.append(i)
        stringed = ''
        for x in lista:
            stringed += str(x)
        return stringed

    # =====| ORCAMENTO |===== #

    def view_Orcamento(self, local):
        self.treeviewDelete(local)
        linhas = orc.view()
        print(linhas)
        for i in linhas:
            local.insert('', END, values=i)

    def listarOrcamentos(self):
        return self.view_Orcamento(self.trv_Orcam)

    def pesquisarORCAMENTO(self):
        chave = self.keyOrcam.get()
        result = orc.search(chave)
        self.treeviewDelete(self.trv_Orcam)
        for i in result:
            self.trv_Orcam.insert('', END, values=i)

    def add_cadastro(self, trvLocal):
        self.tupla = []
        for item in trvLocal.selection():
            self.identificador = trvLocal.item(item, 'values')
            self.tupla.append((self.identificador[4]))
        self.treeviewDelete(self.trvCadastro)
        for i in self.tupla:
            self.trvCadastro.insert(
                '', END, values=self.filtroDeImpurezas(self.tupToStr(i)))

    def pegar_linha3(self, event):
        return self.add_cadastro(self.trv_Orcam)

    def hoverIn(self, event):
        event.widget.config(bg="#1E90FF", fg="white", relief=GROOVE)

    def hoverIn2(self, event):
        event.widget.config(bg="#FF0000", fg="white", relief=GROOVE)

    def hoverIn3(self, event):
        event.widget.config(bg="#FFD700", fg="black", relief=GROOVE)

    def hoverOut(self, event):
        event.widget.config(bg="#484848", fg="white", relief=RAISED)
    # def executeJan(self):
    #     app = cadastrar_orcamento()
    #     return app.janelaCad_Orc.mainloop()


app = cadastrar_orcamento()
